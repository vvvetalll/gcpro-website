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
