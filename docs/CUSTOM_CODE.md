# Custom code and dependency register

## Editorial pilot and quiet menu actions — 2026-10-30

Implemented on staging with ui-ux-pro-max guidance. Single Post123 and synced core pattern3159 remain the existing owners. Pale-blue full-width opening uses the site container, breadcrumb, white rounded topic chip, gray Montserrat700 H1, excerpt, two compact native publication/modified-date chips with decorative calendar/clock glyphs, and one4:3 featured image to the right; core Columns stack on narrow screens. Dates remain actual Post Date blocks; no invented byline, reading time, buttons, reviews or emergency mark. Body remains white with a centered760px reading column, Inter body text, gray Montserrat H2/H3, blue ordinary-weight links without orange underlines, and retained visible focus. User requested photo in the opening rather than duplicated below it.

Pilot Post2046 [Water Damage at Home: What to Do First](https://vitaliiv1.sg-host.com/what-to-do-if-you-notice-water-damage-in-your-home/) retains reviewed wording, URL, publication status, SEO fields, original date and featured media. Safety guidance is a warm#FFF7ED native Group with8px corners and NO colored side rule; existing factual observations form a pale-blue checklist. All six headings have native anchors with180px scroll offset. No TOC inserted because the short article does not need one. Three unsynced native patterns3435 Safety note,3442 Key points and3443 On this page are available in WordPress Patterns; inserted copies remain independently editable. Adjust TOC links to the actual article anchors when useful on a longer article. Other article bodies were not decorated or rewritten.

Single123 Post Content3307e90b is the sole scoped CSS owner for reading width, headings, links, anchor offset and opening alignment; superseded rules replaced there. Pattern3159 owns native dynamic header layout/typography/chips. No plugin, new field, per-post stylesheet or JS added. Final inset CTA80 unchanged. Archives124/2232 and SingleProject2231 protected settings compare unchanged. BeforeAfter493 Elementor data differs from the initial snapshot; this task made no writes to493, so the concurrent difference was preserved and not reverted.

Header113 primary Nav Menu7983af36 retains its existing sole Custom CSS owner. Removed decorative orange active inset and action outlines per owner steering; actions now have a very pale orange#FFF7ED fill, subtly stronger#FFEDD5 hover/focus, navy text and6px corners. Existing native links, order, main CTA and functional focus outline preserved. Ordinary menu items unchanged. This is not a claim of an exhaustive sitewide border audit. Source mirror is recovery documentation, not separately enqueued.

Verification: native saved settings and guest HTTP/HTML checks on pilot2046 and longer-title2050:200, one H1, noindex, self-canonical, one opening photograph, actual date fields; protected article fields unchanged. Archive124/2232 and SingleProject2231 settings unchanged;493 concurrent data difference preserved. Pilot AIOSEO differences are only updated/scan timestamps, not SEO title/description/canonical values. Saved menu rules checked. Actual Chrome screenshot observed the earlier split opening; final desktop/mobile screenshots, computed overflow, anchor-under-sticky and keyboard acceptance remain incomplete: the user stopped Computer Use with physical Escape after repeated simultaneous-input guards. No further Computer Use calls made. Settings/HTML checks are not browser acceptance.

Private recoverable pre-change snapshots remain outside Git in outputs/article-pilot-2026-10-30. Roll back native3159/123/113 settings and pilot2046 body from those snapshots through the supported editor/REST. No credentials, raw admin responses or private backups committed. Existing30-article SEO decisions and canonical URL inventory remain unchanged. Owner rejected the illustrative wall-staining cover as a weak visual choice; replacement selection remains outstanding and no uninspected replacement was silently substituted.


**2026-10-30 archive-only follow-up:** one native Archive Hero3421 reused on124/2232/493, existing masked-image plugin/SVGs and native classes/variables only. No action/review/emergency nodes. Source serviceHero1318 unchanged. Article3159 topic/date badges use native WordPress block styles, no new CSS/JS. Resource archive root29d73bf4 native relative/z-index0 contains category buttons below Header dropdown; unnecessary isolation removed. No global Header styling change, per-Post code, new filtering owner or dependencies. Browser stacking/mobile acceptance still pending; exact owners/rollback in sharedHero/Resources records.

**2026-10-30 editorial templates:** Native synced pattern3159 owns article opening content/dynamic blocks; Single2231 Atomic Opening45461274 owns project opening. Existing Single123/Post Content3307e90b and Single2231/Post Content69a2b5bf each own their scoped native-Post body typography/link CSS exception. No per-article scripts/styles, new plugin, HTML widget, theme enqueue or universal template framework. V3 selectors explicitly use `selector`; corrected an unscoped top-level ampersand that had leaked reading-width rules. Replaced default WordPress Group with native vertical Flex to remove the extra wrapper that defeated header spacing. Empty hidden project-metadata slot removed; native Post Info remains pending visual-editor access rather than a custom workaround. Exact owners/rollback and incomplete browser acceptance are in Resources/Projects records.

**2026-10-29 focused audit:** Coverage1.2.2 is the single ZIP matching/result/focus owner. Removed dormant matching JS/data from Popup1801 HTML7a5e1801; static fallback only. Trigger recognition now uses native popup-action ID rather than link text, fixing verified close-scroll jump. Retained justified existing centralized Header styles, credential tooltips1881, emergency bar903, video847, process590 and vendor BEAF/Trustindex/WPGB runtimes; no new parallel code or dependency. Generated native Elementor inline styles are not treated as accidental custom code. See popup/project component audit records.

**2026-10-26 — dropdown actions:** Owner-approved semantic class on four existing menu items; two rules appended to existing Header113/Nav Menu7983af36 Custom CSS. Orange border/spacing and hover/focus only, same desktop/mobile links; no new widget/script/enqueue. [Owner and rollback](components/header-menu-refinement.md#2026-10-26--selective-dropdown-actions). Projects itself uses native templates, Tabs/Collection Loop and Gallery; no additional custom code.

**2026-10-26 — shared Hero Trustindex:** Owner-authorized addition to existing Atomic plugin0.4.3, native `gcpro-trustindex` ID/show-hide controls, official Trustindex loader only. Shared1318/1453 each own one badge below buttons; no custom CSS/JS or additional plugin. [Controls, checks, dependency and rollback](components/hero-trustindex.md).

**2026-10-23 — popup finish:** Native rounded card, external mobile gutters and300ms fade;44px close control, true prevent_scroll setting and viewport-preserving close. Opening focuses the dialog rather than input. Mobile gutter/focus/position checked. [Owners and recovery](components/service-availability-popup.md).


**2026-10-23 — service availability popup:** Native Popup1801, shared1140 trigger; owner-authorized local form code. Submit stays open, accessible close/focus/reset and mobile checked. Owner supplied provisional Chicagoland scope; no ZIP/neighborhood exclusions are approved. Exact confirmation remains disabled; valid input shows the owner’s call-to-confirm message. Field/button layout is native Atomic,48px high,12px gap, inline desktop/tablet and stacked mobile. No invented coverage or Request492 form claim. [Editing, gap and recovery](components/service-availability-popup.md).


**2026-10-23 — Hero background:** Native Atomic local background-image on1318/root2ddab7e and1453/root5de65e14 owns the two subtle radial gradients. Existing dark-section base token unchanged; no extra stylesheet/JS/widget. [Values and rollback](components/shared-hero.md).

**2026-10-23 — navigation:** Header113 → Nav Menu7983af36 and4ebecbc6 → Advanced Custom CSS own main/mobile and utility styles respectively. Explicit widget-scoped selectors; no new JS/dependency. integrations/header-primary-menu.css and header-utility-menu.css are reference snapshots, not separate enqueues. [Storage, mobile gap correction and rollback](components/header-menu-refinement.md).

**2026-10-23 — shared visual enlargement:** Owner superseded editable-scale controls with direct visual scaling everywhere. Existing media elements489ada85 in Shared Hero1318 and5a4c9954 in Water Hero1453 now use native local transform scale1.25, origin left center; tablet/mobile reset to none. Photo and optional decoration scale together; layout footprint remains4:3. Shared1318 outer section clips horizontal viewport overflow; media frame remains overflow-visible. No Hero rebuild, new controls, PHP/CSS plugin deployment or content/photo change remains. Earlier0.5 control attempt was rolled back to0.4.1. Commercial-only ineffective descendant rule removed. Commercial browser confirmed matrix1.25, loaded image and no page overflow; owner accepts final visuals. Reset media transform to none to roll back.

**2026-10-23 — editable mask correction:** Atomic Masked Image0.4.1 now accepts ordinary SVG silhouettes directly, with separate optional Decoration and explicit None/SVG selector. Shared1318/Water1453 migrated; Water514 Decoration=None verified and photo retained. [Controls and rollback](docs/components/atomic-masked-image.md).

**2026-10-23 — Atomic waves0.2.0:** Existing integrations/gcpro-atomic-masked-image owns optional Background/Accent image props and Twig positioning. Transparent SVG1471/1472 own wave geometry/alpha transitions. Only Water Hero1453 uses them; no new JS, classes, Variables or dependencies. [Owners and rollback](components/atomic-masked-image.md).

**2026-10-23 — authorized Atomic mask extension:** Source owner `integrations/gcpro-atomic-masked-image/`, installed staging plugin GCPRO Atomic Masked Image0.1.0. Two PHP files and Twig template own scoped inline media geometry/mask declarations. No JS, dependency, theme/core/third-party modification or global styling. Active only in Water514 Hero1453. [Controls, limitations and rollback](components/atomic-masked-image.md).

**2026-10-22 — Shared Why certifications layout:** Existing Component1149 now places the same five original logos in a full-width area below the unchanged introduction/four-benefit composition. Existing label is left aligned, without decorative lines. Owner subsequently requested subtle outlined frames and hover: white12% border,8px radius,68%→100% opacity and translateY(-2px),180ms transition with reduced-motion guard; no moving strip. Desktop/tablet five-across; mobile centered 3+2. Reuses existing trust-logos/trust-logo/trust-logo__image classes and Variables; no new nodes, classes, Components, Variables, scripts, media, plugins or dependencies. Applies to Home154, Residential484 and Commercial499. See [current owners, verification and rollback](components/why-gcpro.md).

**E84:** Commercial499 adds no CSS/JS/PHP/Custom Code/plugin/dependency. Existing shared native controls and17 regenerated page-local style IDs reuse the approved composition; all local Custom CSS fields empty.903/590/847, Kit6 and BEAF remain their sole existing owners. [Exact owner record](components/commercial-services.md).

**E83:** Three new Global Classes ba-card g-c02ab3c, ba-card__caption g-c65c717, ba-card__title g-4523dc2 store only native controls; all Custom CSS fields null. No CSS/JS/PHP/Custom Code entry/source mirror or dependency added. Existing Kit6 owns BEAF presentation; plugin files/records and Hero exceptions unchanged. [Owners and rollback](components/before-after.md#e83--approved-a-card-design-2026-10-21).

**E81/E82,2026-10-21:** No new CSS/JS/PHP, Custom Code entries, plugins or dependencies. E82 uses the existing blue button-secondary class on native Button77a9e83d inside77; local native display/wrapping controls counter the existing class mobile-hiding/nowrap behavior. No custom CSS added; existing empty-image CSS retained. Gallery493 uses native Atomic layout and existing BEAF plugin/Kit6 presentation. No source mirror is newly enqueued. [CTA standard](DESIGN_SYSTEM.md#cta-button-hierarchy--e82-2026-10-21).

**Current E80,2026-10-21:** Global AIOSEO setup completed on staging using native settings; owner-activated Local Business1.3.17 now emits verified single Lombard establishment. Short-brand title defaults retained, thin archives/media/terms noindex, breadcrumb hierarchy enabled. Office reception hours unspecified;24/7 emergency availability separate. Owner disabled staging Trustindex Rich Snippets; cache refreshed and Product absent from browser/raw anonymous HTML, reviews remain functional. Seven representative heads checked; bodies154/484/Header113/Footer114 and authored exceptions unchanged.93 Pages88 Published/5 Draft;321 URL histories retained. No new runtime code/classes/Components/Variables/plugins/dependencies; production unchanged. [Exact settings, limits and recovery](SEO_AIOSEO.md) · [Sanitized evidence](evidence/2026-10-21-aioseo-global.json).

E79: **No Custom Code/CSS/JS/PHP additions or changes.** Residential content uses native existing Overrides, AIOSEO metadata/options use the installed plugin. One native Service graph, no custom JSON-LD emitter;903/590/847 and BEAF plugin/shared styling untouched; separately requested Hero reuses existing742 through native shortcode, native frame radius/clipping/zero padding, no custom rule. [Exact SEO storage, dependencies, limitations and recovery](SEO_AIOSEO.md). No new classes, Components, Variables, plugins or dependencies.

E78: no Custom Code/CSS/JS/PHP source change. Residential numbered headings reuse existing section-eyebrow/hide-empty/section-heading--accent;71 adds native optional content only. [Current owners](components/residential-services.md#e78--numbered-heading-consistency-and-native-residential-entry-link).

**E77 current shared owners:** Existing847 now Entire site, semantic `.cta-panel` iteration; source mirror updated once, not enqueued. Existing590 source unchanged, Entire-site condition for shared Timeline. Component80 native panel radius replaces Homepage local CSS. No new code entry/file/dependency;903 and BEAF unchanged. [Current storage, reuse and rollback](components/residential-services.md). Earlier154-only references below describe historical conditions.

**Current E76,2026-10-21:** Projects now links to real structural Page1132 `/portfolio/`, with native All Projects / Before & After dropdown. Existing13 project records/URLs untouched. Standard-grid five-item Header and utility Partner Programs retained.93 staging Pages:88 Published/5 Draft;321 migration rows. No new E76 CSS/JS/classes/plugins/dependencies. [Exact storage, checks and limitations](audits/2026-10-21-projects-navigation.md).

**Current E75 (includes pending E74 sync), 2026-10-21:** Staging structural publication:92 Pages,87 Published/5 Draft;84 newly published approved targets including Resources1007,51 city Pages and Partner982–986. Native shared Single Page1008 supplies79 structural placeholders. Final service-first Header113:five main sections (Residential/Commercial/Service Areas/Projects/About), utility Partner Programs with four children/Careers/Contact Us; Blog and Our Team await real staging destinations. Standard1200px grid/logo sizes retained, native toggle below1200, one complete mobile menu. No production/BEAF/Footer/Homepage-content/903 edits.321 canonical migration rows preserve prior source mappings/decisions. [Exact storage, tests, limitations and rollback](audits/2026-10-21-staging-structure-and-navigation.md) · [Actual hierarchy](SITEMAP.md).

**E73:** Partner Programs982–986 use existing section/container classes, native H1 defaults, Full Width/Hide Title controls; no Custom CSS/JS/PHP or Custom Code entry added. Menu13 is native WordPress metadata, unassigned. Existing Homepage/Header/Footer/BEAF/903 owners unchanged. [Exact editing and recovery](components/partner-programs.md).

**Current E71 (after E70 approval), 2026-10-20:** Main Homepage154 Hero a62cdd3 now uses the approved navy split layout and the FIRST existing BEAF723 comparison in visual484c13ec → Shortcode30e0c45, `[bafg id="723"]`. Native layout, copy, CTA overrides and 8px corners retained. One local wrapper Custom CSS rule hides only its fullscreen button; plugin image-link/zoom is already disabled. All three original comparisons and their fullscreen remain unchanged. E70 removed all old local panorama/technician backgrounds and retired unused, empty hero--panorama g-708f717 after a site-wide usage scan (111 classes/36 variables). Draft970 and Media973 retain the static design experiment. No new class, Variable, library Component, JS, plugin or dependency; no Header/Footer/Core/903/production edits. [Current exact owners, QA and rollback](components/hero-main-beaf.md).

**Historical E69 (superseded by E70/E71),2026-10-20:** Separate **Draft Page970 — Hero Concept B — Restoration Transformation**, root78418107, duplicates the source12-node Atomic structure with fresh IDs and existing286/53/103 instances. New illustrative Media973:1440×1080 WebP/250,828bytes. Native navy split layout, copy/CTAs first on mobile/tablet,8px visual corners; Canvas/Hide Title isolates preview. No new classes/Variables/library Components/custom code/dependencies. Existing Homepage Hero remains active; only separately owner-requested project&nbsp;information wrapping changed in154/7de610a7. No Header/Footer/BEAF/production edits. [Preview, exact owners, QA and activation/discard](components/hero-concept-b.md).

**Historical E68 (superseded by E70),2026-10-20:** Homepage154 Hero a62cdd3 uses supplied Media961 and native brand-navy gradient layers. Local e-7cfcd182-d44a owns bounded1440px canvas/+80px center offset/top framing and responsive75%/80% cover composition CSS. Old hero--panorama detached, definition retained. Tablet native single-column/max600px copy; mobile placeholder hidden;12 nodes/content/links retained. No new class/Variable/Component/JS/dependency; one requested image asset. Footer/Header/Core/903/BEAF/production unchanged. [Exact owners, saved values, nine-width QA and rollback](audits/2026-10-20-hero-technician.md).

**Current E67,2026-10-20:** Footer114 preserves approved desktop geometry; mobile source/visual order is Identity → Contact → Services, with44px compact service rows. Tablet identity/contact share the first row and two-column services the second; cities use4 tablet/2 mobile columns. Copyright/full Back to top share a mobile row with13px type and44px action height. Native controls/existing g-aca1669 reused;36 nodes/112 classes; no new Component/Variable/JS/plugin. Three minimal local CSS gaps: city separator hiding (tablet), top-link nowrap and copyright balanced wrapping (mobile). All corresponding service pages remain Draft, so no invented links. BEAF/Header/903/Core/production untouched. [Exact owners, links, six-width QA, limitations and rollback](audits/2026-10-20-footer-responsive.md).

**Current E65–E66,2026-10-20:** Footer114 root1687d698/local e-65a7ec46-9cb8 gains one `.elementor-social-icon:focus-visible` orange outline rule; native widget handles its size/colors/hover/alignment. Native icon class g-c2210fa, row gap/alignment and local footer layout/muted text are editable native controls. Three script-free SVG sources assets/icons/footer-phone.svg, footer-email.svg, footer-location.svg →Media935/936/937. [E65 exact owners](audits/2026-10-20-footer-contact-icons.md). No903/JS/PHP/theme change.

**New shared BEAF owner:** existing Elementor Kit6 → Site Settings → Custom CSS, source mirror [integrations/beaf-presentation.css](../integrations/beaf-presentation.css). Explicit later owner authorization permits this presentation-only exception; Phase1 exclusion remains. New stylesheet has plugin-class selectors only, inline and body-mounted popup support, one necessary focus !important. No new Custom Code post/JS/plugin dependency. Fresh Homepage154 Page Custom CSS and Kit6 field were empty before E66; historical page overrides below describe earlier state and are superseded for presentation. Do not restore the obsolete numeric block alongside the global style. [Evidence, gap and rollback](audits/2026-10-20-beaf-presentation.md).

**Current E64,2026-10-20:** Existing903 CSS replaces body padding with .gcpro-nav-ready .site-footer measured/safe-area bottom reserve; JS unchanged, Entire site/Body End/priority5 retained and source reread exact. Footer114 root1687d698/e-65a7ec46-9cb8 owns four scoped link/Outline103 hover/focus rules: white text, orange underline/border/outline, no blue state. Other new visual controls are native local footer styles; per-side border style/color and Home logical auto margin retain documented converter CSS. gcpro-footer-link g-373d928 is entirely native; gcpro-footer-item g-aca1669 owns native padding/border widths plus only divider style/color Custom CSS.154 title fixed by native Hide Title, no CSS. [Every owner and recovery](audits/2026-10-20-footer-refresh.md), [exact saved values](audits/2026-10-20-footer-refresh-settings.json). No new code entry, JS/PHP/theme file/plugin/library. Google Maps is an ordinary external action, not an embedded SDK.

**E63,2026-10-20:** No Custom Code903/source changes. Existing class gcpro-mobile-cta g-6771860 owns compact nested Primary53 sizing, no-shrink286 and empty-caption hiding; native panel padding becomes space-xs on all sides. Outline-specific guard replaced, duplicates removed, native colors/layout retained. [Exact class CSS and component locators](audits/2026-10-20-mobile-cta-orange-247.md). No new code entry/class/component/dependency.

**Current E62,2026-10-20:** Existing903 JS removes automatic phone-button suppression, including main content, so Call Now stays through Process entry. First downward fixed entry starts its200ms exit immediately from measured flow top; one-time transient inline transform/transition setup plus style flush prevents gesture-overshoot bounce. Both inline properties are cleared immediately. CSS, native components and all hooks/observers/listeners unchanged. Saved wrapper exact, Entire site/Body End/priority5 preserved. [Exact locations, behavior, evidence and rollback](audits/2026-10-20-process-cta-transition.md). No new code entry, class or dependency.

**Historical E61,2026-10-20:** Existing903 JS limited competing phone actions to main content; footer text phone no longer suppressed Call Now. E62 removes the remaining implicit phone rule. E61 removed E60 introOverlap gate after correcting native section stacking. Homepage154 native styles own section z0 and mobile intro z1. [Owners and rollback](audits/2026-10-20-section-layers-footer.md).

**Historical E60,2026-10-20:** Existing903 remains the sole behavior owner, Entire site/Body End/priority5. Its CSS/JS introduced :focus-visible for keyboard-only pinning/utility reveal, a matching-top normal/fixed handoff, distance reset while pinned, and bottom-panel suppression during a measured Core-intro intersection. Only that last gate was removed in E61. [E60 implementation and tests](audits/2026-10-20-header-cycle-fix.md). E59 below is historical and its broad focus-within behavior is superseded.

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
| Existing Kit6 → Site Settings → **Custom CSS** | Shared BEAF label/expand-button presentation, E66 | Plugin-class selectors; [source](../integrations/beaf-presentation.css), [Before/After record](components/before-after.md). No separate GCPRO JS; former154 page CSS absent on fresh read |
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
| why-benefit | Former SVG fill:none exception removed2026-10-23; native grid remains. Filled SVG uploads now paint; Atomic root currentColor fill can produce silhouettes for outline sources. See [icon controls](components/why-gcpro.md). |
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


2026-10-22 Trust Logos: [current shared1149 media,classes,label,mobile order,hover,verification limits and rollback](components/why-gcpro.md). This record supersedes earlier Why media descriptions.


2026-10-22 — Owner-approved Trust Logos separator: existing trust-logos g-c8bf649 now has a1px solid white16% top border and14px top padding. It spans only the media column; browser1440px confirms40px separation from right benefits,360px retains one logo row/no overflow. Existing native block-start border width/padding controls and class-owned border-top style/color exception; no new class,element,Component,Variable,JS,plugin or dependency. Hover unchanged. Applies to Home154,Residential484,Commercial499 through existing1149. Owner accepted; do not redesign further. Rollback:remove only the added top border and14px padding.

## 2026-10-24 — Centralized affiliation behavior

**1881 — GCPRO / Affiliation Tooltips — staging**: Published Elementor Custom Code, Entire Site/include/general, Body End, priority10. Canonical source: [integrations/affiliation-tooltips.js](../integrations/affiliation-tooltips.js). Staging hostname guard; one initialization and no dependencies. It owns only accessible hover/focus/tap, dismissal, keyboard link access and viewport positioning. Five native editable tooltip boxes remain within Footer114 so document-scoped Elementor styling applies. Ten triggers on Water514 (five elsewhere through Footer); semantic classes gcpro-affiliation-trigger/gcpro-affiliation-tooltip, no authored page/element-ID selectors in JS. Native classes supply cursor and hidden-by-default boxes; native local controls own visual styles. No page-local script, new plugin or duplicate enqueue.

Use role=dialog, aria-modal=false for small nonmodal popovers containing profile links; triggers expose expanded/controls/haspopup and keyboard focus. Escape returns focus without reopening. Links are inside popovers, not competing logo actions. Disable1881 to roll back behavior; native hidden boxes stay hidden. Other custom-code entries remain unchanged. [Full implementation and limits](components/affiliations.md).


2026-10-24 — Shared affiliations rollout: Component1886 reuses existing semantic trigger hooks on all17 service pages. Existing1881 source/meta and Footer114 tooltip text/links remain exactly unchanged. Ten triggers per service page (five large-block/five Footer); no second script, class, stylesheet or code entry. Large layout edits now belong in1886. [Coverage and verification](components/affiliations.md#approved-shared-rollout--current-editing-location).

2026-10-24 — Code903 CSS-only Header state exception: existing floating state supplies Solid Orange palette to Header `.button-secondary`; hover/focus matches53. Canonical integrations/scroll-navigation.css updated; no separately enqueued file, new script/listener/token or JS change. Location/conditions/priority unchanged. Header113/Footer114/Popup1801 preserved. [Scope, owners, contrast/access limits and recovery](audits/2026-10-24-service-consistency.md).

## 2026-10-29 — GCPRO coverage plugin exception

Owner-authorized adaptation under `integrations/gcpro-service-coverage/`, installed1.2.1 staging only. PHP owns one admin registry and lookup; one external popup.js and popup.css replace the existing HTML widget7a5e1801 through the official Elementor render-content filter. Native Popup1801 still owns the modal/form/presentation controls. Admin stylesheet only loads on its own management screen. No copied CM coverage or second modal. Existing Popup1801 document CSS retains only modal/close/focus/motion rules; results are owned solely by popup.css. [Editing, test and rollback record](components/service-availability-popup.md#staging-coverage-bridge-and-owner-approved-cities--2026-10-29).

## Analytics QA / coverage result state — 2026-10-29

Elementor Custom Code3127 (head/priority1/Entire site) is the sole hostname-gated QA GTM loader. `integrations/analytics/qa-loader-template.html` is a redacted reference, not a second enqueue. GTM tag34 owns `integrations/analytics-events.js`; native Google/Event tags31/44 own delivery. No new plugin or HTML widgets. Explicit QA session switch; ordinary visitors not tracked; production activation pending. Native confirmed-success class observer is required because the inspected Atomic handler exposes no success CustomEvent. Coverage plugin1.2.3 popup.js exposes sanitized result status; popup.css owns served-only #ecfdf3, PHP version bump. [Configuration and limitations](ANALYTICS.md).


### 2026-10-29 — Resources follow-up

Resources follow-up: Archive124 Nav Menu6eb3c3c0 is the single scoped V3 Custom CSS owner for topic typography, light panel and active/hover/focus states. Existing Header113 document Custom CSS retains breakpoint/focus rules and owns ancestor highlighting/removal of orange menu lines. No new JS/PHP/filter logic. Native Kit6 Theme Style and core block style attributes are native presentation controls, not a second stylesheet. Restore private pre-change snapshots for rollback.


## Resources redesign CSS owners — 2026-10-29

Archive124 Nav Menu6eb3c3c0 owns existing V3 scoped topic-chip CSS. Archive124 loop layout380a3746 owns native3/2/1 grid plus its first-item spanning/photo-text local exception. Single123 Post Content3307e90b owns scoped V3 CSS for core synced header3159 split composition, category/dates,760px body measure and mobile stack; core block descendants cannot be edited as Atomic controls via this MCP. Existing native container/card controls own supported geometry and typography. Resource Card3133 no longer uses global card/card--interactive assignments; those definitions and other consumers are untouched. No new theme stylesheet/enqueue, class, Component, Variable, JS, PHP, HTML widget, plugin or dependency.

Connector correction: V3 fallback emitted bare ampersand descendant rules at top level, affecting unrelated elements. Replaced all V3 descendant prefixes with explicit Elementor selector keyword, removed loose declarations before the first rule, published123/124 and checked actual CSSOM: no unscoped ampersand rules remain. V4 local nesting is correctly scoped. A unitless V3 line-height had converted1.75 to1.75px; removed V3 base typography so Post Content now inherits native18px/1.75. Do not reintroduce either pattern. No page-ID selectors. First-item layout relies on direct role=listitem/anchor/image/content children; revisit its scoped rule if Card3133 structure changes.

Rollback: restore scoped local styles, card class assignments and query limit from private audit-temp/blog-redesign snapshots through Elementor and publish; preserve content, IDs, dates/pattern3159, Header/Footer/Projects/BEAF. This is an editing record, not a second deployed CSS source.


### Final owner correction — 2026-10-29

Owner requested removing the oversized first feature and keeping the rest. Archive124 now uses an ordinary uniform3/2/1 card grid, six articles per page. Removed all first-item spanning and split-layout rules from380a3746; the first article remains a normal card, no post was deleted. Existing introduction/topic navigation, card design and Single123 remain unchanged. Browser1280px confirmed six cards, three equal378.7px columns, first grid-column auto and no horizontal overflow. Earlier lead-story/seven-per-page statements describe the superseded checkpoint. No new photo or hero was inserted; no new CSS owner or dependency. Native responsive rules retained.


### 2026-10-30 — Blog and article emergency CTA timing

- Authorized scope: delay the mobile bottom emergency CTA on the blog and single articles; preserve its design and other page behavior.
- Sole runtime owner remains Elementor Custom Code903, Body End, priority5, existing site-wide conditions. `integrations/scroll-navigation.js` is a source mirror only, not a second deployment.
- `.blog` and `.single-post` now use 50% of the document's available scroll distance. Other routes retain the existing origin/floating gate. Existing menu, focus, form, chat, keyboard and viewport suppression remains unchanged.
- Published through the native Custom Code editor; saved content read back exactly. Staging cache purged. The Signs of Hidden Water Damage frontend delivers the new gate and initializes `gcpro-nav-ready`; no code text leaks into the page. Mobile scrolling on a physical device remains unverified.
- Recovery: restore the prior `passed` gate in903 and purge staging cache.
- Separate pending work: archive Post Info2ef8cf7 currently displays service categories below cards; badge placement is unfinished. No new CSS exception was authorized or deployed. Reports of broken About/article mobile layout remain unconfirmed; desktop pages rendered intact after cache purge.


### 2026-10-30 — Approved archive service-badge CSS exception, completed

Supersedes the pending badge status above. Owner explicitly approved CSS to put category badges over article photos. Sole active owner: Archive124 > Archive Settings > Advanced > Custom CSS. Consumers: Post Info2ef8cf7 cloned within Item5485f36b, semantic class `resource-category-badge`. Classic widget-ID CSS misses Atomic clones; the scoped semantic selector supplies position, white panel, light-gray border, spacing and inherited typography. No JS/theme changes. See [resources component record](components/resources.md#2026-10-30--published-service-badges-on-card-images) for values, tree, dependencies, checks and rollback. Published and checked on12 live blog cards and mobile Elementor preview; cache purged. Physical-device/anonymous checks remain unperformed. Remove only this block to roll back.

2026-10-30 Resources: existing Single123 Post Content3307e90b scoped Custom CSS simplified after moving masthead composition to native Columns in3159. Existing Card3133 local root style owns descendant-arrow hover/focus; arrow local style owns only transition/base presentation. No new stylesheet/JS/plugin. See Resources component record.


Latest owner correction,2026-10-30: dropdown action items now use a thin1px orange color-accent outline with transparent background in normal/hover/focus states, navy text and existing6px corners. This supersedes the pale-orange fill described above. Header113/Nav7983af36 remains sole owner; native saved readback verified. Links, order and main CTA unchanged.


2026-10-30 corrective fix: owner reported broken article layout. Saved readback demonstrated malformed nested selector wrappers/unbalanced braces introduced by reusing the connector style projection. Repaired the sole existing123/3307e90b CSS owner using complete generated widget-scoped selectors; native saved readback now39 balanced rule pairs. Left reading-column alignment retained. Future edits must read raw existing custom_css rather than reconstructing it from the tool style projection. No body, media, URL or SEO writes. Guest cache-busted article request returned403; final generated CSS delivery and browser visual acceptance are unverified.


2026-10-30 Elementor opening migration checkpoint (unfinished): owner authorized moving the full article opening into existing Single123 so heading/photo/metadata can be selected visually. Removed decorative calendar/clock Unicode glyphs from3159 at owner request; native date values remain. Private snapshots captured outside Git. Tested Atomic post-date with publication/modified dynamic sources and then native Current Query Collection Loop: guest MISS render still returned template October30 instead of article February19,2025. Removed the entire temporary metadata test container/loop; no failed test remains. Existing opening and post references retained until a verified replacement exists. No custom date code or hard-coded dates introduced. Need inspect native Elementor Post Info/terms/date controls through visual editor; connector absence is not proof of Elementor feature absence. Computer Use screenshot showed Windows lock screen; stopped app interaction and requested unlock. This blocks visual-editor completion, not saved WordPress/API access. Full migration is NOT complete. Staging-only cache purge performed for focused verification.
