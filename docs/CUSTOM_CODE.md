# Custom code and dependency register

**E59,2026-10-20:** Existing903 CSS/JS updated in place: generic focus-within only reveals the transform; top reset is restricted to :has(.info-bar :focus). JS clearance uses focusedUtility rather than any Header focus. This fixes the verified40px toggle displacement during pointerdown without intercepting/replacing native menu clicks. Entire site/body-end5 unchanged; source equality verified after native editor reload. No new code entry/class/component/dependency.

## E58 global scroll navigation — 2026-10-20

New active owner: **Custom Code903**, “GCPRO / Scroll Navigation & Emergency CTA”, Published/**Entire site**/**Body End**/**priority5**, jQuery opt-in off. [CSS](../integrations/scroll-navigation.css) + [JS](../integrations/scroll-navigation.js) are wrapped once in style#gcpro-scroll-navigation-css/script#gcpro-scroll-navigation-js in that entry; native editor reload source equality verified. Neither source is separately enqueued. Existing590/847 and their conditions remain unchanged. There are now **three** active code entries.

Native visual owners: classes gcpro-mobile-cta g-6771860 and gcpro-mobile-cta__label g-4d22e61. Panel class Custom CSS contains only nested existing button nowrap/flex-shrink and editor-only static visibility. New Header-root host style e-63fbbef4-8ac8 owns padding0/min-width0. Four empty semantic classes configure Header/origin/sticky clearance/opt-out. [Complete class/element IDs, runtime states/properties, read-only vendor adapters, conditions and rollback](components/smart-navigation.md). No new Variables, external dependencies, theme/PHP/plugin changes. BEAF remains an intentional untouched integration;903 only reads its popup visibility.

**Current E57 update:** [Phase1 exact change record and verification](audits/2026-10-20-phase1-cleanup.md). BEAF is entirely excluded: its necessary page/body/grid/slider numeric isolation selectors are intentional third-party exceptions. Only the approved custom Atomic and CTA/header owners below were cleaned.

Fresh staging audit **2026-10-20**. This file owns **where custom behavior is stored**. Component records own behavior/reuse instructions; the [audit](audits/2026-10-20-architecture-and-mobile.md) owns findings and verification. Generated assets in uploads/elementor/css are outputs, never editing locations.

## Active deployments

| Owner / editing location | Contents and consumers | Source / scope / limits |
| --- | --- | --- |
| Elementor → Editor → Custom Elements → Code **590**, “GCPRO / Process Timeline — Mobile Sequence” | Published; body-end priority10; Page154 display condition. Style gcpro-process-mobile-style and script gcpro-process-mobile-sequence | Canonical [CSS](../integrations/process-timeline-mobile.css) and [JS](../integrations/process-timeline-mobile.js); saved text matches after whitespace normalization. Class hooks; no page/element selector in JS. See [timeline](components/how-we-work.md) |
| Same list, Code **847**, “GCPRO / EXPERIMENT — Final CTA Video (staging only)” | Published; body-end priority1; Page154 condition. Inline style gcpro-cta-video-test-css plus script | Exact saved source mirrored in [integrations/cta-video-experiment.html](../integrations/cta-video-experiment.html); not separately enqueued. Existing experiment; E57 changes only selector dependencies |
| Homepage154 → Page Settings → Advanced → **Custom CSS** | BEAF labels, fullscreen buttons, media/reduced-motion rules | Page/body/grid ID scoped; [Before/After record](components/before-after.md). No separate GCPRO JS |
| Homepage154 → main46c3aad4 → local Style **e-685133d2-110f** → Custom CSS | & .cta-panel { border-radius:8px; } | Existing Final CTA per-instance radius exception. Scope/purpose/migration documented in [CTA](components/final-cta.md) |
| Library74/77 → local layout/image styles | Scoped :has/missing-image collapse/hide exceptions |74: e-30b81e2f-f92c/e-580e21c9-f816;77: e-3cbef3d9-e4cd/e-6bff78bc-1753. [Catalog](components/library-patterns.md); no authored page ID |
| FAQ83 → local header styles | Focus-visible outline exceptions | e-6fab0c7e-1ad9/e-32802adb-5ad2. Native accordion owns interaction; [catalog](components/library-patterns.md) |
| Active theme **wp-content/themes/robylo-starter/assets/css/fallback.css**, appended GCPRO E16 block | Desktop process hover/rings/keyframes and reduced-motion transition override | Canonical [theme-overrides/process-timeline.css](../theme-overrides/process-timeline.css); live appended block matches after whitespace normalization. Enqueued once by functions.php as robylo-fallback, content-MD5 versioning. Preserve on theme updates; do not edit shared ROBYLO repository for this client block |
| Elementor → Design System → Classes | Class-owned CSS exceptions below | Native supported declarations remain in Atomic controls. These blocks complement them; do not replace a class from a partial resource dump |

No HTML widgets occur in the current Homepage rendered tree; four legacy Shortcode widgets are explicitly mapped in component records. No additional GCPRO PHP/JS file was deployed by this audit. Additional WordPress Customizer CSS was not separately audited as a saved database field; frontend CSS inspection does not prove absence throughout the installation.

## Custom Code847 — live Final CTA video experiment

**Verified source (E57):** saved code editor and frontend agree on a staging hostname guard, .gcpro-homepage scope and .cta-panel query, absolute staging MP4 URL and runtime class/layer injection. Marker gcpro-homepage g-d0c199c is applied only to154/main46c3aad4; exactly one panel matches. Native Page154 display condition is retained. Attachment846 is not a saved video element in Component80.

**CSS:** forced navy background; isolation; local panel clipping; content/layer z-index; masked screen-blended decorative layer. Mobile rules force container gutter0,panel radius0,padding32px20px and lower-right layer70% high/right-5%. Four source !important declarations enforce background/gutters/radius/padding, plus reduced-motion layer display:none!important. These are existing experiment values, not architecture recommendations. The right bleed is contained locally and did not cause document overflow in tests.

**JS:** initializes once per marked panel; motion/Save-Data gates; lazily creates muted/autoplay/loop/playsinline,aria-hidden,inert decorative video near300px; visibility pause; requestAnimationFrame-coalesced passive scroll; resize/visibility/motion listeners; error cleanup and playback-state attribute. It is not a reusable native video Component contract. No unnecessary second video script was found. E57 replaces only authored page/element selectors with the semantic scope; native video restructuring remains a separate decision.

**Editing/rollback:** existing847 only; no additional active stylesheet. To remove experiment on staging, explicitly set847 Draft and reload/purge cache; do not delete attachment846 or alter shared80. Reuse/migration must review the semantic scope, single-panel contract, native display condition and host/media coupling deliberately; do not copy this staging experiment to production.

## Global class Custom CSS owners

Fresh editor resource reads cover Homepage/header context; props not returned must not be treated as absent. Below is the complete set of classes with non-empty Custom CSS returned in the inspected Homepage context, not a claim about every unused document.

| Class (Design System → Classes) | Custom CSS purpose / audit note |
| --- | --- |
| section--dark | Scoped descendant text/link/icon/card/menu colors and focus states; broad within a deliberate dark surface |
| city-link | Border sides, pseudo-arrow/hover/focus, transition and reduced motion; one repeated owner, not per-city CSS |
| footer-meta | Top color-mix white25% border |
| navigation--primary | Vendor nav-menu descendants, menu/toggle/focus/layout and spacing; semantic .gcpro-menu-item--header-hidden hides Resources in Header only. E57 removed two superseded declarations |
| navigation-links | Vendor menu-link font/spacing |
| hide-empty | :empty display suppression |
| section | box-sizing:border-box fallback |
| header-row | Final12px block padding and direct button sizing/hiding; E57 removed earlier desktop padding, preserved mobile placement/hiding |
| info-row | Single final desktop0/mobile space-xs padding; redundant cascade removed E57 |
| container | border-box and auto inline margins |
| button-primary | Border-box/wrapping and one focus-visible outline/offset/white halo group |
| button-secondary | Border-box, one focus-visible halo group and nowrap; duplicate/overridden declarations removed E57 |
| button-outline | Border-box/wrapping and one focus-visible outline/offset/white halo group |
| button-outline-orange | Border-box/wrapping/focus halo |
| button-outline-white | Border-box/wrapping; hover/focus-visible/disabled vendor-safe descendant-independent states |
| icon-svg | SVG fill:none; hides fallback when adjacent nonempty card-icon exists |
| site-header | Bottom border style/color fallback |
| info-bar | Utility-link/focus/border styling; E57 removed earlier overridden underline, kept normal none/hover underline |
| info-links | Sibling dividers/spacing; E57 retains final mobile half-xs for info-text siblings and separate anchor rule |
| info-text | nowrap |
| emergency-mark | max-content width |
| emergency-mark__slash | Final inline padding0; earlier superseded value removed E57 |
| emergency-mark__label | Final white-space:normal; earlier superseded nowrap removed E57 |
| audience-card | Parent hover/focus→image/action, media gates, clipped image child and reduced motion |
| section-heading--accent | Direct stack H2 pseudo-line40×3px,space-sm gap; requires that documented structure |
| hero--panorama | Desktop media-specific layered background size/position and no-repeat |
| core-b-row | Parent-state arrow translation/focus outline/color and reduced motion |
| why-benefit | SVG fill:none |
| why-benefit-number | nowrap number protection |

These existing exceptions are not blanket approval for new code. Some basic fallback declarations may now be expressible natively, but mechanically replacing whole variants risks destroying native properties or changing cascade order. The approved E57 cleanup is limited to the exact ten classes/variants in its audit; other native migration proposals remain separate scope.

## Source files and authority

| Repository file | Actual deployed owner |
| --- | --- |
| integrations/cta-video-experiment.html | Exact E57 Code847 source mirror; never separately enqueue/deploy |
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

Required locators include native object/dynamic links, Theme Builder display conditions, Component references and BEAF record IDs. Elementor-generated wrappers/selectors are normal rendering outputs. E57 removed authored numeric dependencies from custom847/radius/header code. BEAF page/grid/plugin selectors remain intentional third-party isolation exceptions and are outside Phase1.

E57 implements the minimal semantic scope/menu selectors and verified redundant declaration cleanup. Native video composition/shared radius migration remains separately scoped; no BEAF refactor is proposed under Phase1. Preserve generated IDs/native object relationships and review consumers before any future structural change.
