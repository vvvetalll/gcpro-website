import fs from 'node:fs/promises';
import path from 'node:path';
import assert from 'node:assert/strict';
import {sharedRuntime,sha256} from './shared-runtime.mjs';

const numeric=value=>Number(value.toString());
const currency='$#,##0.00;[Red]($#,##0.00)';
function table(book,name,headers,rows,m,widths={}) {
  const sheet=book.addWorksheet(name);sheet.addRow(headers);sheet.addRows(rows.map(row=>row.map(value=>value===''?null:value)));
  m.applyTablePresentation(sheet,{maxColumnWidth:55,columns:widths});
  sheet.views=[{state:'frozen',ySplit:1,showGridLines:false}];
  sheet.eachRow(row=>row.eachCell(cell=>{cell.font={...cell.font,name:'Arial',size:10};cell.alignment={...cell.alignment,vertical:'middle'};}));
  sheet.getRow(1).height=44;
  return sheet;
}
function groupRows(block) {
  return block.rows.map(row=>[block.department,row.jobNumber,row.customer||row.jobNumber,
    numeric(row.weight),block.denominator.isZero()?0:numeric(row.weight.div(block.denominator)),numeric(row.allocated),row.services||'',row.sourceRows.join(', ')]);
}

export async function writeReport(model,output) {
  const m=await sharedRuntime(),book=new m.exceljs_workbook_default.Workbook;
  book.creator='GCPRO';book.subject=model.workflow+' accounting '+model.month;
  book.description='Report month '+model.month+'. Amounts are final whole-cent allocations from the existing GCPRO proportional allocator.';
  const widths={1:{minWidth:14,maxWidth:17},2:{minWidth:17,maxWidth:22},3:{minWidth:36,maxWidth:55,wrapText:true},4:{minWidth:17,numberFormat:'0.00'},5:{minWidth:14,numberFormat:'0.0000%'},6:{minWidth:18,numberFormat:currency},7:{minWidth:20,maxWidth:35,wrapText:true},8:{minWidth:18,maxWidth:40,wrapText:true}};
  const headers=['Department','Job Number','Customer / Job','Eligible hours / Estimate weight','Share','Allocated expense (USD)','Service / Basis','Source rows'];
  const bySheet=model.workflow==='inventory'?[['Inventory',model.blocks]]:[['CON&MIT',model.blocks.filter(b=>b.department!=='Construction')],['Construction',model.blocks.filter(b=>b.department==='Construction')]];
  for(const [name,blocks]of bySheet){
    const columns=[...headers];columns[3]=name==='Construction'?'Total Estimates (USD)':'Eligible hours';
    const sheet=table(book,name,columns,blocks.flatMap(groupRows),m,widths);
    const total=sheet.addRow(['Grand Total',null,null,blocks.reduce((sum,b)=>sum.plus(b.denominator),new m.Decimal(0)).toNumber(),null,blocks.reduce((sum,b)=>sum.plus(b.allocated),new m.Decimal(0)).toNumber()]);
    m.styleSummaryRow(total);total.getCell(4).numFmt='0.00';total.getCell(6).numFmt=currency;
  }
  const recRows=model.blocks.map(b=>[b.department,model.month,b.basis,numeric(b.source),numeric(b.allocated),numeric(b.held),numeric(b.source.minus(b.allocated).minus(b.held)),b.status]);
  const reviewCount=model.issues.length;
  const overall=model.blocks.some(b=>b.status==='FAIL')?'FAIL':reviewCount?'REVIEW REQUIRED':'PASS';
  const rec=table(book,'Reconciliation',['Department','Report month','Allocation basis','Source expense (USD)','Allocated (USD)','Held (USD)','Difference (USD)','Status'],recRows,m,
    {1:{minWidth:16},2:{minWidth:14},3:{minWidth:38,maxWidth:58,wrapText:true},4:{minWidth:20,numberFormat:currency},5:{minWidth:20,numberFormat:currency},6:{minWidth:18,numberFormat:currency},7:{minWidth:20,numberFormat:currency},8:{minWidth:22}});
  const sums=col=>model.blocks.reduce((n,b)=>n.plus(b[col]),new m.Decimal(0));
  const total=rec.addRow(['Grand Total',model.month,null,numeric(sums('source')),numeric(sums('allocated')),numeric(sums('held')),0,overall]);m.styleSummaryRow(total);
  for(let c=4;c<=7;c++)total.getCell(c).numFmt=currency;
  rec.addRow([]);rec.addRow(['Timesheet hours','Source','Included project hours','Excluded hours','Review hours','Difference']);
  const hoursRow=rec.addRow(['Hours',numeric(model.hours.sourceHours),numeric(model.hours.aggregation.projectHours),numeric(model.hours.aggregation.excludedHours),numeric(model.hours.aggregation.reviewHours),numeric(model.hours.hourDifference)]);
  hoursRow.eachCell((cell,column)=>{if(column>1)cell.numFmt='0.00';});
  rec.addRow(['Review records',reviewCount]);
  rec.addRow(['Rounding','Existing GAS largest-remainder allocator; stable Job Number tie order; exact whole cents.']);
  if(model.workflow==='inventory')rec.addRow(['Inventory policy','One common monthly pool across all GAS-eligible job hours. Historical separate department pools are not reproduced.']);
  if(model.constructionRule)rec.addRow(['Construction eligibility',model.constructionRule]);
  if(model.sampleNote)rec.addRow(['Sample scope',model.sampleNote]);
  rec.addRow(['Inputs',...model.sources.map(s=>s.file.sourceFilename)]);
  const review=table(book,'Review Required',['Source','Source row','Job Number','Reason'],model.issues.map(i=>[i.source,i.row,i.job,i.reason]),m,{1:{minWidth:20},2:{minWidth:16},3:{minWidth:20},4:{minWidth:60,maxWidth:90,wrapText:true}});
  const excluded=table(book,'Excluded Hours',['Source row','Service Item','Job Code 1','Job Code 2','Hours','Exclusion reason'],model.exclusions.map(c=>[c.row.sourceRow,c.row.serviceItem,c.row.jobCode1,c.row.jobCode2,numeric(c.row.hours),c.reason]),m,{1:{minWidth:14},2:{minWidth:24},3:{minWidth:32,maxWidth:50,wrapText:true},4:{minWidth:20,maxWidth:40,wrapText:true},5:{numberFormat:'0.00'},6:{minWidth:45,maxWidth:65,wrapText:true}});
  // Give long reasons and source-row lists room without shrinking type.
  for(const sheet of [review,excluded,...bySheet.map(([name])=>book.getWorksheet(name))])sheet.eachRow((r,i)=>{if(i>1)r.height=Math.max(18,...r.values.filter(x=>typeof x==='string').map(x=>Math.ceil(x.length/48)*14));});
  rec.getColumn(1).width=24;rec.getColumn(1).alignment={wrapText:true,vertical:'middle'};
  rec.getColumn(2).width=55;rec.getColumn(2).alignment={wrapText:true,vertical:'middle'};
  rec.eachRow((r,i)=>{if(i>model.blocks.length+2){const text=String(r.getCell(2).value||'');r.height=Math.max(32,Math.ceil(text.length/50)*15+8);}});
  const name=(model.workflow==='inventory'?'Inventory':'Dumpster')+'_'+model.month+'.xlsx';
  await fs.mkdir(output,{recursive:true});const file=path.resolve(output,name);
  const bytes=Buffer.from(await book.xlsx.writeBuffer());await fs.writeFile(file,bytes,{flag:'wx'});
  const verification=await verifyReport(file,model);
  return {success:true,workflow:model.workflow,reportMonth:model.month,outputPath:file,outputSha256:sha256(bytes),runnerVersion:'1.2.0',gasRuntimeUnchanged:true,overallStatus:overall,
    pools:model.blocks.map(b=>({department:b.department,source:b.source.toFixed(2),allocated:b.allocated.toFixed(2),held:b.held.toFixed(2),difference:b.source.minus(b.allocated).minus(b.held).toFixed(2),weight:b.denominator.toString(),jobs:b.rows.length})),reviewRequiredCount:reviewCount,verification};
}

