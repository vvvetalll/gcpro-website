import sys,types,json,importlib.util
from pathlib import Path
root=Path.cwd()
src=root/'work/kit/GCPRO_ASP_Kit_SOURCE'
out=root/'outputs/GCPRO-ERP-source'
# Load the supplied layout functions without invoking its browser renderer.
stub=types.ModuleType('playwright.sync_api');stub.sync_playwright=lambda:None
sys.modules['playwright']=types.ModuleType('playwright');sys.modules['playwright.sync_api']=stub
spec=importlib.util.spec_from_file_location('kit',src/'build.py');kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit)
c=json.loads((out/'original-copy.json').read_text(encoding='utf8'))
i=json.loads((root/'work/csp-inside.json').read_text(encoding='utf8'))
kit.ROOT=out
e=kit.e
items=''.join(f'<li><span class="bignum">{n+1:02d}</span><span class="t">{e(s)}</span></li>' for n,s in enumerate(c['benefits']))
flap=(kit.photo('LB.flap',kit.bleed(top=True,left=True,right=True,first=True)+'height:2.45in;flex-shrink:0')
      +f'<div style="margin-top:.3in" class="h2">{e(c["heading"])}</div><div class="accent"></div><ul class="list5">{items}</ul>')
outside=(kit.panel(0,3.625,first=True,body=flap)
         +kit.panel(3.625,3.6875,body=kit.back_v5(''))
         +kit.panel(7.3125,3.6875,'ink5',last=True,body=kit.cover_v5('RC.cover',c['cover'],tail=2)))
p1=(f'<div class="h2">{e(i["title"])}</div><div class="accent"></div>'
    +f'<div class="h3">{e(i["planningHeading"])}</div><p>{e(i["planning"])}</p>'
    +f'<div class="hair"></div><div class="h3">{e(i["priorityHeading"])}</div><p>{e(i["priority"])}</p>'
    +kit.photo('RC.inside1','flex:1;min-height:1.3in;margin-top:.16in'))
p2=(f'<div class="h2">{e(i["supportHeading"])}</div><div class="accent"></div><p>{e(i["supportIntro"])}</p>'
    +kit.bullets(i['leftBullets']+i['rightBullets']))
features=''.join(f'<div style="display:grid;grid-template-columns:.46in 1fr;padding:.12in 0;border-top:.6pt solid rgba(255,255,255,.16)"><span class="bignum">{n+1:02d}</span><div><div class="h3">{e(f["h"])}</div><p style="margin:0">{e(f["p"])}</p></div></div>' for n,f in enumerate(i['features']))
p3=(features+f'<div class="h3" style="margin-top:.18in">{e(i["servicesHeading"])}</div>'
    +''.join(f'<div class="svc" style="color:#fff">{e(s)}</div>' for s in i['services'])
    +'<div style="flex:1"></div>'+kit.contact_dark())
inside=(kit.panel(0,3.6875,first=True,body=p1)+kit.panel(3.6875,3.6875,body=p2)+kit.panel(7.375,3.625,'navy5',last=True,body=p3))
html=('<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="kit.css">'
      '<style>@page{size:11.25in 8.75in;margin:0}.sheet:last-child{page-break-after:auto}.t-csp .list5 li{padding:.1in 0}.t-csp .list5 .t{font-size:9.1pt}.t-csp .display{font-size:26pt}.guides{display:none}body.review .guides{display:block}</style></head><body>'
      +f'<section class="sheet tri v5 t-lb t-csp">{outside}{kit.guides([3.625,7.3125])}</section>'
      +f'<section class="sheet tri v5 t-lb t-csp">{inside}{kit.guides([3.6875,7.375])}</section></body></html>')
(out/'index.html').write_text(html,encoding='utf8')
print('Used supplied kit functions: photo, back_v5, cover_v5, bullets, contact_dark, panel, guides. Unmodified kit.css.')
