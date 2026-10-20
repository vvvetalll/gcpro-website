# Core Services B

Six-item restoration directory on Homepage154. Fresh saved tree, native editor and rendered scroll checks on2026-10-20; [test evidence](../audits/2026-10-20-architecture-and-mobile.md).

## Location and structure

Parent Homepage main **46c3aad4** → section **3fd180bb** (“Core Services B — Experimental”; historical name, current approved section) → editorial grid **61328a99**. Intro **6cb38139** contains eyebrow135f55, H2 **1aa0cb69**, divider4a4d8cc5 and paragraph7775c3e8. Sibling directory **48842292** contains article rows54ee8d2d,97cc573,2ebf3e02,24281f6b,2890630,463d381e. Each row has an SVG, a title/description stack and a separate arrow span.

## Styles, code and dependencies

Atomic Global Classes: section, section--light, container, stack, stack--compact, icon-svg; repeated roles **core-b-row g-d37a353**, **core-b-title g-757705e**, **core-b-description g-6bb05c4**, **core-b-arrow g-c3123c0**, section-eyebrow. Variables include font-heading/body, color-primary/accent/text/text-muted/border, color-surface-alternate and space-sm.

Edit unique grid/intro/heading dimensions in their **local native Style controls**; repeated row presentation in Design System → Classes. Intro local style **e-67ba0794-7b2b** owns position and mobile padding/background. Core-b-row owns the small parent-state→arrow/reduced-motion Custom CSS exception; icon-svg owns outline SVG fill protection. [Complete ownership](../CUSTOM_CODE.md).

**No section JavaScript, Custom Code entry, HTML widget, shortcode or extra plugin.** SVG attachment IDs596/597/607/599/600/601 are asset references, not selector hooks.

## Responsive behavior and interaction

| Range | Layout and intro |
| --- | --- |
| Desktop >1024px | Columns minmax(0,.9fr)/minmax(0,1.4fr),80px gap; intro sticky96px; H2 40px |
| Tablet768–1024px | One column,40px gap; intro static/auto; H2 36px |
| Mobile ≤767px | One column,24px gap; intro sticky0px,z-index9999,opaque surface-alternate #EFF6FF; **16px top/bottom token space-sm**, zero horizontal padding; H2 28px |

Mobile padding is inside the opaque sticky box, covering rows behind both breathing areas. No spacer or scroll listener is involved. CSS sticky remains constrained by grid61328a99; it releases as that grid ends. Mobile entry/active/release verified at360/393/430px; tablet768 and desktop1440 checked.

Row hover inherits orange and moves the arrow0.2rem; reduced motion suppresses movement. Rows remain articles without destination links; do not describe them as functioning service navigation.

## Maintenance and limits

Preserve grid minmax(0,…) tracks and existing class ownership. Change this unique intro through local mobile controls, not the shared stack class. No new reusable sticky class was warranted for one intro. Do not add body/html overflow masking or fixed heights.

The six inline SVGs repeat internal group IDs ink/accent. E57 found no fragment references, inspected matching CSS/script consumers or paint conflict; all12 groups have expected navy/orange strokes and all six rendered SVG markup strings are unchanged. Per owner scope, harmless duplicates are documented and left unchanged; no asset cleanup is warranted now. Reassess if future code references these IDs. [Evidence/limits](../audits/2026-10-20-phase1-cleanup.md). Existing z-index9999 is preserved, not adopted as a sitewide stacking token. Exact transition geometry and rollback are in the audit. To roll back this task, remove only the four explicit mobile padding values; keep existing sticky/background values and all other breakpoints.
