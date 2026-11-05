import sys,types,json,re,importlib.util,shutil
from pathlib import Path
import pymupdf
root=Path.cwd();src=root/'work/kit/GCPRO_ASP_Kit_SOURCE';out=root/'outputs/GCPRO-PGP-Pre-Authorization-source';out.mkdir(exist_ok=True)
for name in ['assets','fonts']:shutil.copytree(src/name,out/name,dirs_exist_ok=True)
shutil.copy2(src/'kit.css',out/'kit.css')
original=pymupdf.open(r'C:/Users/VitaliiVozniak/Downloads/GC PRO  FILL IN PGP Pre Auth (1).pdf')
original[0].get_pixmap(matrix=pymupdf.Matrix(4,4),clip=pymupdf.Rect(132,77,465,410)).save(out/'assets/pgp-logo.png')
stub=types.ModuleType('playwright.sync_api');stub.sync_playwright=lambda:None
sys.modules['playwright']=types.ModuleType('playwright');sys.modules['playwright.sync_api']=stub
spec=importlib.util.spec_from_file_location('kit',src/'build.py');kit=importlib.util.module_from_spec(spec);spec.loader.exec_module(kit)
e=kit.e;k=kit.K;raw=json.loads((root/'work/pgp-extracted.json').read_text(encoding='utf8'))
def clean(s):
 s=s.replace('\x85','').replace('•','').strip()
 s=re.sub(r'^\s*-\s*','',s)
 return ' '.join(s.split())
def b(pg,*indexes):return clean(' '.join(raw[pg-1]['blocks'][n]['text'] for n in indexes))
sections3=[{'h':b(3,34),'items':[b(3,35)]},{'h':b(3,36),'items':[b(3,37)]},{'h':b(3,38),'items':[b(3,n) for n in range(39,45)]},{'h':b(3,45),'items':[b(3,46)]}]
sections4=[{'h':b(4,27,28),'items':[b(4,n) for n in range(29,34)],'notes':b(4,34)}, {'h':b(4,35),'items':[b(4,36)]}, {'h':b(4,37),'items':[b(4,38),b(4,39)]}, {'h':b(4,40),'items':[b(4,n) for n in range(41,45)]}, {'h':b(4,45),'items':[b(4,46)]}, {'h':b(4,47),'items':[b(4,48),b(4,49)]}]
sections5=[{'h':b(5,40),'items':[b(5,41)]},{'h':b(5,42),'items':[b(5,43)]}]
copy={'title':b(2,0),'coverTagline':b(1,1),'tagline':b(2,1),
'page2':{'intro':[b(2,n) for n in range(27,31)],'bullets':[b(2,n) for n in range(31,37)],'riskHeading':b(2,37,38),'risks':[b(2,41,42,43,44,45),b(2,51,52),b(2,46,47),b(2,48,49,50)],'benefitHeading':b(2,39,40),'benefits':[b(2,53,54,55),b(2,61,62),b(2,70,71,72),b(2,57,58),b(2,65,66,67),b(2,74,75,76),b(2,56),b(2,63,64),b(2,73),b(2,59,60),b(2,68,69),b(2,77)]},
'page3':{'heading':b(3,25),'intro':[b(3,26),b(3,27)],'owner':b(3,28),'location':b(3,29),'and':b(3,31),'with':b(3,32),'choose':b(3,33),'sections':sections3},
'page4':sections4,
'page5':{'sections':sections5,'resource':b(5,25),'paragraphs':[b(5,n) for n in range(26,29)],'yes':b(5,29),'agreements':[b(5,30,31),b(5,32,33)],'signatureHeadings':[b(5,34),b(5,37)]},
'page6':{'heading':b(6,0),'contact':'Key Contact (Name & Phone #)'}}
(out/'copy.json').write_text(json.dumps(copy,indent=2,ensure_ascii=False),encoding='utf8')
expected=[]
def text(s,tag='p',cls=''):
 expected.append(s)
 content=kit.emph_tail(s,1) if cls=='display' else e(s)
 return f'<{tag} class="{cls}" data-original>{content}</{tag}>'
def field(name,cls='',multi=False):return f'<div class="entry {cls}" data-field="{"multi" if multi else "text"}" data-name="{name}"></div>'
def checkbox(name):return f'<span class="check" data-field="check" data-name="{name}"></span>'
def section(s,num):
 h='<div class="option">'+checkbox('Option_'+str(num))+text(s['h'],'h3')+'</div>'
 h+='<ul class="terms">'+''.join('<li>'+text(v)+'</li>' for v in s['items'])+'</ul>'
 if s.get('notes'):h+='<div class="notes">'+text(s['notes'],'span')+field('NTE_Notes')+'</div>'
 return '<div class="option-group">'+h+'</div>'
