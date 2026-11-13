import fs from 'node:fs/promises';
import {sharedRuntime,readInput} from './shared-runtime.mjs';

export function amount(value,Decimal,label='expense') {
  if(typeof value!=='string'||!/^\d+(?:\.\d{1,2})?$/.test(value))throw new Error(label+' must be a nonnegative decimal amount with at most two decimal places.');
  const result=new Decimal(value);
  if(!result.isFinite()||result.gt('9000000000000'))throw new Error(label+' is outside the supported amount range.');
  return result;
}
const keySort=(a,b)=>a.jobNumber<b.jobNumber?-1:a.jobNumber>b.jobNumber?1:0;
export async function readHours(file,month,m) {
  if(!/^\d{4}-(0[1-9]|1[0-2])$/.test(month||''))throw new Error('A report month in YYYY-MM format is required.');
  const input=await readInput(file,'timesheet',m);
  const normalized=await m.readTimesheetInput(input);
  const hours=m.buildWorkHoursDataset({...normalized,additionalInternalCodes:[],employeeHoursMappings:m.GCPRO_EMPLOYEE_HOURS_MAPPINGS});
  const dateColumn=hours.parsed.sourceHeaders.findIndex(h=>['date','localdate','workdate'].includes(m.normalizeHeaderName(h)));
  if(dateColumn<0&&hours.parsed.rows.length)throw new Error('Timesheet requires a date column to establish the report month.');
  for(const row of hours.parsed.rows){
    const date=m.parseDate(row.sourceValues[dateColumn]);
    if(!date||!m.isInReportMonth(date,month))throw new Error('Timesheet row '+row.sourceRow+' has a missing, invalid or out-of-period date.');
  }
  return {hours,input};
}

export function allocate(pool,jobs,m) {
  for(const job of jobs)if(!job.weight.isFinite()||job.weight.isNegative())throw new Error('Allocation weights must be finite and nonnegative.');
  const allocation=m.allocateProportionally(pool,[...jobs].sort(keySort).map(job=>({value:job,weight:job.weight})));
  return {source:pool,allocated:allocation.allocated,held:allocation.difference,denominator:allocation.denominator,
    rows:allocation.allocations.map(a=>({...a.value,allocated:a.amount})),status:allocation.difference.isZero()?'PASS':'FAIL'};
}

export async function inventory(options) {
  const m=await sharedRuntime(),pool=amount(options.total,m.Decimal,'Inventory total');
  const {hours,input}=await readHours(options.timesheet,options.month,m);
  const jobs=new Map();
  for(const group of hours.aggregation.projectGroups){
    const jobNumber=m.timesheetJobNumber(group.jobCode2,m.GCPRO_COMPANY_PROFILE.jobNumber);
    if(!jobNumber)throw new Error('An eligible timesheet group has no canonical job number.');
    if(m.parseJobNumber(jobNumber,m.GCPRO_COMPANY_PROFILE.jobNumber).jobTypeCode===null)throw new Error('The existing GAS company profile cannot resolve this eligible job type: '+jobNumber+'. Correct or confirm the source classification before allocating Inventory.');
    const existing=jobs.get(jobNumber)||{jobNumber,customer:group.combinedProject,weight:new m.Decimal(0),services:new Set(),sourceRows:[]};
    existing.weight=existing.weight.plus(group.hours);existing.services.add(group.serviceItem);jobs.set(jobNumber,existing);
  }
  for(const c of hours.classifications.filter(c=>c.kind==='project')){
    jobs.get(m.timesheetJobNumber(c.row.jobCode2,m.GCPRO_COMPANY_PROFILE.jobNumber))?.sourceRows.push(c.row.sourceRow);
  }
  const result=allocate(pool,[...jobs.values()].map(j=>({...j,services:[...j.services].join('; ')})),m);
  return {workflow:'inventory',month:options.month,blocks:[{department:'Inventory',basis:'Eligible hours',...result}],hours,input,
    issues:hours.aggregation.reviewRows.map(c=>({source:'Timesheet',row:c.row.sourceRow,job:c.row.jobCode2,reason:c.reason})),
    exclusions:hours.classifications.filter(c=>c.kind==='excluded'),sources:[input]};
}

