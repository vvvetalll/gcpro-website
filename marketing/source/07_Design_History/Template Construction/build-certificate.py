from pathlib import Path
import shutil,json
root=Path.cwd();src=root/'work/kit/GCPRO_ASP_Kit_SOURCE';out=root/'outputs/GCPRO-PGP-Certificate-trial-source';out.mkdir(exist_ok=True)
for name in ['assets','fonts']:shutil.copytree(src/name,out/name,dirs_exist_ok=True)
shutil.copy2(src/'kit.css',out/'kit.css')
shutil.copy2(r'C:/Users/VitaliiVozniak/Downloads/Shielded Skyline with Orbiting Swoosh.png',out/'assets/pgp-trial-symbol.png')
brand=json.loads((src/'content.json').read_text(encoding='utf8'))['contact']
html='''<!doctype html><html><head><meta charset="utf-8"><title>GCPRO Property Guardian Program Certificate</title><link rel="stylesheet" href="kit.css"><style>
@page{size:11.25in 8.75in;margin:0}*{box-sizing:border-box}
.certificate{width:11.25in;height:8.75in;position:relative;overflow:hidden;background:white;color:var(--navy);font-family:Inter}
.frame{position:absolute;inset:.32in;border:1pt solid var(--navy);pointer-events:none;z-index:4}
.frame:before,.frame:after{content:'';position:absolute;width:.45in;height:3pt;background:var(--ember);top:-1.5pt}
.frame:before{left:.45in}.frame:after{right:.45in}
.city{position:absolute;bottom:0;left:0;width:100%;height:1.05in;background:url(assets/skyline-full.png) 50% 100%/auto 2.6in no-repeat;opacity:.33}
.gcpro{position:absolute;left:.65in;top:.59in;width:1.65in}
.top-label{position:absolute;right:.65in;top:.7in;font:700 7.5pt Montserrat;letter-spacing:.2em;color:var(--navy)}
.heading{position:absolute;top:1.08in;left:.7in;right:.7in;text-align:center}
.eyebrow{font:600 10pt Montserrat;letter-spacing:.18em;text-transform:uppercase;margin-bottom:.1in}
h1{font:800 25pt/1.12 Montserrat;margin:0;color:var(--navy)}
.rule{height:2pt;width:.45in;background:var(--ember);margin:.2in auto 0}
.property{position:absolute;left:2.05in;right:2.05in;top:2.23in}
.property-field{border-bottom:.6pt solid #a7b2ca;height:.38in;margin-bottom:.06in;background:#fbfcfe}
.property-field:first-child{height:.47in}.property-field:last-child{height:.3in}
.protected{position:absolute;top:3.72in;left:.7in;right:.7in;text-align:center;font:600 9pt Montserrat;letter-spacing:.08em}
.program-lockup{position:absolute;top:4.04in;left:.7in;right:.7in;display:flex;align-items:center;justify-content:center;gap:.3in}
.program-lockup img{width:2.03in;height:2.03in;object-fit:contain;flex-shrink:0}
.program-name{font:800 24pt/1.03 Montserrat;letter-spacing:-.01em}
.program-name .program{font:700 11pt Montserrat;letter-spacing:.3em;color:var(--ember);margin-top:.14in}
.slogan{position:absolute;top:6.25in;left:.7in;right:.7in;text-align:center;font:500 9pt Inter;color:var(--body)}
.bottom{position:absolute;left:.67in;right:.67in;top:7.12in;display:flex;justify-content:space-between;align-items:flex-start}
.courtesy{font:600 7pt Montserrat;letter-spacing:.1em;margin-bottom:.08in}
.company{font:700 10pt Montserrat;color:var(--navy);margin-bottom:.07in}
.contact-label{font:700 6.2pt Montserrat;letter-spacing:.1em;color:var(--ember);margin-bottom:.04in}
.phone{font:800 13pt Montserrat;line-height:1.1}.web{font:400 8pt Inter;margin-top:.045in;color:var(--body)}
.signatures{display:grid;grid-template-columns:2.9in 1.1in;gap:.3in;padding-top:.33in}
.signature-field{height:.29in;border-bottom:.6pt solid #7b89aa}
.signature-label{font:400 8pt Inter;color:var(--body);margin-top:.07in}
</style></head><body><section class="certificate"><div class="city"></div><div class="frame"></div>
<img class="gcpro" src="assets/logo.svg"><div class="top-label">PROPERTY GUARDIAN PROGRAM</div>
<div class="heading"><div class="eyebrow">Certificate of</div><h1>EMERGENCY RESPONSE PROGRAM</h1><div class="rule"></div></div>
<div class="property"><div class="property-field" data-field="text" data-name="Property_Name"></div><div class="property-field" data-field="text" data-name="Property_Address"></div><div class="property-field" data-field="text" data-name="Property_Additional_Line"></div></div>
<div class="protected">IS OFFICIALLY PROTECTED BY</div>
<div class="program-lockup"><img src="assets/pgp-trial-symbol.png"><div class="program-name">PROPERTY<br>GUARDIAN<div class="program">PROGRAM</div></div></div>
<div class="slogan">You Can’t Know the Future, But You Can Prepare for It!</div>
<div class="bottom"><div><div class="courtesy">COURTESY OF:</div><div class="company">GCPRO Restoration</div><div class="contact-label">24-HOUR EMERGENCY SERVICE</div><div class="phone">PHONE</div><div class="web">WEBSITE</div></div>
<div class="signatures"><div><div class="signature-field" data-field="text" data-name="Official_Signature"></div><div class="signature-label">Official Signature</div></div><div><div class="signature-field" data-field="text" data-name="Date"></div><div class="signature-label">Date</div></div></div></div>
</section></body></html>'''.replace('>PHONE<','>'+brand['phone']+'<').replace('>WEBSITE<','>'+brand['web']+'<')
(out/'index.html').write_text(html,encoding='utf8')
print('One certificate trial; supplied symbol preserved, brand typography added.')
