# Desktop Hero composition polish — E33

2026-10-16, staging Homepage154 Hero a62cdd3. Owner requested the smaller-desktop visual relationship on wider screens, both-side blending, unchanged content/structure/mobile. Visual approval pending.

## Implementation Summary

Existing hero--panorama g-708f717 now anchors the photograph to the center of the same viewport as the1200px content container, with an80px left offset. The native photograph still scales to100% of the content-driven Hero height, without stretching or a forced section height. A bounded1500px horizontal blend fades both edges into existing navy. No top/vertical gradient, added objects or photo edits. Media633, H1/eyebrow/paragraph, CTA order and definitions, placeholder behavior and all145 saved Homepage nodes/settings remain unchanged.

## Technical Changes

Reused the existing class, native Background gradient/image controls, full-resolution WordPress Media633 reference, section--dark/container/hero-layout and CTA Components53/103. Native gradient stops are0/34/48/65/82/95/100%,90deg, existing navy plus transparent navy; the central clear area keeps vehicle branding visible. Image position becomes native center-center as the fallback.

**One new custom code source mirror:** [integrations/hero-panorama-composition.css](../../integrations/hero-panorama-composition.css). It is not separately enqueued. Deployed exception lives in **Hero → Style → Global Class hero--panorama → normal → Custom CSS**. Native gradient UI supports colors/stops but exposes no independent gradient-canvas width or shared offset for the gradient and photograph. Three scoped declarations set the gradient layer1500px×100%, preserve the photograph's native auto×100%, center both80px left and prevent repetition, only above1024px. Without the bounded gradient canvas, its fade follows viewport width while the photograph has a fixed height-derived width, exposing a seam on ultra-wide screens.

In Elementor use `&` instead of `.hero--panorama` inside the media query, as shown in the source comment. Retain the generated editor wrapper; publish the Global Class before frontend testing. To tune composition edit the1500px blend width and80px offset there. Colors/stops and image selection remain in ordinary native Background controls. This is a narrow, documented exception under the authorized Hero native-capability fallback; no widget/local CSS, inline styling, theme/shared ROBYLO modification, JS/PHP or new dependency. No new Global Classes, Variables or Components.

## Complexity Audit

No wrappers, duplicate Hero, new media, animation or preload. Fresh full Homepage comparison is identical to the pretask145-node tree. All other Global Classes match baseline; native usage scan confirms hero--panorama has one consumer,154/a62cdd3. Class count unchanged. One small source mirror records the existing-class exception rather than creating another deployed stylesheet/system. Tablet/mobile are excluded from the custom canvas rule; the native mobile variant is byte-for-byte unchanged. Native desktop fallback now uses the updated gradient/center position, inherited on tablet; no tablet layout/copy change.

## Verification

Published native Global Class, purged staging SiteGround cache and checked the ordinary anonymous frontend, not an incognito session:

| CSS viewport | Hero height | Photo left edge relative to copy left | Horizontal overflow |
| --- | --- | --- | --- |
|1280 |562.906px |−215.810px |No |
|1440 |562.906px |−215.810px |No |
|1920 |562.906px |−215.810px |No |
|2560 |562.906px |−215.810px |No |

Photo edge is calculated from the actual section height, supplied1983/793 aspect ratio and computed background offset, not a DOM image element. Constant relative position verifies that the image no longer drifts from the content container. Actual screenshots show clear heading/copy, front SUV/rear van, both-side fades, retained skyline and no vertical edge on2560. Vehicle ends soften into the blends intentionally; do not claim the complete source is uncropped at every width. No top mask or image distortion. Formal WCAG contrast/LCP/CLS benchmarking and physical devices were not tested.

390px measured styles/geometry match E32's saved baseline exactly, including solid navy background, stacked CTAs and retained placeholder. Native image selector/Full, gradient controls and the central CSS editing field inspected; raw-class readback plus computed frontend confirms the deployed rule. First media-query attempt without an inner `&` did not compile; corrected in the same class, not a second injection. Functional navigation unchanged: primary tel:+18476563322 and secondary approved-but-unresolved #; no new manual internal destinations.

Evidence: [1280](../evidence/E33/1280.jpg), [1440](../evidence/E33/1440.jpg), [1920](../evidence/E33/1920.jpg), [2560](../evidence/E33/2560.jpg), [390](../evidence/E33/390.jpg), [measurements](../evidence/E33/verification.json), [saved class](../evidence/E33/class-after.json). Before screenshots retained for1280/2560. Full baseline class recovery reference outside Git: project outputs/recovery/hero-panorama-before-E33.json; not a full backup/tested restore.

## GitHub / Outstanding Items

PROJECT_CONTEXT, CHANGELOG, DESIGN_SYSTEM, ELEMENTOR_MAP, this milestone, source mirror and evidence synchronized to gcpro-website/main; final report records commit/push/remote SHA. Git does not deploy WordPress. Await owner visual approval; physical-device/incognito and formal performance/accessibility benchmarks remain unperformed. Mobile photography and Request Service destination remain deferred. Reverse through native class controls and remove only this class's composition CSS, using the pretask reference; publish, purge and verify.