export async function dumpster(options) {
  const m=await sharedRuntime();
  const pools=Object.fromEntries(['construction','contents','mitigation'].map(k=>[k,amount(options[k],m.Decimal,k+' Dumpster total')]));
  if(!/^\d{4}-(0[1-9]|1[0-2])$/.test(options.month||''))throw new Error('A report month in YYYY-MM format is required.');
  if(!options.timesheet&&(!pools.contents.isZero()||!pools.mitigation.isZero()))throw new Error('Timesheet is required for nonzero Contents or Mitigation expenses.');
  const {hours,input}=options.timesheet?await readHours(options.timesheet,options.month,m):{hours:m.buildWorkHoursDataset({csvBytes:new TextEncoder().encode('Date,Service Item,Job Code 2,Hours\n'),sheetName:'Sheet1',headerRow:1,additionalInternalCodes:[],employeeHoursMappings:m.GCPRO_EMPLOYEE_HOURS_MAPPINGS}),input:null};
  // Feed department expense pools to the existing CON/MIT allocator's established
  // pool interface. These are supplied expenses, not fabricated QB transactions.
  const totalsByClass=new Map([['Contents',pools.contents],['Mitigation',pools.mitigation]]);
  const quickBooks={records:[...totalsByClass].map(([departmentOrClass,amount])=>({vehicleOrName:'Dumpster departmental expense',departmentOrClass,amount})),reviewRows:[],
    aggregation:{totalsByClass,totalsByVehicleAndClass:new Map([...totalsByClass].map(([cls,value])=>[JSON.stringify(['Dumpster departmental expense',cls]),value])),validAmount:pools.contents.plus(pools.mitigation)},
    reconciliation:{status:'PASS',amountDifference:new m.Decimal(0),recordDifference:0,unreadableMonetaryRows:0}};
  const existing=m.buildConMitAllocationDataset({workHours:hours,quickBooks,totalTollPool:new m.Decimal(0),policy:m.GCPRO_CLASS_HOURS_POLICY,companyProfile:m.GCPRO_COMPANY_PROFILE});
  const blocks=existing.blocks.map(b=>({department:b.id,basis:'Eligible hours',source:b.gasPool,allocated:b.allocatedGas,held:b.gasPool.minus(b.allocatedGas),denominator:b.reconciliation.allocatedHours,
    status:b.gasPool.eq(b.allocatedGas)?'PASS':'FAIL',rows:b.jobs.map(j=>({jobNumber:j.jobNumber,customer:j.jobNumber,weight:j.hours,allocated:j.gasAllocation,sourceRows:j.sourceRows,services:b.id}))}));
  const issues=hours.aggregation.reviewRows.map(c=>({source:'Timesheet',row:c.row.sourceRow,job:c.row.jobCode2,reason:c.reason}));
  issues.push(...existing.issues.filter(i=>i.code!=='UNMAPPED_PROJECT_SERVICE_ITEM').map(i=>({source:'CON/MIT allocator',row:(i.sourceRows||[]).join(', '),job:i.jobNumber||'',reason:i.code})));
  if(pools.construction.isZero()&&!options.pmStart){
    blocks.unshift({department:'Construction',basis:'No expense',...allocate(pools.construction,[],m)});
    return {workflow:'dumpster',month:options.month,blocks,hours,input,issues,exclusions:hours.classifications.filter(c=>c.kind==='excluded'),sources:[input].filter(Boolean)};
  }
  if(!options.pmStart)throw new Error('PM Start is required for a nonzero Construction Dumpster expense.');
  const start=await readInput(options.pmStart,'dash_jobs',m);
  const dataset=await m.generateDashJobsDataset([start]);
  if(dataset.conflicts.length||dataset.reviewIssues.length)throw new Error('PM Start contains conflicting or invalid fields: '+JSON.stringify({conflicts:dataset.conflicts,issues:dataset.reviewIssues}));
  const jobs=dataset.jobs.filter(job=>{
    const construction=['CIP','CND','CNI'].includes(m.parseJobNumber(job.jobNumber,m.GCPRO_COMPANY_PROFILE.jobNumber).jobTypeCode);
    if(construction&&!job.dates.started)issues.push({source:'PM Start',row:job.sources.map(s=>s.sourceRow).join(', '),job:job.jobNumber,reason:'Missing Start Date; cannot establish monthly Construction eligibility.'});
    return construction&&m.isInReportMonth(job.dates.started,options.month);
  }).map(job=>{
    const jobNumber=job.jobNumber;
    if(job.totalEstimate===null||!job.totalEstimate.isFinite()||job.totalEstimate.isNegative())throw new Error('Selected job has a missing or invalid Total Estimates value: '+jobNumber);
    return {jobNumber,customer:job.customer||jobNumber,weight:job.totalEstimate,services:'Construction',sourceRows:job.sources.map(s=>s.sourceRow)};
  });
  blocks.unshift({department:'Construction',basis:'Total Estimates — monthly PM Start jobs',...allocate(pools.construction,jobs,m)});
  return {workflow:'dumpster',month:options.month,blocks,hours,input,issues,exclusions:hours.classifications.filter(c=>c.kind==='excluded'),sources:[input,start].filter(Boolean),constructionRule:'Construction Job Numbers CIP/CND/CNI with Start Date in the report month; confirmed by the user. One global Total Estimates denominator.'};
}
