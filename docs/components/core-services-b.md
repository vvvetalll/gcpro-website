# Core Services B

## Current heading architecture — 2026-11-01

Homepage154 sticky wrapper6cb38139 now contains existing **Section Heading71 instance4bb0fedf**, with supported eyebrow/title/heading_tag/description Overrides preserving “OUR SERVICES”, “Core Restoration Services”, H2 semantics and the approved introduction. The existing section-heading--accent class is attached only to this local wrapper; its sticky styles and service catalogue are unchanged. Removed manual heading children50dcec03 (including2a83f0f7),1aa0cb69,4a4d8cc5 and7775c3e8. No shared definition, class, Variable or Custom Code was edited; no CSS imitation or dependency was added.

**Scoped verification:** published MCP readback confirms both new71 instances and native Hero project binding; excluding the explicitly changed heading groups/caption, the entire saved Homepage main tree compares exactly with the before snapshot. Authenticated frontend at actual1562 CSS px, visualViewport.scale1: one Core H2, existing orange pseudo-line, unchanged copy and sticky96px declaration, no document horizontal overflow; Core heading remains28px and description now follows71's standard16px instead of the former18px. Heading wrapper height changed184.23→169.82px. Testimonials heading remains94.66px high; Hero caption retains its657.61×16.80px dimensions at that viewport; Trustindex rendered from the same public source. Requested1440/768/393 before/after visual checks remain **unverified**: viewport override left actual width1562 unchanged; the one native UI alternative failed with unavailable coordinate geometry. A keyboard-flow check timed out; the project link is a real A element with tabindex0 and the unchanged resolved destination, but keyboard-focus/activation and sticky entry/release were not fully verified. These are explicit limits, not viewport or interaction acceptance. No anonymous-delivery, physical-device or cache-purge check was performed.

Recoverable affected-element before/after JSON snapshots are private workspace files `home154-heading-link-before-20261101.json` and `home154-heading-link-after-20261101.json`, outside Git. Restore only the affected wrappers/caption through native Elementor after rereading current state; never restore the whole page over concurrent edits. Earlier heading locators and browser width claims below are historical where they conflict with this checkpoint.