export async function verifyReport(file,model) {
  const m=await sharedRuntime(),book=new m.exceljs_workbook_default.Workbook;await book.xlsx.readFile(file);
  const expected=model.workflow==='inventory'?['Inventory','Reconciliation','Review Required','Excluded Hours']:['CON&MIT','Construction','Reconciliation','Review Required','Excluded Hours'];
  assert.deepEqual(book.worksheets.map(s=>s.name),expected);
  for(const [name,blocks] of (model.workflow==='inventory'?[['Inventory',model.blocks]]:[['CON&MIT',model.blocks.filter(b=>b.department!=='Construction')],['Construction',model.blocks.filter(b=>b.department==='Construction')]])){
    const sheet=book.getWorksheet(name),last=sheet.getRow(sheet.rowCount);
    assert.equal(sheet.rowCount,blocks.reduce((n,b)=>n+b.rows.length,0)+2);
    assert.equal(last.getCell(1).value,'Grand Total');
    assert.ok(new m.Decimal(last.getCell(6).value).eq(blocks.reduce((sum,b)=>sum.plus(b.allocated),new m.Decimal(0))));
  }
  for(const block of model.blocks){
    const sheet=book.getWorksheet(model.workflow==='inventory'?'Inventory':block.department==='Construction'?'Construction':'CON&MIT');
    const rows=[];sheet.eachRow((row,n)=>{if(n>1&&row.getCell(1).value===block.department)rows.push(row);});
    assert.equal(rows.length,block.rows.length);const seen=new Set();let total=new m.Decimal(0),weight=new m.Decimal(0);
    for(const row of rows){const key=row.getCell(2).value;assert.ok(!seen.has(key),'Duplicate job expense: '+key);seen.add(key);
      const source=block.rows.find(x=>x.jobNumber===key);assert.ok(source);assert.ok(new m.Decimal(row.getCell(4).value).eq(source.weight));assert.ok(new m.Decimal(row.getCell(6).value).eq(source.allocated));
      total=total.plus(row.getCell(6).value);weight=weight.plus(row.getCell(4).value);
    }
    assert.ok(total.eq(block.allocated));assert.ok(weight.eq(block.denominator));assert.ok(total.plus(block.held).eq(block.source));
    assert.ok(block.source.minus(block.allocated).minus(block.held).isZero());
    const index=model.blocks.indexOf(block)+2,rec=book.getWorksheet('Reconciliation').getRow(index);
    assert.ok(new m.Decimal(rec.getCell(4).value).eq(block.source));assert.ok(new m.Decimal(rec.getCell(5).value).eq(total));assert.ok(new m.Decimal(rec.getCell(6).value).eq(block.held));assert.equal(rec.getCell(8).value,block.status);
  }
  assert.equal(book.getWorksheet('Review Required').rowCount-1,model.issues.length);
  for(const sheet of book.worksheets)sheet.eachRow(row=>row.eachCell(cell=>assert.ok(!(cell.value&&typeof cell.value==='object'&&'error' in cell.value),'Spreadsheet error at '+sheet.name+'!'+cell.address)));
  return {success:true,worksheetNames:expected,verifiedJobRows:model.blocks.reduce((n,b)=>n+b.rows.length,0),exactCentReconciliation:true};
}
