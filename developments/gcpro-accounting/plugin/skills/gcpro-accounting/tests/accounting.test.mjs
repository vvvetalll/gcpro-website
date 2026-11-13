import {test,after} from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {sharedRuntime,verifyDistribution,gasRunner,gasSha256,sha256} from '../scripts/shared-runtime.mjs';
import {inventory,dumpster,amount,allocate} from '../scripts/workflows.mjs';
import {writeReport,verifyReport} from '../scripts/report-workbook.mjs';
import {main} from '../scripts/run-accounting.mjs';

const temp=await fs.mkdtemp(path.join(os.tmpdir(),'gcpro-accounting-test-'));
after(()=>fs.rm(temp,{recursive:true,force:true}));
const m=await sharedRuntime();
const headers='Date,Service Item,Job Code 1,Job Code 2,Hours,Fname,Lname\n';
const lines=[
 '2026-10-05,Restoration / Mitigation,Alpha,26-0001-MIT,4,Test,Employee',
 '2026-10-06,Restoration / Mitigation,Bravo,26-0002-MIT,6,Test,Employee',
 '2026-10-07,Contents,Charlie,26-0003-CON,5,Test,Employee',
 '2026-10-08,Construction,Other,26-0004-CIP,8,Ordinary,Employee',
 '2026-10-08,Lunch Break,Internal,Lunch Break,1,Test,Employee'];
const timesheet=path.join(temp,'hours.csv');await fs.writeFile(timesheet,headers+lines.join('\n')+'\n');
const pmStart=path.join(temp,'start.xlsx');
const book=new m.exceljs_workbook_default.Workbook;
book.addWorksheet('Jobs').addRows([
 ['Job Number','Customer','Division','Foreman','Total Estimates','Start Date'],
 ['26-0100-CIP','Alpha','Construction Program','Someone',100,'2026-10-01'],
 ['26-0101-CND','Bravo','Construction direct pay','Another',300,'2026-10-02'],
 ['26-0102-CNI','Other month','Construction insurance','Someone',9999,'2026-09-03'],
 ['26-0103-MIT','Wrong department','Mitigation','Someone',900,'2026-10-03']]);
await book.xlsx.writeFile(pmStart);
const selection=path.join(temp,'selection.json');
const selected={month:'2026-10',confirmation:'Synthetic test accountant selection',jobs:['26-0100-CIP','26-0101-CND']};
await fs.writeFile(selection,JSON.stringify(selected));
const io={timesheet,month:'2026-10',total:'100.00'};
const dump={timesheet,month:'2026-10',construction:'100.00',contents:'200.00',mitigation:'300.00',pmStart,constructionSelection:selection};

