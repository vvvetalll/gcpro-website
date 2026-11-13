import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {execFileSync} from 'node:child_process';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const prefix='developments/gcpro-accounting/';
const names=execFileSync('git',['diff','--cached','--name-only','--diff-filter=ACMR'],{cwd:root,encoding:'utf8'}).trim().split('\n').filter(Boolean);
if(!names.length)throw new Error('No staged accounting files to inspect.');
for(const file of names){
 if(!file.startsWith(prefix))throw new Error('Change outside the authorized accounting directory: '+file);
 if(/(?:\/engine\/|\/private-validation\/|\/private-inputs\/|\/dist\/|\/test-results\/|\/node_modules\/)/.test(file))throw new Error('Private/generated path must not be committed: '+file);
 if(/\.(?:xls[xm]?|csv|zip|tar\.gz|png|jpe?g|pdf)$/i.test(file)||/(?:^|\/)(?:auth\.json|\.env)$/.test(file))throw new Error('Source data, media or credential file staged: '+file);
 const bytes=execFileSync('git',['show',':'+file],{cwd:root,maxBuffer:4*1024*1024});
 if(bytes.length>200000)throw new Error('Unexpected large source file; inspect for embedded private payload: '+file);
 const text=bytes.toString('utf8');
 if(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i.test(text))throw new Error('Email address found; sanitize before publication: '+file);
 if(/(?:DASH_PASS|api[_-]?key|access[_-]?token)\s*[:=]\s*["'][^"']+["']/i.test(text))throw new Error('Possible embedded credential: '+file);
}
console.log(JSON.stringify({success:true,stagedFiles:names.length,scope:prefix,privatePathsExcluded:true}));
