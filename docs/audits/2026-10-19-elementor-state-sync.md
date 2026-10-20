# GCPRO saved-state audit — E55

Read-only staging audit on **2026-10-19 America/Chicago / 2026-10-20 UTC**. Target: https://vitaliiv1.sg-host.com. Repository baseline: `b10631277d9787cde8abc69a97e2d16f2a85e1e3`, branch `main`.

## Evidence and limits

Fresh Elementor MCP reads covered Homepage154 main46c3aad4 with content, Header113/root4ef1aa21, Footer114/root1687d698, CTA Component80/root324d9854, timeline Component582/root16ae2220, archive structures703/822, component discovery, Theme Builder assignments, video assets, class identities and all36 variable values. Homepage154 is listed as published at the staging root; Header113/Footer114 are published, active and assigned `include/general`. Homepage's returned main tree has190 nodes; this count excludes expanded Component internals.

**Completed and verified** below means presence/configuration in the returned saved data. It does not mean every feature is production-ready. No Elementor/WordPress writes, preview creation, publication, cache purge, production access or live-design changes occurred. No browser, anonymous, physical-device, scrolling, keyboard, media-playback, performance or editor-interaction tests were run in this audit. Historical E15–E54 QA remains dated evidence.

The connector returns local V4 CSS and defaults, but its Global Classes resource returned only102 identities/order, not declarations. No document-settings read tool is exposed; page Custom CSS was not freshly inspected. Legacy shortcode widgets return empty settings: their presence is verified, their shortcode text/plugin configuration is not. Navigation widget configuration was returned, but individual WordPress menu-item targets/types were not. A published document status does not establish the absence of an autosave or equality with cached visitor output.

## Saved implementation and status

