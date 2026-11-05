# PHOTOS — slots, files and prompt templates

Photos live in `assets/photos/` (a file in `assets/photos/graded/` with the same name takes priority).
Mapping is in `photos.json`: `"SLOT": {"file": "...jpg", "focus": "X% Y%", "zoom": 1.0}`.
`focus` = CSS object-position: lower Y shows more of the top of the image (headroom); X moves left/right.
A slot with `"idea": "..."` and no file shows a gray placeholder with that caption.

## Slots
| Slot | Where | Approx. size (in) | Generate as | Current file |
|---|---|---|---|---|
| LB.cover | ASP Leave Behind – front cover | 3.8 x 4.05 | 4:5 vertical | lb-desk-handshake2.jpg |
| LB.flap | ASP Leave Behind – flap | 3.9 x 2.45 | 3:2 | lb-flap-agent.jpg |
| LB.inside1 / inside2 | ASP Leave Behind – inside | ~3.9 x 3.85 / flexible | 1:1 or 3:2 | lb-agency-team.jpg / lb-report-tablet.jpg |
| RC.cover / flap / inside1 / inside2 | Renewal Trifold Commercial | as above | | rc-fleet / rc-restaurant-doc / rc-lobby-manager / rc-flood |
| RR.cover / flap / inside1 / inside2 | Renewal Trifold Residential | as above | | rr-cover-family2 / gc-pickup-house / gc-flap-consult / rr-extraction-real (real photo, zoom 1.7) |
| PSP.cover | PSP Plumber trifold – front cover | 3.8 x 4.05 | 4:5 vertical | psp-cover-plumber4.jpg |
| PSP.flap | PSP – flap | 3.9 x 2.45 | 3:2 | psp-handshake3.jpg |
| PSP.inside1 | PSP – inside left (plumber gives GCPRO card) | ~3.9 x 2.5 | 3:2 | psp-plumber-card2.jpg |
| PSP.inside2 | PSP – inside middle (GCPRO documents on tablet) | ~3.8 x 2.8 | 3:2 | psp-tech-tablet2-ext.jpg (extended upward for headroom) |
| DF.hero | Digital Flyer | full width band | 16:9 | df-inspection.jpg |
| SR01/02/03/05.hero | Special Reports p.1 | 8.75 wide x auto (~2–3.5) | 16:9, people in middle band | sr01-handshake / sr02-neighbors / sr03-basement-consult / sr05-agent-office |

Other image assets: `city-wide-src.jpg` (grayscale skyline → `assets/bg-city-wide.jpg` navy duotone), `skyline-line-src.png` (line art → `assets/skyline-full.png` for white panels, `assets/skyline-on-navy.png` for footers), `gcpro-business-card.png` (reference/composite for business cards).

## Rules
- People scenes can be AI. No AI equipment, machines, water puddles or stains (look fake).
- GCPRO tech: navy polo + navy cap with GCPRO logo (give the generator a logo/polo reference).
- PSP plumber: plain gray work shirt, no logo. Keep the same plumber across PSP photos (use a face reference).
- Typical American suburban home in the Chicago area (white shaker cabinets, quartz counters) — not British kitchens.
- Leave ≥15% empty space above heads (images are cropped by the layout and the trim).
- Resolution: ≥1500 px on the long side (≥2500 px for full-width letter heroes).
- If the generator distorts a logo/card/text: generate it plain/blank and composite the real asset afterward.

## Prompt template (people scene)
```
Photorealistic candid photo, 3:2 horizontal. [WHO + CLOTHING] [ACTION] in [typical American suburban home in the Chicago area, white shaker cabinets, natural window light].
[EMOTION]. Faces clearly visible in the middle of the frame, generous empty space above their heads.
Shot on a 50mm lens, natural skin texture, documentary style.
No water damage, no stains, no equipment, no text, no logos.
```
With references: "Image 1 = … (use face/hair exactly). Image 2 = GCPRO logo/polo…". One change per request; start a new chat if results degrade.

## Extend a photo upward (headroom)
```
Extend this image upward: add about 20% more background above the people's heads (continue the background naturally). Keep the people, faces, clothing, logos, lighting and everything else exactly the same.
```

## Background textures
- City duotone (large navy blocks): grayscale, overcast, low-contrast Chicago skyscrapers, 3:1 panorama, no people/text. Toned so the average color = #1a327d.
- Skyline line art: "Minimalist line art of the Chicago skyline, clean black outline on pure white, 4:1 panorama, Willis Tower with antennas, no fill, no shading, no text".
