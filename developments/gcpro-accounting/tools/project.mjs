import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {spawnSync} from 'node:child_process';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const skill=path.join(root,'plugin/skills/gcpro-accounting');
const engine=path.join(skill,'engine');
const gasDigest='8D461CB3189DFEE5C12373642DDBE8009151C9969551C352980D0439C0F03948';
const files=['scripts/run-accounting.mjs','scripts/shared-runtime.mjs','scripts/workflows.mjs','scripts/report-workbook.mjs','tests/accounting.test.mjs','references/accounting-workflows.md'];
const args=process.argv.slice(2),command=args[0]||'check';
const option=name=>{const at=args.indexOf(name);return at<0?null:args[at+1];};
const sha=bytes=>createHash('sha256').update(bytes).digest('hex').toUpperCase();
function run(program,args,options={}){
 const p=spawnSync(program,args,{encoding:'utf8',windowsHide:true,...options});
 if(p.error)throw p.error;
 if(p.status)throw new Error((p.stdout||'')+(p.stderr||'')||'Command failed: '+program);
 return p.stdout;
}
async function prepare(){
 const source=option('--engine');
 if(source){
  if(path.resolve(source)===engine)throw new Error('Engine source must be outside the destination.');
  try{await fs.access(engine);throw new Error('Private engine already exists; do not overwrite it.');}catch(e){if(e.code!=='ENOENT')throw e;}
  const bytes=await fs.readFile(path.join(source,'scripts/dist/run-gas-report.mjs'));
  if(sha(bytes)!==gasDigest)throw new Error('Supplied private engine does not match the pinned GAS release.');
  await fs.cp(source,engine,{recursive:true,errorOnExist:true});
 }
 let bytes;try{bytes=await fs.readFile(path.join(engine,'scripts/dist/run-gas-report.mjs'));}catch{throw new Error('Private GAS payload is not committed to this public repository. Obtain the authorized 1.1.6 engine directory privately and run with --engine ABSOLUTE_DIRECTORY.');}
 if(sha(bytes)!==gasDigest)throw new Error('GAS engine changed; no rebuild or accounting replacement is allowed.');
 let manifest='';for(const file of [...files].sort())manifest+=sha(await fs.readFile(path.join(skill,file)))+'  '+file+'\n';
 await fs.writeFile(path.join(skill,'references/accounting-manifest.sha256'),manifest);
 const meta=await fs.readFile(path.join(skill,'SKILL.md'),'utf8');
 if(!meta.startsWith('---\nname: gcpro-accounting\n'))throw new Error('Renamed Skill metadata is invalid.');
 const agent=await fs.readFile(path.join(skill,'agents/openai.yaml'),'utf8');
 if(!/display_name:\s*['"]?GCPRO Accounting['"]?\s*$/m.test(agent)||!agent.includes('$gcpro-accounting'))throw new Error('Skill invocation metadata is not renamed.');
 const primary=JSON.parse(await fs.readFile(path.join(root,'plugin/plugin.json'),'utf8'));
 const compat=JSON.parse(await fs.readFile(path.join(root,'plugin/.codex-plugin/plugin.json'),'utf8'));
 if(primary.version!==compat.version||JSON.stringify(primary.extensions['com.openai'].interface)!==JSON.stringify(compat.interface))throw new Error('Plugin manifests disagree.');
 if(compat.interface.displayName!=='GCPRO Accounting')throw new Error('Plugin display name is not renamed.');
 const result=JSON.parse(run(process.execPath,[path.join(skill,'scripts/run-accounting.mjs'),'--verify-distribution']));
 if(!result.success)throw new Error('Runtime verification failed.');
 return result;
}
async function tests(){
 const gasTests=(await fs.readdir(path.join(engine,'tests'))).filter(f=>f.endsWith('.test.mjs')).sort().map(f=>path.join(engine,'tests',f));
 const p=spawnSync(process.execPath,['--test',path.join(skill,'tests/accounting.test.mjs'),...gasTests],{encoding:'utf8',windowsHide:true});
 await fs.mkdir(path.join(root,'test-results'),{recursive:true});
 await fs.writeFile(path.join(root,'test-results/latest.txt'),(p.stdout||'')+(p.stderr||''));
 if(p.error)throw p.error;if(p.status)throw new Error('Tests failed; details remain in ignored test-results/latest.txt.');
 const count=/(?:tests\s+)(\d+)/.exec(p.stdout)?.[1];
 let baselineComparison='not run';
 const baseline=option('--baseline')||path.join(root,'private-validation/baseline-engine/scripts/dist/run-gas-report.mjs');
 try{await fs.access(baseline);
  const text=run(process.execPath,[path.join(engine,'tests/runtime.test.mjs'),baseline]);
  await fs.writeFile(path.join(root,'test-results/gas-baseline.txt'),text);baselineComparison='zero populated-cell differences across nine sheets';
 }catch(e){if(e.code!=='ENOENT')throw e;}
 const summary={success:true,tests:Number(count),failures:0,baselineComparison,gasRunnerSha256:gasDigest};
 await fs.writeFile(path.join(root,'test-results/summary.json'),JSON.stringify(summary,null,2)+'\n');
 return summary;
}
try{
 const verification=await prepare();
 if(!['check','test','package'].includes(command))throw new Error('Use check, test, or package.');
 const result=command==='check'?verification:await tests();
 if(command==='package'){
  const python=process.env.PYTHON||'python';
  process.stdout.write(run(python,[path.join(root,'tools/package.py')]));
 }
 process.stdout.write(JSON.stringify(result,null,2)+'\n');
}catch(e){process.stderr.write(e.message+'\n');process.exitCode=1;}
