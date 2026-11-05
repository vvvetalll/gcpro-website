// Portable renderer for the seven current Commercial / PGP templates.
const fs=require('fs'),path=require('path'),http=require('http');
const {chromium}=require(process.env.GCPRO_PLAYWRIGHT_PATH||'playwright');
const root=path.resolve(__dirname,'..');
const arg=process.argv.indexOf('--output');const output=arg>=0?path.resolve(process.argv[arg+1]):path.join(root,'rebuilt');
const intermediate=path.join(output,'.render');fs.mkdirSync(intermediate,{recursive:true});
const cases=JSON.parse(fs.readFileSync(path.join(root,'documents.json'),'utf8'));
const mime={'.svg':'image/svg+xml','.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.html':'text/html','.css':'text/css','.woff2':'font/woff2','.js':'text/javascript','.json':'application/json'};
(async()=>{const browser=await chromium.launch({headless:true,...(process.env.GCPRO_BROWSER_CHANNEL?{channel:process.env.GCPRO_BROWSER_CHANNEL}:{})});
try{for(const c of cases){const source=path.resolve(root,c.source);const server=http.createServer((req,res)=>{let file;try{file=path.resolve(source,'.'+decodeURIComponent(req.url.split('?')[0]));}catch{res.writeHead(400);return res.end()}
if(!file.startsWith(source+path.sep)){res.writeHead(403);return res.end()}
fs.readFile(file,(err,data)=>{if(err){res.writeHead(404);return res.end()}res.setHeader('Content-Type',mime[path.extname(file)]||'application/octet-stream');res.end(data)})});
await new Promise(r=>server.listen(0,'127.0.0.1',r));const p=await browser.newPage({viewport:{width:1100,height:1100}});
try{await p.goto(`http://127.0.0.1:${server.address().port}/index.html`);await p.evaluate(()=>document.fonts.ready);await p.evaluate(async()=>{if(window.__layout)await window.__layout()});await p.evaluate(()=>document.fonts.ready);
if(await p.locator(c.selector).count()!==c.pages)throw Error('Page count mismatch: '+c.id);
const broken=await p.locator('img').evaluateAll(imgs=>imgs.filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src));if(broken.length)throw Error('Missing images: '+broken.join(', '));
await p.pdf({path:path.join(intermediate,c.id+'.pdf'),preferCSSPageSize:true,printBackground:true});
const fields=await p.evaluate(sel=>[...document.querySelectorAll(sel)].flatMap((section,page)=>{const box=section.getBoundingClientRect();return [...section.querySelectorAll('[data-field]')].map(e=>{const r=e.getBoundingClientRect();return{page,name:e.dataset.name,type:e.dataset.field,x:r.left-box.left,y:r.top-box.top,w:r.width,h:r.height}})}),c.selector);
if(fields.length!==c.fields)throw Error('Field count mismatch: '+c.id);
fs.writeFileSync(path.join(intermediate,c.id+'-fields.json'),JSON.stringify(fields,null,2));console.log(c.id+': rendered '+c.pages+' pages, '+fields.length+' fields');
}finally{await p.close();await new Promise(r=>server.close(r))}}
}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