| Area / locators | Freshly verified saved state | Classification / remaining verification |
| --- | --- | --- |
| Hero a62cdd3; H1 7941b532 | H1 “Property restoration in Chicago”; Component286 eyebrow; primary18a239c4 →53 calls `tel:+18476563322`; secondarya7bcc76 →103 is REQUEST SERVICE →`#`. Section uses hero--panorama g-708f717; mobile media17c26181 uses hero-media--mobile g-02b63b3 and still contains label708a5ff2 “Hero Image — 16:9”. | Completed and verified: structure/copy/CTA settings. E32–E35 Media633 desktop photograph/blend is historical; current class background declarations and mobile rendering were not exposed. Do not mistake a Navigator placeholder title for proof the desktop photograph is absent. |
| Residential / Commercial 7b416658 | Local white background; cards4c8810dc/2066a26 use audience-card g-38b29fb and `#` destinations. Native images295bf90e/27ec40d5 reference629/630; body/action classes and SVG464 remain. | Completed and verified: two photo cards and saved white surface. Shared hover declarations/rendering not rechecked; category routes pending. |
| Core Services B 3fd180bb; grid61328a99; intro6cb38139 | Sole current Core Services section; six article rows54ee8d2d,97cc573,2ebf3e02,24281f6b,2890630,463d381e. Water; Fire & Smoke; Mold; Reconstruction; Storm; Personal Property. Rows have no link setting. Desktop0.9fr/1.4fr grid,80px gap; tablet one column/40px gap; mobile24px gap. H2 1aa0cb69 remains40/36/28px, color-text. | Completed and verified: approved B structure/settings; Navigator still says “Experimental”, but E45 documents owner promotion. Routing and actual sticky/hover behavior remain unfinished/untested here. Exact sticky settings below. |
| Emergency CTA 6cde656f | Heading2631f818 uses71; call300e78c6 →53 with `tel:+18476563322`; request91ce6f0 →103 with `#`. | Completed and verified: saved strip/content/tel link. Request destination pending; no call/interaction test. |
| How We Work 4681b8f5; instance79a67ca3 | Component582 contains four steps with Homepage overrides Contact, Assessment, Restoration, Review and non-placeholder descriptions. Native source classes process-timeline g-a12d836, step g-07d3365, number g-e17507d, connector g-261ecb6 remain attached. | Completed and verified: four-step content/Component structure. Ripple/viewport code deployment and runtime not freshly verified; source inspection below. |
| Before / After 4221ba60; grid66b1c7d4 | Three shortcode widgets eb597a1/6a2a094/961e3c2; saved3/2/1 grid. Project roots22e7aed8/b72017c/31087133 use16px image/caption gaps; titles0fccf2a/3a39c79b/5931ddb6 use22px desktop/tablet and20px mobile. Current titles: residential fire/Tinley Park; water/Glenview; garage fire/Northbrook. Portfolio2364d92a →`#`. | Completed and verified: wrapper layout/text/widget presence. E48–E51 mappings to BEAF723/742/767, labels/fullscreen/page CSS are historical, not revalidated by empty shortcode settings. Northbrook factual confirmation, gallery route, anonymous/security/keyboard/fit-to-window work remain open. |
| Why GCPRO 5b2c6d3c | Editorial introduction90a7f6e plus benefits1159b0ff; four numbered benefits40005fc4/3a445659/6b2b3e0f/1d5836e9. H2 62a085d4 local style contains only white color, inheriting default32/28/24px Montserrat700/1.15; intro31a44bf8 retains85% opacity and inherits Inter body defaults. | Completed and verified: E54 typography normalization and E52 structure. Copy/visual approval remains pending; shared class rendering not retested. |
| Testimonials 10a34543 | Light-blue local surface; heading3d727826 “WHAT OUR CLIENTS SAY”; shortcode02441ff under7d037e04. No three placeholder-card subtree in current section. | Implemented but not fully tested. E54 identifies Trustindex Google reviews/Poppins historically; current shortcode value, source authenticity/permissions and widget typography not exposed. |
| Service Areas 7d8c17ad; citiesd6dbbe2 | Saved3/2/1 grid with12 city rows; directory2b5f493 →`#`; button5350691e text “Check Service Availability”, tag button, no saved interactions and no surrounding native form/input in this subtree. | Completed and verified: layout/content/prototype presence. ZIP search/popup/backend integration **pending**; button presence is not working search. See current link register below. |
| Final CTA 37feb023 →80; panel5ec4592 | Existing copy, primary call `tel:+18476563322`, secondary request `#`; panel uses existing cta-panel g-e1d4327 and section--dark g-43edd01. Main46c3aad4 local CSS contains only panel-scoped8px radius. No video widget exists in returned Homepage tree or Component80. | Completed and verified: E54 radius/structure/overrides. Navy/orange/white treatment is supported by E54 history and current class references, not fresh class-declaration/render QA. Video placement/mobile full-width/corner-video experiment pending. |
| Header113 | Root4ef1aa21; dynamic site-logo72df1b0c uses native internal-url binding to Page154. Menu7983af36 selects robylo-primary, full-width stretch dropdown; CTAcd66895 →56 REQUEST SERVICE →`#`. Utility273b2dbd/1853f25b/4979c34 display Contact Us/Careers/Blog, all `#`. | Published/active assignment and settings verified. Menu-item destinations/mobile toggle/sticky background/z-index not freshly verified; no claim of functioning navigation. Utility Navigator labels differ from text. |
| Footer114 | Root1687d698; image4eac9eb →232,200px local width; intro1432e75b; menu1faf8090 uses robylo-primary vertically. Contact30cd7524 contains telephone, restore@gcprochicago.com and Lombard address; year890602e uses current-date-time dynamic tag. | Published/active assignment and content verified. Logo has no saved link destination. Menu-item objects/targets and contact factual accuracy/delivery were not tested. |

## Core B sticky: supersedes only the older mobile-static description

Exact returned intro6cb38139 local style **e-67ba0794-7b2b**:

```css
position: sticky; inset-block-start: 96px;
@media(--tablet) { position: static; inset-block-start: auto; }
@media(--mobile) {
  position: sticky;
  inset-block-start: 0px;
  z-index: 9999;
  background-color: var(--color-surface-alternate);
}
```

Returned default-style media rules establish tablet max1024px and mobile max767px. Thus the saved intent is desktop sticky96px, tablet static, mobile sticky0px. The mobile color variable freshly resolves to **#EFF6FF**, an opaque color; the returned local style has no opacity reduction. This proves the local background value, not a full computed-cascade/ancestor-opacity audit. No explicit desktop/tablet z-index or background is present in this local block; do not infer a desktop transparent background or a computed z-index from that absence.

E44/E45 statements that mobile remains static are now historical. The author/time of this later setting change is not established. **Implemented but not fully tested:** check actual mobile scrolling, containing-block limits, opaque coverage and stacking against the Header before calling the mobile sticky behavior complete. 9999 may overlap navigation; that is a test candidate, not a reproduced defect. Preserve these values during this documentation-only audit.

## Current Service Areas link register

