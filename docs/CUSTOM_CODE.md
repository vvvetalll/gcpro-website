# Custom code and dependency register

Fresh staging audit **2026-10-20**. This file owns **where custom behavior is stored**. Component records own behavior/reuse instructions; the [audit](audits/2026-10-20-architecture-and-mobile.md) owns findings and verification. Generated assets in uploads/elementor/css are outputs, never editing locations.

## Active deployments

| Owner / editing location | Contents and consumers | Source / scope / limits |
| --- | --- | --- |
| Elementor → Editor → Custom Elements → Code **590**, “GCPRO / Process Timeline — Mobile Sequence” | Published; body-end priority10; Page154 display condition. Style gcpro-process-mobile-style and script gcpro-process-mobile-sequence | Canonical [CSS](../integrations/process-timeline-mobile.css) and [JS](../integrations/process-timeline-mobile.js); saved text matches after whitespace normalization. Class hooks; no page/element selector in JS. See [timeline](components/how-we-work.md) |
| Same list, Code **847**, “GCPRO / EXPERIMENT — Final CTA Video (staging only)” | Published; body-end priority1; Page154 condition. Inline style gcpro-cta-video-test-css plus script | Exact source lives in847, no repository source mirror/enqueue. Existing experiment, not added by this task. Detailed entry below |
| Homepage154 → Page Settings → Advanced → **Custom CSS** | BEAF labels, fullscreen buttons, media/reduced-motion rules | Page/body/grid ID scoped; [Before/After record](components/before-after.md). No separate GCPRO JS |
| Homepage154 → main46c3aad4 → local Style **e-685133d2-110f** → Custom CSS | & [data-interaction-id="5ec4592"] { border-radius:8px; } | Existing Final CTA per-instance radius exception. Scope/purpose/migration documented in [CTA](components/final-cta.md) |
| Library74/77 → local layout/image styles | Scoped :has/missing-image collapse/hide exceptions |74: e-30b81e2f-f92c/e-580e21c9-f816;77: e-3cbef3d9-e4cd/e-6bff78bc-1753. [Catalog](components/library-patterns.md); no authored page ID |
| FAQ83 → local header styles | Focus-visible outline exceptions | e-6fab0c7e-1ad9/e-32802adb-5ad2. Native accordion owns interaction; [catalog](components/library-patterns.md) |
| Active theme **wp-content/themes/robylo-starter/assets/css/fallback.css**, appended GCPRO E16 block | Desktop process hover/rings/keyframes and reduced-motion transition override | Canonical [theme-overrides/process-timeline.css](../theme-overrides/process-timeline.css); live appended block matches after whitespace normalization. Enqueued once by functions.php as robylo-fallback, content-MD5 versioning. Preserve on theme updates; do not edit shared ROBYLO repository for this client block |
| Elementor → Design System → Classes | Class-owned CSS exceptions below | Native supported declarations remain in Atomic controls. These blocks complement them; do not replace a class from a partial resource dump |

No HTML widgets occur in the current Homepage rendered tree; four legacy Shortcode widgets are explicitly mapped in component records. No additional GCPRO PHP/JS file was deployed by this audit. Additional WordPress Customizer CSS was not separately audited as a saved database field; frontend CSS inspection does not prove absence throughout the installation.

## Custom Code847 — live Final CTA video experiment

**Verified source:** saved code editor and frontend agree on a staging hostname guard, .elementor-154 scope, panel[data-interaction-id="5ec4592"], absolute staging MP4 URL and runtime class/layer injection. Attachment846 is not a saved video element in Component80.

**CSS:** forced navy background; isolation; local panel clipping; content/layer z-index; masked screen-blended decorative layer. Mobile rules force container gutter0,panel radius0,padding32px20px and lower-right layer70% high/right-5%. Four source !important declarations enforce background/gutters/radius/padding, plus reduced-motion layer display:none!important. These are existing experiment values, not architecture recommendations. The right bleed is contained locally and did not cause document overflow in tests.

**JS:** initializes once per marked panel; motion/Save-Data gates; lazily creates muted/autoplay/loop/playsinline,aria-hidden,inert decorative video near300px; visibility pause; requestAnimationFrame-coalesced passive scroll; resize/visibility/motion listeners; error cleanup and playback-state attribute. It is not a reusable native video Component contract. No confirmed unnecessary second video script was found; replacing this working experiment requires an agreed native/semantic-class plan.

**Editing/rollback:** existing847 only; no additional active stylesheet. To remove experiment on staging, explicitly set847 Draft and reload/purge cache; do not delete attachment846 or alter shared80. Reuse/migration must replace page/element/host/media coupling deliberately, not copy this snippet to production.

## Global class Custom CSS owners

Fresh editor resource reads cover Homepage/header context; props not returned must not be treated as absent. Below is the complete set of classes with non-empty Custom CSS returned in the inspected Homepage context, not a claim about every unused document.

