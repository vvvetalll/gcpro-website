from pathlib import Path
import json
root=Path.cwd();out=root/'outputs/GCPRO-PGP-Vector-Logo';out.mkdir(exist_ok=True)
navy='#1a327d';orange='#f05a29'
orbit='M867 412 C1048 390 1170 443 1156 568 C1134 800 731 987 393 966 C153 956 38 861 160 666 C115 800 209 864 407 874 C699 888 1023 719 1060 576 C1094 486 1013 427 867 412 Z'
shield='M627 79 L1078 274 L1078 579 C1078 900 903 1083 628 1200 C353 1089 174 899 174 579 L174 274 Z M627 172 L253 332 L253 579 C253 860 416 1022 628 1105 C839 1022 1000 860 1000 579 L1000 332 Z'
buildings='''
<path d="M471 323 628 212V1100H471Z M641 222 783 325V1100H641Z"/>
<path d="M276 518 396 436V1100H276Z M410 426 458 455V1100H410Z"/>
<path d="M797 454 841 428V1100H797Z M855 438 980 521V1100H855Z"/>
'''
cuts='''
<path d="M521 287V1100 M553 264V1100 M585 242V1100" fill="none" stroke="black" stroke-width="8"/>
<path d="M641 426 783 505 M641 458 783 537 M641 490 783 569" fill="none" stroke="black" stroke-width="10"/>
<path d="M276 577 396 495 M276 626 396 544 M276 675 396 593" fill="none" stroke="black" stroke-width="11"/>
<path d="M855 493 980 576 M855 541 980 624 M855 589 980 672" fill="none" stroke="black" stroke-width="11"/>
'''
def graphic(blue=navy,accent=orange,mono=False):
 return f'''<defs>
<mask id="orbit-clearance" maskUnits="userSpaceOnUse" x="0" y="0" width="1254" height="1254"><rect width="1254" height="1254" fill="white"/><path d="{orbit}" fill="black" stroke="black" stroke-width="22" stroke-linejoin="round"/></mask>
<mask id="building-channels" maskUnits="userSpaceOnUse" x="0" y="0" width="1254" height="1254"><rect width="1254" height="1254" fill="white"/>{cuts}</mask>
<mask id="shield-interior" maskUnits="userSpaceOnUse" x="0" y="0" width="1254" height="1254"><rect width="1254" height="1254" fill="black"/><path d="M627 172 L253 332 L253 579 C253 860 416 1022 628 1105 C839 1022 1000 860 1000 579 L1000 332 Z" fill="white" stroke="black" stroke-width="26" stroke-linejoin="round"/></mask>
<clipPath id="tower-zone"><path d="M0 0H1254V410H867C1013 427 1094 486 1060 576C1023 719 699 888 407 874C209 864 115 800 160 666H0Z"/></clipPath>
</defs>
<g fill="{blue}" mask="url(#orbit-clearance)"><path d="{shield}" fill-rule="evenodd"/><g clip-path="url(#tower-zone)"><g mask="url(#shield-interior)"><g mask="url(#building-channels)">{buildings}</g></g></g></g>
<path d="{orbit}" fill="{accent}"/>
'''
def svg(content,view='0 0 1254 1254',title='Property Guardian Program'):
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view}" role="img" aria-label="{title}"><title>{title}</title>{content}</svg>'
for name,blue,accent in [('pgp-mark',navy,orange),('pgp-mark-navy',navy,navy),('pgp-mark-reversed','#ffffff',orange)]:
 (out/(name+'.svg')).write_text(svg(graphic(blue,accent)),encoding='utf8')
(out/'palette.json').write_text(json.dumps({'navy':navy,'orange':orange,'background':'transparent','typeface':'Montserrat','style':'flat vector'},indent=2),encoding='utf8')
(out/'README.txt').write_text('GCPRO Property Guardian Program — vector mark\n\nOriginal vector reconstruction of the supplied shield, buildings and orbit.\nExact brand colors: navy #1A327D; orange #F05A29.\nTransparent background. No embedded raster images. No gradients.\nMark variants: two-color, navy monochrome, reversed white/orange.\nLogo wordmark: Montserrat, converted to vector paths.\nSVG files remain editable in Illustrator, Inkscape, Figma and other vector editors.\n',encoding='utf8')
print('Created vector mark in three color versions.')

