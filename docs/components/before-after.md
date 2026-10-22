# Before / After

**Latest owner clarification,2026-10-22:** Water's current project photographs/title/city/description are temporary design data pending owner selection, not final approved project evidence. The requested interactive page-owned Shortcode grid is not implemented: the direct MCP does not expose the legacy Shortcode Widget, and Browser editing needs approval under the current verification-only boundary. Existing1360, native Gallery493 link, BEAF records/images and every gallery remain unchanged. [Exact blocker and scope](water-damage.md#not-implemented-interactive-project-shortcode-grid).

**2026-10-22 — Water consumer:** New full-section Project Comparison1360 uses native Atomic Images746/747 in the existing ba-card/caption/title design, with independent image/caption/link Overrides. Existing742 BEAF data and all galleries are untouched. Legacy Shortcode cannot be placed inside an Atomic Component; Water therefore presents static before/after photographs and a native link to approved Gallery493 for interactive comparisons. [Exact implementation and limitations](water-damage.md).

**E84 consumer addition only:** Commercial499 places existing1209 in itsHero and existing1202/1209 in two Variant A result cards. Two additional shared ba-card/caption/title consumers; exact captions match Gallery493. No BEAF record/asset/configuration/CSS or existing Home/Residential/gallery edit. [Commercial locators](commercial-services.md).

## E83 — approved A card design, 2026-10-21

The owner selected A (clean frame): photo-first4:3 comparison, thin border, white caption area, consistent title/description. Applied to all20 current BA cards: Homepage154(3), Residential484(2), Before & After493(15). Hero comparisons are not cards and remain unchanged. This is the single approved card presentation for future GCPRO placements.

### Shared native owners

| Global Class | Exact owner | Values |
| --- | --- | --- |
| ba-card | g-c02ab3c | Native flex column, zero gap/padding, height100%, white color-background, color-text,1px color-border,10px radius, overflow hidden |
| ba-card__caption | g-c65c717 | Native grid,24px space-md padding,10px gap, start alignment, flexible height |
| ba-card__title | g-4523dc2 | Native Montserrat/font-heading,600,20px at desktop/tablet/mobile,1.35 line-height,color-text,zero margin,no capitalization transform |

All three classes have **Custom CSS:null** at every variant. Existing generic card/image-led-card have different padding, surface and mobile behavior; modifying them would affect unrelated consumers. Dedicated shared styles are justified by20 actual repeated cards. No new Variables, library Components, custom CSS/JS/PHP, Custom Code entries, plugins, dependencies or media uploads. Existing Inter16px body text retained. Existing local card/caption/title style copies removed instead of left competing with the three shared owners. Two native caption containers added on Residential so the same structure applies everywhere; they are not new library Components. Existing media wrappers retain native zero padding; their inner radius no longer competes with the outer frame.

Parent grid/section layout, native shortcode widget and BEAF records/images stay in place. HTML structure: article.ba-card → existing media slot/shortcode + div.ba-card__caption → existing semantic heading and paragraph. Gallery heading tags remainH2 under one H1; Home/Residential card headings remainH3. Border clipping belongs to the outer article; existing Kit6 still owns plugin labels/expand controls. Existing vendor runtime handles clipping/drag/fullscreen; no comparison JavaScript was added.

### Exact editable locations

| Page | Card article | Media slot | Caption | Title | Native shortcode |
| --- | --- | --- | --- | --- | --- |
|154|22e7aed8|33681ad8|ae30c3b|0fccf2a|[bafg id="723"]|
|154|b72017c|55241554|2f6babff|3a39c79b|[bafg id="742"]|
|154|31087133|5f199388|1b321c8b|5931ddb6|[bafg id="767"]|
|484|25d5b401|b909654|57237c9f|5489a838|[bafg id="723"]|
|484|14e979f|38e48a8d|6b9038c8|1a1cca70|[bafg id="742"]|
|493|e61e4810|e0dd873a|d5111008|548e15bf|[bafg id="1165"]|
|493|eb355409|a0e6407b|96800794|22eb69d8|[bafg id="1198"]|
|493|3532ebd9|9a515080|bfc96742|b886446f|[bafg id="1199"]|
|493|5d71e732|9fe021fa|b827742d|560f38d1|[bafg id="1200"]|
|493|67c5f89a|fc58adf8|7c8e1cf6|916abd12|[bafg id="1201"]|
|493|fadc48fa|5857d990|a22a3794|f068f469|[bafg id="1202"]|
|493|bfa420b5|9a83c299|5747d9e6|fddc3c34|[bafg id="1203"]|
|493|78b6f9b1|7a5fed28|7639c54b|cbd019a8|[bafg id="1204"]|
|493|ffa1ae51|cff89c50|29df2c48|b6cc1ece|[bafg id="1205"]|
|493|77f6cc7a|99e9f54e|a973ac57|8c943184|[bafg id="1206"]|
|493|f945089e|58a780d8|15eb71d5|709fcef1|[bafg id="1207"]|
|493|c8142deb|9cdcb489|1e8c3f57|45f312e0|[bafg id="1208"]|
|493|0302ccfc|ef5131ae|78ccb223|72392b1d|[bafg id="1209"]|
|493|b847df27|648bc2c2|5c38a62f|29f38aff|[bafg id="1210"]|
|493|c8003fcf|f549a350|07754b94|7d209f39|[bafg id="1245"]|