test('the GAS bundle remains exactly pinned and both integrity scopes verify',async()=>{
 assert.equal(sha256(await fs.readFile(gasRunner)),gasSha256);assert.equal((await verifyDistribution()).success,true);
});
test('unspecified workflow asks gas/dumpster/inventory and writes nothing',async()=>{
 await assert.rejects(()=>main([]),error=>error.code==='workflow_required');
});
test('Inventory uses one common pool, preserves GAS exclusions and canonical job hours',async()=>{
 const report=await inventory(io);const b=report.blocks[0];assert.equal(b.rows.length,3);assert.equal(b.denominator.toString(),'15');
 assert.deepEqual(b.rows.map(r=>r.allocated.toFixed(2)),['26.67','40.00','33.33']);assert.equal(b.allocated.toFixed(2),'100.00');assert.equal(report.exclusions.length,2);
 const output=await writeReport(report,path.join(temp,'inventory'));
 assert.equal(output.verification.success,true);assert.equal(output.overallStatus,'PASS');assert.equal(output.verification.verifiedJobRows,3);
});
test('Inventory aggregates the same job across eligible services without duplicating its expense',async()=>{
 const file=path.join(temp,'shared.csv');await fs.writeFile(file,headers+lines[0]+'\n2026-10-07,Contents,Alpha,26-0001-MIT,6,Test,Employee\n');
 const r=await inventory({...io,timesheet:file});assert.equal(r.blocks[0].rows.length,1);assert.equal(r.blocks[0].rows[0].weight.toString(),'10');assert.equal(r.blocks[0].allocated.toString(),'100');
});
test('largest-remainder cent rounding is deterministic and never loses a cent',()=>{
 const b=allocate(new m.Decimal('.01'),['26-0003-MIT','26-0001-MIT','26-0002-MIT'].map(jobNumber=>({jobNumber,weight:new m.Decimal(1)})),m);
 assert.deepEqual(b.rows.map(r=>[r.jobNumber,r.allocated.toFixed(2)]),[['26-0001-MIT','0.01'],['26-0002-MIT','0.00'],['26-0003-MIT','0.00']]);assert.equal(b.held.toString(),'0');
});
test('Dumpster keeps budgets separate; Construction uses month-eligible estimate-weighted jobs',async()=>{
 const r=await dumpster(dump);const [con,mit,contents]=r.blocks;
 assert.equal(con.allocated.toFixed(2),'100.00');assert.deepEqual(con.rows.map(x=>x.allocated.toFixed(2)),['25.00','75.00']);assert.equal(con.rows.length,2);
 assert.equal(mit.department,'Mitigation');assert.equal(mit.allocated.toFixed(2),'300.00');assert.deepEqual(mit.rows.map(x=>x.allocated.toFixed(2)),['120.00','180.00']);
 assert.equal(contents.department,'Contents');assert.equal(contents.allocated.toFixed(2),'200.00');
 const output=await writeReport(r,path.join(temp,'dumpster'));assert.equal(output.overallStatus,'PASS');assert.equal(output.verification.success,true);
});
test('confirmed monthly Construction rule needs no selection file or foreman allowlist',async()=>{
 const r=await dumpster({...dump,constructionSelection:undefined});assert.equal(r.blocks[0].rows.length,2);assert.equal(r.blocks[0].denominator.toString(),'400');
});
test('no month-eligible Construction jobs holds that pool without taking other department money',async()=>{
 const r=await dumpster({...dump,month:'2026-11',timesheet:undefined,contents:'0',mitigation:'0'});assert.equal(r.blocks[0].held.toString(),'100');assert.equal(r.blocks[0].rows.length,0);
});
test('missing PM Start input for a positive Construction expense is rejected',async()=>{
 await assert.rejects(()=>dumpster({...dump,pmStart:undefined}),/PM Start is required/);
});
test('nonzero pool with zero weights is explicitly held and marked FAIL',async()=>{
 const file=path.join(temp,'excluded.csv');await fs.writeFile(file,headers+lines[4]+'\n');
 const r=await inventory({...io,timesheet:file});assert.equal(r.blocks[0].allocated.toString(),'0');assert.equal(r.blocks[0].held.toString(),'100');assert.equal(r.blocks[0].status,'FAIL');
 const out=await writeReport(r,path.join(temp,'held'));assert.equal(out.overallStatus,'FAIL');assert.equal(out.verification.success,true);
});
test('empty Timesheet with zero expense creates a reconciled empty report',async()=>{
 const file=path.join(temp,'empty.csv');await fs.writeFile(file,headers);
 const r=await inventory({...io,timesheet:file,total:'0'});assert.equal(r.blocks[0].rows.length,0);assert.equal(r.blocks[0].status,'PASS');
 await writeReport(r,path.join(temp,'empty'));
});
test('zero departmental budgets do not require irrelevant source files',async()=>{
 const r=await dumpster({month:'2026-10',construction:'0',contents:'0',mitigation:'0'});
 assert.ok(r.blocks.every(b=>b.source.isZero()&&b.allocated.isZero()));
});
test('negative, fractional-cent, nonnumeric and missing amounts are rejected',()=>{
 for(const value of ['-1','NaN','Infinity','1.001','',undefined,'1e3','$20'])assert.throws(()=>amount(value,m.Decimal));
 assert.equal(amount('0',m.Decimal).toString(),'0');
});
test('out-of-period and invalid dates fail before allocation',async()=>{
 for(const date of ['2026-09-30','2026-02-30','']){
  const file=path.join(temp,'date-'+date.replaceAll('-','')+'.csv');await fs.writeFile(file,headers+lines[0].replace('2026-10-05',date)+'\n');await assert.rejects(()=>inventory({...io,timesheet:file}));
 }
});
test('malformed/missing job numbers remain review items and do not receive an allocation',async()=>{
 const file=path.join(temp,'missing.csv');await fs.writeFile(file,headers+lines[0]+'\n2026-10-05,Contents,Missing,,2,Test,Employee\n2026-10-05,Contents,Malformed,26-broken-CON,2,Test,Employee\n');
 const r=await inventory({...io,timesheet:file});assert.equal(r.issues.length,2);assert.equal(r.blocks[0].rows.length,1);assert.equal(r.blocks[0].allocated.toString(),'100');
 const out=await writeReport(r,path.join(temp,'review'));assert.equal(out.overallStatus,'REVIEW REQUIRED');
});
test('reopened report verifier catches a changed or duplicated allocation',async()=>{
 const r=await inventory(io),out=await writeReport(r,path.join(temp,'tamper'));
 const b=new m.exceljs_workbook_default.Workbook;await b.xlsx.readFile(out.outputPath);b.getWorksheet('Inventory').getCell('F2').value=999;
 const bad=path.join(temp,'bad.xlsx');await b.xlsx.writeFile(bad);await assert.rejects(()=>verifyReport(bad,r));
});
test('the original Excel timesheet adapter produces the same Inventory allocations',async()=>{
 const b=new m.exceljs_workbook_default.Workbook;b.addWorksheet('Hours').addRows([headers.trim().split(','),...lines.map(line=>line.split(',').map((s,i)=>i===4?Number(s):s))]);
 const f=path.join(temp,'hours.xlsx');await b.xlsx.writeFile(f);
 const a=await inventory(io),x=await inventory({...io,timesheet:f});assert.deepEqual(x.blocks[0].rows.map(r=>[r.jobNumber,r.weight.toString(),r.allocated.toString()]),a.blocks[0].rows.map(r=>[r.jobNumber,r.weight.toString(),r.allocated.toString()]));
});
test('duplicate identical PM Start rows allocate once; conflicting estimates fail closed',async()=>{
 const b=new m.exceljs_workbook_default.Workbook;await b.xlsx.readFile(pmStart);
 const values=b.getWorksheet('Jobs').getRow(2).values.slice(1);b.getWorksheet('Jobs').addRow(values);
 const same=path.join(temp,'duplicate-start.xlsx');await b.xlsx.writeFile(same);
 const r=await dumpster({...dump,pmStart:same});assert.equal(r.blocks[0].rows.length,2);assert.equal(r.blocks[0].denominator.toString(),'400');assert.equal(r.blocks[0].allocated.toString(),'100');
 b.getWorksheet('Jobs').getCell('E6').value=101;
 const conflict=path.join(temp,'conflict-start.xlsx');await b.xlsx.writeFile(conflict);
 await assert.rejects(()=>dumpster({...dump,pmStart:conflict}),/conflicting|invalid/i);
});
test('missing Total Estimates on a month-eligible Construction job is an error',async()=>{
 const b=new m.exceljs_workbook_default.Workbook;await b.xlsx.readFile(pmStart);b.getWorksheet('Jobs').getCell('E2').value=null;
 const f=path.join(temp,'missing-estimate.xlsx');await b.xlsx.writeFile(f);
 await assert.rejects(()=>dumpster({...dump,pmStart:f}),/missing or invalid Total Estimates/);
});
test('missing Start Date is visible for review and never guessed into the monthly population',async()=>{
 const b=new m.exceljs_workbook_default.Workbook;await b.xlsx.readFile(pmStart);b.getWorksheet('Jobs').getCell('F2').value=null;
 const f=path.join(temp,'missing-start-date.xlsx');await b.xlsx.writeFile(f);
 const r=await dumpster({...dump,pmStart:f});assert.equal(r.blocks[0].rows.length,1);assert.equal(r.blocks[0].rows[0].jobNumber,'26-0101-CND');assert.ok(r.issues.some(i=>/Missing Start Date/.test(i.reason)));
});
test('unknown GAS job type cannot receive an invented Inventory allocation',async()=>{
 const file=path.join(temp,'unknown-type.csv');await fs.writeFile(file,headers+'2026-10-05,Contents,Synthetic,26-0001-UNKNOWN,2,Test,Employee\n');
 await assert.rejects(()=>inventory({...io,timesheet:file}),/company profile cannot resolve/);
});
