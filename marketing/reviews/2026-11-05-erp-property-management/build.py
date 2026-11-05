"""Text-only ERP review; retains the released PDF's existing artwork and geometry."""
from pathlib import Path
import json, re, hashlib
import pymupdf as fitz
from fontTools.ttLib import TTFont

HERE=Path(__file__).resolve().parent
MARKETING=HERE.parents[1]
SOURCE=MARKETING/'releases/2026-10-20/01 ASP and PSP/2 Flyers/GCPRO ASP - Agency ERP Flyer - Emergency Response Program.pdf'
DATA=json.loads((HERE/'copy.json').read_text(encoding='utf-8'))
FONTS=MARKETING/'source/01_Brand_System/fonts'
CACHE=HERE/'.cache-fonts';CACHE.mkdir(exist_ok=True)
OUTPUT=HERE/'GCPRO-ERP-Property-Management-REVIEW.pdf'
doc=fitz.open(SOURCE);page=doc[0]
regions=[(113,129,580,149),(52,186,589,224),(40,233,296,333),(315,233,590,333),
         (65,404,204,634),(246,404,414,635),(456,404,577,634),(40,679,590,711)]
for rect in regions:page.add_redact_annot(fitz.Rect(rect),fill=None)
page.apply_redactions(images=0,graphics=0,text=0)
for alias,name in [('Copy','inter-latin-400-normal'),('Heading','montserrat-latin-700-normal'),('Tag','montserrat-latin-600-normal')]:
    font=TTFont(FONTS/(name+'.woff2'));font.flavor=None;font.save(CACHE/(name+'.ttf'))
    page.insert_font(fontname=alias,fontfile=str(CACHE/(name+'.ttf')))
navy=(26/255,50/255,125/255);body=(.23,.26,.32)
def text(rect,content,font='Copy',size=8.8,color=body,lineheight=1.18):
    result=page.insert_textbox(fitz.Rect(rect),content,fontname=font,fontsize=size,color=color,lineheight=lineheight)
    assert result>=0,('Text does not fit',content,result)
text((114.9,131,580,149),DATA['tagline'],'Tag',11.5,(.85,.88,.94))
text((53,189,586,224),DATA['banner'],'Heading',12,navy,1.25)
paragraph=DATA['provided_paragraph']
left,right=paragraph.split(' With a property-specific',1)
columns=[left,'With a property-specific'+right]
for rect,content in zip([(41.4,236,293,334),(316.4,236,589,334)],columns):
    text(rect,content,size=9.25,lineheight=1.23)
for x,right,ys,key in [(66.6,204,[406.8,461.5],'before'),(247.3,414,[406.8,448.8,490.8,532.8,574.8,604],'during'),(457.6,577,[406.8,512.5],'after')]:
    for i,(y,content) in enumerate(zip(ys,DATA[key])):
        bottom=ys[i+1]-5 if i+1<len(ys) else 634
        text((x,y,right,bottom),content)
prefix,tail=DATA['cta'].split('(847) 656-3322')
cursor=41.4
for content,alias,color in [(prefix,'Copy',body),('(847) 656-3322','Heading',(240/255,90/255,41/255)),(tail,'Copy',body)]:
    page.insert_text((cursor,690.7),content,fontname=alias,fontsize=10,color=color)
    font_name='montserrat-latin-700-normal' if alias=='Heading' else 'inter-latin-400-normal'
    cursor+=fitz.Font(fontfile=str(CACHE/(font_name+'.ttf'))).text_length(content,fontsize=10)
assert cursor<=590,'CTA exceeds its original width'
doc.set_metadata({**doc.metadata,'title':'GCPRO Emergency Response Program — Property Management','subject':'Review: existing ERP Agency Flyer with property-management copy; original design retained'})
doc.save(OUTPUT,garbage=4,deflate=True)
final=fitz.open(OUTPUT);page=final[0]
normalize=lambda value: re.sub(r'\s+',' ',value.replace('’',"'").replace('ʼ',"'")).strip()
assert normalize(paragraph) in normalize(page.get_text()),'Provided paragraph must remain word-for-word'
assert len(final)==1 and page.rect==fitz.open(SOURCE)[0].rect
assert 'insurance agent' not in page.get_text().lower()
assert '\ufffd' not in page.get_text() and '\u25a1' not in page.get_text()
assert not list(page.widgets() or [])
page.get_pixmap(matrix=fitz.Matrix(1.75,1.75)).save(HERE/'GCPRO-ERP-Property-Management-REVIEW.png')
(HERE/'checks.json').write_text(json.dumps({'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),'pages':1,'media_points':[630,810],'provided_paragraph':'exact after whitespace/apostrophe normalization','insurance_agent_copy_removed':True,'missing_glyphs':False,'status':'REVIEW — not promoted to main release'},indent=2)+'\n',encoding='utf-8')
print(OUTPUT)