### Unified captions

Known locations use `Service / project — City, IL` in titles. Descriptions explain the visible work without repeating a location. Unknown locations are omitted; internal project numbers are not used as customer-facing titles. View labels use parentheses. The same project reused across pages uses identical title/description (723 and742). Northbrook was already in the published title; independent confirmation remains the earlier recorded limitation, not a new verified location claim.

| BEAF reference | Title | Description |
| --- | --- | --- |
|723|Fire Damage Restoration — Tinley Park, IL|Damaged framing and finishes transformed into a completed interior.|
|742|Water Damage Restoration — Glenview, IL|Ceiling damage repaired and a living space restored.|
|767|Garage Fire Damage Restoration — Northbrook, IL|A garage exterior restored with finished trim, a white door and a side entrance.|
|1165|Kitchen Renovation|A kitchen updated with cabinetry, lighting and an island.|
|1198|Bathroom Restoration|Exposed lower wall framing restored to a finished vanity and tile floor.|
|1199|Interior Restoration — Wonder Lake, IL|Open framing transformed into completed walls, ceilings and flooring.|
|1200|Living Area Fire Damage Restoration — Tinley Park, IL|A fire-damaged living area and kitchen restored to completed interiors.|
|1201|Kitchen Restoration — Wonder Lake, IL|Exposed framing restored to a kitchen with finished cabinetry and countertops.|
|1202|Club Room Renovation (Window View)|A club room updated with new flooring, wall finishes and an open ceiling.|
|1203|Club Room Renovation (Door View)|Another view of the club room with updated flooring, wall finishes and lighting.|
|1204|Fireplace Room Restoration — Wonder Lake, IL|An unfinished fireplace room restored with stone finishes, flooring and painted walls.|
|1205|Bedroom Fire Damage Restoration — Tinley Park, IL|A fire-damaged bedroom restored with finished walls, carpeting and lighting.|
|1206|Exterior Fire Damage Restoration — Tinley Park, IL|A fire-damaged home exterior restored with finished trim and windows.|
|1207|Shower Room Fire Damage Restoration — Tinley Park, IL|A fire-damaged shower room restored with finished walls, tile and fixtures.|
|1208|Bathroom Fire Damage Restoration — Tinley Park, IL|A fire-damaged bathroom restored with a finished vanity, tub and wall finishes.|
|1209|Commercial Entrance Renovation|A commercial entrance updated with white framing, dark doors and finished flooring.|
|1210|Living Room Renovation|A living room updated with lighter finishes, flooring and an open layout around the brick fireplace.|
|1245|Kitchen Restoration|A kitchen restored with white cabinetry, countertops and finished flooring.|

### Verification and preservation

Saved native reads confirm20 class applications and unchanged shortcodes, image references, links, Hero trees and all content outside these card articles. Authored AIOSEO titles/descriptions/canonicals/noindex unchanged. No BEAF record, plugin file, shared Button/CTA, Header/Footer or production write. All images are the existing assets; E81 gallery WebP/alt metadata retained.

18 authenticated responsive cases: three pages at360/393/430/768/1024/1440px; all20 cards use20px titles,24px padding,10px corners, loaded4:3 comparisons and no horizontal/caption overflow. Following caption unification, all20 texts were read back in the browser at their recorded desktop widths; native saved copy matches the table. Representative inline drag and fullscreen open/close pass on each of the three pages. Gallery fullscreen opens with Enter. Existing vendor DIV handles/close control lack full keyboard slider/dialog semantics; that limitation was not modified. Physical devices/screen readers not tested. Anonymous raw HTML returns200/noindex and3/2/15 card class tokens respectively after Elementor Files & Data + SG Cache refresh; this is anonymous delivery evidence, not an incognito interactive certification. [Sanitized evidence](../evidence/2026-10-21-ba-card-style-a.json).

### Future reuse and recovery

Reuse these three classes and native article/media/caption/heading/paragraph structure. Supply optimized paired4:3 WebP assets with truthful alt metadata, retain the BEAF native shortcode and appropriate H2/H3 semantics. Do not add independent local frame/type styles or change the plugin to reproduce this design. Keep one existing Kit6 owner for labels/fullscreen. New cards inherit the same typography/spacing; their parent controls how many columns fit.

