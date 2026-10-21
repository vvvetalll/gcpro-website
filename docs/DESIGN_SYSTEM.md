# GCPRO design system

**E84 application:** [Commercial499](components/commercial-services.md) reuses the existing service cards, numbered headings, shared sections and BA Variant A. Six Orange Outline cards are followed by Solid Blue77 consultation; exploration remains Blue Outline, Hero/final Call uses Solid Orange with White Outline Request on navy. Purpose plus adjacent context is applied without new styles or variants.

**E83,2026-10-21:** Approved A now styles all20 BA cards identically across Homepage154, Residential484 and Gallery493. Three native shared Global Classes own the frame/caption/title;20px titles,24px padding,10px radius,4:3 photos. Captions unified: known City, IL in title, outcome-only description; reused projects share copy. No custom code/Variables/library Components/plugins/media added; vendor records/Hero/links/authored SEO/production untouched.18 responsive cases and three representative drag/fullscreen placements pass; anonymous HTML200 on all three. [Exact owners, caption copy, evidence and rollback](components/before-after.md#e83--approved-a-card-design-2026-10-21).

## Photographic media — E81

Optimize new/replaced photographic images to WebP with suitable dimensions and truthful alt/title/description. Comparison pairs use the owner-approved4:3 crop, matching dimensions and no stretching; retain original files. Avoid redundant near-identical comparison cards. This does not require rasterizing SVG logos/icons or rewriting historical media outside scope. [Gallery owners and verification](components/before-after.md#e81--owner-supplied-gallery-and-optimized-photographs-2026-10-21).

## CTA button hierarchy — E82, 2026-10-21

Select an existing Atomic Button by **both action purpose and page context**. Apply this rule to future Residential, Commercial, individual service, Service Areas, Projects and Partner Programs pages; it does not authorize a site-wide redesign.

Before selecting a variant evaluate the section background/layout, immediately preceding and following sections, the number of similar buttons visible nearby, overall visual rhythm/hierarchy, and whether the action converts, supports conversion or navigates. Avoid excessive repetition and visually competing primary actions. If multiple variants seem equally suitable or a choice could disrupt established hierarchy, ask the owner before implementing.

| Hierarchy / role | Existing variant | Typical use |
| --- | --- | --- |
| Primary conversion | Solid Orange53 / button-primary g-92745fa, #F05A29 | Call Now, Request Service, principal Hero and final emergency/conversion action |
| Supporting conversion | Orange Outline100 / button-outline-orange g-563da68 | Contextual contact/consultation when appropriate among surrounding actions |
| Supporting conversion, contextual alternative | Solid Blue56 / button-secondary g-e47e377, white text | Residential assessment CTA after six Orange Outline service cards: distinguish the section action from a seventh card action |
| Navigation / exploration | Blue Outline59 / button-outline g-b5f3969 | View Projects, Explore Services, View All Service Areas, Learn More |

Preserve destinations, sizing, typography, spacing, radius, native hover and keyboard focus. Reuse existing Button components/established variants; do not create a new component, duplicate Global Class or custom CSS for a variant choice. Verify contrast on actual light/dark backgrounds. Do not automatically replace approved dark-surface/white-outline compositions. Context may justify an existing alternative while preserving the action's logical role.

**Current Residential correction:** Discuss Your Home Restoration uses existing Solid Blue styling with white text. All six service-card Orange Outline actions remain unchanged. Its native Internal URL still targets Request Service492. The temporary Orange Outline assessment treatment is superseded by this explicit owner refinement.

**Exact implementation/necessary native exception:** existing Image + Text77 root62ef2b5 → Container5a2d7f63 → Layout239b4748 → Copy6bec24a (Heading12670ce8→71, CTA77a9e83d) and Image5222447. CTA is a native Atomic e-button using the existing button-secondary class, with the existing77 cta_text/cta_link Overrides. Shared Button53/56/59/100 definitions and shared Global Classes are unchanged. Existing56 cannot be placed unchanged here: its class globally hides buttons at≤1024px and forces nowrap. Therefore this one77 action has native local style e-536d7b45-aba6: display inline-flex at desktop/tablet/mobile and white-space normal. No custom CSS, new Global Class or new library Component; the native override keeps the existing variant visible and its long label wrapped. This is an instance-specific visibility correction, not a new visual button style.77's other styles and seven public Overrides remain. Residential484/26c8a5b5 is its only published Page consumer found; Draft Style Guide50 inherits the same section pattern.

**Verification:**393/768/1440px authenticated frontend: solid navy rgb(26,50,125), white text, same /service-request/ URL, all six Orange Outline service actions, no horizontal overflow. Padding16px24px, Montserrat600/16px,8px radius; height52.53px desktop/71.73px naturally wrapped mobile/tablet. Keyboard focus retains navy outline and white halo. White/navy contrast is about11.7:1. Existing shared hover rules retained; no physical-device or screen-reader certification. Orange Outline elsewhere still uses #F05A29 on white (~3.39:1), below AA normal-text4.5:1; do not claim site-wide contrast compliance from this correction.

Edit [Image + Text77](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=77&action=elementor). Recovery: return this native action to the previous existing Orange Outline class and remove its native display/wrapping override; retain label/link Overrides and the component. Clear Elementor Files & Data and SG Cache. E82 changes no BEAF records or production. Separately requested Homepage caption3a39c79b now reads Water Damage Restoration — Glenview, IL; no photo/slider change.


**Current E78,2026-10-21:** Residential484 main content headings now follow01–07 using existing Section Heading71/styles and shared section content Overrides. Optional empty-default eyebrow added to existing71 and forwarded by77; Homepage visible headings unchanged. Homepage Residential card4c8810dc now binds to native InternalURL Page484; existing menu109 already references that Page. No new classes/Components/custom code/dependencies or URL changes. Seven-width heading tests and real card navigation pass. [Exact owners, checks and rollback](components/residential-services.md#e78--numbered-heading-consistency-and-native-residential-entry-link).

**Current E77,2026-10-21:** Residential Services484 is a completed nine-section Atomic service hub. Existing Homepage designs promoted once into shared How We Work1152, Why1149 and Service Areas1140 and placed on both Pages; residential content uses Overrides. Existing CTA80/Code847 now share video/radius behavior;590 shares touch timeline animation. No new Global Classes/Variables/plugins/dependencies; three actual shared definitions,52 Page nodes/no new local Page CSS. Header/Footer/Core/BEAF unaffected.93 Pages88 Published/5 Draft;321 URL records preserved. Seven-width browser tests pass; anonymous403, editor loading and rendered meta-description remain explicit limits. [Exact owners, reuse, evidence and rollback](components/residential-services.md).

**Current E76,2026-10-21:** Projects now links to real structural Page1132 `/portfolio/`, with native All Projects / Before & After dropdown. Existing13 project records/URLs untouched. Standard-grid five-item Header and utility Partner Programs retained.93 staging Pages:88 Published/5 Draft;321 migration rows. No new E76 CSS/JS/classes/plugins/dependencies. [Exact storage, checks and limitations](audits/2026-10-21-projects-navigation.md).

**Current E75 (includes pending E74 sync), 2026-10-21:** Staging structural publication:92 Pages,87 Published/5 Draft;84 newly published approved targets including Resources1007,51 city Pages and Partner982–986. Native shared Single Page1008 supplies79 structural placeholders. Final service-first Header113:five main sections (Residential/Commercial/Service Areas/Projects/About), utility Partner Programs with four children/Careers/Contact Us; Blog and Our Team await real staging destinations. Standard1200px grid/logo sizes retained, native toggle below1200, one complete mobile menu. No production/BEAF/Footer/Homepage-content/903 edits.321 canonical migration rows preserve prior source mappings/decisions. [Exact storage, tests, limitations and rollback](audits/2026-10-21-staging-structure-and-navigation.md) · [Actual hierarchy](SITEMAP.md).

**Current E71 (after E70 approval), 2026-10-20:** Main Homepage154 Hero a62cdd3 now uses the approved navy split layout and the FIRST existing BEAF723 comparison in visual484c13ec → Shortcode30e0c45, `[bafg id="723"]`. Native layout, copy, CTA overrides and 8px corners retained. One local wrapper Custom CSS rule hides only its fullscreen button; plugin image-link/zoom is already disabled. All three original comparisons and their fullscreen remain unchanged. E70 removed all old local panorama/technician backgrounds and retired unused, empty hero--panorama g-708f717 after a site-wide usage scan (111 classes/36 variables). Draft970 and Media973 retain the static design experiment. No new class, Variable, library Component, JS, plugin or dependency; no Header/Footer/Core/903/production edits. [Current exact owners, QA and rollback](components/hero-main-beaf.md).

**Historical E69 (superseded by E70/E71),2026-10-20:** Separate **Draft Page970 — Hero Concept B — Restoration Transformation**, root78418107, duplicates the source12-node Atomic structure with fresh IDs and existing286/53/103 instances. New illustrative Media973:1440×1080 WebP/250,828bytes. Native navy split layout, copy/CTAs first on mobile/tablet,8px visual corners; Canvas/Hide Title isolates preview. No new classes/Variables/library Components/custom code/dependencies. Existing Homepage Hero remains active; only separately owner-requested project&nbsp;information wrapping changed in154/7de610a7. No Header/Footer/BEAF/production edits. [Preview, exact owners, QA and activation/discard](components/hero-concept-b.md).

**Historical E68 (superseded by E70),2026-10-20:** Homepage154 Hero a62cdd3 uses supplied Media961 and native brand-navy gradient layers. Local e-7cfcd182-d44a owns bounded1440px canvas/+80px center offset/top framing and responsive75%/80% cover composition CSS. Old hero--panorama detached, definition retained. Tablet native single-column/max600px copy; mobile placeholder hidden;12 nodes/content/links retained. No new class/Variable/Component/JS/dependency; one requested image asset. Footer/Header/Core/903/BEAF/production unchanged. [Exact owners, saved values, nine-width QA and rollback](audits/2026-10-20-hero-technician.md).

**Current E67,2026-10-20:** Footer114 preserves approved desktop geometry; mobile source/visual order is Identity → Contact → Services, with44px compact service rows. Tablet identity/contact share the first row and two-column services the second; cities use4 tablet/2 mobile columns. Copyright/full Back to top share a mobile row with13px type and44px action height. Native controls/existing g-aca1669 reused;36 nodes/112 classes; no new Component/Variable/JS/plugin. Three minimal local CSS gaps: city separator hiding (tablet), top-link nowrap and copyright balanced wrapping (mobile). All corresponding service pages remain Draft, so no invented links. BEAF/Header/903/Core/production untouched. [Exact owners, links, six-width QA, limitations and rollback](audits/2026-10-20-footer-responsive.md).

## Compact footer and restrained comparison controls — E65–E66

Native brand block7ac91d92 uses24px space-md gaps at all breakpoints.

Global Footer114 now has compact direct icon/value contact rows with8px native parent gap, equal-height services/contact columns on desktop, and one native Social Icons widget734b137 under the brand intro. Removed repeated emergency strip671c4f66, six unnecessary contact label/wrapper nodes, and the coverage top divider. Existing5a520a4e becomes ↑ Back to top (#top). Coverage list/copyright/top link use existing color-border #CBD5E1; headings remain white. Native responsive grid1fr/1.1fr/1.1fr desktop, two columns/tablet contact span, one column/mobile. New native icon class g-c2210fa plus SVG935/936/937;112 Classes/36 Variables/36 saved footer nodes. One added footer-root social focus rule; no new Component/JS/plugin. Exact owners, sources, links, verification and rollback: [E65 audit](audits/2026-10-20-footer-contact-icons.md).

New gcpro-footer-contact-icon g-c2210fa owns native20px/accent/no-shrink styling; Custom CSS=null. Existing icon-svg has different shared size/color consumers, so this avoids three independent copies. Existing footer-item gains native16px gap/center alignment for Flexbox rows. Three matching decorative SVGs935/936/937 use currentColor and no IDs. Native Social Icons20px glyphs/44px targets/8px spacing, white on white8% background, orange hover. Footer root supplies orange keyboard focus. Muted footer #CBD5E1 is existing color-border token; darker text-muted is unsuitable on navy. BEAF presentation lives only in Kit6 global Custom CSS; see [E66](audits/2026-10-20-beaf-presentation.md). No new Variables/Components/plugins/libraries.

## Footer hierarchy and separated rows — E64, 2026-10-20

Added **gcpro-footer-link / g-373d928**: native quiet white44px footer actions/body typography/underline hover, replacing repeated local action styles; no class Custom CSS. Added **gcpro-footer-item / g-aca1669**: shared8px row padding and white16% bottom divider across six service rows and two contacts; only border style/color remain converter CSS. Row modifier precedes link class in priority.111 classes/36 existing Variables; no new Components/dependencies.

Existing103/286, palette and spacing reused. Footer114 local native grid/spacing/20px headline/copyright controls create four clear areas and a quieter contact prompt below the unchanged primary page CTA. Root-scoped state rules override verified blue theme/shared103 hover/focus: white text11.69:1 on navy, orange indicators3.45:1. Avoid normal orange text on navy at3.45:1. [Exact owners, scopes, complexity review and tests](audits/2026-10-20-footer-refresh.md).

## Smart navigation additions — E58, 2026-10-20

Six Global Classes added (103→109): gcpro-smart-header, gcpro-cta-origin, gcpro-mobile-cta, gcpro-mobile-cta__label, gcpro-sticky-intro and gcpro-cta-off. Only panel/label own new visual native controls; other four are empty semantic hooks. Existing36 Variables, palette/fonts/spacing and103 button reused. One reusable Atomic Component895 added; no new button definition. [Exact class IDs, native values and two narrow Custom CSS exceptions](components/smart-navigation.md), [saved native snapshot](audits/2026-10-20-smart-navigation-classes.json).

## Phase 1 class cascade cleanup — E57, 2026-10-20

[Exact class IDs/variants and removed declarations](audits/2026-10-20-phase1-cleanup.md). Ten existing classes retain final effective values and all native design controls;20 superseded Custom CSS declaration occurrences removed. Added one Global Class **gcpro-homepage g-d0c199c**, a visual-neutral scope on Homepage154/main46c3aad4, taking the E56 identity count102→103. Existing class priority is unchanged. No new Variable or design token. The menu marker gcpro-menu-item--header-hidden belongs to native WordPress Menus, not Atomic. BEAF overrides remain untouched intentional third-party exceptions.

## Current ownership and mobile refinement — E56, 2026-10-20

Use [component records](components/README.md) for editing/reuse and [CUSTOM_CODE](CUSTOM_CODE.md) for every active custom CSS/JS owner. The global palette/typography/spacing system remains unchanged:36 variables and102 class identities at this task's discovery; no additions.

Core B's unique intro6cb38139 keeps local native responsive ownership: desktop sticky96px/tablet static/mobile sticky0px,z-index9999,opaque color-surface-alternate. **Mobile padding now space-sm16px top/bottom,0 horizontal**, verified in native Spacing controls; no intro Custom CSS. Do not put this one-off sticky rule on shared stack/container or create a redundant class.

The [live CTA experiment847](components/final-cta.md) overrides native mobile gutters/radius/padding at runtime. Native80/default styles alone do not describe actual frontend appearance. This staging experiment is an explicit code exception, not a new design-system convention.

Fresh class CSS inspection found historical repeated/overridden declarations in navigation/header/utility/button classes; preserve working cascade until a consumer-aware cleanup is approved. Avoidable authored IDs and local/vendor exceptions are inventoried rather than blindly removed. New native spacing reuses an existing token, introduces no parallel values, wrappers or active source mirror.

## Current saved-state qualifications — E55, 2026-10-19 Chicago / 2026-10-20 UTC

[Read-only audit](audits/2026-10-19-elementor-state-sync.md) preserves all existing native/token/class ownership and scoped exceptions. Fresh variables still number36 (Montserrat headings, Inter body, navy #1A327D, orange #F05A29, surface-alternate #EFF6FF); class resource returns102 identities/order only, not declarations. Earlier class counts are dated baselines.

**Core B local responsive exception:** intro6cb38139/style e-67ba0794-7b2b is now sticky96px desktop, static/auto tablet, sticky0px mobile with z-index9999 and background var(--color-surface-alternate). The local mobile background resolves to opaque #EFF6FF; no local opacity reduction is returned. Full computed opacity, Header stacking and scrolling remain untested. This supersedes the mobile-static description in E44/E45, without adopting a new sitewide sticky rule or changing any style.

E54 remains current for the Final CTA radius-only Homepage rule and WHY H2/body inheritance. E53 orange panel and E52 placeholder testimonial-card treatment are historical: current Testimonials contains shortcode02441ff. E54's Trustindex/Poppins exception still needs a source/typography decision; its current plugin settings were not exposed.

Uploaded CTA video846 is an unplaced experiment; no video widget is saved in Homepage154/CTA80. No approved mobile corner-video/full-width CTA pattern is established by this audit. Hero background/hover class rules, BEAF page CSS and process Code590 deployment equality were not reverified through the limited read API; source mirrors are not separately enqueued proof.

## Provisional WHY editorial styles — 2026-10-19, E52

These three new Atomic Global Classes are scoped to the four benefits on staging Homepage154's WHY section and await final visual approval. They are not a mandate to restyle other sections.

- **why-benefit / g-9bf65cb**: repeated native grid with56px number track, flexible content,16px gap and24px padding; mobile48px number track and24px vertical/zero horizontal padding. Thin white22% dividers are local to the required grid edges. Existing classes did not provide this numbered editorial arrangement. Minimal scoped `& svg { fill: none; }` preserves outline details of existing attachments that otherwise render as solid shapes.
- **why-benefit-number / g-046e833**: Montserrat700,36px desktop/tablet and32px mobile, line-height1, white28%, nowrap so01–04 never split. Existing general number styles target other sections and were not changed.
- **why-benefit-title / g-48d2a32**: Montserrat600,20px/1.3, white, natural case; reused by all four benefit titles. Existing generic heading defaults have different size/case.

Edit these in Elementor Design System → Classes. Native Variables supply navy#1A327D, accent#F05A29, text#334155, white, surface-alternate#EFF6FF and spacing. Existing Global Class definitions unchanged; no new Variables, Components or dependencies. H2 accents match the current Homepage40×3px orange/16px below-heading treatment. On light surfaces use standard dark text for H2; on navy use white. Testimonials reuses existing testimonial-card styling with local white surface,8px radius and no shadow. No universal testimonial/carousel pattern is approved by this task.

## Shared BEAF expand-button treatment — 2026-10-19, E51

Approved native BEAF expand button treatment: white20px SVG;36px translucent black48% button;4px radius; no border or shadow. Hover/focus darkens to68% over160ms, without scaling or movement. Keyboard focus has a2px white outline/3px offset; one outline !important counters BEAF's native important focus reset. Mobile≤767px/coarse pointer uses44px touch targets. Reduced motion disables the transition.

One owner: Homepage154 → Page Settings → Advanced → Custom CSS, alongside the unchanged E50 label rules. Selector uses BEAF classes and the homepage body scope, not individual slider IDs; future Homepage comparisons inherit it automatically. Native plugin controls provide functionality/SVG; the existing inspected BEAF settings expose no shared expand-button styling control. No new Global Class, Variable, Component, JS/PHP, theme stylesheet, plugin or dependency.

This is a reusable treatment implemented on Homepage154; other pages require explicitly extending the approved scope once they exist. Do not copy the CSS into each comparison or modify the native SVG/behavior. Remove only the E51 block to roll back.

## BEAF labels in inline and expanded views — 2026-10-19, E50

Homepage 154 uses one central BEAF label rule set in **Page Settings → Advanced → Custom CSS**. This supersedes the storage location of E48's grid-local exception, while preserving its inline appearance exactly: 9px Inter, 60% opacity, transparent background, 8px top inset and subtle dark text shadow.

Expanded BEAF popups require a distinct readable variant: 11px Inter, white text at full opacity, 55% black translucent background, 3px vertical / 7px horizontal padding, 18px line-height, .08em letter spacing, 2px radius and 12px top inset. AFTER is 48px from the right to avoid the native close control. White navigation handles and slider settings remain native BEAF record values, unchanged by this rule.

The exception is necessary because BEAF mounts its popup under body, outside the Atomic section; section-local classes cannot style that portal. Scope is body.elementor-page-154 plus the existing grid ID for inline labels or .bafg_popup_preview for expanded labels. No global brand tokens, Global Classes, Components, JavaScript, PHP, theme stylesheet or plugin settings were added. Keep this single rule owner; do not copy it into each BEAF record. It applies to future Homepage comparisons in the same integration, not automatically to other pages.

Rollback and exact element ownership are recorded in the E50 Elementor map. Native popup dimensions/scrollbars and keyboard handling are plugin behavior outside this label-only exception.

## BEAF label exception — 2026-10-19, E48

Unique OUR WORK section exception on staging154, authorized by the BEAF integration request and subsequent explicit label feedback. No new reusable brand rule or Global Class. Layout, typography for project captions, gaps and3/2/1 breakpoints use native Atomic controls/defaults/tokens. BEAF's native options own images, orientation/offset, orange divider and disabled automatic effects.

**One owner:** Project grid66b1c7d4 → local e-50f5e7b2-899b → Custom CSS. Applies only to BEAF descendants of that grid (currently723/742/767). Native BEAF has no observed control for persistent, compact, text-only labels; its default labels are hover-only with colored backgrounds. The owner explicitly requested barely noticeable labels without blue boxes.

The scoped block sets BEFORE/AFTER label opacity0.6; pseudo-labels use font-body/Inter,9px,0.08em tracking,18px line height,0 padding, top8px/margin-top0 and a restrained0px1px2px rgba(0,0,0,0.5) shadow. `background:transparent !important` is the single narrow specificity exception: BEAF emits label backgrounds with !important. Native BEAF label text color is white. No other !important escalation or per-slider copied block. Do not move these rules into the theme or enqueue a parallel stylesheet.

Small/faint text is an owner-selected secondary visual indicator; image alternative text identifies before/after. Do not claim label contrast or full slider accessibility conformance: installed BEAF handle is nonfocusable and lacks keyboard range behavior. No custom JS was authorized/added to emulate it. Autoplay/on-scroll/hover-follow are off; comparison movement is deliberate mouse/touch input. Native keyboard enhancement remains a vendor follow-up.

Rollback: remove only this grid-local descendant block to return default BEAF labels, keeping native grid/breakpoint declarations. Change source photographs/settings in BEAF records, and captions in their native H3/P elements; do not edit shared cards or Core/Service Areas classes. No new class, variable, Component, CSS file or theme layer.

## Audience-card hover recovery — 2026-10-19, E47

Supersedes E31's reduced-motion limitation only; original normal-motion design remains. **Editing owner: Global Class audience-card g-38b29fb → desktop/normal → Custom CSS**, exactly two154 consumers4c8810dc and2066a26. Retain native layout, border/radius/surface and280ms border transition; card-action g-a5c0d65 keeps280ms background transition; audience-card__image g-77c2a17 keeps280ms transform transition.

Recovered E30/E31 fine-pointer behavior: whole-card hover → image scale1.025, circle color-accent orange with white SVG, border color-mix35% primary against color-border; no card translate/lift/shadow or layout change. Existing original rule was present but gated off when actual browser :hover=true and media hover:none/pointer:none. CSS gate now accepts either original fine-hover or the none/none compatibility case; coarse-touch remains excluded. Source of browser capability mismatch remains unknown.

One existing class-owned scoped block is retained because native parent self-hover cannot style the descendant image/action. &:is(*) identity nesting preserves media queries through this installed Atomic converter; it adds no specificity. Reduced-motion block now includes &:hover .audience-card__image with transform:none to resolve E31's specificity defect, plus0s transitions on card/action/image. Focus-visible orange circle and existing native outline retained. No per-card copies, new classes/Variables/Components, code files, JS/PHP, dependencies or theme rules. [Canonical mirror](../integrations/audience-card-hover.css) stays non-enqueued.

White audience section is a separate owner-approved native local background-color:var(--color-white) on7b416658, not a palette/shared section--light change. Native Global Class properties and every other class match prechange. Rollback: restore previous Custom CSS from commit286a2553d0ac5420cffadd287bbf74f84d8c6b9f/source mirror, then native save/publish/cache purge/retest; remove only7b416658's local background to recover light blue if explicitly requested. Never delete classes/shared images.

## Numbered section eyebrow pattern — 2026-10-19, E46

**Editable owner: Atomic Global Classes → section-eyebrow (g-b12aa04).** One reusable native class for the six Homepage154 labels, based on the existing Core B02 reference. No per-element copies or Custom CSS.

| Native property | Approved value |
| --- | --- |
| Font family | Existing font-body / Inter (e-gv-c82d6d2) |
| Weight |600 |
| Font size |12px |
| Line height |1.5 (18px) |
| Letter spacing |2px |
| Color | Existing color-text-muted #5B6575 (e-gv-bce0476) |

Use a non-heading Paragraph/P with the exact numbered text; no additional H1/H2. Existing parent stack alignment supplies left alignment and existing gaps24px desktop/tablet,16px mobile. No extra margin/padding or underline added to labels. Existing H2 accents, sizes, descriptions and backgrounds stay intact. On Why GCPRO's navy surface, the existing section--dark paragraph rule supplies white for contrast; preserve that contextual exception without a competing local override. Hero and CTAs/Header/Footer/Testimonials are excluded.

**Related owner color correction:** Core Services H2 1aa0cb69 uses existing color-text #334155, the normal dark heading color, rather than navy. This is a single element's native token selection, not a new reusable heading class or palette change. Existing Montserrat70040/36/28px and1.15 line-height retained.

Saved class has six native properties, Custom CSS=null. All six labels are18px high, single-line and aligned at1440/840/390; no overflow. No new Variables, Components, JS/PHP, style files, plugins/dependencies or theme rules. Existing process ripple, Core row arrow/sticky and Service Areas hover/focus/reduced-motion ownership remains unchanged.

## Approved Core Services arrow motion — 2026-10-19, E45

B3fd180bb is now the approved main Core Services section; E44's experimental/no-motion status is historical. Native Template703 archives original A, including shared styles and Components; no global palette/font/breakpoint/card rule was redesigned.

Reused Service Areas' established200ms/default-ease color+transform transition and0.2rem(3.2px) horizontal motion. **Did not apply or modify city-link:** its pseudo-arrow/layout/divider properties would conflict with B's existing native arrow span and grid. No new Global Class or duplicate arrow markup. Existing class consumers checked: core-b-row g-d37a353 and core-b-arrow g-c3123c0 each have six B-only page consumers.

- **Global Classes→core-b-arrow→desktop base→native Effects/Transition:** color0.2s, transform0.2s. Existing font/size/alignment/color inheritance and mobile variant unchanged; Custom CSS remains null.
- **Global Classes→core-b-row→desktop base→Custom CSS:** retains E44 focus outline2px navy/4px offset; adds `&:hover > .core-b-arrow { transform:translate(0.2rem, 0); }`, focus-visible orange row color and same direct-arrow transform. The installed converter cannot map parent-state descendant selectors to native child controls, so this small section-scoped fallback is necessary. Native row hover color already supplies orange via inheritance; no per-row CSS copies.
- Reduced-motion uses the previously verified nesting approach: `&:is(*) { @media (prefers-reduced-motion: reduce) { & > .core-b-arrow { transition:none; transform:none; } &:hover > .core-b-arrow { transform:none; } &:focus-visible > .core-b-arrow { transform:none; } } }`. Top-level arbitrary media-query conversion is unreliable on this installation. Colors remain visible; movement/transition stop.

Native layout/sticky/spacing/typography/icons/links and all saved element settings are unchanged. No background fill, shadow, scale or row layout shift; only arrow visual position changes. All six desktop rows produce orange/matrix3.2px hover; intermediate entry samples and return to navy/no transform verified. Reduced motion: all six0s/no movement. Focus outline/color/motion verified through forced pseudo-state; actual keyboard link activation remains pending real destinations, with no fake focus stops added.

Complexity audit: only two existing classes changed; no new class/Variable/Component/code file/JS/PHP/theme/plugin/dependency. One native archived Template is required for recovery, not a parallel styling system. Other class definitions compare unchanged after loading archive dependencies. [Archive name/703, reuse test, IDs, link register and rollback](ELEMENTOR_MAP.md#approved-core-services-and-original-template-archive--2026-10-19-e45).

## Experimental Core Services B — 2026-10-19, E44

Section-local experimental pattern on staging154/B3fd180bb; not a replacement of approved A or a new site-wide design rule. Existing palette/fonts/Variables/tag defaults/breakpoints and class definitions/order unchanged. Reuses section, section--light(#EFF6FF), container, stack, stack--compact, layout-reset, text-muted and icon-svg.32px approved SVGs596/597/607/599/600/601 use existing icon-svg fill:none rule. No duplicated icon system.

| New class (six B-only consumers each) | Native ownership / present gap |
| --- | --- |
| core-b-row g-d37a353 | Editorial grid40px/minmax(0,1fr)/24px with24px gaps and24px vertical padding; mobile32px/minmax(0,1fr)/20px with16px gaps and22px padding. Native1px bottom border, navy color, orange hover/active. Existing city-link has a pseudo-arrow/motion and incompatible spacing; existing cards introduce unwanted surfaces/borders. |
| core-b-title g-757705e | Montserrat700,24px desktop (current tablet default renders22px),18px mobile,1.3 line height, inherited row color, unchanged case. Existing text classes do not provide this title role. |
| core-b-description g-6bb05c4 | Inter16px/1.6 muted;14px mobile, short two-line copy at390/375. Existing text-meta lacks this mobile size. |
| core-b-arrow g-c3123c0 | Native span arrow,24px/1.3 desktop20px mobile, inherited row color, vertically centered. Existing card-action supplies an unwanted circle/background. |

Unique section layout controls remain local: desktop0.9fr/1.4fr columns,80px gap, sticky introduction top96px; native tablet max1024 uses one column/gap40px/static intro; mobile gap24px. Header H2 is40/36/28px; orange native e-divider40×3px; intro18/16px with text-transform:none to offset text-muted's existing uppercase setting. No shared class edited to accommodate B.

**Only new scoped CSS exception:** Global Classes→core-b-row→desktop base→Custom CSS: `&:focus-visible { outline:2px solid var(--color-primary); outline-offset:4px; }`. The installed converter stores this unsupported state/outline as fallback; all row border/layout/hover/active and the other three classes are native with Custom CSS:null. No theme/JS/PHP/custom code entry. No transforms/transitions/animations are used; reduced-motion has no movement to suppress. Color changes use inherited native row state, not per-element CSS.

Pending rows are noninteractive articles with no href/tabindex; focus-visible is prepared for valid future row anchors. Forced-state rendering confirmed2px navy outline/4px offset; actual keyboard activation and mobile touch-action feedback are deferred until valid routes exist. Emulated touch on current article did not produce :active/navigation; do not call it a functional link. No dead links or fake focus stops added.

Complexity audit removed temporary core-b-icon g-b11c23f in favor of existing icon-svg and removed redundant cursor fallback declarations from B classes/local text. Four retained classes solve actual sixfold repeated styling; one copy wrapper groups title/description and avoids extra card wrappers; no new Component/Variable/plugin/dependency. Before/after saved comparisons confirm all original sections and existing classes unchanged. [Structure, pending-link register and recovery](ELEMENTOR_MAP.md#experimental-core-services-b--2026-10-19-e44).

## HOW WE WORK hover compatibility — E43

2026-10-19: existing approved E16/Code590 CSS exception adds a hover:none/pointer:none compatibility branch after a verified Chrome :hover/media mismatch. Original fine-pointer desktop and coarse-touch mobile behavior retained; no native style or class changes. Ring creation/pulse still requires no reduced-motion preference; actual :hover remains the trigger. Same2px rings/1000ms,160ms delay,scale1→1.55/fade0.55→0 and1160ms number-color synchronization. Exactly three media-query lines in the existing deployments/canonical mirrors changed; no new CSS system, file, keyframe or JavaScript. [Evidence, native-first rationale, editing and rollback](milestones/2026-10-16-process-ripple.md#e43--pointer-capability-compatibility-restoration-2026-10-19). Browser reason for reporting pointer:none and physical/anonymous acceptance remain unverified.


## CSS architecture policy — 2026-10-19, E41

This is the agreed policy for future authorized styling work. It does not migrate existing styles or authorize changes to the website.

| Priority | Layer and responsibility | Use boundary |
| --- | --- | --- |
| 1 | Native Atomic controls and approved Variables | First choice for layout, spacing, typography, color, border, responsive rules and supported states. Reuse the current design tokens. |
| 2 | Reusable Global Classes | Own real repeated styling patterns. Inspect/reuse an existing suitable class, its priority and consumers before adding one. Keep supported properties in native class controls. |
| 3 | Minimal scoped Custom CSS in Elementor | Only for a demonstrated native capability gap. Prefer one class-owned exception for a repeated pattern; keep a unique exception local. Document exact location, scope, reason, approval and rollback. |
| 4 | Theme stylesheet | Only genuinely global technical rules that cannot be managed cleanly through Elementor, within separately authorized theme/deployment scope. Section-specific repetition does not qualify. |

The styling mechanism and scope are separate decisions: a Global Class should still use native properties wherever possible, with only its unsupported remainder in Custom CSS. A raw CSS string accepted by the connector is not proof that everything became native controls; the converter may split native properties and Custom CSS or omit unsupported input. Inspect the saved output and actual editor/render before claiming native editability or successful implementation.

Use one authoritative owner per property/state/breakpoint. Inspect HTML defaults, class priority, local overrides and existing exceptions before writing. Avoid duplicated per-element CSS, equivalent classes, redundant overrides, specificity escalation, unnecessary `!important`, broad selectors and parallel Elementor/theme styling systems. Inheritance can coordinate child text with a row state. State overrides and responsive differences that implement a real requirement are not automatically redundant. Reuse approved colors/spacing rather than introducing parallel tokens; a single scoped tint need not become a new global Variable.

Preserve approved visual results. Working Custom CSS may be the simplest maintainable solution; do not replace it merely to reach zero CSS, create a Component just to centralize styling, or relocate a page interaction to the theme. Assess each historical exception in its actual scope. A refactor must have a concrete benefit, approval within task scope, scoped recovery and comparison of saved values, responsive geometry, hover/focus, reduced motion and affected consumers. Repository source mirrors are documentation/recovery sources unless explicitly deployed; never load them in parallel with their active Elementor rules.

### Service Areas consolidated styles — 2026-10-19, E42

Owner approved a small staging-only maintainability refactor after E41. This supersedes E40's per-element style ownership and resolves E41's proposed consolidation; approved appearance/behavior is unchanged.

| Resource | Current ownership and consumers | Native vs necessary CSS / editor location |
| --- | --- | --- |
| Existing city-link g-9a26448 | All12 city-row anchors in Homepage154 → Service Areas7d8c17ad → d6dbbe2. Before reuse, its variants were empty, the all-page usage scan reported no consumers, and all16 active Component definitions were separately checked with no references. | Native min-height, navy color, no underline, padding, radius, transparent background, flex layout/gap/alignment and orange hover color. Existing border/transition/::after/focus-visible/reduced-motion fallback is now owned once by this class. Edit row → Style → city-link; unsupported remainder in that class's Custom CSS. |
| New city-link__text g-efb17e3 | All12 existing city-name paragraphs on154 only. One class is needed because existing text-meta/text-lead/text-emphasis definitions do not match18px/500 Inter, inherited row color and17px mobile. | All properties native, Custom CSS:null on desktop/mobile: font-body,500,1.125rem,1.5 line height,color:inherit,cursor:pointer; mobile1.0625rem. Paragraph zero margin now comes from native paragraph defaults. Edit label → Style → city-link__text. |
| Existing city-links g-6ebef89 | Empty and unused; left unchanged. Grid d6dbbe2 retains its existing native local3/2/1 layout. | No class attached/redefinition/cleanup merely for naming symmetry. |
| Existing approved buttons | Navy Component59/2b5f493 and orange outline5350691e/g-563da68 unchanged. | No shared button definition or local geometry changes. |

Cleared local styles on all24 row/text nodes (previously8 repeated row and8 repeated text style IDs across12 pairs). The connector retains inert local ID references in settings, but saved styles arrays are empty; no local declarations remain on these24 nodes. Removed only the redundant &:hover transparent background and explicit paragraph margin:0. Preserved native dimensions/typography and the existing border/transition/arrow/focus/reduced-motion rules verbatim otherwise. Necessary fallback was centralized, not expanded into a second implementation; no theme stylesheet, Custom Code entry, JavaScript/PHP, Component, Variable, plugin or dependency added. Only one Global Class added; only the previously empty city-link definition changed among existing classes, with their relative order preserved. Final page usage scan reports exactly12 row/12 label consumers on154 and no other pages.

Verification: captured pre-change saved-main/class snapshots and1440/840/392 CSS-px screenshots/measurements before writes. Saved-main comparison: exactly24 nodes changed only style/class ownership; same IDs, content, links, other settings, grid, heading/intro, buttons and all outside-section nodes. Global-resource comparison: only city-link changed plus one appended text class. Regenerated native Elementor rendered assets. At1440/840/392, before/after computed properties, node geometry (0.03px comparison tolerance), text and href checks returned no differences; screenshot views inspected, no page horizontal overflow. Real blank-space row hover and real Tab focus states match baseline exactly, including orange text/arrow/divider,3.2px/200ms and navy focus outline; emulated reduced-motion focus matches baseline and all12 rows have0s transitions/no arrow transform. Checks used authenticated frontend/browser emulation; anonymous/incognito, physical devices, screen reader, performance and full-site restore were not tested.

Recovery: restore only24 prior local styles/class assignments from the private before snapshot, reset g-9a26448 to its prior empty definition, detach/remove the new text class only after checking consumers, regenerate cache and recheck. Snapshots are scoped recovery aids, not a tested full-site backup. No unrelated shared resources or production writes. Existing city/SEO/coverage approval, pending staging destinations and ZIP popup/functionality remain outstanding; no route activation occurred.

### Service Areas CSS audit — read-only, 2026-10-19

**Source/scope:** fresh existing GCPRO Elementor MCP saved-tree read of staging Homepage154 → Service Areas7d8c17ad → grid d6dbbe2, plus active Global Class registry. No website write, cache purge, publication, theme edit or runtime test was performed in this audit. E40 records the prior hover/render tests; they were not repeated here. The round-trip `styles.css` combines native properties and fallback CSS, so its length is not a count of handwritten Custom CSS or emitted stylesheet bytes.

| Finding | Evidence and implication | Disposition |
| --- | --- | --- |
| Confirmed repeated local row pattern | All12 row nodes expose byte-identical style strings across8 distinct local style IDs; the four later city duplicates reuse4 of those IDs. The repeated pattern includes the pseudo-element arrow, transition, hover/focus-visible and nested reduced-motion exception. There are not12 independent definitions. | Maintenance/drift risk. A scoped reusable row class is a possible simplification, subject to inspecting existing class definitions/consumers and preserving the approved result. No consolidation performed. |
| Confirmed repeated text pattern | All12 paragraph nodes expose byte-identical typography/inheritance strings across8 local style IDs. The native paragraph default already supplies margin:0; the local pattern repeats it. | Optional consolidation/native inheritance review alongside the row pattern. Do not mislabel ordinary Atomic local typography as entirely Custom CSS. |
| Confirmed redundant state declaration | Each row sets background-color:transparent normally and again in &:hover. The hover value adds no change relative to its own normal rule. | Small cleanup candidate only; preserve the white/no-fill result and check the cascade before removal. |
| Necessary current exception, not an automatic removal target | The existing arrow uses ::after; focus-visible and reduced-motion behavior share its local fallback. E40 records the connector dropping a top-level arbitrary media query and retaining the nested &:is(*) form. | Preserve working accessibility and motion behavior. A converter limitation is not proof that every native editor control lacks that capability; recheck installed controls before a future refactor. |
| Potential cascade complexity, not a demonstrated defect | Row styles mix logical border widths with physical bottom border style/color, and intentionally override native anchor default color/underline/focus. The saved row scopes contain no !important. | No actual broken cascade, layout shift or specificity failure established by this saved-state audit. Do not remove required resets or focus rules as cosmetic cleanup. |
| Existing shared resources are not automatically suitable | Registry still lists city-links g-6ebef89 and city-link g-9a26448. Neither is attached to the current grid/rows. Their definitions and all consumers were not audited here. Current availability button already reuses button-outline-orange g-563da68; the navy action remains Component59. | Do not blindly reattach, modify, delete or duplicate old classes. Check purpose/consumer compatibility first; leave both approved buttons intact. |

Affected rows (current visible labels, not potentially stale Navigator titles):

| Row ID | City | Local row style ID |
| --- | --- | --- |
|52ad5087|Lombard|e-cbe2b79-2354|
|29925a5c|Arlington Heights|e-3efe4b2a-d95e|
|7f8df755|Elmhurst|e-cbe2b79-2354|
|64f07ac9|Naperville|e-6a788526-f201|
|7703752a|Northbrook|e-7db9abd0-5434|
|28cc87b|Downers Grove|e-3efe4b2a-d95e|
|961c608|Oak Brook|e-2ab0b56a-9d98|
|311eade2|Glenview|e-5189acaa-eef2|
|3e9e185f|Highland Park|e-6a788526-f201|
|3478458c|Schaumburg|e-2549be1b-ff4f|
|166c23ea|Evanston|e-5d272d4-73bd|
|5fcaef53|Elk Grove Village|e-7db9abd0-5434|

**Approval-only follow-up:** inspect existing city-class definitions/usages, then assess whether one scoped row Global Class and shared native text styling reduce maintenance without increasing complexity. Move only the genuinely unsupported remainder into the same class's scoped Custom CSS if needed. Preserve3/2/1 grid, all names/pending URLs, typography/spacing, both buttons, whole-row hover, keyboard focus and reduced motion; compare before/after and read saved structures. Do not rebuild the section, alter unrelated consumers or introduce a theme implementation. This audit does not approve that refactor; owner approval is required before Elementor changes. Leaving the working section as-is is acceptable.


## Current Hero blend — E35

Supersedes E34: existing hero--panorama has native right gradient90deg at0/40/65/80/95/100%, navy opacity0/0/0.35/0.85/1/1; native left gradient90deg at0/34/48/65/100%, opacity1/1/0.9/0/0. Media633 remains third layer. Existing centralized Global Class CSS gives both gradients1500px×100%, photograph auto×100%, all centered80px left above1024px; no-repeat applies at all widths. Mobile native opaque navy layer retained. No new class/component. [Exact controls, source mirror, compiler limitation and QA](milestones/2026-10-16-hero-composition.md#e35--extended-soft-right-blend). Earlier E33/E34 settings below are historical.

E34 current native Hero gradient stops:0/34/48/65/**66**/95/100%,90deg. Transparent right fade begins66% instead of82%, extending435px across the same1500px canvas. Image placement, Global Class composition CSS and mobile variant unchanged. Edit the native right transparent stop; no added code/classes/components. [Trial evidence](milestones/2026-10-16-hero-composition.md#e34--longer-right-side-fade-trial).

## Desktop Hero composition — E33

Existing hero--panorama g-708f717 retains native Media633/Full, height100% and horizontal gradient, now with both-side fade. Above1024px a documented Global Class CSS exception bounds the blend1500px, keeps photo auto×100%, positions both calc(50% - 80px) center and disables repeat. This keeps artwork aligned with centered1200px content at1280–2560px. Native gradient UI lacks independent canvas sizing; source mirror integrations/hero-panorama-composition.css is not separately enqueued. Edit colors/stops/photo natively; canvas/offset in that named Global Class's Custom CSS. No top fade/new class/component. Mobile variant unchanged. [Rationale, controls and QA](milestones/2026-10-16-hero-composition.md).

## Desktop photographic Hero — E32

Native hero--panorama g-708f717 supplies Media633/Full background, auto width/100% height, center-right/no-repeat, one horizontal navy fade. No vertical/top fade. Mobile≤767 uses solid navy native layer to replace desktop background; empty native array did not reliably clear inheritance. hero-media--mobile g-02b63b3 hides only the existing placeholder above mobile, native flex below. Existing geometry/tokens/components unchanged; both classes custom_css:null. [Native editing, rationale and evidence](milestones/2026-10-16-desktop-hero-background.md).

## Current audience photo presentation — E31

Existing audience-card__image g-77c2a17 uses native16:9 (supersedes historical4:3 below), same cover/center/full-width rules. Final images1152×648 match the frame with no default composition crop. No new design resource in E31. Existing E30 hover uses native280ms transitions plus scoped parent→child CSS in audience-card Global Class; [exact location, source mirror and motion limitation](milestones/2026-10-16-final-audience-images.md#e30-carryover--existing-audience-hover-documented-without-new-deployment). No theme/shared-repository change.

## Audience photography trial — E28

New native Global Class **audience-card__image g-77c2a17**: display block, width100%, height auto, aspect ratio4:3, object fit cover, object position50%50%. Current consumers: only native Images295bf90e/27ec40d5 on154. All values are native Atomic properties, custom_css:null; no local styles. Existing media-placeholder is a padded/background/bordered flex placeholder, image-led-card styles a parent, header-logo is logo-specific; none fits a full-bleed photograph. This single shared class is required to preserve symmetry without affecting other media. Edit Image → Style → select audience-card__image → Size/Show more for ratio/fit/position. Images themselves remain independently selected in General → Content. Existing audience-card owns24px clipping/corners/border; layout-reset removes obsolete placeholder frame presentation. Classes90→91; Components16/Variables36 unchanged. [Assets, trial/QA and limitations](milestones/2026-10-16-audience-card-images.md).

## Current optional H2 accent — E26

Use section-heading--accent g-a537304 on the existing native container directly holding Section Heading71 (.stack > h2). One scoped GLOBAL class pseudo-element rule adds40×3px/radius2 orange line,16px below H2 via color-accent/space-sm. Apply selectively; current five are Audience/Core/Process/Projects/Areas on154, all start-aligned. No global H2 default or71 definition change. Attach/remove via native container Classes; geometry lives in that selected global class's documented Custom CSS, not local widget CSS. [Canonical mirror](../integrations/section-heading-accent.css) is not separately enqueued; [editing/limits/map/QA](milestones/2026-10-16-section-heading-system.md).

E26 owner correction removes E25's H3 line and copy wrapper from62; retires heading-accent and stack--tight after usage/16-component checks. Global Classes now90, Variables36, Components16. The following E25 description is historical and superseded.

E25: Component62 uses new reusable heading-accent g-01bd1bd (36×3px, radius2px, color-accent) and stack--tight g-19f58a6 (space-xs8px, desktop/mobile) with existing stack. Native copy grouping keeps icon/CTA spacing unchanged and adds only3px mobile height. Classes89→91; no new Variables/Components/code/local styles. Native controls and custom_css:null verified. [Editing/QA](milestones/2026-10-16-service-heading-accent.md).

E24: service-card__icon g-b759e84 native padding10px (previous12), same56px square/14px radius/light-blue Variable/margins; inner SVG36px, +12.5%. No transform/local/custom CSS. B Mold source now spore/cleaning sparkle; same48×48/2.25 stroke, Media607. Other five designs unchanged. [QA and editing](milestones/2026-10-16-icon-refinement.md).

E23: owner selected B; navy/orange service SVGs now applied through existing instance icon Overrides on Homepage154. Media596–601, same badge classes/geometry; no new styles/components/code. Both color channels and intended fills verified in actual frontend. Source-level colors remain explicit; native per-channel color controls not claimed. [Integration/QA](milestones/2026-10-16-icon-b-integration.md).

E22 **proposed, not deployed**: [original Core Services SVG family](../assets/icons/core-services/README.md), A/currentColor outline and B/navy-orange accent.48×48,2.25 rounded strokes, six service meanings per treatment. No new Global Classes/Variables/Components or site code. Use existing SVG Icon Override only after visual approval and native color/instance tests. [Study/QA](milestones/2026-10-16-core-service-icon-concepts.md).

E21 supersedes E19 CTA colors: existing button-outline-orange g-563da68 supplies transparent/orange default and orange/white hover. service-card__action g-d0416c8 keeps compact dimensions/bottom alignment/native200ms transition; its redundant navy color and state overrides removed. Orange Outline unchanged; no new resources/custom code. [Editing, contrast and QA](milestones/2026-10-16-core-orange-cta.md).

E20: Code590 remains Homepage154-only and now includes the color-only `gcpro-process-number` keyframe in existing integrations/process-timeline-mobile.css. Reuses current hover/played triggers and stagger; no JS, theme, global typography or Atomic structure changes. [Source, timing, accessibility and QA](milestones/2026-10-16-timeline-number-color.md).

E19: Global Classes87→89. Existing service-card g-f569734 now controls full bordered surface/card height/padding/hover. New service-card__icon g-b759e84 is the56px SVG badge modifier (priority before icon-svg); new service-card__action g-d0416c8 is the compact Montserrat600 outline CTA/bottom alignment. Three classes use native Atomic properties only, custom_css:null; Variables36 unchanged. grid3 reused without grid--flush. [Details/editing/QA](milestones/2026-10-16-service-cards.md).

## Touch sequence — E17, 2026-10-16

Desktop E16 rules unchanged. On hover:none/pointer:coarse/no-reduced-motion, [mobile CSS](../integrations/process-timeline-mobile.css) reuses `gcpro-process-ripple` with step delays0/400/800/1200ms and second-ring+160ms. It applies only after native Custom Code590's observer sets `data-gcpro-ripple="played"` on the existing root. Before that, no rings are generated. Mobile uses forwards fill so future delayed rings remain invisible. Pseudo-element geometry is explicitly touch-gated because E16's equivalent definitions are fine-pointer-only; no theme refactoring or duplicated base typography/layout tokens. Same2px accent-token rings; no new Atomic Class/Variable/Component. [Controls, native gap and QA](milestones/2026-10-16-mobile-sequence.md).

## Process ripple — E16, 2026-10-16

Supersedes only E15's static hover outline: existing client CSS block now uses `.process-timeline__number::before/::after`, triggered by `.process-timeline__step:hover`, and scoped keyframes `gcpro-process-ripple`. Two **2px** orange rings expand/fade once,1000ms duration/160ms stagger, without transforming the circle. Generation/animation requires fine hover pointer and no reduced-motion preference; reduced motion also disables the existing native background transition. Classes87/Variables36 and Component582 remain unchanged. [Native gap, exact CSS, editing and QA](milestones/2026-10-16-process-ripple.md); no Elementor Custom CSS or shared starter edits.

## Process timeline — E15, 2026-10-16

Current register: **87 Global Classes, 36 Variables**. Four added native classes support Component582: `process-timeline` (`g-a12d836`, four-column zero-gap grid→one column at1024px), `process-timeline__step` (`g-07d3365`, column→row step layout), `process-timeline__number` (`g-e17507d`, 64→56px navy/white circle), `process-timeline__connector` (`g-261ecb6`, 2px horizontal→vertical segment). Existing `process-step-number` provides Montserrat600 24/24/22px; stack/compact/reset and color/spacing Variables are reused. Circle class has priority over existing number typography color; other existing class priority relationships are unchanged.

Base properties and the 200ms background transition are native Atomic Global Class settings, editable through the selected class in Style controls; no retained local styles or Elementor Custom CSS. Three native connector divs meet centers continuously; no pseudo-elements. Owner-approved minimal external exception supplies whole-step hover → circle color/outline and reduced motion: [canonical CSS](../theme-overrides/process-timeline.css), deployed in existing ROBYLO Starter `assets/css/fallback.css`. No typography/base-size duplication, plugins, dependencies or shared repository changes. [E15](milestones/2026-10-16-process-timeline.md) contains IDs, capability findings, measured responsive results, editing and recovery. This supersedes only earlier process-grid/card descriptions below.

Observed 2026-10-16 through read-only Elementor MCP on staging (E3 in [PROJECT_CONTEXT](../PROJECT_CONTEXT.md#evidence-register)). These are saved resource values and class identities, not a new design proposal or proof of rendered use. Re-read resources before editing.

## ZIP UI and Homepage refinements — E8

Current class total is 83. The 71-class register below is the earlier baseline. Existing variables and classes were reused; no tokens or duplicate Components were created. These additions use native Global Class controls, with no retained Custom CSS:

| Class | ID | Purpose |
| --- | --- | --- |
| form-panel | g-ecfd56c | Light-blue panel, 1px token border, 12px radius, 32px padding / 24px mobile, 16px gap |
| form-controls | g-a9bac3a | Input/action row; stacked at tablet breakpoint 1024px and below |
| form-input | g-4a008b9 | Inter 16px, 52px control, native border/radius/background; navy 2px focus border |
| button--inactive | g-bf5bb9b | Montserrat 600, 14px, 52px control and muted disabled presentation; disabled is a native attribute, not CSS |
| form-label | g-f760e1c | Inter 14px/600 with text-color token |
| form-field | g-7a37771 | Native vertical field layout with 8px gap and zero padding |
| form-note | g-77663f6 | Inter 14px normal-case muted help text |
| process-step-number | g-af5ab08 | Montserrat 600, 24px desktop/tablet and 22px mobile, 1.3 line height |
| audience-card | g-38b29fb | Rounded white linked card with token border, clipped placeholder and no underline |
| audience-card__body | g-19a0c6f | Copy/action grid, 32px padding / 24px mobile |
| card-action | g-a5c0d65 | Navy circle, 64px desktop/tablet / 52px mobile |
| card-action__icon | g-8a7dd36 | 24px white SVG glyph |

Only process-step-number was moved ahead of card-icon; other existing classes retain relative priority. Step Number keeps card-icon and hide-empty because the existing icon-svg rule hides an SVG immediately followed by a nonempty card-icon. Changing that contract requires an explicit supported visibility design. This is a documented pre-existing selector, not new code introduced here.

Heading capitalization remains H1/H2 uppercase, H3/H4 capitalize, H5/H6 none. Sizes, weights, colors and responsive defaults match the pre-task snapshot. Audience copy reuses stack--compact plus stack; placeholders reuse media-placeholder.

The converter initially retained unsupported cursor/white-space and a focus-visible border as Custom CSS. These declarations were removed in the visual editor; ordinary link keyboard focus remains provided by the existing HTML Default. No new custom styling remains in the added classes. See [milestone](milestones/2026-10-16-zip-and-homepage-refinements.md) for verification and limitations.

## Global conventions

- Keep reusable values in native Global Variables, base typography in tag defaults, shared styling/layout in Global Classes, repeated structures in Components and instance content in supported overrides.
- Reuse the existing labels. Component names are human-readable; class labels use lower-case role names, with existing `--modifier` and `__part` conventions. Do not rename existing classes merely to impose a new convention.
- Inspect actual class declarations, priority, local overrides and tag defaults before diagnosing the cascade. The resource says earlier classes have higher priority; do not reorder casually.
- Preserve native responsive controls, meaningful headings, readable contrast, visible focus and usable menu/touch controls. Record the actual breakpoints and values inspected, rather than assuming defaults.
- Document new labels, scope, consumer effects and the editor location after each milestone. Avoid duplicated local settings and hidden theme rules.

## Observed Global Variables — 36

Source: discovered `elementor://global-variables`, active kit, read 2026-10-16. Values are transcribed as returned, including px units and formulas. Their existence does not prove every heading or layout currently references them. Internal variable IDs are omitted; labels are the useful editing reference.

| Label | Type | Saved value |
| --- | --- | --- |
| `color-primary` | color | `#1A327D` |
| `color-primary-hover` | color | `#142862` |
| `color-secondary` | color | `#334155` |
| `color-accent` | color | `#F05A29` |
| `color-text` | color | `#334155` |
| `color-text-muted` | color | `#5B6575` |
| `color-background` | color | `#FFFFFF` |
| `color-surface` | color | `#F8FAFC` |
| `color-surface-alternate` | color | `#EFF6FF` |
| `color-border` | color | `#CBD5E1` |
| `color-white` | color | `#FFFFFF` |
| `color-success` | color | `#15803D` |
| `color-error` | color | `#B91C1C` |
| `font-body` | font | `Inter` |
| `font-heading` | font | `Montserrat` |
| `space-xs` | size | `8px` |
| `space-sm` | size | `16px` |
| `space-md` | size | `24px` |
| `space-lg` | size | `32px` |
| `space-xl` | size | `48px` |
| `space-2xl` | size | `64px` |
| `space-3xl` | size | `96px` |
| `container-max` | size | `1200px` |
| `content-max` | size | `800px` |
| `page-gutter` | size | `32px` |
| `page-gutter-mobile` | size | `20px` |
| `section-spacing` | size | `96px` |
| `section-spacing-mobile` | size | `56px` |
| `font-size-h1` | custom-size | `clamp(2.5rem, 1.75rem + 3vw, 3rem)` |
| `font-size-h2` | custom-size | `clamp(2rem, 1.5rem + 2vw, 3rem)` |
| `font-size-h3` | custom-size | `clamp(1.5rem, 1.25rem + 1vw, 2rem)` |
| `font-size-h4` | custom-size | `clamp(1.25rem, 1.125rem + 0.5vw, 1.5rem)` |
| `font-size-h5` | custom-size | `clamp(1.125rem, 1rem + 0.5vw, 1.25rem)` |
| `font-size-h6` | size | `1rem` |
| `font-size-body` | size | `1rem` |
| `font-size-lead` | custom-size | `clamp(1.125rem, 1rem + 0.5vw, 1.25rem)` |

## Observed Global Class register — 71

Source: discovered `elementor://global-classes`, read 2026-10-16. Full returned order is preserved below, highest priority first. This resource returned IDs and labels, not a complete declaration audit. Locate these in Elementor Global Classes; inspect the native controls and affected consumers before changing them.

| Priority | Class label | Internal ID |
| --- | --- | --- |
| 1 | `section--dark` | `g-43edd01` |
| 2 | `service-card` | `g-f569734` |
| 3 | `text-link` | `g-f85f475` |
| 4 | `image-led-card` | `g-f382380` |
| 5 | `grid--four` | `g-aadf7b4` |
| 6 | `grid--flush` | `g-5e84b20` |
| 7 | `feature-summary` | `g-8333fe1` |
| 8 | `project-summary` | `g-3eb7605` |
| 9 | `testimonial-card` | `g-c51baa3` |
| 10 | `section--strip` | `g-8f39284` |
| 11 | `split-row` | `g-5f7b649` |
| 12 | `hero-layout` | `g-c4cc431` |
| 13 | `comparison-media` | `g-05670b8` |
| 14 | `comparison-panel` | `g-637b3ac` |
| 15 | `city-links` | `g-6ebef89` |
| 16 | `city-link` | `g-9a26448` |
| 17 | `cta-panel` | `g-e1d4327` |
| 18 | `site-footer` | `g-a9afb6b` |
| 19 | `footer-columns` | `g-fb9219a` |
| 20 | `footer-column` | `g-3f96b71` |
| 21 | `text-measure--short` | `g-d480b26` |
| 22 | `heading-label` | `g-0526546` |
| 23 | `text-meta` | `g-2f5e3b0` |
| 24 | `footer-meta` | `g-11ba71a` |
| 25 | `navigation--primary` | `g-be97fc2` |
| 26 | `navigation-links` | `g-683eaef` |
| 27 | `panel` | `g-b691ab0` |
| 28 | `align-start` | `g-63e627b` |
| 29 | `stack--compact` | `g-3bac536` |
| 30 | `media-placeholder--dark` | `g-710713a` |
| 31 | `media-placeholder--neutral` | `g-dc38375` |
| 32 | `media-placeholder--project` | `g-09f1205` |
| 33 | `media-placeholder--badge` | `g-7b4239a` |
| 34 | `media-placeholder` | `g-7242622` |
| 35 | `card-icon` | `g-2c25e20` |
| 36 | `hide-empty` | `g-dea53d0` |
| 37 | `text-emphasis` | `g-3c6116d` |
| 38 | `section--light` | `g-1834399` |
| 39 | `layout-reset` | `g-0152925` |
| 40 | `section--compact` | `g-4225410` |
| 41 | `section--large` | `g-d5b53ca` |
| 42 | `section` | `g-d3248b3` |
| 43 | `container--narrow` | `g-0013c25` |
| 44 | `header-row` | `g-eeaa1f2` |
| 45 | `info-row` | `g-bf95de4` |
| 46 | `container` | `g-68fb534` |
| 47 | `stack` | `g-6f5f11a` |
| 48 | `cluster` | `g-0e529a5` |
| 49 | `grid-2` | `g-9b8782d` |
| 50 | `grid-3` | `g-2f37dc0` |
| 51 | `card--interactive` | `g-d63edc0` |
| 52 | `card` | `g-8ca905f` |
| 53 | `button-primary` | `g-92745fa` |
| 54 | `button-secondary` | `g-e47e377` |
| 55 | `button-outline` | `g-b5f3969` |
| 56 | `text-lead` | `g-8c1a9a9` |
| 57 | `text-muted` | `g-68bba82` |
| 58 | `button-outline-orange` | `g-563da68` |
| 59 | `button-outline-white` | `g-c8eb142` |
| 60 | `icon-svg` | `g-b84ed52` |
| 61 | `site-header` | `g-34b5e46` |
| 62 | `header-brand` | `g-fba6f58` |
| 63 | `header-logo` | `g-a59f4e5` |
| 64 | `info-bar` | `g-1f9d3da` |
| 65 | `info-links` | `g-f94864f` |
| 66 | `info-text` | `g-e2b178b` |
| 67 | `emergency-mark` | `g-d54b228` |
| 68 | `emergency-mark__numbers` | `g-bdc93ca` |
| 69 | `emergency-mark__number` | `g-5d6cddf` |
| 70 | `emergency-mark__slash` | `g-1529654` |
| 71 | `emergency-mark__label` | `g-32c8e95` |

## HTML Defaults read during integration — E6

These are fresh saved tag-default values, not changes made by this documentation task. Tablet rules use max-width 1024px; mobile rules use max-width 767px. All headings reference `font-heading` (Montserrat), use `color-text` at the default layer, and have zero margin. Dark-section foreground treatment is a separate shared-class concern.

| Tag | Desktop / tablet / mobile size | Weight | Line height | Transform |
| --- | --- | --- | --- | --- |
| H1 | `var(--font-size-h1)`; existing clamp token | 700 | 1.1 | uppercase |
| H2 | 32 / 28 / 24px | 700 | 1.15 | uppercase |
| H3 | 24 / 22 / 20px | 600 | 1.3 | capitalize |
| H4 | 20 / 19 / 18px | 600 | 1.3 | capitalize |
| H5 | 18 / 17 / 16px | 600 | 1.4 | none |
| H6 | 16 / 15 / 14px | 600 | 1.4 | none |

The retained `font-size-h2` through `font-size-h5` variable formulas above do not describe these explicit HTML Default sizes. Do not overwrite defaults merely to make them match unused or differently scoped tokens.

## Homepage V2 class roles — 17 additions in the implementation record

Current identities/order are confirmed by E6; the roles below are corroborated by saved class assignments and the historical E7 implementation. This is not a fresh audit of every class declaration.

| Classes | Role / native editing location |
| --- | --- |
| `service-card`, `text-link` | Shared Component 62 layout and understated action; Global Classes layout, spacing and typography/state controls |
| `image-led-card` | Unified audience/project image-and-body wrapper |
| `grid--four`, `grid--flush` | Four-step responsive grid and compact service-grid gaps |
| `feature-summary`, `project-summary`, `testimonial-card` | Lighter shared definitions for 65, 68 and 86 |
| `section--strip`, `split-row` | Compact emergency strip and responsive copy/action layout |
| `hero-layout` | Native grid column proportions, gaps and responsive stacking |
| `comparison-media`, `comparison-panel` | Static 4:3 Before/After placeholders; no slider |
| `city-links`, `city-link` | Wrapping compact location links, without normal/hover underline |
| `cta-panel` | Inset navy CTA layout within a light section |
| `media-placeholder--dark` | Legible dark Hero placeholder variant |

Existing `section`, `container`, `stack`, `cluster`, grids, icon and button classes were reused. No new design-token set or duplicate Component ID was introduced. The temporary `eyebrow`, `header-navigation` and `menu-control` classes were removed and are not part of the final 71-class register.

Final E7 refinements: existing emergency-mark classes give the caption 12px desktop/tablet and 11px mobile with an 8px gap after the numbers. Component 286 has a DIV root, so the informational mark has no anchor underline. `button-secondary` prevents shrinking/wrapping; recorded Header CTA size is about 204×53px on desktop and hidden on tablet/mobile. The mobile Header grid reserves a 44px toggle column. Native Full Width replaced the conflicting legacy dropdown right/min-width rule; other pre-existing legacy navigation styling remains. These class behavior values are historical rendered checks, not remeasured here.

## Reported conventions and limits

E4 reports one Homepage H1, Montserrat headings, a compact navy Hero, 16:9 Hero/audience placeholders and 4:3 project placeholders. It reports core service grids at 3/3/2/1 columns and process grids at 4/4/2/1 for 1440/1200/900/390 px. Those viewport checks are historical, not configured breakpoint values verified here.

The older E5 component artifact contains typography/default/style definitions that may be stale. Do not replay it over the current kit. The full saved tag-default settings, all class declarations, responsive breakpoints and any legacy custom CSS still need a current audit.

E4 reports white text on orange `#F05A29` around 3.39:1 and leaves the treatment unresolved. Preserve the issue in the next design review; no palette or styling was changed in this documentation task.

## Editing locations

| Change | Native location / scope |
| --- | --- |
| Reusable colors, fonts, spacing | Global Variables; inspect references before changing |
| Base heading/body typography | Atomic tag defaults; inspect class/local overrides |
| Shared layout, buttons and states | Global Classes; check order and responsive/state controls |
| Reusable structure | Component definition; affects consumers |
| Individual title, icon or destination | Component instance's exposed overrides; do not detach |
| Header/footer assignment | Separate Theme Builder document and display conditions |

Actual controls and persistence must be verified on the installed Elementor version. No hidden CSS/JS or new styling was added by documentation initialization.
