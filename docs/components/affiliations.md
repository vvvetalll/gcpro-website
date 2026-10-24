# Staging affiliations — 2026-10-24

Water Damage514: https://vitaliiv1.sg-host.com/residential-services/water-damage/

Owner-directed trial only. The larger blue section is **between Reviews and FAQ**, with no rollout to other pages. Footer114 is intentionally shared across staging. No production edits.

## Native layout and ownership

- Page514 root72095bb2, heading Professional Credentials & Affiliations; navy `color-primary` (#1A327D), white text, approved white artwork, thin frames, native hover/focus. Grid5 columns desktop/tablet,2+2+centered1 mobile. RIA artwork reduced to120×55px (constrained proportionally on tablet). No CSS filters or asset alterations.
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

## Checks performed

- Scoped private pre-edit WordPress snapshots of514 and114, plus snippet snapshots retained outside Git; no raw authenticated exports or credentials committed.
- Fresh saved readback: publication states/URLs preserved. Removing only the new root and restoring the five permitted Why image Overrides yields **exact equality** to both pre-task Elementor trees. Existing Footer copyright `text-wrap:balance` was restored after the native connector dropped its serialization. No new element contains custom CSS. [Saved checks](../evidence/2026-10-24-affiliations-saved-checks.json).
- Actual connected browser desktop1440,tablet768,mobile390: all ten logos load; correct proportions/no filters; no horizontal overflow; Footer remains five across, and final heading is one line. Footer appears once on Home with five triggers; larger trial absent there.
- Popovers: all five organizations in both locations checked on desktop and mobile-width browser; viewport bounds checked. Mouse hover opens; pointer can enter popup without closing. Click toggles and outside click dismisses. Tab enters the certificate link; Escape closes and restores trigger focus. All ten marks expose keyboard button semantics and controlled-popup relationships. Mobile checks use resized connected browser and click/tap-equivalent input, not a physical touch device or screen-reader certification.
- Source code syntax check passed; exact deployed Custom Code1881 source readback verified. Popovers stay in Footer DOM to retain native document-scoped styles; fixed positioning works because its ancestors do not establish transformed containing blocks.
- No forms submitted, customers contacted or site SEO/content/review settings changed. No independent anonymous/cache-HIT or physical-device certification claimed.

## Screenshots

Final native browser captures, cropped only to the relevant visible regions (no artwork modification):

- [Desktop trial](../evidence/2026-10-24-affiliations-trial-desktop.jpg)
- [Tablet trial](../evidence/2026-10-24-affiliations-trial-tablet.jpg)
- [Mobile trial](../evidence/2026-10-24-affiliations-trial-mobile.jpg)
- [Desktop Footer](../evidence/2026-10-24-affiliations-footer-desktop.jpg)
- [Mobile Footer](../evidence/2026-10-24-affiliations-footer-mobile.jpg)

## Rollback / maintenance

Copy stays native and editable in Footer114's five Affiliation tooltip groups. Layout stays native in514/114. Change behavior only in the central source and1881 together. Disable1881 to remove behavior; hidden boxes do not become visible. Full scoped rollback restores514/114 pre-task snapshots, disables1881, then removes only the two new semantic classes after checking consumers. Do not replace shared1149 or other pages. Refresh generated Elementor styles/cache after restoration. Owner visual acceptance remains pending; do not extend the large trial.
