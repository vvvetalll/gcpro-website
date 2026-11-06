"""Reword only existing PM Trifold text areas; retain the supplied current PDF artwork."""
from pathlib import Path
import json,io,hashlib,re
import pymupdf as fitz
from fontTools.ttLib import TTFont
from PIL import Image,ImageOps,ImageChops,ImageDraw

HERE=Path(__file__).resolve().parent
MARKETING=HERE.parents[1]
SOURCE=HERE.parent/'2026-11-06-pm-trifold-corridor-photo/GCPRO-PM-Trifold-CORRIDOR-PHOTO-REVIEW.pdf'
PHOTO=HERE/'assets/gcpro-man-office2.jpg'
COPY=json.loads((HERE/'copy.json').read_text(encoding='utf-8'))
FONTDIR=MARKETING/'source/01_Brand_System/fonts'
CACHE=HERE/'.cache';CACHE.mkdir(exist_ok=True)
OUT=HERE/'GCPRO-PM-Trifold-Water-Mitigation-Messaging-REVIEW.pdf'
original=fitz.open(SOURCE);doc=fitz.open(SOURCE)

# These rectangles are the original text slots. Their origins, sizes, colors and
# line spacing are read from the current PDF, not recreated as a new composition.
zones=[
 (0,'outer_heading',(31,195,253,254),18),
 *[(0,f'outer_{i}',(64,y0,252,y1),12) for i,(y0,y1) in enumerate([(282,324),(335,365),(376,407),(417,448),(458,489),(499,531)],1)],
 (1,'inside_left_heading',(31,29,253,107),18),
 (1,'inside_left_subhead_1',(31,129,253,144),12),
 (1,'inside_left_body_1',(31,146,253,246),14.25),
 (1,'inside_left_subhead_2',(31,275,253,291),12),
 (1,'inside_left_body_2',(31,292,253,378),14.25),
 (1,'inside_middle_heading',(296,29,519,89),18),
 (1,'inside_middle_intro',(296,112,519,127),14.25),
 *[(1,f'inside_middle_{i}',(309,y0,519,y1),14.25) for i,(y0,y1) in enumerate([(134,204),(206,235),(237,266),(268,297),(299,328),(330,372),(374,417),(419,448),(450,520)],1)],
 (1,'inside_right_heading_1',(595,38,779,56),12),
 (1,'inside_right_body_1',(595,57,779,115),14.25),
 (1,'inside_right_heading_2',(595,128,779,148),12),
 (1,'inside_right_body_2',(595,148,779,248),14.25),
 (1,'inside_right_heading_3',(595,261,779,281),12),
 (1,'inside_right_body_3',(595,281,779,381),14.25),
 (1,'service_1',(574,421,779,436),12)
]
fontfiles={
 'MontserratThin-ExtraBold':'montserrat-latin-800-normal',
 'MontserratThin-Bold':'montserrat-latin-700-normal',
 'MontserratThin-SemiBold':'montserrat-latin-600-normal',
 'Inter-Regular':'inter-latin-400-normal',
 'Inter-Medium':'inter-latin-500-normal'}
