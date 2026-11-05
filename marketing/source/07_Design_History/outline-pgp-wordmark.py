from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import importlib.util
root=Path.cwd();out=root/'outputs/GCPRO-PGP-Vector-Logo';fonts=root/'work/kit/GCPRO_ASP_Kit_SOURCE/fonts'
spec=importlib.util.spec_from_file_location('mark',root/'work/build-vector-pgp.py');mark=importlib.util.module_from_spec(spec);spec.loader.exec_module(mark)
def word(text,file,size,x,y,color,spacing=0):
 font=TTFont(fonts/file);glyphs=font.getGlyphSet();cmap=font.getBestCmap();scale=size/font['head'].unitsPerEm;pen=SVGPathPen(glyphs);cursor=x
 for c in text:
  name=cmap[ord(c)];glyphs[name].draw(TransformPen(pen,(scale,0,0,-scale,cursor,y)))
  cursor+=font['hmtx'].metrics[name][0]*scale+spacing
 return f'<path d="{pen.getCommands()}" fill="{color}"/>',cursor-x
for reversed in [False,True]:
 blue='#ffffff' if reversed else mark.navy
 lines=[];width=0
 for text,size,y,color,spacing,file in [('PROPERTY',170,505,blue,-2,'montserrat-latin-800-normal.woff2'),('GUARDIAN',170,705,blue,-2,'montserrat-latin-800-normal.woff2'),('PROGRAM',80,850,mark.orange,22,'montserrat-latin-700-normal.woff2')]:
  d,w=word(text,file,size,1300,y,color,spacing);lines.append(d);width=max(width,w)
 art=mark.graphic(blue,mark.orange)+''.join(lines)
 name='pgp-logo-horizontal-reversed.svg' if reversed else 'pgp-logo-horizontal.svg'
 (out/name).write_text(mark.svg(art,f'0 0 {int(1380+width)} 1254'),encoding='utf8')
print('Wordmarks converted to editable vector paths; fonts not required to open.')
