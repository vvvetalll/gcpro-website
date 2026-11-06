"""Apply only the four owner-requested grammar corrections to the existing ERP PDF."""
from pathlib import Path
import json,re,hashlib,io
import pymupdf as fitz
from fontTools.ttLib import TTFont
from PIL import Image,ImageChops,ImageDraw
import zxingcpp

HERE=Path(__file__).resolve().parent;MARKETING=HERE.parents[1]
SOURCE=HERE.parent/'2026-11-05-erp-property-management/GCPRO-ERP-Property-Management-REVIEW.pdf'
OUT=HERE/'GCPRO-ERP-Property-Management-FINAL.pdf'
FONTDIR=MARKETING/'source/01_Brand_System/fonts'
CACHE=HERE/'.cache';CACHE.mkdir(exist_ok=True)
normalize=lambda s:re.sub(r'\s+',' ',s).strip()
corrections=json.loads((HERE/'corrections.json').read_text())
source_copy=json.loads((SOURCE.parent/'copy.json').read_text(encoding='utf-8'))
copy=json.loads(json.dumps(source_copy))
for patch in corrections[:3]:
    copy['during']=[patch['new'] if t==patch['old'] else t for t in copy['during']]
copy['after_heading']=corrections[3]['heading']
(HERE/'copy.json').write_text(json.dumps(copy,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
original=fitz.open(SOURCE);doc=fitz.open(SOURCE);p=doc[0]
blocks=[b for b in p.get_text('dict')['blocks'] if 'lines' in b]
spans=[s for b in blocks for l in b['lines'] for s in l['spans']]
patches=[]
for patch in corrections:
    if 'heading' in patch:
        matches=[s for s in spans if s['text']==patch['old'] and s['origin'][0]>440]
        assert len(matches)==1
        selected=matches;rect=fitz.Rect(matches[0]['bbox'])
    else:
        matches=[b for b in blocks if normalize(' '.join(s['text'] for l in b['lines'] for s in l['spans']))==patch['old']]
        assert len(matches)==1,patch['old']
        selected=[s for l in matches[0]['lines'] for s in l['spans']]
        rect=fitz.Rect(matches[0]['bbox'])
    first=selected[0];lineheight=selected[1]['origin'][1]-first['origin'][1] if len(selected)>1 else 10.05948
    rect=fitz.Rect(rect.x0-.3,rect.y0-.3,578 if 'heading' in patch else 414,rect.y1+.3)
    p.add_redact_annot(rect,fill=None)
    patches.append({**patch,'rect':list(rect),'origin':first['origin'],'size':first['size'],'color':first['color'],'lineheight':lineheight,'font':'Heading' if 'heading' in patch else 'Copy'})
p.apply_redactions(images=0,graphics=0,text=0)
fonts={}
for alias,name in [('Copy','inter-latin-400-normal'),('Heading','montserrat-latin-700-normal')]:
    file=CACHE/(name+'.ttf');tt=TTFont(FONTDIR/(name+'.woff2'));tt.flavor=None;tt.save(file)
    p.insert_font(fontname=alias,fontfile=str(file));fonts[alias]=fitz.Font(fontfile=str(file))
for patch in patches:
    x,y=patch['origin']
    for i,line in enumerate(patch['lines']):
        assert x+fonts[patch['font']].text_length(line,fontsize=patch['size'])<patch['rect'][2]
        p.insert_text((x,y+i*patch['lineheight']),line,fontname=patch['font'],fontsize=patch['size'],color=fitz.sRGB_to_pdf(patch['color']))
p.set_trimbox(fitz.Rect(9,9,621,801));p.set_bleedbox(fitz.Rect(0,0,630,810))
doc.set_metadata({**doc.metadata,'title':'GCPRO ERP Property Management - Final','subject':'Four requested English corrections; existing design preserved'})
doc.save(OUT,garbage=4,deflate=True)
final=fitz.open(OUT);q=final[0]
assert len(final)==1 and q.rect==original[0].rect
for patch in patches:
    actual=normalize(q.get_textbox(fitz.Rect(patch['rect'])))
    assert patch['new'] in actual,(patch['new'],actual)
assert normalize(q.get_textbox(fitz.Rect(445,373,579,400)))==corrections[3]['heading']
for rect in [fitz.Rect(40,233,296,333),fitz.Rect(315,233,590,333)]:
    assert q.get_textbox(rect)==original[0].get_textbox(rect),'Main paragraph changed'
expected_terms=['FREE','Property Management','property-specific response plan','application customized','24/7','full restoration','business continuity','resident retention','NOI']
alltext=normalize(q.get_text())
assert all(term.lower() in alltext.lower() for term in expected_terms)
assert '\ufffd' not in alltext and '\u25a1' not in alltext
refs={font[0] for font in q.get_fonts(full=True)}
assert all(final.extract_font(xref)[3] for xref in refs)
def render(page,scale=2,clip=None):
    pix=page.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False,clip=clip)
    return Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
a,b=render(original[0]),render(q)
diff=ImageChops.difference(a,b);mask=ImageDraw.Draw(diff)
for patch in patches:
    x0,y0,x1,y1=patch['rect'];mask.rectangle(((x0-2)*2,(y0-2)*2,(x1+2)*2,(y1+2)*2),fill=(0,0,0))
assert diff.getbbox() is None,'Design changed outside the four corrections'
qr_box=fitz.Rect(530,730,590,795)
qr_before=zxingcpp.read_barcodes(render(original[0],5,qr_box))
qr_after=zxingcpp.read_barcodes(render(q,5,qr_box))
assert len(qr_before)==len(qr_after)==1
assert qr_before[0].text==qr_after[0].text=='https://gcprochicago.com/'
assert ImageChops.difference(render(original[0],3,qr_box),render(q,3,qr_box)).getbbox() is None
b.save(HERE/'GCPRO-ERP-Property-Management-FINAL.png')
(HERE/'checks.json').write_text(json.dumps({'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'final_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),'exact_corrections':4,'unchanged_outside_correction_regions':'pixel-identical at 144 dpi','main_paragraph':'unchanged text and artwork','required_message_terms':expected_terms,'missing_glyphs':False,'all_fonts_embedded':len(refs),'page_media_inches':[8.75,11.25],'trim_inches':[8.5,11],'bleed_inches':.125,'qr_decoded_url':qr_after[0].text,'qr_visual_and_url':'unchanged','qr_destination_purpose':'GCPRO public homepage, not a dedicated ERP landing page','base_release_and_pm_trifold':'unchanged; final candidate on separate review branch'},indent=2)+'\n')
print(OUT)