## E34 — Longer right-side fade trial

2026-10-16: owner requested a long right transition resembling the left. Changed only the existing native transparent gradient stop82%→66%, retaining the navy endpoint95%. On the existing1500px blend canvas this lengthens the right fade195px→435px, close to the left465px transition. Image633, position/scale, content, structure, mobile variant and existing three-declaration composition CSS are unchanged.

Native editing: Hero154 → Style → hero--panorama g-708f717 → Background → Linear Gradient → right transparent stop → Stop66%. Publish, purge staging cache, inspect anonymous frontend. Full Global Class before/after diff confirms exactly one numeric offset change. No new classes, components or custom code; no new Variables/plugins/dependencies/markup. No redundant resources introduced. Revert66→82 to restore E33.

Verified actual anonymous1440/2560 desktop after native SiteGround purge and390 mobile; no overflow, mobile styles/geometry match E33 baseline. Native image reference, CSS and other Global Classes preserved. Incognito/physical-device/formal contrast/LCP testing not performed. Evidence: [1440](../evidence/E34/1440.jpg), [2560](../evidence/E34/2560.jpg), [390](../evidence/E34/390.jpg), [readback](../evidence/E34/verification.json). This is a visual trial awaiting approval. Documentation/CHANGELOG/PROJECT_CONTEXT/DESIGN_SYSTEM updated, committed/pushed to main; final report records verified remote SHA.

## E35 — Extended soft right blend

**Implementation Summary:** Owner clarified the RIGHT edge near the van, then requested that the outer vehicle edge barely show through navy. Homepage154/a62cdd3 keeps its existing photograph633, section dimensions, copy, CTA and structure. The right fade extends40→95% of the existing1500px canvas,825px versus E34's435px, with stronger gradual opacity toward the van's front. No top/vertical fade.

**Technical Changes:** Reused hero--panorama g-708f717, native Background gradients/image and the existing centralized class CSS exception. Two native gradient layers independently manage right and left tracks. Right90deg stops0/40/65/80/95/100%, rgba navy alpha0/0/0.35/0.85/1/1. Left90deg stops0/34/48/65/100%, alpha1/1/0.9/0/0, preserving the prior left track. The overlapping right layer intentionally adds some shading near the central vehicle area. Native Media633/Full remains third, height100%, widthauto. Edit colors/stops under Hero → Style → hero--panorama → Background, right layer first, left second.

Existing custom CSS was modified, not newly introduced: [source mirror](../../integrations/hero-panorama-composition.css), deployed in that same Global Class's Custom CSS. Both gradient canvases1500px×100%, photo auto×100%, common calc(50% - 80px) center above1024px. No-repeat now sits before the media query, applying at all widths. In the installed editor, a field containing only the nested media rule saved raw but omitted it from generated frontend CSS; declaration-first nesting compiled and was verified in actual computed styles. Paste the declaration-first field syntax documented in the mirror inside Elementor's protected wrapper. This supersedes the earlier E33 inner-`&` editing guidance. Native controls still lack independent gradient-canvas sizing; no additional CSS declarations or new injection. Mirror is not separately enqueued. No new Global Classes, Variables, Components, files, plugins, JS/PHP or shared ROBYLO changes.

**Complexity Audit:** One extra native gradient layer enables independent fade tracks; no DOM wrappers, duplicate Hero or new media. Only existing g-708f717 differs in the full Global Class comparison; native mobile variant is identical. Three composition declarations retained. Native image reference and Component link overrides retained. Existing tel:+18476563322 and approved unresolved Request Service # remain unchanged; no new manual internal URLs.

**Verification:** Published, purged staging SiteGround cache and checked ordinary anonymous frontend at1440/2560 plus390 browser emulation. Computed desktop layers confirm1500px/1500px/auto sizing and the common offset; Hero height562.906px, no horizontal overflow. Screenshots show the gradual right blend, with the van's outer edge subdued. Mobile seven-element geometry/background/font/gap checks match prior baseline; no overflow. No-repeat differs at mobile but its opaque navy background covers the same area and appearance remains unchanged. Native gradient controls, image reference and class CSS read back after save. No physical device/incognito or formal contrast/LCP/CLS benchmarking performed.

**GitHub:** PROJECT_CONTEXT, CHANGELOG, DESIGN_SYSTEM, ELEMENTOR_MAP, this record, existing CSS mirror and E35 evidence updated; final report records pushed and verified main commit. [1440](../evidence/E35/1440.jpg), [2560](../evidence/E35/2560.jpg), [390](../evidence/E35/390.jpg), [readback](../evidence/E35/verification.json), [native class](../evidence/E35/class-after.json).

**Outstanding Items:** Visual approval pending. Mobile photography and Request Service destination remain deferred. Restore E34's combined gradient and two-layer CSS mirror from commit5d252fb if reversing the trial, then publish, purge and recheck; no full backup/restore test claimed.
