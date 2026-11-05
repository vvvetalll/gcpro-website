import sys,types,json,importlib.util,shutil
from pathlib import Path
from PIL import Image
root=Path.cwd();src=root/'work/kit/GCPRO_ASP_Kit_SOURCE';out=root/'outputs/GCPRO-ERP-Comparison-source';out.mkdir(exist_ok=True)
for name in ['assets','fonts']:shutil.copytree(src/name,out/name,dirs_exist_ok=True)
shutil.copytree(root/'work/provided-icons',out/'icons',dirs_exist_ok=True)
shutil.copy2(src/'kit.css',out/'kit.css')
shutil.copy2(r'C:/Users/VITALI~1/AppData/Local/Temp/codex-clipboard-2120b79a-7cf7-4b23-9fbb-27df6092bd8f.jpg',out/'original.jpg')
stub=types.ModuleType('playwright.sync_api');stub.sync_playwright=lambda:None
sys.modules['playwright']=types.ModuleType('playwright');sys.modules['playwright.sync_api']=stub
spec=importlib.util.spec_from_file_location('kit',src/'build.py');kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit)
e=kit.e;k=kit.K
c={'title':'EMERGENCY RESPONSE PROGRAM','tagline':'Nobody Knows the Future, But You Can Prepare for It!',
'columns':['NO PLAN IN PLACE','ERP IN PLACE'],
'labels':['DISPLACED OCCUPANTS/UNIT OWNERS','LOST TENANTS/OCCUPANTS','EMERGENCY PERSONNEL/EQUIPMENT','PROPERTY MANAGER STRESS','LOST TIME','TOTAL COST OF RESTORATION'],
'equation':'SEVERITY + DURATION = COST',
'message':'WHEN YOU HAVE AN EMERGENCY RESPONSE PROGRAM IN PLACE, WE’RE THERE FOR YOU BEFORE, DURING AND AFTER!'}
(out/'copy.json').write_text(json.dumps(c,indent=2,ensure_ascii=False),encoding='utf8')
# Place unchanged portions of the supplied infographic into the new document layout.
def crop(box,w,h,align='left',fixed=None):
 x,y,bw,bh=box
 scale=fixed if fixed is not None else min(w/bw,h/bh)
 left=(w-bw*scale)/2 if align=='center' else 0
 return f'<div class="source-graphic" style="width:{w}px;height:{h}px"><img src="original.jpg" style="width:{960*scale}px;height:{742*scale}px;left:{left-x*scale}px;top:{-y*scale}px;clip-path:inset({y*scale}px {(960-x-bw)*scale}px {(742-y-bh)*scale}px {x*scale}px)"></div>'
boxes=[[(37,401,137,81),(204,401,82,46),(28,518,148,83),(207,518,140,54),(28,635,146,61),(205,634,149,73)],[(388,401,134,47),None,(383,518,133,47),(556,519,86,31),(381,635,145,24),(556,634,125,27)]]
files=['walking_traveler_with_suitcase.png','navy_exit_door_pictogram.png','navy_rescue_worker_helmet_icon.png','navy_restoration_equipment_icon.png','stressed_face_with_lightning_marks.png','time_lost_clock_icon.png','bold_navy_dollar_sign_icon.png']
def icon(index,size=18):
 file=files[index];im=Image.open(out/'icons'/file)
 x,y,x1,y1=im.getchannel('A').point(lambda a:255 if a>64 else 0).getbbox();w=x1-x;h=y1-y
 scale=min(size/w,size/h)
 left=(size-w*scale)/2-x*scale;top=(size-h*scale)/2-y*scale
 return f'<span class="png-icon" style="width:{size}px;height:{size}px"><img src="icons/{file}" style="width:{im.width*scale}px;height:{im.height*scale}px;left:{left}px;top:{top}px"></span>'
def iconfield(n,j):
 counts=[[20,6,10,7,21,24],[10,0,4,3,7,8]]
 count=counts[n][j]
 if j==2:
  return '<div class="icon-field crew"><div class="crew-row">'+icon(2,16)*count+'</div><div class="crew-row">'+icon(3,16)*count+'</div></div>'
 which=[0,1,2,4,5,6][j]
 cols={0:10,1:6,3:5,4:7,5:8}[j]
 size=15 if j==0 else 18 if j in [1,3] else 16
 return f'<div class="icon-field" style="grid-template-columns:repeat({cols},{size}px)">'+icon(which,size)*count+'</div>'
