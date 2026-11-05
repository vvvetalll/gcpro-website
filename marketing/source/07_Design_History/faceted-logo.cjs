const fs=require('fs');const path=require('path');const {pathToFileURL}=require('url');
const {chromium}=require('C:/Users/VitaliiVozniak/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const root=path.resolve('outputs');
function clean(svg){return svg.replace(/<path[^>]+stroke="black"[^>]*>/g,tag=>tag.replace(/M(641|276|855) (\d+) (783|396|980) (\d+)/g,(all,a,b,c,d)=>{a=+a;b=+b;c=+c;d=+d;const slope=(d-b)/(c-a);return `M${a-8} ${b-8*slope} ${c+8} ${d+8*slope}`;}));}
for(const file of fs.readdirSync(path.join(root,'GCPRO-PGP-Vector-Logo')).filter(x=>x.endsWith('.svg'))){const p=path.join(root,'GCPRO-PGP-Vector-Logo',file);fs.writeFileSync(p,clean(fs.readFileSync(p,'utf8')));}
let svg=fs.readFileSync(path.join(root,'GCPRO-PGP-Vector-Logo/pgp-mark.svg'),'utf8').replace(/\r\n/g,'\n');
const before=`<path d="M471 323 628 212V1100H471Z M641 222 783 325V1100H641Z"/>
<path d="M276 518 396 436V1100H276Z M410 426 458 455V1100H410Z"/>
<path d="M797 454 841 428V1100H797Z M855 438 980 521V1100H855Z"/>`;
const after=`<path d="M471 323 628 212V1100H471Z" fill="#40568f"/>
<path d="M641 222 783 325V1100H641Z" fill="#1a327d"/>
<path d="M276 518 396 436V1100H276Z" fill="#40568f"/>
<path d="M410 426 458 455V1100H410Z" fill="#13275f"/>
<path d="M797 454 841 428V1100H797Z" fill="#13275f"/>
<path d="M855 438 980 521V1100H855Z" fill="#40568f"/>`;
if(!svg.includes(before))throw new Error('Building geometry not found');
svg=svg.replace(before,after);
fs.writeFileSync(path.join(root,'GCPRO-PGP-faceted-idea.svg'),svg);
const html=`<!doctype html><meta charset="utf-8"><style>*{box-sizing:border-box}body{margin:0;background:#fff;color:#1a327d;font-family:Arial;padding:38px 60px;width:1000px}header{font-size:20px;font-weight:700;letter-spacing:1px}main{display:flex;justify-content:center}main img{width:770px;height:770px}footer{border-top:1px solid #e0e5ee;padding-top:24px;display:flex;align-items:center;gap:22px;font-size:17px}footer img{width:95px;height:95px}.swatches{margin-left:auto;display:flex;gap:8px}.swatches i{width:24px;height:24px;border-radius:50%}p{margin:0;line-height:1.5}</style><header>PROPERTY GUARDIAN PROGRAM</header><main><img src="GCPRO-PGP-faceted-idea.svg"></main><footer><img src="GCPRO-PGP-faceted-idea.svg"><p>Світліші фасади · темніші бічні грані<br>Основний синій та помаранчевий — збережені</p><div class="swatches"><i style="background:#13275f"></i><i style="background:#1a327d"></i><i style="background:#40568f"></i><i style="background:#f05a29"></i></div></footer>`;
fs.mkdirSync('work/faceted-preview',{recursive:true});
fs.writeFileSync('work/faceted-preview/index.html',html.replaceAll('src="GCPRO-PGP-faceted-idea.svg"','src="'+pathToFileURL(path.join(root,'GCPRO-PGP-faceted-idea.svg')).href+'"'));
(async()=>{const b=await chromium.launch({channel:'msedge',headless:true});const p=await b.newPage({viewport:{width:1000,height:1000},deviceScaleFactor:1.5});await p.goto(pathToFileURL(path.resolve('work/faceted-preview/index.html')).href);await p.screenshot({path:path.join(root,'GCPRO-PGP-faceted-idea.png'),fullPage:true});await b.close()})();
