"""Cover-only concept using the released Commercial Trifold's original artwork."""
from pathlib import Path
import json, io, hashlib
import pymupdf as fitz
from fontTools.ttLib import TTFont
from PIL import Image, ImageOps, ImageChops, ImageDraw

HERE=Path(__file__).resolve().parent
MARKETING=HERE.parents[1]
SOURCE=MARKETING/'releases/2026-10-20/02 Commercial and PGP/GCPRO CSP - Commercial Leave Behind Trifold.pdf'
COPY=json.loads((HERE/'copy.json').read_text(encoding='utf-8'))
CACHE=HERE/'.cache';CACHE.mkdir(exist_ok=True)
font=TTFont(MARKETING/'source/01_Brand_System/fonts/montserrat-latin-800-normal.woff2')
font.flavor=None;font.save(CACHE/'Montserrat-800.ttf')
original=fitz.open(SOURCE);doc=fitz.open(SOURCE);p=doc[0]
photo_rect=fitz.Rect(535.5,0,810,291.75)
photos=[img[0] for img in p.get_images() if any(r.x0>530 and r.y0<0 and r.y1>290 for r in p.get_image_rects(img[0]))]
assert len(photos)==1
photo_path=HERE/'assets/commercial_water_damage_restoration.jpg'
photo=ImageOps.exif_transpose(Image.open(photo_path)).convert('RGB')
# Preserve proportions in the original clipped image placement; crop only the sides.
placement=p.get_image_rects(photos[0])[0]
height=photo.height;width=round(height*placement.width/placement.height)
photo=ImageOps.fit(photo,(width,height),method=Image.Resampling.LANCZOS,centering=(.58,.5))
stream=io.BytesIO();photo.save(stream,format='JPEG',quality=97,subsampling=0)
p.replace_image(photos[0],stream=stream.getvalue())
source_spans=[s for b in p.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']]
first=next(s for s in source_spans if s['text']=='WHEN')
p.add_redact_annot(fitz.Rect(557,377,789,522),fill=None)
p.apply_redactions(images=0,graphics=0,text=0)
p.insert_font(fontname='CoverHeading',fontfile=str(CACHE/'Montserrat-800.ttf'))
tag=TTFont(MARKETING/'source/01_Brand_System/fonts/montserrat-latin-700-normal.woff2')
tag.flavor=None;tag.save(CACHE/'Montserrat-700.ttf')
p.insert_font(fontname='CoverTag',fontfile=str(CACHE/'Montserrat-700.ttf'))
font_metrics=fitz.Font(fontfile=str(CACHE/'Montserrat-800.ttf'))
x,y=first['origin']
for i,line in enumerate(COPY['headline_lines']):
    assert x+font_metrics.text_length(line,fontsize=26)<789
    color=(1,1,1) if i<2 else (240/255,90/255,41/255)
    p.insert_text((x,y+27*i),line,fontname='CoverHeading',fontsize=26,color=color)
p.insert_text((x,514),COPY['subtitle'],fontname='CoverTag',fontsize=8.5,color=(.85,.88,.94))
out=HERE/'GCPRO-PM-Trifold-Water-Mitigation-PHOTO-REVIEW.pdf'
doc.save(out,garbage=4,deflate=True)
result=fitz.open(out)
assert len(result)==2
assert 'WATER\nDAMAGE?' in result[0].get_text()
assert 'WHEN\nDISASTER' not in result[0].get_text()
def render(page,scale=2):
    pix=page.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False)
    return Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
a,b=render(original[0]),render(result[0]);diff=ImageChops.difference(a,b);draw=ImageDraw.Draw(diff)
draw.rectangle((1069,0,1620,585),fill=(0,0,0))
draw.rectangle((1112,752,1580,1046),fill=(0,0,0))
assert diff.getbbox() is None,'Unexpected front-page changes'
assert ImageChops.difference(render(original[1]),render(result[1])).getbbox() is None,'Inside changed'
result[0].get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(535.5,0,810,630)).save(HERE/'GCPRO-PM-Water-Cover-PHOTO.png')
for i in range(2):result[i].get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(HERE/f'GCPRO-PM-Trifold-Page-{i+1}.png')
(HERE/'checks.json').write_text(json.dumps({'pages':2,'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'headline':COPY['headline'],'photo':'owner supplied commercial_water_damage_restoration.jpg; proportional crop only','photo_sha256':hashlib.sha256(photo_path.read_bytes()).hexdigest(),'inside':'pixel-identical at 144 dpi','other_front_artwork':'pixel-identical outside headline/photo regions at 144 dpi','status':'photo trial for owner review'},indent=2)+'\n')
print(out)
