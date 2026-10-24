# Staging affiliations — shared component, 2026-10-24

Water Damage514: https://vitaliiv1.sg-host.com/residential-services/water-damage/

Approved shared rollout: all17 service pages use **Component1886 — GCPRO / Professional Credentials & Affiliations**, immediately **Reviews → dark-blue affiliations → FAQ**. The navy strip intentionally separates the two light-blue sections. Footer114 remains unchanged; no production edits.

## Native layout and ownership

- Shared Component1886, native root60e6d354 (frontend IDs are regenerated per instance), heading Professional Credentials & Affiliations; navy `color-primary` (#1A327D), white text, approved white artwork, thin frames, native hover/focus. Grid5 columns desktop/tablet,2+2+centered1 mobile. RIA artwork reduced to120×55px (constrained proportionally on tablet). No CSS filters or asset alterations.
- Why instance43194cd8: only trust_iicrc/trust_iaqa/trust_bbb/trust_ria/trust_ra image Overrides cleared. Shared1149 untouched. No extra Why logos render on514.
- Footer114 root6c46aed9 directly below existing cities5fe71200 within5245645d. Compact left alignment. Header69799971 uses heading-label, white, single line:16px desktop/tablet,11px mobile. Container500px/max100%; logo grid5cdd54d1 is360px/max100%, five columns on desktop and mobile,8px gaps. Frames44px high,4px padding. Bottom padding24px. IICRC23×32,IAQA24×32,BBB19×32,RIA52×24,RA44×32px; contain preserves proportions. No fixed heights hide text.
- Ten frame triggers use native opacity.85→1 and border-white22%→50%,180ms transitions; focus equivalent. No shadows, carousel, recoloring or decorative icons.
- Approved existing attachments1294/1295/1296/1297/1303: IICRC-white.svg,IAQA-white.svg,BBB-white.svg,RIA.svg,gcpro-ra-white.png. Existing alt text preserved. Five native editable popovers live under the Footer block, hidden outside interaction. Three verified document/profile links occur inside popovers; marks themselves do not navigate.
- New semantic classes: gcpro-affiliation-trigger g-b8dbc32; gcpro-affiliation-tooltip g-a92542b. These own cursor/hidden default only. No new Variables, plugins, theme changes or dependencies.
- Central Custom Code1881 supplies the authorized small script; canonical [source](../../integrations/affiliation-tooltips.js), registry in [CUSTOM_CODE](../CUSTOM_CODE.md). No per-page script. Native Hotspot's hover-or-click controls did not cover the combined focus, Escape, outside dismissal and interactive-link requirements; owner explicitly authorized central JS.

## Relationship wording and sources

Heading says **Credentials & Affiliations**, not certifications for every mark. No endorsement, work guarantee or current status is inferred from a logo.

| Mark / full name | Explanation and exact supported relationship | Evidence / remaining limit |
|---|---|---|
| IICRC — Institute of Inspection, Cleaning and Restoration Certification | Develops cleaning/restoration standards and certifies professionals and firms. GCPRO publishes a **2024 Certified Firm certificate**; current renewal has not been independently verified. | [Published certificate](https://gcprochicago.com/wp-content/uploads/2024/02/iicrc.jpg) identifies GCPRO LLC, company202083, valid through12/31/2024. [Official verification explanation](https://iicrc.org/certifiedfirmverification/). Do not describe this as verified current2026 certification. |
| IAQA — Indoor Air Quality Association | Provides education/resources for indoor air quality professionals. GCPRO reports IAQA membership in its company records; current membership has not been independently verified. | [Company records](https://gcprochicago.com/about-us/), [official organization](https://www.iaqa.org/). Prior company member link led to maintenance; no verified current profile link added. The company page's erroneous expanded name is not reused. |
| BBB — Better Business Bureau | Provides business information, handles complaints and accredits businesses against standards. GCPRO LLC is listed as a BBB Accredited Business. | [Verified GCPRO profile](https://www.bbb.org/us/il/lombard/profile/fire-water-damage-restoration/gcpro-llc-0654-88372213), linked inside popup. Accreditation is not restoration certification. |
| RIA — Restoration Industry Association | Provides education, advocacy and professional resources for restoration. GCPRO LLC appears in RIA's member directory. | [Verified GCPRO member profile](https://pro.restorationindustry.org/find-a-member/gcpro-llc), matching company website and Lombard address; linked inside popup. Membership is not a service guarantee. |
| Restoration Affiliates | National network of independent restoration companies. The organization announced GCPRO as a network member; a current individual member profile has not been verified. | Official indexed [membership announcement](https://www.restorationaffiliates.com/article/restoration-affiliates-adds-three-new-members). Direct retrieval403; limited to the indexed announcement. No homepage presented as membership proof. |

Owner information still needed: current IICRC renewal certificate, current IAQA membership/profile and current RA member listing. Existing published artwork was retained as instructed; tooltip copy explicitly discloses the limits.

## Trial checks performed before shared rollout

- Scoped private pre-edit WordPress snapshots of514 and114, plus snippet snapshots retained outside Git; no raw authenticated exports or credentials committed.
- Fresh saved readback: publication states/URLs preserved. Removing only the new root and restoring the five permitted Why image Overrides yields **exact equality** to both pre-task Elementor trees. Existing Footer copyright `text-wrap:balance` was restored after the native connector dropped its serialization. No new element contains custom CSS. [Saved checks](../evidence/2026-10-24-affiliations-saved-checks.json).
- Actual connected browser desktop1440,tablet768,mobile390: all ten logos load; correct proportions/no filters; no horizontal overflow; Footer remains five across, and final heading is one line. Footer appears once on Home with five triggers; larger trial absent there.
- Popovers: all five organizations in both locations checked on desktop and mobile-width browser; viewport bounds checked. Mouse hover opens; pointer can enter popup without closing. Click toggles and outside click dismisses. Tab enters the certificate link; Escape closes and restores trigger focus. All ten marks expose keyboard button semantics and controlled-popup relationships. Mobile checks use resized connected browser and click/tap-equivalent input, not a physical touch device or screen-reader certification.
- Source code syntax check passed; exact deployed Custom Code1881 source readback verified. Popovers stay in Footer DOM to retain native document-scoped styles; fixed positioning works because its ancestors do not establish transformed containing blocks.
- No forms submitted, customers contacted or site SEO/content/review settings changed. No independent anonymous/cache-HIT or physical-device certification claimed.

## Historical trial screenshots

Final native browser captures, cropped only to the relevant visible regions (no artwork modification):

- [Desktop trial](../evidence/2026-10-24-affiliations-trial-desktop.jpg)
- [Tablet trial](../evidence/2026-10-24-affiliations-trial-tablet.jpg)
- [Mobile trial](../evidence/2026-10-24-affiliations-trial-mobile.jpg)
- [Desktop Footer](../evidence/2026-10-24-affiliations-footer-desktop.jpg)
- [Mobile Footer](../evidence/2026-10-24-affiliations-footer-mobile.jpg)

## Rollback / maintenance

Copy stays native and editable in Footer114's five Affiliation tooltip groups. Large-block layout now lives only in Component1886; compact row and tooltip copy stay in Footer114. Change behavior only in the central source and1881 together. Disable1881 to remove behavior; hidden boxes do not become visible. Shared-rollout rollback restores the17 pre-rollout page snapshots, including the original standalone trial on514 and the prior Why image Overrides. Leave Footer114, tooltip copy,1881 and both hook classes unchanged. Remove/archive1886 only after confirming zero consumers. Refresh Elementor Files & Data and staging cache. No full-site restore test was performed.



## Approved shared rollout — current editing location

Edit the larger block once in [Component1886](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1886&action=elementor), not independently on pages. Native source-copy creation from514 preserved all14 nodes’ content, native CSS/breakpoint/state values, image proportions and global behavior classes exactly (excluding regenerated identifiers). Component UID: `component-ad5dca93-d460-4097-9127-fa1ac1e399c2`. No per-page content Overrides or new design variants. Each page has one native e-component reference, instance363ead93 (element IDs are scoped to each document). Original standalone72095bb2 was removed from514.

The five tooltip text groups and profile links remain **exactly** as approved in Footer114. Existing central behavior1881 and its source are unchanged; it discovers semantic trigger classes, so the component needs no new scripts. The compact Footer tree/meta and shared Why1149 definition were read back equal to their pre-rollout baselines. Membership verification is explicitly outside this rollout; no wording was strengthened.

Twelve primary/Commercial pages have Why1149 instances: only the five trust-image Overrides were cleared. Five supporting pages487–491 have no Why1149 instance or corresponding logos, so none was added or removed there. All17 retain their existing Published state, exact URLs, page settings, service content, Heroes, CTAs, FAQ data, review shortcodes/widget mappings and authored SEO settings.

### Page coverage

| Page | Staging URL | Why instance cleared | Reviews / FAQ locators |
|---|---|---|---|
| 487 | https://vitaliiv1.sg-host.com/water-extraction/ | Not present | 10a34543 / d6ef007 |
| 488 | https://vitaliiv1.sg-host.com/board-up/ | Not present | 10a34543 / 7fd6207f |
| 489 | https://vitaliiv1.sg-host.com/odor-removal/ | Not present | 10a34543 / 4de7b6b7 |
| 490 | https://vitaliiv1.sg-host.com/moisture-mapping/ | Not present | 10a34543 / 817f2cb |
| 491 | https://vitaliiv1.sg-host.com/dehumidification/ | Not present | 10a34543 / 403e2833 |
| 514 | https://vitaliiv1.sg-host.com/residential-services/water-damage/ | 43194cd8 | 10a34543 / 38d09d71 |
| 515 | https://vitaliiv1.sg-host.com/commercial-services/water-damage/ | 250e98ea | 10a34543 / 208c7687 |
| 516 | https://vitaliiv1.sg-host.com/residential-services/mold-removal/ | 4325e31f | 10a34543 / 6fe7367a |
| 517 | https://vitaliiv1.sg-host.com/residential-services/fire-smoke/ | 3bce386 | 10a34543 / 1efdba75 |
| 518 | https://vitaliiv1.sg-host.com/residential-services/reconstruction/ | 11924603 | 10a34543 / 4752c32f |
| 519 | https://vitaliiv1.sg-host.com/commercial-services/mold-removal/ | 490141ee | 10a34543 / 428b40a8 |
| 520 | https://vitaliiv1.sg-host.com/commercial-services/fire-smoke/ | 339e9064 | 10a34543 / 1f1ae670 |
| 521 | https://vitaliiv1.sg-host.com/residential-services/personal-property-restoration/ | 42671675 | 10a34543 / 5948338a |
| 522 | https://vitaliiv1.sg-host.com/commercial-services/general-contracting/ | c15304f | 10a34543 / 18ea6097 |
| 523 | https://vitaliiv1.sg-host.com/residential-services/storm-damage/ | 2931d6c9 | 10a34543 / 41d95dbb |
| 524 | https://vitaliiv1.sg-host.com/commercial-services/reconstruction/ | 76d33b83 | 10a34543 / 1985efaa |
| 525 | https://vitaliiv1.sg-host.com/commercial-services/personal-property-restoration/ | 7bc6a0a0 | 10a34543 / 5b2daaba |

### Save method, recovery and delivery

Private scoped pre-edit page, Footer, shared-Why, source/component and Custom Code snapshots retained outside Git. Native MCP created1886 by copying the approved source and generated its native instance. The connector’s read/staged-autosave mismatch made follow-up insertion unreliable; existing authenticated standard WordPress REST updated only `_elementor_data` with the native component reference and five authorized image Overrides. No custom HTML, theme code, plugin, database access or alternate layout was introduced.514’s pending native autosave was reconciled and published; all final saved trees were independently read back. Protected trees match before/after after excluding only the authorized component insertion/replacement and five logo Overrides. Original review subtrees and metadata/SEO were checked, not reconstructed.

Some old rendered HTML persisted after SiteGround purge. Used existing **Elementor → Tools → Clear Files & Data**, followed by staging SiteGround purge; unchanged native settings then rendered correctly. No cache/security settings changed.

### Final rollout verification

- Actual frontend: **17/17 pages at each of1440×1000,768×1024,390×844**. Each has one large block immediately after Reviews/before native FAQ, navy #1A327D between two #EFF6FF sections, five loaded logos, five initialized main popover triggers and ten total approved marks including Footer. No horizontal overflow. Logo-center row grouping verifies5 desktop/tablet and2+2+1 mobile. Component1886 matches the approved source’s exact native content/style/state/breakpoint signature. [51 rendered checks](../evidence/2026-10-24-affiliations-rollout-browser.json), [17 saved-state checks](../evidence/2026-10-24-affiliations-rollout-saved.json).
- Existing behavior on the shared instance: mouse hover opens; moving into the popup keeps it open. Keyboard Tab focuses the next logo and opens its popup, Tab reaches the certificate link, Escape dismisses and restores focus. All five mobile-width popovers were opened/toggled and stayed inside the viewport; outside click dismissed. This is resized-browser click/tap-equivalent testing, not a physical touch-device or screen-reader certification.
- Component1886 opened in the native Elementor editor with its correct shared title. Content/layout is edited there; no temporary editor content/style edits were made.
- Footer114 meta/tree, current tooltip text/links, central1881 meta/source and shared Why1149 native definition are equal to the pre-rollout snapshots. No scripts were added or duplicated. No review text, widget filters, service content, images, Hero, CTA, URLs, publication states or SEO values were changed.
- Anonymous raw HTTP requests to all17 ordinary routes returned **HTTP403 Forbidden** from this environment. Authenticated connected-browser rendering was verified; independent incognito/cache-HIT delivery remains unverified. No publishing or rendering blockers remain in the tested session.
- Current shared-block screenshots: [desktop](../evidence/2026-10-24-affiliations-rollout-desktop.jpg), [mobile](../evidence/2026-10-24-affiliations-rollout-mobile.jpg). Screenshots were cropped to the block only, with no customer reviews/admin details committed.
