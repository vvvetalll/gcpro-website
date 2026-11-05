import sys,types,importlib.util,shutil,json,re
from pathlib import Path
import pymupdf
root=Path.cwd();src=root/'work/kit/GCPRO_ASP_Kit_SOURCE';out=root/'outputs/GCPRO-PGP-ERP-Full-source';out.mkdir(exist_ok=True)
for name in ['assets','fonts']:shutil.copytree(src/name,out/name,dirs_exist_ok=True)
shutil.copy2(src/'kit.css',out/'kit.css')
p=pymupdf.open(r'C:/Users/VitaliiVozniak/Downloads/GC PRO FILL IN CSP PGP-ERP FULL (1).pdf')
shutil.copy2(root/'outputs/GCPRO-PGP-Pre-Authorization-source/assets/pgp-logo.png',out/'assets/pgp-logo.png')
stub=types.ModuleType('playwright.sync_api');stub.sync_playwright=lambda:None
sys.modules['playwright']=types.ModuleType('playwright');sys.modules['playwright.sync_api']=stub
spec=importlib.util.spec_from_file_location('kit',src/'build.py');kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit)
e=kit.e;k=kit.K
titles={1:'EMERGENCY RESPONSE PROGRAM',2:'PROPERTY GUARDIAN PROGRAM',3:'PROPERTY GUARDIAN PROGRAM',4:'PROPERTY GUARDIAN PROGRAM',5:'PROPERTY GUARDIAN PROGRAM',6:'Additional Locations Covered Under This ERP Agreement',7:'Emergency Contacts',8:'Emergency Response Team',9:'Insurance Information',10:'Key/Preferred Vendors',11:'Tenant/Occupant Profile',12:'Property Data Chart',13:'Property Data Chart',14:'Property Data Chart',15:'PROPERTY GUARDIAN PROGRAM'}
pages=[];records=[]
raw=json.loads((root/'work/pgp-erp-extracted.json').read_text(encoding='utf8'))
def content(*ids):return ' '.join(' '.join(raw[1]['blocks'][i]['text'] for i in ids).replace('•','').split())
overview={'intro':[content(i) for i in range(26,30)],'bullets':[content(i) for i in range(30,36)],'riskHeading':content(36,37),'risks':[content(40,41),content(47),content(42,43,44),content(45,46)],'benefitHeading':content(38,39),'benefits':[content(48,49,50),content(56,57,58),content(66,67),content(52,53),content(61,62,63),content(69,70,71),content(51),content(59,60),content(68),content(54,55),content(64,65),content(72)]}
for num,page in enumerate(p,1):
 allspans=[s for b in page.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
 spans=[]
 for s in allspans:
  x,y=s['origin'];txt=s['text'].replace('\t','').rstrip()
  if num==1:continue
  if num in [2,3,4,5,15] and y<108:continue
  if num in range(6,15) and y<80 and s['size']>16:continue
  if y>742 or 'Full PGP' in txt or 'ERP Full GEN' in txt:continue
  if not txt.strip():continue
  if num in [12,13,14] and txt.strip()=='o':continue
  spans.append({'x':x,'y':y,'box':s['bbox'],'size':s['size'],'text':txt,'bold':bool(s['flags']&16) or 'bold' in s['font'].lower(),'italic':bool(s['flags']&2),'light':s['color']>0xd0d0d0})
 fields=[]
 for ix,w in enumerate(page.widgets() or []):
  if w.field_name.lower().startswith(('website','phone number')):continue
  fields.append({'name':f'P{num:02d}_{w.field_name.replace(" ","_")}', 'source_name':w.field_name,'box':list(w.rect),'type':'check' if w.field_type_string=='CheckBox' else 'text','value':w.field_value or '', 'multi':bool(w.field_flags & pymupdf.PDF_TX_FIELD_IS_MULTILINE)})
 if num==1:
  y0=0;y1=1;shapes=[]
 else:
  ys=[s['box'][1] for s in spans]+[f['box'][1] for f in fields]
  ye=[s['box'][3] for s in spans]+[f['box'][3] for f in fields]
  y0=min(ys)-3;y1=max(ye)+7
  y0={7:76,8:57,10:57,11:57}.get(num,y0)
  shapes=[]
  for d in page.get_drawings():
   r=d['rect']
   if r.y0<y0-3 or r.y1>y1+3 or r.x0<29 or r.x1>583:continue
   if num not in [7,8,10,11,15]:continue
   if d['fill'] is not None and r.width>20 and r.height>9:
    fill=d['fill']
    shade=sum(fill)/len(fill)
    rects=[item[1] for item in d['items'] if item[0]=='re'] or [r]
    for q in rects:shapes.append({'kind':'rect','box':list(q),'fill':True,'color':'#ffffff' if shade>.97 else '#e8edf7' if shade<.6 else '#f4f6fa','accent':False})
   if d['fill'] is None:
    for item in d['items']:
     if item[0]=='l':
      if abs(item[1].y-item[2].y)<.1 and abs(item[1].x-item[2].x)<500:continue
      shapes.append({'kind':'line','p1':list(item[1]),'p2':list(item[2])})
     elif item[0]=='re':shapes.append({'kind':'rect','box':list(item[1]),'fill':False})
 rec={'page':num,'y0':y0,'y1':y1,'spans':spans,'fields':fields,'shapes':shapes};records.append(rec)
 right=f'<div class="hcontact"><div class="kicker">{e(k["label"])}</div><div class="hphone">{e(k["phone"])}</div></div>'
 header=kit.letter_header(right)
 tagline='You Can’t Know the Future, But You Can Prepare for It!' if num==1 else 'Nobody Knows the Future, But You Can Prepare for It!'
 program=num in [1,2,3,4,5,15]
 band='<div class="lband full-band">'
 if program and num!=1:band+='<img class="pgp-small" src="assets/pgp-logo.png">'
 band+='<div><div class="display">'+kit.emph_tail(titles[num],1)+'</div>'
 if program:band+=f'<div class="program-tagline">{e(tagline)}</div>'
 band+='</div></div>'
 if num==1:
  body='<div class="document-body full-cover"><img src="assets/pgp-logo.png"><div class="prepared"><div class="h3">Prepared for:</div><div class="entry prepared-field" data-name="'+fields[0]['name']+'" data-field="multi"></div></div></div>'
 elif num==2:
  left=''.join('<p>'+e(s)+'</p>' for s in overview['intro'])+'<ul class="overview-list">'+''.join('<li>'+e(s)+'</li>' for s in overview['bullets'])+'</ul>'
  rightbody='<h3>'+e(overview['riskHeading'])+'</h3><div class="risk-grid">'+''.join('<div class="risk-card">'+e(s)+'</div>' for s in overview['risks'])+'</div>'
  rightbody+='<h3 class="benefit-heading">'+e(overview['benefitHeading'])+'</h3><div class="benefit-grid">'+''.join('<div class="benefit-card">'+e(s)+'</div>' for s in overview['benefits'])+'</div>'
  body='<div class="document-body"><div class="overview-grid"><div>'+left+'</div><div>'+rightbody+'</div></div></div>'
 else:body=f'<div class="document-body"><div class="source-canvas" data-page="{num}"></div></div>'
 pages.append(f'<section class="sheet letter v5 full-erp p{num}"><div class="lpage">{header}{band}{body}{kit.letter_footer()}</div></section>')
(out/'layout-data.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
style='''
@page{size:8.75in 11.25in;margin:0}.sheet:last-child{page-break-after:auto}
.full-band{display:flex;align-items:center;gap:.18in}.full-band .display{font-size:20pt;line-height:1.1}
.p6 .full-band .display{font-size:17pt}
.program-tagline{font:600 8.3pt/1.35 Montserrat;color:white;margin-top:.065in}
.pgp-small{width:.58in;height:.58in;border-radius:50%;flex-shrink:0}
.document-body{flex:1;min-height:0;position:relative;margin:.2in 0}
.source-canvas{position:absolute;inset:0}
.source-text{position:absolute;white-space:pre;line-height:1;transform-origin:left top;color:var(--body);font-family:Inter;font-weight:400}
.source-text.bold{font-family:Montserrat;font-weight:700;color:var(--navy)}
.source-grid{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.source-field{position:absolute;background:#f4f6fb;border-bottom:.55pt solid #a7b2ca}
.source-field.table-cell{background:transparent;border:0}
.source-field.check{background:white;border:.7pt solid var(--navy)}
.full-cover{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:.4in}
.full-cover>img{width:4.3in;height:4.3in}
.prepared{width:5in}.prepared .h3{margin-bottom:.08in}.prepared-field{height:.65in;background:#f4f6fb;border-bottom:.7pt solid #a7b2ca}
.overview-grid{display:grid;grid-template-columns:1fr 1fr;gap:.3in;height:100%}.overview-grid>div:last-child{border-left:.6pt solid var(--hair);padding-left:.22in}
.overview-grid p{font:400 8.3pt/1.42 Inter;margin:0 0 .075in}.overview-list{list-style:none;padding:0;margin:.1in 0 0}.overview-list li{position:relative;padding-left:.15in;margin-bottom:.07in;font:400 8.3pt/1.42 Inter;color:var(--body)}.overview-list li:before{content:'';position:absolute;left:0;top:.055in;width:4pt;height:4pt;background:var(--ember)}
.overview-grid h3{font:700 9pt/1.35 Montserrat;color:var(--navy);margin:0 0 .13in}.risk-grid{display:grid;grid-template-columns:1fr 1fr;gap:.09in}.risk-card{font:500 8pt/1.35 Inter;color:var(--navy);background:var(--paper);border-top:2pt solid var(--ember);padding:.13in .11in;min-height:.85in;display:flex;align-items:center}
.overview-grid .benefit-heading{margin-top:.23in;padding-top:.16in;border-top:.6pt solid var(--hair)}.benefit-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.07in}.benefit-card{background:var(--paper);padding:.1in .075in;font:500 7pt/1.3 Inter;color:var(--navy);min-height:.83in;display:flex;align-items:center;border-top:1.5pt solid var(--navy)}.benefit-card:nth-child(3n+1){border-top-color:var(--ember)}
'''
script='''
const NS='http://www.w3.org/2000/svg';
window.__layout=async()=>{const data=await(await fetch('layout-data.json')).json();
for(const rec of data){if(rec.page===1||rec.page===2)continue;const canvas=document.querySelector('.source-canvas[data-page="'+rec.page+'"]');
const W=canvas.clientWidth,H=canvas.clientHeight,sx=W/546,sy=H/(rec.y1-rec.y0);const X=x=>(x-33)*sx,Y=y=>(y-rec.y0)*sy;
const svg=document.createElementNS(NS,'svg');svg.setAttribute('class','source-grid');svg.setAttribute('viewBox',`0 0 ${W} ${H}`);canvas.append(svg);
for(const d of rec.shapes){let el;if(d.kind==='rect'){el=document.createElementNS(NS,'rect');const[x0,y0,x1,y1]=d.box;Object.entries({x:X(x0),y:Y(y0),width:(x1-x0)*sx,height:(y1-y0)*sy,fill:d.fill?d.color:'none',stroke:d.fill?'none':'#d9deea','stroke-width':.75}).forEach(([k,v])=>el.setAttribute(k,v));svg.append(el);if(d.fill&&rec.page===2){const l=document.createElementNS(NS,'line');Object.entries({x1:X(x0),x2:X(x1),y1:Y(y0),y2:Y(y0),stroke:d.accent?'#f05a29':'#1a327d','stroke-width':2}).forEach(([k,v])=>l.setAttribute(k,v));svg.append(l)}}else{el=document.createElementNS(NS,'line');Object.entries({x1:X(d.p1[0]),y1:Y(d.p1[1]),x2:X(d.p2[0]),y2:Y(d.p2[1]),stroke:'#d9deea','stroke-width':.75}).forEach(([k,v])=>el.setAttribute(k,v));svg.append(el)}}
for(const f of rec.fields){const[x0,y0,x1,y1]=f.box,el=document.createElement('div');const table=[7,8,10,11,15].includes(rec.page);el.className='source-field'+(table?' table-cell':'')+(f.type==='check'?' check':'');Object.assign(el.style,{left:X(x0)+'px',top:Y(y0)+'px',width:(x1-x0)*sx+'px',height:(y1-y0)*sy+'px'});el.dataset.name=f.name;el.dataset.field=f.type==='check'?'check':(f.multi||y1-y0>35?'multi':'text');el.dataset.sourceValue=f.value;canvas.append(el)}
for(const s of rec.spans){const el=document.createElement('span');el.className='source-text'+(s.bold||s.light?' bold':'');el.textContent=s.text;el.dataset.original='';const fs=s.size*sx*.96;Object.assign(el.style,{left:X(s.x)+'px',top:(Y(s.y)-fs*.83)+'px',fontSize:fs+'px',fontStyle:s.italic?'italic':'normal'});if(s.light)el.style.color='#1a327d';canvas.append(el);const measured=el.getBoundingClientRect().width,target=(s.box[2]-s.box[0])*sx;if(measured>target&&target>0)el.style.transform='scaleX('+target/measured+')'}
}
};
'''
(out/'layout.js').write_text(script,encoding='utf8')
(out/'index.html').write_text('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="kit.css"><style>'+style+'</style></head><body>'+''.join(pages)+'<script src="layout.js"></script></body></html>',encoding='utf8')
print('15 pages. Preserved working fields:',sum(len(r['fields']) for r in records))