def col(n):
 cards=''.join(f'<div class="metric"><div class="metric-label" data-original>{e(label)}</div>'+iconfield(n,j)+'</div>' for j,label in enumerate(c['labels']))
 return f'<div class="comparison-column col-{n}"><div class="comparison-heading" data-original>{c["columns"][n]}</div>'+crop((60 if n==0 else 413,196,292,163),302,100,'center')+f'<div class="metrics">{cards}</div></div>'
right=f'<div class="hcontact"><div class="kicker">{e(k["label"])}</div><div class="hphone">{e(k["phone"])}</div></div>'
body=(kit.letter_header(right)+f'<div class="lband erp-title"><img src="assets/erp-shield.png"><div><div class="display" style="font-size:23pt" data-original>{kit.emph_tail(c["title"],2)}</div><div class="tagline" data-original>{e(c["tagline"])}</div></div></div>'
 +'<div class="comparison-body"><div class="comparison">'+col(0)+col(1)+'</div>'
 +'<aside><div class="chart">'+crop((750,151,184,177),186,180,'center')+'</div>'
 +f'<div class="equation" data-original>{e(c["equation"])}</div><div class="accent"></div><div class="message" data-original>{e(c["message"])}</div><img class="erp-mark" src="assets/erp-shield.png"></aside></div>'+kit.letter_footer())
html='''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="kit.css"><style>
@page{size:11.25in 8.75in;margin:0}.sheet.landscape{width:11.25in;height:8.75in;page-break-after:auto}
.erp-title{display:flex;align-items:center;gap:.24in}.erp-title>img{height:.68in;width:auto}.tagline{font:600 10pt/1.3 Montserrat;color:white;margin-top:.06in}
.comparison-body{flex:1;display:grid;grid-template-columns:1fr 2.05in;gap:.25in;padding:.22in 0 .2in;min-height:0}
.comparison{display:grid;grid-template-columns:1fr 1fr;gap:.24in}
.comparison-column{min-width:0;border-right:.6pt solid var(--hair);padding-right:.12in}.comparison-column:last-child{border-right:0;padding-right:0}
.comparison-heading{background:var(--navy);color:white;font:800 12pt Montserrat;text-align:center;padding:.09in .04in;margin-bottom:.08in}
.col-1 .comparison-heading{background:var(--ember)}
.source-graphic{position:relative;overflow:hidden;flex-shrink:0}.source-graphic img{position:absolute;max-width:none;display:block}
.comparison-column>.source-graphic{margin:0 auto .12in}
.metrics{display:grid;grid-template-columns:1fr 1fr;gap:.08in .12in}
.metric{min-width:0;border-top:.6pt solid var(--hair);padding-top:.07in}
.metric-label{font:700 6.5pt/1.25 Montserrat;color:var(--navy);min-height:.26in;margin-bottom:.035in}
.col-1 .metric-label{color:var(--ember)}
.icon-field{height:64px;display:grid;align-content:start;gap:2px 0}
.png-icon{display:block;position:relative;overflow:hidden;flex-shrink:0}
.png-icon img{position:absolute;display:block;max-width:none;filter:brightness(0) saturate(100%) invert(54%) sepia(12%) saturate(1018%) hue-rotate(186deg) brightness(94%) contrast(86%)}
.icon-field.crew{display:flex;flex-direction:column;gap:3px}
.crew-row{display:grid;grid-template-columns:repeat(5,16px);gap:0 2px}
aside{background:var(--paper);padding:.13in .12in;display:flex;flex-direction:column}
.chart{display:flex;justify-content:center;background:white;margin-bottom:.15in}
.equation{font:800 10.2pt/1.25 Montserrat;color:var(--navy)}
aside .accent{margin:.13in 0 .15in}
.message{font:600 9.2pt/1.5 Montserrat;color:var(--navy)}
.erp-mark{height:.75in;width:.75in;object-fit:contain;margin:.1in auto 0}
</style></head><body><section class="sheet landscape v5"><div class="lpage">'''+body+'</div></section></body></html>'
(out/'index.html').write_text(html,encoding='utf8')
print('Built with native kit header, title band, footer and existing artwork.')
