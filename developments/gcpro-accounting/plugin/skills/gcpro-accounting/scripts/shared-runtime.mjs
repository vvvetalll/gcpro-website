import fs from 'node:fs/promises';
import path from 'node:path';
import os from 'node:os';
import {fileURLToPath, pathToFileURL} from 'node:url';
import {createHash} from 'node:crypto';
import {execFileSync} from 'node:child_process';

export const skillRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
export const gasRunner = path.join(skillRoot, 'engine/scripts/dist/run-gas-report.mjs');
export const gasSha256 = '8D461CB3189DFEE5C12373642DDBE8009151C9969551C352980D0439C0F03948';
export const sha256 = bytes => createHash('sha256').update(bytes).digest('hex').toUpperCase();
export const protectedFiles = Object.freeze([
  'scripts/run-accounting.mjs', 'scripts/shared-runtime.mjs', 'scripts/workflows.mjs',
  'scripts/report-workbook.mjs', 'tests/accounting.test.mjs', 'references/accounting-workflows.md'
]);
export async function verifyDistribution() {
  const lines=(await fs.readFile(path.join(skillRoot,'references/accounting-manifest.sha256'),'utf8')).trim().split(/\r?\n/);
  const entries=new Map();
  for(const line of lines){
    const m=/^([A-Fa-f0-9]{64})  (.+)$/.exec(line);
    if(!m||!protectedFiles.includes(m[2])||entries.has(m[2]))throw new Error('Invalid accounting manifest entry: '+line);
    entries.set(m[2],m[1].toUpperCase());
  }
  if(entries.size!==protectedFiles.length)throw new Error('Incomplete accounting manifest.');
  for(const file of protectedFiles){
    const target=path.join(skillRoot,file);
    if(!(await fs.lstat(target)).isFile()||sha256(await fs.readFile(target))!==entries.get(file))throw new Error('Accounting hash mismatch: '+file);
  }
  if(sha256(await fs.readFile(gasRunner))!==gasSha256)throw new Error('Protected GAS runtime differs from the pinned 1.1.6 release.');
  const gas=JSON.parse(execFileSync(process.execPath,[gasRunner,'--verify-distribution'],{encoding:'utf8',windowsHide:true}));
  if(!gas.success)throw new Error('GAS payload verification failed.');
  return {success:true,workflowFiles:entries.size,gas};
}

let cached;
export async function sharedRuntime() {
  if(cached)return cached;
  cached=(async()=>{
    // Existing GAS tests expose these same bundled functions this way. The
    // protected file remains untouched. No bundler, eval of inputs or npm deps.
    await verifyDistribution();
    let source=await fs.readFile(gasRunner,'utf8');
    const relative='from "./dynamic-participants.mjs"';
    const cli='try{let args2=process.argv.slice(2)';
    if(source.split(relative).length!==2||source.split(cli).length!==2)throw new Error('Unsupported GAS runtime adapter boundary.');
    source=source.replace(relative,`from ${JSON.stringify(pathToFileURL(path.join(path.dirname(gasRunner),'dynamic-participants.mjs')).href)}`);
    const exports=['init_monthly_accounting','init_work_hours','init_workbook_presentation','init_dash_jobs','init_detector','exceljs_workbook_default','Decimal','buildWorkHoursDataset','readTimesheetInput','detectAccountingInput','generateDashJobsDataset','GCPRO_COMPANY_PROFILE','GCPRO_EMPLOYEE_HOURS_MAPPINGS','GCPRO_CLASS_HOURS_POLICY','allocateProportionally','timesheetJobNumber','parseJobNumber','parseDate','applyTablePresentation','styleSummaryRow','normalizeHeaderName','isInReportMonth','buildConMitAllocationDataset'];
    source=source.replace(cli,`export {${exports.join(',')}};if(false)${cli}`);
    const temp=await fs.mkdtemp(path.join(os.tmpdir(),'gcpro-shared-runtime-'));
    try{
      const modulePath=path.join(temp,'verified-runtime.mjs');await fs.writeFile(modulePath,source);
      const m=await import(pathToFileURL(modulePath));
      m.init_monthly_accounting();m.init_work_hours();m.init_workbook_presentation();m.init_dash_jobs();m.init_detector();
      return m;
    }finally{await fs.rm(temp,{recursive:true,force:true});}
  })();
  return cached;
}

export async function readInput(filePath,type,m) {
  const absolute=path.resolve(filePath),ext=path.extname(absolute).toLowerCase();
  const mime={'.csv':'text/csv','.xlsx':'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet','.xlsm':'application/vnd.ms-excel.sheet.macroEnabled.12'}[ext];
  if(!mime)throw new Error('Unsupported input extension: '+ext);
  const file={sourceId:absolute,sourceFilename:path.basename(absolute),contentMimeType:mime,bytes:new Uint8Array(await fs.readFile(absolute))};
  const detection=await m.detectAccountingInput(file);
  if(detection.detectedType!==type||detection.ambiguousSignals.length)throw new Error('Expected '+type+' in '+file.sourceFilename+': '+JSON.stringify(detection));
  return {file,detection};
}
