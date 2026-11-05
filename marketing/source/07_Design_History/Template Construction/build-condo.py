import sys,types,json,importlib.util,shutil
from pathlib import Path
root=Path.cwd();src=root/'work/kit/GCPRO_ASP_Kit_SOURCE';out=root/'outputs/GCPRO-Condo-source';out.mkdir(exist_ok=True)
for name in ['assets','fonts']:shutil.copytree(src/name,out/name,dirs_exist_ok=True)
shutil.copy2(src/'kit.css',out/'kit.css')
shutil.copy2(r'C:/Users/VITALI~1/AppData/Local/Temp/codex-clipboard-7780bc12-bcf5-4ced-a611-88372478c10f.jpg',out/'original.jpg')
stub=types.ModuleType('playwright.sync_api');stub.sync_playwright=lambda:None
sys.modules['playwright']=types.ModuleType('playwright');sys.modules['playwright.sync_api']=stub
spec=importlib.util.spec_from_file_location('kit',src/'build.py');kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit)
e=kit.e;k=kit.K
c={
'title':'Unit Owner vs. Association Hazard Insurance Coverage Areas',
'disclaimer':'This diagram is provided for illustration purposes only and should not be solely relied upon as the basis for insurance. We recommend you review Your State’s Condominium Statute and your specific condominium documents for updated insurance and maintenance responsibilities.',
'associationHeading':'Association Responsibilities Hazard Insurance',
'association':[
'Hot/Cold Water Pipes including: Fire Systems/ Sprinklers',
'Perimeter/Load Bearing Walls including: Common/Party Walls',
'Electrical Wiring','Balcony/Porches/Stairs','Unfinished Drywall/Wallboard',
'Roofs to include: Covering, Insulation and Trusses','Unfinished Floors','Exterior Doors','Windows/Sliding Glass Doors','A/C and Heating Unit including: Compressor'],
'ownerHeading':'Unit Owner Responsibilities Hazard Insurance',
'owner':['Bathtub/Shower','Toilet','Bathroom Sink','Wall/Floor/Ceiling Coverings including: paint, wallpaper, tile, wood, carpet, laminate, etc.','Electrical Outlets and Fixtures','Interior Doors','Refrigerator','Oven/Stove and Hood','Counter Tops and Cabinets','Kitchen Sink','Dishwasher','Light Fixtures','Water Heaters and Water Filters','Window Treatments, including: curtains, drapes, blinds and all hardware']}
(out/'copy.json').write_text(json.dumps(c,indent=2,ensure_ascii=False),encoding='utf8')
right=f'<div class="hcontact"><div class="kicker">{e(k["label"])}</div><div class="hphone">{e(k["phone"])}</div></div>'
rows=lambda items,letters=False:''.join(f'<li><span class="mark">{chr(65+n) if letters else n+1}</span><span data-original>{e(s)}</span></li>' for n,s in enumerate(items))
body=(kit.letter_header(right)+f'<div class="lband"><div class="display" style="font-size:22pt" data-original>{kit.emph_tail(c["title"],2)}</div></div>'
 +f'<div class="condo-body"><p class="disclaimer" data-original>{e(c["disclaimer"])}</p>'
 +f'<div class="h2 section-title" data-original>{e(c["associationHeading"])}</div><div class="accent"></div>'
 +f'<div class="association-grid"><ol class="coverage">{rows(c["association"][:5],True)}</ol><ol class="coverage">'+''.join(f'<li><span class="mark">{chr(70+n)}</span><span data-original>{e(s)}</span></li>' for n,s in enumerate(c['association'][5:]))+'</ol></div>'
 +f'<div class="owner-section"><div class="h2 section-title" data-original>{e(c["ownerHeading"])}</div><div class="accent"></div><div class="owner-grid"><ol class="coverage owners">{rows(c["owner"])}</ol><div class="diagram"><img src="original.jpg" alt="Original insurance coverage diagram, labels A–J and 1–14"></div></div></div></div>'
 +kit.letter_footer())
html='''<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="kit.css"><style>
@page{size:8.75in 11.25in;margin:0}.sheet:last-child{page-break-after:auto}
.condo-body{flex:1;display:flex;flex-direction:column;padding:.19in 0 .2in}
.disclaimer{font-size:8.4pt;line-height:1.42;margin:0 0 .22in}
.section-title{font-size:12pt;line-height:1.15}
.condo-body .accent{margin:.09in 0 .13in}
.association-grid{display:grid;grid-template-columns:1fr 1fr;gap:.3in}
.coverage{list-style:none;margin:0;padding:0}
.coverage li{display:grid;grid-template-columns:.23in 1fr;gap:.035in;font:400 8.4pt/1.34 Inter;margin:0 0 .065in;color:var(--body)}
.mark{font-family:Montserrat;font-weight:800;color:var(--ember)}
.owner-section{margin-top:.18in;padding-top:.17in;border-top:.6pt solid var(--hair)}
.owner-grid{display:grid;grid-template-columns:2.85in 1fr;gap:.2in;align-items:start}
.owners li{font-size:8.2pt;line-height:1.3;margin-bottom:.065in}
.diagram{width:3.75in;height:4.125in;position:relative;overflow:hidden;clip-path:polygon(60% 0,100% 0,100% 100%,0 100%,0 73%,4% 73%,4% 37%,7.3% 37%,7.3% 10.6%,60% 10.6%)}
.diagram img{position:absolute;max-width:none;width:6.7866in;height:8.7805in;left:-2.6982in;top:-3.5122in}
</style></head><body><section class="sheet letter v5"><div class="lpage">'''+body+'</div></section></body></html>'
(out/'index.html').write_text(html,encoding='utf8')
print('Created using native letter_header, letter_footer and unmodified kit.css. Original diagram is embedded unchanged and cropped by page layout.')