| Class (Design System → Classes) | Custom CSS purpose / audit note |
| --- | --- |
| section--dark | Scoped descendant text/link/icon/card/menu colors and focus states; broad within a deliberate dark surface |
| city-link | Border sides, pseudo-arrow/hover/focus, transition and reduced motion; one repeated owner, not per-city CSS |
| footer-meta | Top color-mix white25% border |
| navigation--primary | Vendor nav-menu descendants, menu/toggle/focus/layout and spacing; **.menu-item-242** ID coupling; superseded nowrap/padding declarations retained as debt |
| navigation-links | Vendor menu-link font/spacing |
| hide-empty | :empty display suppression |
| section | box-sizing:border-box fallback |
| header-row | Padding and direct button sizing/hiding; redundant earlier padding/grid placement |
| info-row | Repeated superseded padding-block declarations in desktop/mobile variants |
| container | border-box and auto inline margins |
| button-primary | Border-box/wrapping and repeated focus-visible group; later group adds white halo |
| button-secondary | Same focus/wrapping pattern plus final nowrap |
| button-outline | Same repeated focus-visible group |
| button-outline-orange | Border-box/wrapping/focus halo |
| button-outline-white | Border-box/wrapping; hover/focus-visible/disabled vendor-safe descendant-independent states |
| icon-svg | SVG fill:none; hides fallback when adjacent nonempty card-icon exists |
| site-header | Bottom border style/color fallback |
| info-bar | Utility-link/focus/border styling; earlier underline declaration superseded |
| info-links | Sibling dividers/spacing; mobile padding override repetition |
| info-text | nowrap |
| emergency-mark | max-content width |
| emergency-mark__slash | Earlier tiny inline padding superseded by0 |
| emergency-mark__label | Earlier nowrap superseded by normal |
| audience-card | Parent hover/focus→image/action, media gates, clipped image child and reduced motion |
| section-heading--accent | Direct stack H2 pseudo-line40×3px,space-sm gap; requires that documented structure |
| hero--panorama | Desktop media-specific layered background size/position and no-repeat |
| core-b-row | Parent-state arrow translation/focus outline/color and reduced motion |
| why-benefit | SVG fill:none |
| why-benefit-number | nowrap number protection |

These existing exceptions are not blanket approval for new code. Some basic fallback declarations may now be expressible natively, but mechanically replacing whole variants risks destroying native properties or changing cascade order. Consumer-aware cleanup is a proposed follow-up, not an automatic audit mutation.

## Source files and authority

| Repository file | Actual deployed owner |
| --- | --- |
| integrations/process-timeline-mobile.css and .js | Canonical Code590 source; whitespace-normalized equality verified |
| theme-overrides/process-timeline.css | Canonical appended theme exception; whitespace-normalized equality verified |
| integrations/audience-card-hover.css | Non-enqueued class-owned rule mirror; current class behavior inspected, not a full native-property serialization |
| integrations/section-heading-accent.css | Non-enqueued class-owned pseudo-line mirror |
| integrations/hero-panorama-composition.css | Non-enqueued composition mirror; native backgrounds own remaining image/blend settings |

No automatic Git→WordPress deployment exists. Never enqueue a mirror as a second active owner. Do not commit raw admin HTML/session configuration, database dumps or credential-bearing responses.

## Third-party/runtime dependencies

Read from Plugins UI: WordPress7.1.3; Elementor4.3.5; Elementor Pro4.3.2; BEAF Free4.7.21/Pro4.5.7; Widgets for Google Reviews14.2; Speed Optimizer7.8.4; Security Optimizer1.6.9; SiteGround Central3.4.8; AI Agent by SiteGround1.3.1; AI Provider for Anthropic1.0.5 and OpenAI1.2.0 active; Google provider1.2.0 inactive. Inventory is not a recommendation to remove admin/AI plugins. No plugin settings, versions, credentials or security controls changed.

Homepage dependencies: Elementor/Pro native rendering/Components/Theme Builder; BEAF jQuery/twentytwenty/fullscreen Ajax; Trustindex plugin/CDN/data/font; Google font styles for Inter/Montserrat (also vendor font assets); existing staging media. Decorative Code590/847 use browser APIs, not another framework. [Theme](ARCHITECTURE.md) is standalone ROBYLO Starter0.2.0; one installed theme, no active child theme.

## Coupling policy and planned migrations

Required locators include native object/dynamic links, Theme Builder display conditions, Component references and BEAF record IDs. Elementor-generated wrappers/selectors are normal rendering outputs. The avoidable couplings are authored page/grid/element selectors in BEAF/radius847 code and menu-item242 styling.

Proposals: semantic opt-in video contract/native video composition; reusable comparison class plus reliable popup ownership; native/shared CTA radius after consumer review; semantic menu-item role rather than numeric ID. Test old/new consumers, popup body mounting, native editability and all breakpoints before approval/deployment. Leave working behavior in place until then.