All12 row anchors are saved literal `#`; their child paragraph destinations are empty strings. No approved WordPress object bindings or working city routes are established by these reads. Native binding/publication/access and migration retests remain pending under WORKFLOWS. Navigator labels were preserved and are unreliable for several cities; use the displayed text and IDs below.

| Displayed city | Row ID | Text ID |
| --- | --- | --- |
| Lombard |52ad5087 |2651d55b |
| Arlington Heights |29925a5c |3eaa5679 |
| Elmhurst |7f8df755 |736d15ef |
| Naperville |64f07ac9 |538d7ed8 |
| Northbrook |7703752a |72608afe |
| Downers Grove |28cc87b |788cb19d |
| Oak Brook |961c608 |6a7a855c |
| Glenview |311eade2 |3090cc15 |
| Highland Park |3e9e185f |5c43eda1 |
| Schaumburg |3478458c |642d5d94 |
| Evanston |166c23ea |3cbb955e |
| Elk Grove Village |5fcaef53 |7ebac29a |

Header request/utility, Homepage request, audience, directory and portfolio placeholders above are unresolved destinations, not verified routes. Core rows are articles without hrefs; no working service navigation is claimed. Destination publication/access remains unverified; do not publish drafts merely to remove placeholders.

## Pending and archived experiments

- **Pending video placement:** Media Library read returns one video, attachment **846**, `gcpro-cta-test.mp4`,1280×676. Upload is verified; playback, optimization, poster/autoplay/accessibility, final placement and mobile treatment are not. No video was inserted by this audit.
- **Archived/superseded:** original Core A remains readable in Template703/root3ee0b7bc; combined Why/Testimonials remains readable in Template822/root434b3976. Neither root occurs in current Homepage main. Presence is verified, not a restore test or fresh template-status audit.
- **Historical experiment:** orange CTA E53 was reversed in E54; current Homepage local rule retains radius only. Do not reapply E53 colors from historical prose.
- **Pending owner decisions:** Northbrook project location/final project copy; WHY visual/copy approval; testimonial source/permission and Poppins exception; real service/category/city/gallery/request destinations and ZIP workflow; video/mobile CTA treatment. Earlier accessibility/security/contrast and anonymous/performance/backup/transfer holds remain open.

## Repository/source comparison

Reviewed AGENTS, PROJECT_CONTEXT, CHANGELOG, ELEMENTOR_MAP, DESIGN_SYSTEM, WORKFLOWS, ARCHITECTURE, DECISIONS, README, recursive main tree and eight latest main commits through b106312. Recent history records audience hover, three BEAF comparisons, spacing, labels/fullscreen, Why separation and CTA reversal; it contains no later commit documenting mobile Core sticky or the uploaded CTA video.

Inspected these existing sources without editing or deploying them:

| Source | What the repository establishes / comparison limit |
| --- | --- |
| integrations/audience-card-hover.css | E47 non-enqueued mirror of class-owned hover, fine/none-pointer gates,1.025 image zoom and reduced-motion suppression. Current card class assignments agree; saved class declaration equality not exposed. |
| integrations/hero-panorama-composition.css | E33 non-enqueued mirror of desktop background sizing/position. Later E34/E35 blend settings belong to native backgrounds; source alone does not capture or verify the complete current Hero. |
| integrations/section-heading-accent.css | Non-enqueued class mirror for40×3px pseudo-element/space-sm accent. Current audience/process/project/Service Areas container class assignments agree; class CSS not freshly returned. |
| integrations/process-timeline-mobile.css and .js | Source retains touch-only IntersectionObserver, once per timeline at10% visibility, reduced-motion gate, stagger and number-color/ripple styling; desktop compatibility gate retained. Current582 structure/classes agree. Actual Code590 text/conditions and deployed source equality were not exposed by these reads. |
| theme-overrides/process-timeline.css | Canonical scoped parent-hover two-ring exception with1000ms/160ms timing,2px strokes and reduced-motion rule. Current theme file/enqueue equality was not inspected. |

No automatic Git→WordPress deployment or current runtime equivalence is established by these source files. Existing source/history/design architecture are preserved. This synchronization changes documentation only; AGENTS needs no policy change.

## Documentation verification and delivery

Review the containing commit diff: only PROJECT_CONTEXT.md, CHANGELOG.md, docs/ELEMENTOR_MAP.md, docs/DESIGN_SYSTEM.md and this audit should change. Additive summaries supersede specific dated claims; retain historical sections. Check relative links, actual IDs, whitespace and secret patterns before committing. The containing commit and remote main ref are the delivery evidence; no guessed self-referential commit hash is embedded here.
