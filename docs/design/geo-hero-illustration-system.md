# GEO Hero illustration system — owner-approved direction, 2026-11-04

Status: **visual direction approved; first production master pending review.** No authorization to replace existing staging assets or edit production. This document is the handoff for 11 location-specific Hero illustrations, not evidence that any assets have been installed.

## Approved visual reference
- Owner supplied an Elementor screenshot of the Lombard Hero with the current blue-map illustration in the existing asymmetric blob mask. The blue city silhouette is preferred to orange because the orange Call CTA must remain the visual priority.
- Existing Hero: Elementor Atomic component **1318**, page-specific `image` Override; current Lombard Media **4216** (PNG 1448 × 1086, about 1.70 MB), per Work's read-only inspection supplied by owner.
- Current `object-fit: cover; object-position: 50% 50%`; mask `blob-haikei-4.svg`, viewBox **900 × 675**, alpha, centered `contain`, no-repeat. Observed image box desktop 1440 viewport: **695 × 521.25 CSS px**; mobile 390 viewport: **334.67 × 251 CSS px**.
- **Do not change** Elementor mask, Hero component, columns, buttons, global CSS, or layouts to fit the illustration. Make image art fit the existing mask.

## Master and exports
- Editable **2000 × 1500 px, 4:3** master (vector preferred), rectangular **without baked-in blob silhouette**; opaque navy background, sRGB.
- WebP 2000 × 1500, quality 85, method 6 as a starting point; target 150–300 KB, accept up to ~400 KB if clean edges require it. Verify actual file size and visual quality; use lossless if necessary. Do not repeatedly recompress.
- Work-provided approximate safe zones (2000 × 1500 coordinates): principal recognizable object X 560–1440 / Y 480–1050; critical details/text X 700–1300 / Y 570–1050. Exact original SVG mask overlay is authoritative, not these rectangles.
- Work-reported visible X range by height: at 10% Y, 21.7–44.8%; 30%, 14.5–76%; 50%, 15.4–85.9%; 70%, 23.3–81.4%; 90%, 44.3–69.2%. These are reported measurements, not independently reverified here.

## Brand art direction
- Deep navy/blue gradient; white and pale blue main landmark and building highlights; orange limited to restrained decorative accents (~5% visible area as design target), **not the city fill**.
- One visually dominant real, identifiable local landmark; secondary architecture generalized, never represented as actual GCPRO work or a real named building without evidence.
- City boundaries only from validated municipal or Census TIGER/Line geometry; correct orientation/proportions. Do not generate cartographic boundaries or office pins by visual guesswork. If accurate geography unavailable, omit the map rather than invent it.
- Lombard office marker only at verified location **220 Eisenhower Lane North, Lombard, IL 60148**; other cities must not imply an office. Avoid redundant city-name label when the H1 already identifies the city; a landmark's actual lettering may be preserved if accurate.
- Water tower for Lombard is the focal landmark. In prior attempts the tower lettering was cut by the mask, the orange map competed with CTA, and small office text was hard to read on mobile. Place critical lettering within the mask safe area. The previously AI-rendered map silhouette/pin are **unverified decorative approximations**, not authoritative geometry.

## 11-city art matrix (candidates, not verified building renderings)
| City | Subject | Verification / constraints |
| --- | --- | --- |
| Lombard | Local water tower | Approved motif; verify tower colors and lettering against user-provided photos, map boundary and real office coordinates |
| Downers Grove | Historic Main Street station candidate | Verify actual façade; no Lombard tower reuse |
| Highland Park | City Hall | Compare to licensed authentic reference already recorded in GEO documentation |
| Elmhurst | Train station candidate | Verify actual façade |
| Glenview | Municipal water tower candidate | Verify shape and lettering |
| Northbrook | Village Hall | Verify façade against official municipal source |
| Oak Brook | Village Hall or verified civic landmark | No Promenade/Oakbrook Center identity |
| Carol Stream | Local water tower | Preserve actual lettering and proportions; no fabricated adjoining structures |
| Elk Grove Village | Village Hall candidate | Verify actual building; no invented local landmark |
| Schaumburg | Schweikher House candidate | Verify distinctive architecture and reference use rights |
| Naperville | Moser Tower / Millennium Carillon | Verify recognizable proportions against Park District reference |

## Implementation / acceptance
1. Produce **one Lombard pilot**, visually compare with the actual SVG mask at desktop **695 × 521.25** and mobile **334.67 × 251**; ensure full tower name legibility and no competing orange map.
2. Confirm any geographical layer and office pin using actual source geometry before calling the asset geographically accurate. Otherwise exclude them from the production pilot.
3. Obtain owner visual approval. Only after explicit authorization, upload optimized WebP and change **Lombard page Hero image Override only**, keeping `full`, existing mask and styles. Add accurate descriptive alt.
4. After pilot acceptance, make ten variants with the same master/safe zones and per-city evidence. Do not batch-publish unreviewed art.
5. Keep source, licenses/geometry provenance, export dimensions and test limitations in this record. No unrelated site changes.

## Current verification and limits
This record consolidates the owner-provided Work specification and screenshots. GitHub source docs were read 2026-11-04. The mask path, dimensions and measured crops were **reported by Work** and have not been independently remeasured in this chat. Neither the Elementor staging environment nor geographic source geometry was independently inspected here. No claim of published or production-ready art.
