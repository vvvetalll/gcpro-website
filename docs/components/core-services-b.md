# Core Services B

**Current E61,2026-10-20:** Intro mobile z9999 replaced by local z1; section3fd180bb now has native local z0, style e-3ed21e1f-ddd9. This contains intro layering inside Core while global Header/Call Now remain above. Removing intro z entirely was tested and caused service rows to paint over intro text, so local z1 is necessary. Native sticky offsets/padding/background are unchanged. [Evidence, exact owners and rollback](../audits/2026-10-20-section-layers-footer.md).

**E58,2026-10-20:** Saved native intro style is unchanged. Browser testing demonstrated the returning Header covering79px of the mobile intro. Added empty gcpro-sticky-intro g-43749f7 to6cb38139; the shared global controller903 temporarily adds measured clearance while Header is visible and removes it when hidden. Tablet static positioning and native grid-bound release preserved. [Exact conflict evidence, ownership and rollback](smart-navigation.md#core-services-b-verified-conflict-only). No separate Core script.

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
| Mobile ≤767px | One column,24px gap; intro sticky0px,local z-index1 inside section z0,opaque surface-alternate #EFF6FF; **16px top/bottom token space-sm**, zero horizontal padding; H2 28px |

Mobile padding is inside the opaque sticky box, covering rows behind both breathing areas. No spacer or scroll listener is involved. CSS sticky remains constrained by grid61328a99; it releases as that grid ends. Mobile entry/active/release verified at360/393/430px; tablet768 and desktop1440 checked.

Row hover inherits orange and moves the arrow0.2rem; reduced motion suppresses movement. Rows remain articles without destination links; do not describe them as functioning service navigation.

## Maintenance and limits

Preserve grid minmax(0,…) tracks and existing class ownership. Change this unique intro through local mobile controls, not the shared stack class. No new reusable sticky class was warranted for one intro. Do not add body/html overflow masking or fixed heights.

The six inline SVGs repeat internal group IDs ink/accent. E57 found no fragment references, inspected matching CSS/script consumers or paint conflict; all12 groups have expected navy/orange strokes and all six rendered SVG markup strings are unchanged. Per owner scope, harmless duplicates are documented and left unchanged; no asset cleanup is warranted now. Reassess if future code references these IDs. [Evidence/limits](../audits/2026-10-20-phase1-cleanup.md). E61 supersedes the old preservation of accidental z9999. For E61 rollback see its audit; E56's padding-only rollback remains separate and must preserve later layering changes.

## 2026-10-23 — approved icon rollout

**2026-10-23 — approved service icon rollout:** Uploaded six original Flaticon Uicons Regular Rounded SVGs once: Raindrops1438, Flame1439, Disease1440, Wrench Simple1441, Thunderstorm1442, Box Open1443. Replaced six Home154 Core SVG references, six Residential484 and five Commercial499 service-card icon Overrides. Existing Service Card62 keeps its five content/link Overrides and56px badge; native12px inset yields32px artwork. Detached legacy icon-svg only from these updated widgets to avoid its fill:none rule; that shared class remains unchanged. Home uses native32px dimensions/color-accent. No new Global Classes, Variables, Components, custom CSS/JS/PHP or dependencies; six media uploads. Why1149/icons, certification logos, functional arrows and BEAF untouched in this rollout. Commercial General Contracting207 has no specifically approved equivalent and remains pending. Saved-document/component inventory covered103 page/library records and27 components; broader visual acceptance belongs to the owner. Home Chrome checks at1440/768/393 confirmed six orange32px SVGs, preserved desktop40px/24px and mobile32px/16px tracks/gaps, no overflow and retained row-arrow hover. Further tests stopped on owner instruction; hub/individual-page visual checks and complete final preservation comparison are not certified. Original SVGs, license certificates and pre-change snapshots retained privately outside Git. [Registry and recovery](docs/ICONOGRAPHY.md#approved-core-rollout--2026-10-23).

Owner stopped further QA; remaining visual acceptance is owner-led. See AGENTS.md permanent acceptance rule.
