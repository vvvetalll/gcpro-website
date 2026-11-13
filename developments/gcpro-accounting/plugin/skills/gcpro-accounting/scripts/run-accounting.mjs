import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {spawnSync} from 'node:child_process';
import {verifyDistribution,gasRunner} from './shared-runtime.mjs';
import {inventory,dumpster} from './workflows.mjs';
import {writeReport} from './report-workbook.mjs';

export async function main(args=process.argv.slice(2)) {
  if(args.length===1&&args[0]==='--verify-distribution')return verifyDistribution();
  if(args.length%2)throw new Error('Use --name value argument pairs.');
  const flags=new Map();for(let i=0;i<args.length;i+=2){if(!args[i].startsWith('--')||flags.has(args[i]))throw new Error('Invalid or duplicate argument: '+args[i]);flags.set(args[i],args[i+1]);}
  const workflow=flags.get('--workflow');
  if(!['gas','dumpster','inventory'].includes(workflow))throw Object.assign(new Error('Which accounting report: gas, dumpster, or inventory?'),{code:'workflow_required'});
  await verifyDistribution();
  if(workflow==='gas'){
    const pass=args.filter((_,i)=>i!==args.indexOf('--workflow')&&i!==args.indexOf('--workflow')+1);
    const result=spawnSync(process.execPath,[gasRunner,...pass],{stdio:'inherit',windowsHide:true});
    if(result.error)throw result.error;process.exitCode=result.status;return null;
  }
  const allowed=workflow==='inventory'?['--workflow','--timesheet','--month','--total','--output']:['--workflow','--timesheet','--month','--construction','--contents','--mitigation','--pm-start','--output'];
  for(const key of flags.keys())if(!allowed.includes(key))throw new Error('Unneeded or unknown '+workflow+' argument: '+key);
  const required=workflow==='inventory'?['--timesheet','--month','--total','--output']:['--month','--construction','--contents','--mitigation','--output'];
  for(const key of required)if(!flags.has(key))throw Object.assign(new Error('Missing '+workflow+' input: '+key),{code:'input_required',requiredInput:key});
  const options=Object.fromEntries([...flags].map(([k,v])=>[k.slice(2).replace(/-([a-z])/g,(_,l)=>l.toUpperCase()),v]));
  const model=await (workflow==='inventory'?inventory:dumpster)(options);
  return writeReport(model,path.resolve(options.output));
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
  try{const result=await main();if(result)process.stdout.write(JSON.stringify(result,null,2)+'\n');}
  catch(error){process.stderr.write(JSON.stringify({success:false,code:error.code||'accounting_failed',message:error.message,requiredInput:error.requiredInput},null,2)+'\n');process.exitCode=1;}
}