fonts={};aliases={};source_spans=[]
for p in original:
    source_spans.append([s for b in p.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']])
layout=[];overflows=[]
for pi,key,coords,leading in zones:
    rect=fitz.Rect(coords)
    candidates=[s for s in source_spans[pi] if rect.contains(fitz.Point(s['origin']))]
    assert candidates,('No original text style',key)
    first=sorted(candidates,key=lambda s:(s['origin'][1],s['origin'][0]))[0]
    name=first['font'];assert name in fontfiles,(key,name)
    if name not in fonts:
        fn=fontfiles[name];ttf=CACHE/(fn+'.ttf')
        font=TTFont(FONTDIR/(fn+'.woff2'));font.flavor=None;font.save(ttf)
        fonts[name]=fitz.Font(fontfile=str(ttf));aliases[name]='Text'+str(len(fonts))
        for p in doc:p.insert_font(fontname=aliases[name],fontfile=str(ttf))
    x,y=first['origin'];size=first['size'];metrics=fonts[name]
    # Original live line width; keep the type size and line height, edit copy to fit.
    right=coords[2]-1
    lines=[];line=''
    for word in COPY[key].split():
        test=(line+' '+word).strip()
        if line and metrics.text_length(test,fontsize=size)>right-x:
            lines.append(line);line=word
        else:line=test
    if line:lines.append(line)
    end=y+(len(lines)-1)*leading-size*metrics.descender
    if end>coords[3]+.5:overflows.append((key,len(lines),round(end,2),coords[3],lines))
    if pi==0 and key.startswith('outer_') and key!='outer_heading':
        row=int(key.rsplit('_',1)[1])-1
        bounds=[(278.25,330.75),(331.5,372),(372.75,413.25),(414,454.5),(455.25,495.75),(496.5,537)][row]
        center=sum(bounds)/2
        y=center-(len(lines)-1)*leading/2+size*(metrics.ascender+metrics.descender)/2
    layout.append({'page':pi,'key':key,'rect':list(coords),'origin':[x,y],'font':name,'size':size,'color':first['color'],'leading':leading,'lines':lines})
    doc[pi].add_redact_annot(rect,fill=None)

assert not overflows,('Copy too long at original type size',overflows)
number_boxes=[];numbers=[]
for item in layout:
    if item['page']==0 and item['key'].startswith('outer_') and item['key']!='outer_heading':
        n=int(item['key'].rsplit('_',1)[1]);label=f'{n:02d}'
        source=next(s for s in source_spans[0] if s['text']==label and s['origin'][0]<40)
        x0,y0,x1,y1=item['rect'];box=fitz.Rect(31,y0,61,y1)
        number_boxes.append(box);doc[0].add_redact_annot(box,fill=None)
        text_font=fonts[item['font']];size=item['size'];first_y=item['origin'][1]
        center=first_y+(len(item['lines'])-1)*item['leading']/2-size*(text_font.ascender+text_font.descender)/2
        num_font=fonts['MontserratThin-ExtraBold'];num_size=source['size']
        baseline=center+num_size*(num_font.ascender+num_font.descender)/2
        numbers.append((source['origin'][0],baseline,label,num_size,source['color']))
for p in doc:p.apply_redactions(images=0,graphics=0,text=0)
for name,alias in aliases.items():
    for p in doc:p.insert_font(fontname=alias,fontfile=str(CACHE/(fontfiles[name]+'.ttf')))
for item in layout:
    p=doc[item['page']];x,y=item['origin']
    for i,line in enumerate(item['lines']):
        p.insert_text((x,y+i*item['leading']),line,fontname=aliases[item['font']],fontsize=item['size'],color=fitz.sRGB_to_pdf(item['color']))
for x,y,label,size,color in numbers:
    doc[0].insert_text((x,y),label,fontname=aliases['MontserratThin-ExtraBold'],fontsize=size,color=fitz.sRGB_to_pdf(color))

# Owner correction: flood photograph stays on the cover; office photo only on flap.
p=doc[0]
photos=[i[0] for i in p.get_images() if any(r.x0>530 and r.y0<0 and r.y1>290 for r in p.get_image_rects(i[0]))]
assert len(photos)==1
flap=[i[0] for i in p.get_images() if any(abs(r.x0)<1 and r.y0<0 and r.width>250 for r in p.get_image_rects(i[0]))]
assert len(flap)==1
photo_dpi=[]
for xref in [photos[0],flap[0]]:
    placement=p.get_image_rects(xref)[0]
    cover=xref==photos[0]
    asset=HERE/'assets/commercial-water-loss.jpg' if cover else PHOTO
    photo=ImageOps.exif_transpose(Image.open(asset)).convert('RGB')
    ph=photo.height;pw=round(ph*placement.width/placement.height)
    photo=ImageOps.fit(photo,(pw,ph),method=Image.Resampling.LANCZOS,centering=(.58 if cover else .48,.5))
    buf=io.BytesIO();photo.save(buf,format='JPEG',quality=97,subsampling=0)
    p.replace_image(xref,stream=buf.getvalue())
    photo_dpi.append(round(ph/(placement.height/72)))
for p in doc:
    # Preserve full bleed media/crop geometry; explicitly identify the existing trim.
    p.set_trimbox(fitz.Rect(9,9,801,621));p.set_bleedbox(fitz.Rect(0,0,810,630))
doc.set_metadata({**doc.metadata,'title':'GCPRO Property Management - Water Mitigation and Full Restoration','subject':'Messaging review; existing two-sided trifold design retained'})
doc.save(OUT,garbage=4,deflate=True)

result=fitz.open(OUT)
font_refs={v[0] for p in result for v in p.get_fonts(full=True)}
missing_fonts=[xref for xref in font_refs if not result.extract_font(xref)[3]]
assert not missing_fonts,('Missing embedded fonts',missing_fonts)
normalize=lambda s:re.sub(r'\s+',' ',s).strip()
text=' '.join(p.get_text() for p in result)
assert len(result)==2 and '\ufffd' not in text and '\u25a1' not in text
for item in layout:
    actual=result[item['page']].get_textbox(fitz.Rect(item['rect']))
    assert normalize(COPY[item['key']]) in normalize(actual),('Text check',item['key'],actual)
for banned in ['Public Relations nightmare','half the time','licensed, insured and certified','The Importance of Disaster Planning','Priority Response for Our Clients']:
    assert banned.lower() not in normalize(text).lower(),banned
def render(page,scale=2):
    pix=page.get_pixmap(matrix=fitz.Matrix(scale,scale),alpha=False)
    return Image.frombytes('RGB',(pix.width,pix.height),pix.samples)
for pi in range(2):
    a,b=render(original[pi]),render(result[pi]);diff=ImageChops.difference(a,b);draw=ImageDraw.Draw(diff)
    for item in layout:
        if item['page']==pi:
            r=item['rect'];draw.rectangle(((r[0]-2)*2,(r[1]-2)*2,(r[2]+2)*2,(r[3]+2)*2),fill=(0,0,0))
    if pi==0:
        draw.rectangle((1069,0,1620,585),fill=(0,0,0))
        draw.rectangle((0,0,541,359),fill=(0,0,0))
        for r in number_boxes:draw.rectangle(((r.x0-2)*2,(r.y0-2)*2,(r.x1+2)*2,(r.y1+2)*2),fill=(0,0,0))
    assert diff.getbbox() is None,('Unexpected artwork change',pi)
    b.save(HERE/f'GCPRO-PM-Trifold-{["Outside","Inside"][pi]}-REVIEW.png')
    assert list(result[pi].mediabox)==[0,0,810,630]
    assert list(result[pi].trimbox)==[9,9,801,621]
    assert not list(result[pi].widgets() or [])
result[0].get_pixmap(matrix=fitz.Matrix(2,2),clip=fitz.Rect(535.5,0,810,630)).save(HERE/'GCPRO-PM-Cover-REVIEW.png')
(HERE/'layout.json').write_text(json.dumps(layout,indent=2)+'\n')
checks={'pages':2,'copy_blocks':len(layout),'all_copy_fits_original_sizes':True,'all_copy_extracted_and_matched':True,
        'artwork_outside_edited_regions':'pixel-identical at 144 dpi','media_inches':[11.25,8.75],
        'trim_inches':[11,8.5],'bleed_inches':.125,'photo_effective_dpi_cover_flap':photo_dpi,'outer_list_alignment':'numbers and left-aligned text vertically centered within original row boundaries',
        'fonts_embedded':len(font_refs),'missing_embedded_fonts':missing_fonts,
        'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'output_sha256':hashlib.sha256(OUT.read_bytes()).hexdigest(),
        'photo_sha256':hashlib.sha256(PHOTO.read_bytes()).hexdigest(),'status':'REVIEW - approval pending; base release and ERP Flyer unchanged'}
checks['cover_photo']='commercial-water-loss.jpg; retained commercial flood photo'
checks['flap_photo']='gcpro-man-office2.jpg; replaced only the outer flap photograph'
(HERE/'checks.json').write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