Private pre-E83 page snapshots permit scoped restore of just the three/two/15 card subtrees; outside-card content must remain current. To reverse only the new captions, use the private pre-caption snapshots. Remove the new class assignments before considering retirement of a shared class, then check all consumers. Do not delete media or plugin records. Purge Elementor and SG caches after restoration. The approved A prototype remains a design artifact, not separately enqueued site code.


## E81 — owner-supplied gallery and optimized photographs, 2026-10-21

Existing [Before & After Page493](https://vitaliiv1.sg-host.com/before-and-after/) now contains15 native comparisons. The owner explicitly authorized this separate gallery task; it does not expand Phase1 BEAF cleanup. Homepage's three original comparisons and BEAF723/742/767 were preserved. E82 CTA work subsequently made no BEAF changes.

Native Atomic body reuses the established Homepage card/grid design and existing Section Heading71, section/container/stack/grid classes. Gallery uses three/two/one columns on desktop/tablet/mobile, one H1 and H2 project captions styled to existing22/20px project typography. No new Global Classes, Variables, library Components, HTML widgets, custom code, plugins or dependencies. Existing BEAF native two-image horizontal mode owns dividers, labels and fullscreen; existing Kit6 owns presentation.

Page493 uses native Elementor Full Width (`elementor_header_footer`) and Hide Title, so its own gallery replaces the structural placeholder while retaining global Header/Footer. Single1008's conditions and body were restored to the original snapshot after template testing. Existing Header113/Footer114/Home154 saved bodies match their baselines. No production changes.

| BEAF record | Before / after source basenames | Active WebP attachment IDs |
| --- | --- | --- |
| 1165 | ania9 / ania10 | 1250 / 1248 |
| 1198 | bath2 / bath23 | 1247 / 1246 |
| 1199 | entrance-wonder-lake / entrance-wonder-lake-2 | 1216 / 1215 |
| 1200 | tinley-fire-1 / tinley-fire-2 | 1217 / 1218 |
| 1201 | kitchen-wander-lake-1 / kitchen-wander-lake-2 | 1221 / 1219 |
| 1202 | jordan-bg-club1 / jordan-bg-club2 | 1220 / 1222 |
| 1203 | jordan-bg-club3 / jordan-bg-club4 | 1224 / 1223 |
| 1204 | fireplace-wonder-lake-1 / fireplace-wonder-lake-2 | 1225 / 1226 |
| 1205 | fire-damage-tinley-8 / fire-damage-tinley-8-8 | 1227 / 1228 |
| 1206 | fire-damage-tinley-2 / fire-damage-tinley-2-2 | 1229 / 1230 |
| 1207 | fire-damage-tinley-3 / fire-damage-tinley-3-3 | 1231 / 1232 |
| 1208 | fire-damage-tinley-4 / fire-damage-tinley-4-4 | 1249 / 1251 |
| 1209 | entrance1 / entrance2 | 1235 / 1238 |
| 1210 | ania7 / ania8 | 1252 / 1253 |
| 1245 | 19-0255-CNI-1 / 19-0255-CNI-2 | 1241 / 1242 |

All30 gallery photographs are real optimized WebP files in exactly4:3; the mixed-width and portrait pairs were cropped without stretching. Source files retained. Both sides of a comparison have matching dimensions. The near-duplicate Alternate View1244 (Ania5/6) is Draft and its card/caption were removed; retain the single Fireplace View1210. Extra original/uncropped attachments remain unplaced rollback sources, not extra gallery cards; no permanent media deletion was performed.

Residential484 separately replaces the static assessment image through existing77/image Override with technician WebP1243 (1448x1086). [Residential owners and recovery](residential-services.md). Descriptive image filenames, Media alt/title/description and Page493 AIOSEO title/description/canonical were supplied. Featured image1248 is the optimized4:3 kitchen after image; staging remains noindex. No new fabricated project location or damage claims were added where unconfirmed.

**Verification:** at360/393/430/768/1024/1440px,15 sliders, one H1, all30 images loaded/WebP/4:3/with alt,4:3 frames and no horizontal overflow. First seven inline dividers were individually dragged successfully; the remaining eight, fullscreen interaction and physical devices are not individually certified in this pass. Existing vendor DIV-handle keyboard limitation remains. Final cache refresh removed the Alternate View caption as well as its slider. Full-size media bytes and sanitized asset locators are in [evidence](../evidence/2026-10-21-before-after-media.json); these are not a full-page performance score. Existing plugin eager-load behavior retained; no new lazy-loader script was added.

**Edit/reuse:** edit493 for captions/grid, native BEAF records above for image pairs and native Media for SEO fields. Keep existing Kit6 presentation as the sole style owner. New comparisons should use optimized paired4:3 assets and distinct views. Do not copy these numeric IDs to production without migration mapping. Recovery: remove the new gallery body/restore Page493's previous default-template placeholder; move the new records to Draft if withdrawing the gallery, without deleting media. Restore Residential image724 only if requested. Clear Elementor Files & Data and SG Cache after changes.


**E71 explicit owner scope:** Reuse existing723 in the CURRENT main Hero only. Shortcode30e0c45 under visual484c13ec, same original photos; local wrapper rule hides its fullscreen entry point. Original eb597a1/6a2a094/961e3c2 and records723/742/767 are unchanged. This later integration authorization does not expand Phase1 refactoring. [Exact implementation and QA](hero-main-beaf.md).

**Current E66,2026-10-20:** A later explicit owner request authorizes shared presentation-only correction. Existing Kit6 Site Settings Custom CSS now owns restrained10px dark-translucent/white labels and36px desktop/44px mobile expand buttons,16px glyph, orange focus. No page-ID dependence in the new style. Historical Homepage CSS below was absent on fresh native read; do not restore alongside Kit6. Plugin files/shortcodes/records/images/handle code unchanged. [Exact source, tests, limits and rollback](../audits/2026-10-20-beaf-presentation.md). The following E57 boundary and earlier CSS record are historical Phase1 evidence.

**Phase1 boundary (E57):** BEAF Pro is an existing third-party plugin and is entirely excluded from refactoring. Its files, shortcodes, CSS overrides, popup behavior, selectors and Elementor integration are untouched. Necessary Homepage/page-body/grid/slider scoping is an intentional isolation exception, not an automatic architecture defect. Rendered BEAF page CSS equals the E56 baseline byte-for-byte; [verification](../audits/2026-10-20-phase1-cleanup.md).

Three project comparisons; plugin records own the images and comparison behavior, Atomic owns the surrounding layout.

## Location and structure

Homepage154/main46c3aad4 → section **4221ba60** → container14d7e71c; heading instance6b4663fc →71; grid **66b1c7d4**; portfolio instance2364d92a →59.

| Project wrapper → image wrapper → Shortcode widget | Saved shortcode | Caption title |
| --- | --- | --- |
| 22e7aed8 →33681ad8 →**eb597a1** | [bafg id="723"] | 0fccf2a, residential fire/Tinley Park |
| b72017c →55241554 →**6a2a094** | [bafg id="742"] | 3a39c79b, water/Glenview |
| 31087133 →5f199388 →**961e3c2** | [bafg id="767"] | 5931ddb6, garage fire/Northbrook |

Shortcodes freshly read in the visual editor; actual images rendered. Slider record IDs are required plugin references. Do not replace them with guessed IDs after migration.

## Styles, JavaScript and dependencies

Atomic grid/local controls own three/two/one columns at desktop/tablet/mobile,16px media/caption gaps and22px desktop/tablet,20px mobile project titles. Shared heading/container/section/grid-3 classes and font/color tokens apply to native text.

**Current owner: Kit6 → Site Settings → Custom CSS.** Shared plugin-class selectors style inline/body-mounted popup labels and expand buttons; source mirror integrations/beaf-presentation.css. Homepage154 Custom CSS was empty on fresh E66 native read. The former body.elementor-page-154/grid data-id66b1c7d4 override is historical, not a parallel current owner. The E57 isolation exception was intentional at that time.

Plugin CSS/JS owns handles, clipping and fullscreen Ajax: **Ultimate Before After Image Slider & Gallery–BEAF4.7.21 + BEAF Pro4.5.7** (some asset URLs still say4.5.6). jQuery/twentytwenty and plugin popup code are vendor dependencies. No GCPRO-developed comparison JS or Custom Code entry. No HTML widget.

## Behavior and safe modification

Current labels10px/white on black60%, ordinary opacity1; popup AFTER clears close control by56px. Expand buttons36px desktop/44px mobile or coarse pointer,16px white existing SVG, black52% background, subtle border, orange hover/focus. Vendor focus suppression requires one scoped !important. No GCPRO comparison JavaScript. Edit media/options in existing BEAF records; Atomic owns captions/grid; Kit6 owns presentation. All3 inline drags and all3 fullscreen open/close tested at1440/393; six-width layouts tested. Existing non-keyboard handle/close semantics remain a vendor limitation. See E66 for exact evidence and recovery.

Historical E56 verification:

393px fullscreen723 opened and closed in Chrome with document/popup width393 and no horizontal overflow; page grid checked360/393/430/768/1440. All three inline pairs rendered. Current handles are DIVs with no role, tabindex or ARIA value: keyboard slider semantics are missing. Fullscreen fit-to-window/keyboard coverage, physical-device and anonymous access remain separate QA. Historical endpoint403/security issue is not resolved by disabling site security in this audit. Portfolio still#; Northbrook location remains owner-unconfirmed.