**Current links — 2026-10-26:** All six existing Home154 Core rows now select actual Residential pages by WordPress title through native Internal URL → Content. No text/design/class definitions changed. [Exact mapping and checks](../audits/2026-10-26-native-named-links.md#homepage-core-and-shared-footer--residential-services--2026-10-26).

**Current E61,2026-10-20:** Intro mobile z9999 replaced by local z1; section3fd180bb now has native local z0, style e-3ed21e1f-ddd9. This contains intro layering inside Core while global Header/Call Now remain above. Removing intro z entirely was tested and caused service rows to paint over intro text, so local z1 is necessary. Native sticky offsets/padding/background are unchanged. [Evidence, exact owners and rollback](../audits/2026-10-20-section-layers-footer.md).

**E58,2026-10-20:** Saved native intro style is unchanged. Browser testing demonstrated the returning Header covering79px of the mobile intro. Added empty gcpro-sticky-intro g-43749f7 to6cb38139; the shared global controller903 temporarily adds measured clearance while Header is visible and removes it when hidden. Tablet static positioning and native grid-bound release preserved. [Exact conflict evidence, ownership and rollback](smart-navigation.md#core-services-b-verified-conflict-only). No separate Core script.

Six-item restoration directory on Homepage154. Fresh saved tree, native editor and rendered scroll checks on2026-10-20; [test evidence](../audits/2026-10-20-architecture-and-mobile.md).

## Location and structure

Parent Homepage main **46c3aad4** → section **3fd180bb** (“Core Services B — Experimental”; historical name, current approved section) → editorial grid **61328a99**. Intro **6cb38139** contains Section Heading71 instance **4bb0fedf**; the former manual eyebrow/H2/divider/introduction nodes are historical. Sibling directory **48842292** contains article rows54ee8d2d,97cc573,2ebf3e02,24281f6b,2890630,463d381e. Each row has an SVG, a title/description stack and a separate arrow span.

## Styles, code and dependencies

Atomic Global Classes: section, section--light, container, stack, stack--compact, icon-svg; repeated roles **core-b-row g-d37a353**, **core-b-title g-757705e**, **core-b-description g-6bb05c4**, **core-b-arrow g-c3123c0**, section-eyebrow. Variables include font-heading/body, color-primary/accent/text/text-muted/border, color-surface-alternate and space-sm.

Edit unique grid/intro/heading dimensions in their **local native Style controls**; repeated row presentation in Design System → Classes. Intro local style **e-67ba0794-7b2b** owns position and mobile padding/background. Core-b-row owns the small parent-state→arrow/reduced-motion Custom CSS exception; icon-svg owns outline SVG fill protection. [Complete ownership](../CUSTOM_CODE.md).

**No section JavaScript, Custom Code entry, HTML widget, shortcode or extra plugin.** SVG attachment IDs596/597/607/599/600/601 are asset references, not selector hooks.

## Responsive behavior and interaction

| Range | Layout and intro |
| --- | --- |
| Desktop >1024px | Columns minmax(0,.9fr)/minmax(0,1.4fr),80px gap; intro sticky96px; Heading71 H2 28px |
| Tablet768–1024px | One column,40px gap; intro static/auto; Heading71 H2 26px |
| Mobile ≤767px | One column,24px gap; intro sticky0px,local z-index1 inside section z0,opaque color-white; **16px top/bottom token space-sm**, zero horizontal padding; Heading71 H2 24px |

Mobile padding is inside the opaque sticky box, covering rows behind both breathing areas. No spacer or scroll listener is involved. CSS sticky remains constrained by grid61328a99; it releases as that grid ends. Mobile entry/active/release verified at360/393/430px; tablet768 and desktop1440 checked.

Row hover inherits orange and moves the arrow0.2rem; reduced motion suppresses movement. The six previously informational rows now have native Internal URL / Content links to the verified Residential pages (2026-10-26 owner instruction); whole-row anchors retain the existing presentation and hover behavior.

## Maintenance and limits

Preserve grid minmax(0,…) tracks and existing class ownership. Change this unique intro through local mobile controls, not the shared stack class. No new reusable sticky class was warranted for one intro. Do not add body/html overflow masking or fixed heights.

The six inline SVGs repeat internal group IDs ink/accent. E57 found no fragment references, inspected matching CSS/script consumers or paint conflict; all12 groups have expected navy/orange strokes and all six rendered SVG markup strings are unchanged. Per owner scope, harmless duplicates are documented and left unchanged; no asset cleanup is warranted now. Reassess if future code references these IDs. [Evidence/limits](../audits/2026-10-20-phase1-cleanup.md). E61 supersedes the old preservation of accidental z9999. For E61 rollback see its audit; E56's padding-only rollback remains separate and must preserve later layering changes.

## 2026-10-23 — approved icon rollout

**2026-10-23 — approved service icon rollout:** Uploaded six original Flaticon Uicons Regular Rounded SVGs once: Raindrops1438, Flame1439, Disease1440, Wrench Simple1441, Thunderstorm1442, Box Open1443. Replaced six Home154 Core SVG references, six Residential484 and five Commercial499 service-card icon Overrides. Existing Service Card62 keeps its five content/link Overrides and56px badge; native12px inset yields32px artwork. Detached legacy icon-svg only from these updated widgets to avoid its fill:none rule; that shared class remains unchanged. Home uses native32px dimensions/color-accent. No new Global Classes, Variables, Components, custom CSS/JS/PHP or dependencies; six media uploads. Why1149/icons, certification logos, functional arrows and BEAF untouched in this rollout. Commercial General Contracting207 has no specifically approved equivalent and remains pending. Saved-document/component inventory covered103 page/library records and27 components; broader visual acceptance belongs to the owner. Home Chrome checks at1440/768/393 confirmed six orange32px SVGs, preserved desktop40px/24px and mobile32px/16px tracks/gaps, no overflow and retained row-arrow hover. Further tests stopped on owner instruction; hub/individual-page visual checks and complete final preservation comparison are not certified. Original SVGs, license certificates and pre-change snapshots retained privately outside Git. [Registry and recovery](docs/ICONOGRAPHY.md#approved-core-rollout--2026-10-23).

Owner stopped further QA; remaining visual acceptance is owner-led. See AGENTS.md permanent acceptance rule.


2026-10-31 — Homepage-only eyebrow trial: replaced numbered label with native row 50dcec03, decorative 6×6px brand-accent dot 7999c442 and “Our services” label 2a83f0f7 (Inter/body token, navy primary, 14px/500, normal spacing, centered with 8px gap). Desktop computed dimensions/alignment and native Elementor Mobile Portrait preview checked; main heading, orange underline, introduction and section styles verified unchanged. No shared component or other eyebrow changed.


2026-10-31 — Owner expanded eyebrow style to the whole site: shared section-eyebrow g-b12aa04 in Kit6 now owns Montserrat 500, uppercase, normal tracking, navy, 13px desktop/tablet and 12px mobile, with a 6px orange decorative dot and 8px gap (nonempty labels only). Removed homepage selector overrides and duplicate native dot; cleaned 117 numeric-prefix overrides across 31 published pages and added 11 unnumbered Why-label instance overrides where shared defaults contained numbering, preserving actual process-step numbers. Scope scan covered 63 published pages plus relevant components; 12 non-Elementor placeholders and protected blog-index2043 were not editable through this endpoint; shared class reaches applicable rendered headings. Frontend Moisture Mapping confirmed number-free labels, Montserrat13px and 6px dots; no shared component binding was removed (MCP rejects writing bound default-value envelopes).