def header():
 right=f'<div class="hcontact"><div class="kicker">{e(k["label"])}</div><div class="hphone">{e(k["phone"])}</div></div>'
 return kit.letter_header(right)
def band(tagline,cover=False):
 logo='' if cover else '<img class="pgp-small" src="assets/pgp-logo.png">'
 return '<div class="lband program-band">'+logo+'<div>'+text(copy['title'],'div','display')+text(tagline,'div','program-tagline')+'</div></div>'
def page(n,body,cls='',cover=False):
 return f'<section class="sheet letter v5 pgp p{n}"><div class="lpage">'+header()+band(copy['coverTagline'] if cover else copy['tagline'],cover)+f'<div class="pgp-body {cls}">{body}</div>'+kit.letter_footer()+'</div></section>'
pages=[]
pages.append(page(1,'<img class="cover-logo" src="assets/pgp-logo.png">','cover',True))
c=copy['page2']
intro=''.join(text(s) for s in c['intro'])+'<ul class="intro-list">'+''.join('<li>'+text(s)+'</li>' for s in c['bullets'])+'</ul>'
cards=text(c['riskHeading'],'h3','card-heading')+'<div class="risk-grid">'+''.join(text(s,'div','risk-card') for s in c['risks'])+'</div>'
cards+=text(c['benefitHeading'],'h3','card-heading benefits-heading')+'<div class="benefit-grid">'+''.join(text(s,'div','benefit-card') for s in c['benefits'])+'</div>'
pages.append(page(2,'<div class="overview-grid"><div>'+intro+'</div><div>'+cards+'</div></div>','overview'))
c=copy['page3']
body=text(c['heading'],'h2','h2 doc-heading')+''.join(text(s) for s in c['intro'])
body+=text(c['owner'])+field('Owner_Name')+text(c['location'])+field('Facility_Address')+text(c['and'])
body+=text(c['with'],'h2','h2 with-heading')+text(c['choose'],'h3','choice-heading')+''.join(section(s,n+1) for n,s in enumerate(c['sections']))
pages.append(page(3,body,'form-copy'))
pages.append(page(4,''.join(section(s,n+5) for n,s in enumerate(copy['page4'])),'form-copy dense'))
c=copy['page5'];body=''.join(section(s,n+11) for n,s in enumerate(c['sections']))
body+='<div class="resource">'+text(c['resource'],'h2','h2')+''.join(text(s) for s in c['paragraphs'])+'</div>'
body+=text(c['yes'],'h2','h2 enrollment')
for n,s in enumerate(c['agreements']):body+='<div class="agreement">'+checkbox('Agreement_'+str(n+1))+text(s)+'</div>'
body+='<div class="signature-area">'
for n,h in enumerate(c['signatureHeadings']):
 body+='<div class="signature-group">'+text(h,'h3')+'<div class="signature-grid">'
 for label in ['Print Name','Date','Signature','Title']:
  body+='<div class="signature-cell">'+field(f'Signer_{n+1}_{label.replace(" ","_")}')+text(label,'span')+'</div>'
 body+='</div></div>'
body+='</div>'
pages.append(page(5,body,'form-copy enrollment-page'))
c=copy['page6'];body=text(c['heading'],'h2','h2 doc-heading')+'<div class="locations">'
for n in range(1,6):
 body+=f'<div class="location"><div class="location-top"><span class="location-number">{n:02d}</span>'+field(f'Location_{n}')+'</div>'+text(c['contact'],'span','contact-label')+field(f'Location_{n}_Key_Contact','contact-entry',True)+'</div>'
