# GCPRO mobile and architecture audit — E56

**Superseding E57 scope/result:** [Approved Phase1 cleanup](2026-10-20-phase1-cleanup.md) removes custom CTA/header numeric selectors and verified redundant declarations. BEAF is completely excluded: existing page/body/grid/slider scoping is an intentional third-party integration exception, not an automatic defect. Six Core SVGs have no verified ID-reference/paint conflict and remain unchanged. The findings below retain their original E56 audit context; this notice supersedes the prior proposed BEAF/SVG cleanup dispositions.

**Date:**2026-10-20 America/Chicago. **Environment:**https://vitaliiv1.sg-host.com only. **Repository:**vvvetalll/gcpro-website,main,initial331c6a6adc84047687653982033d30187b760942. Production and shared ROBYLO source untouched.

## Findings reported before further architectural changes

| Finding | Evidence / consequence | Disposition |
| --- | --- | --- |
| Core B sticky content had0px padding | Saved intro6cb38139 and computed mobile box; eyebrow touched sticky top, description ended at opaque box edge | **Fixed:** native mobile space-sm top/bottom16px; no spacer/JS |
| Reported Android page drag | Initial360/393/430 scans, fresh Android-UA/touch393 tests and later full-page five-width tests show no document overflow | **Currently not reproducible.** Owner independently rechecked Android and could no longer reproduce; explicitly requested no speculative fix |
| Live video missing from handoff | Saved Code847 published/Page154/body-end1; frontend script injects video although Atomic tree has no video widget | **Documentation corrected.** New component/code ownership records; existing experiment preserved |
| Avoidable ID coupling |E56:847 uses .elementor-154 and panel interaction ID5ec4592; main local radius targets5ec4592; navigation class targets.menu-item-242. BEAF body/page/grid scoping is intentional third-party isolation, excluded from Phase1 | **Documented debt/proposals.** Required plugin/object/Component IDs distinguished from authored selectors; no blind selector removal |
| Redundant cascade | Fresh global-class Custom CSS has superseded padding/nowrap/underline declarations and repeated button focus groups | **Documented debt.** No broad class replacement from partial native prop data |
| Two timeline CSS storage layers | Theme appended E16 block plus Code590; source mirrors agree after whitespace normalization | **Verified intentional split**, not duplicate deployment; preserve exact owners |
| Duplicate SVG IDs | Six Core B SVGs each contain groups ink/accent | **HTML uniqueness debt**; E57 verifies no current conflict and leaves artwork/IDs unchanged as requested |
| Comparison keyboard semantics | Three inline handles are DIVs without role,tabindex,aria-valuenow | **Verified accessibility debt**; vendor-supported keyboard solution or separately approved integration needed |
| Availability affordance |5350691e is enabled BUTTON/type submit without surrounding form, ZIP input or saved interaction | **Documented prototype limit**; “Inactive” Navigator label is not disabled semantics |
| Third-party typography/data | Trustindex uses vendor Poppins; visible review count and aggregate JSON-LD count differ | **Owner/configuration review**, not automatic review/schema or font rewrite |
| Literal visual values | Intentional panorama dimensions, borders/translucency, tiny comparison labels and hardcoded847 colors/gutters | Existing tokens reused for new change; do not create tokens for every one-off value or silently change approved visuals |

No newly introduced duplicate class, Component, DOM wrapper, page-ID selector, JS, PHP, plugin, dependency or design token. No speculative class deletion: library entries not used by Homepage can still have Style Guide/other-page consumers.

## Exact implementation

Fresh snapshot of Homepage154/main46c3aad4 captured locally before writing. Changed only intro **6cb38139**, local style **e-67ba0794-7b2b**:

```css
@media(--mobile) { padding: var(--space-sm) 0; }
```