body+='</div>';pages.append(page(6,body,'locations-page'))
style='''
@page{size:8.75in 11.25in;margin:0}.sheet:last-child{page-break-after:auto}
.program-band{display:flex;align-items:center;gap:.18in}.program-band .display{font-size:20pt}.program-tagline{font:600 8.3pt/1.35 Montserrat;color:#fff;margin-top:.065in}
.pgp-small{width:.58in;height:.58in;border-radius:50%;flex-shrink:0}
.pgp-body{flex:1;padding:.2in 0;min-height:0}.pgp-body p{font-size:8.3pt;line-height:1.42;margin:0 0 .075in}
.cover{display:flex;align-items:center;justify-content:center}.cover-logo{width:4.65in;height:4.65in}
.overview-grid{display:grid;grid-template-columns:1fr 1fr;gap:.3in;height:100%}
.overview-grid>div:last-child{border-left:.6pt solid var(--hair);padding-left:.22in}
.overview p{font-size:8.3pt;line-height:1.42}.intro-list{list-style:none;margin:.1in 0 0;padding:0}.intro-list li{position:relative;padding-left:.15in;margin-bottom:.07in}.intro-list li:before{content:'';position:absolute;left:0;top:.055in;width:4pt;height:4pt;background:var(--ember)}
.card-heading{font:700 9pt/1.35 Montserrat;color:var(--navy);margin:0 0 .13in}.risk-grid{display:grid;grid-template-columns:1fr 1fr;gap:.09in}.risk-card{font:500 8pt/1.35 Inter;color:var(--navy);background:var(--paper);border-top:2pt solid var(--ember);padding:.13in .11in;min-height:.85in;display:flex;align-items:center}
.benefits-heading{margin-top:.23in;padding-top:.16in;border-top:.6pt solid var(--hair)}
.benefit-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:.07in}
.benefit-card{background:var(--paper);padding:.1in .075in;font:500 7pt/1.3 Inter;color:var(--navy);min-height:.83in;display:flex;align-items:center;border-top:1.5pt solid var(--navy)}
.benefit-card:nth-child(3n+1){border-top-color:var(--ember)}
.form-copy{padding:.18in 0}.form-copy p{font-size:8pt;line-height:1.36;margin-bottom:.055in}
.doc-heading{font-size:13pt;line-height:1.15;margin-bottom:.13in}
.entry{height:.27in;border-bottom:.65pt solid #a7b2ca;background:#f6f8fc;min-width:0;margin:.035in 0 .07in}
.with-heading{font-size:12pt;margin:.13in 0 .08in}.choice-heading{font:700 8.5pt/1.35 Montserrat;color:var(--navy);margin:0 0 .1in}
.option-group{margin:0 0 .085in}.option{display:grid;grid-template-columns:.13in 1fr;gap:.08in;align-items:start}
.check{display:block;width:.115in;height:.115in;border:.8pt solid var(--navy);margin-top:.025in;background:white}
.option h3{font:700 8.5pt/1.3 Montserrat;color:var(--navy);margin:0 0 .055in}
.terms{list-style:none;margin:0 0 0 .21in;padding:0}.terms li{position:relative;padding-left:.12in}.terms li:before{content:'';width:2.5pt;height:2.5pt;background:var(--ember);position:absolute;left:0;top:.06in}
.notes{display:flex;align-items:center;gap:.1in;margin-left:.33in;font:400 8pt Inter}.notes .entry{flex:1;height:.23in}
.dense .option-group{margin-bottom:.11in}.dense p{font-size:8.1pt;line-height:1.4}
.resource{border-top:.6pt solid var(--hair);padding-top:.12in;margin-top:.1in}.resource .h2{font-size:11pt;margin-bottom:.09in}
.enrollment{font-size:11pt;margin:.13in 0 .12in}.agreement{display:grid;grid-template-columns:.13in 1fr;gap:.08in;margin-bottom:.09in}
.enrollment-page{display:flex;flex-direction:column}.signature-area{margin-top:auto;padding-top:.06in}
.signature-group{margin-bottom:.08in}.signature-group:last-child{margin-bottom:0}.signature-group h3{font:700 9pt Montserrat;color:var(--navy);margin:0 0 .07in}
.signature-grid{display:grid;grid-template-columns:2fr 1fr;gap:.04in .3in}.signature-cell .entry{height:.3in;margin-bottom:.035in}.signature-cell>span{font:400 7.5pt Inter;color:var(--body)}
.locations-page{display:flex;flex-direction:column}.locations-page .doc-heading{font-size:15pt}.locations{flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:.12in;padding-bottom:.12in}
.location{border-top:.6pt solid var(--hair);padding-top:.12in}.location-top{display:flex;align-items:center;gap:.15in}.location-top .entry{flex:1;height:.32in;margin:0 0 .08in}.location-number{font:800 15pt Montserrat;color:var(--ember);width:.3in}.contact-label{font:600 8.5pt Inter;color:var(--navy)}.contact-entry{height:.5in;margin-bottom:0}
'''
html='<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="kit.css"><style>'+style+'</style></head><body>'+''.join(pages)+'</body></html>'
(out/'index.html').write_text(html,encoding='utf8')
(out/'expected-text.json').write_text(json.dumps(expected,ensure_ascii=False,indent=2),encoding='utf8')
print('Built six pages using native kit header/footer and preserved source paragraphs.')