Saved native output is padding-block-start/end var(--space-sm),padding-inline-start/end0px. Existing mobile sticky0px,z-index9999,background var(--color-surface-alternate) (#EFF6FF) remain. Desktop sticky96px and tablet static/auto are unchanged. No body/html overflow masking or new custom CSS.

MCP initially staged an autosave; published **staging154** explicitly, then read live content. Saved before/after trees each contain190 nodes; exactly one node's style changed, every other returned setting/style/content/interaction/ID identical. Native editor on mobile shows space-sm buttons for Top/Bottom,0px Right/Left; intro Custom CSS editor is empty. All global resources and shared structures were read, not rewritten.

Scoped rollback: remove only the four explicit mobile padding values in intro local Style → Spacing; preserve sticky/background and other breakpoint variants. Affected-tree snapshot supports this small rollback; **no full database/files backup or restore test was established**, and this evidence is not a full-site backup.

## Browser verification

Authenticated staging frontend in Chromium in-app browser and Chrome; Android UA/touch emulation is **simulation**, not an agent-operated physical Android device. Owner's physical recheck is separately reported above. Initial browser zoom/viewport mismatches were detected; only explicit measured CSS widths below count as requested-width tests.

| Measured CSS width | Document client/scroll width in overlay-scrollbar simulation | Intro | Result |
| --- | --- | --- | --- |
|360|360/360|sticky0,16px top/bottom|No horizontal range; entry/active/release measured |
|393|393/393|sticky0,16px top/bottom|Opaque top/bottom coverage; Chrome screenshot; navigation/popup tests |
|430|430/430|sticky0,16px top/bottom|No horizontal range; entry/active/release measured |
|768|768/768|static/auto,0 padding|One-column tablet preserved |
|1440|1440/1440|sticky96,0 padding|Two-column desktop preserved |

A separate normal-scrollbar desktop check measured innerWidth1440,client1425,scroll1425: scrollbar space is not overflow. Native desktop screenshot inspected; no text overlap.

At every width, sampled page top, before/inside sticky, y4000,y7000 and page bottom. Forced horizontal scroll to+1000 clamped to0 everywhere. At393 Chrome synthesized touch horizontal drag also left scrollX0. Expanded mobile navigation width393; first comparison fullscreen/popup width393, opened/closed; inline image pairs rendered. Offscreen Trustindex slides are contained by their own clipped carousel ancestors and are not evidence of page overflow. Decorative847's negative right inset is contained at the local panel.

**Sticky geometry:** intro height≈216.58px after padding (previous≈184.58px); at393 it reaches top0 near scroll2018px, stays there through the middle, then moves upward at the grid boundary (around scroll2839px); after grid end3055px the intro is entirely above the viewport.360 and430 have the same bounded behavior with content-dependent positions. ±1px sampling follows smooth position constraints within device rounding; no new spacer/jump. At393,y2450, last intro content ends200.58px,opaque box ends216.58px: exactly16px breathing room. Hit tests in both padding areas return intro6cb38139 while rows occupy positions behind it. Mobile screenshots show no exposed/overlapping row text inside that opaque area.

Regression scope: responsive layout, mobile menu toggle, one fullscreen open/close and existing href inspection; no telephone call/service request submitted. Shared interactions/source were preserved. This is not a fresh full-site keyboard, screen-reader, performance, animation timing or all-popup certification. Actual main DOM has one H1,one main,no nested anchors and alt attributes on native main images; this is a focused inspection, not a full HTML validator/accessibility certification.

**Cache/guest limit:** staging Purge SG Cache control was invoked from a fresh frontend tab and subsequent authenticated reloads show16px. No reliable cache response/HIT proof was captured. A separate anonymous HTTP request received403; available browser sessions were authenticated. No successful separate incognito/anonymous frontend or guest asset-cache equivalence is claimed. Historical E18 cache behavior remains a reason to repeat guest QA, not permission to bypass security.

## Architecture/source inspection

Fresh MCP reads: full154; all16 discovered Component definitions and override schemas; Header113/Footer114; global variable identities/values and classes; actual editor class-resource Custom CSS. Native editor inspected intro controls, page CSS and four Shortcode values. Code listing contains exactly two published entries590/847, both Page154,body-end,priorities10/1; saved sources read without saving. Code590 CSS/JS and theme appended ripple block match repository source after removing whitespace. Additional library74/77 missing-image selectors and83 focus exceptions are explicitly recorded, with unused-library browser validation left unclaimed.

WordPress theme UI shows a single installed active **ROBYLO Starter0.2.0**, standalone with no Template header/child theme. Read20 active theme PHP/CSS source files via Theme File Editor without saving. functions.php enqueues fallback.css once with content-MD5 version; native comment-reply conditional only. Public Elementor location/document APIs handle fallbacks; native renderers use escaping and accessible main/skip-link. No client page-ID selectors found in the reviewed theme PHP; GCPRO-specific timeline CSS is the documented appended exception. No complete deployment-commit equality or runtime test of all non-Homepage fallback routes is claimed.

Plugin versions and exact CSS/JS locations are centralized in [CUSTOM_CODE](../CUSTOM_CODE.md). Newly introduced [component index](../components/README.md) covers every current custom Homepage section, shared primitives and Header/Footer, including prototypes and runtime code absent from the saved tree.

## Safe improvements delivered and deferred proposals

Delivered: mobile native padding; complete component/code locator documentation; current video correction; standalone-theme correction; permanent audit/documentation/coupling rules. No architectural code refactor was necessary to solve the verified mobile spacing issue.

Deferred proposals requiring a separate consumer-aware plan/approval before significant structural change: native/semantic-class replacement for847; CTA radius ownership migration; semantic menu visibility; shared-class cascade cleanup; SVG ID review and ZIP product behavior. E57 implements the approved minimal subset; BEAF integration, popup and accessibility changes are excluded and require separately explicit scope. These are explicit technical debt, not silently completed work. Preserve working approved designs and never change production.

## Documentation and delivery

Updated AGENTS,PROJECT_CONTEXT,CHANGELOG,README,ARCHITECTURE,ELEMENTOR_MAP,DESIGN_SYSTEM,WORKFLOWS and this audit; added CUSTOM_CODE and component records. [Sanitized numerical checks](../evidence/2026-10-20-mobile/viewport-results.json) and [393px screenshot](../evidence/2026-10-20-mobile/mobile-sticky-393.png) accompany the audit. Component records own maintenance instructions; historical milestone narratives remain dated. Repository content/diff/relative links/whitespace/secret review and remote-main commit verification form the delivery gate. The containing commit records exact SHA; no speculative self-referential SHA is embedded here.
