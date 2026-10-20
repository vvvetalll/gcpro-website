# Hero and audience cards

**Current E71 (after E70 approval), 2026-10-20:** Main Homepage154 Hero a62cdd3 now uses the approved navy split layout and the FIRST existing BEAF723 comparison in visual484c13ec → Shortcode30e0c45, `[bafg id="723"]`. Native layout, copy, CTA overrides and 8px corners retained. One local wrapper Custom CSS rule hides only its fullscreen button; plugin image-link/zoom is already disabled. All three original comparisons and their fullscreen remain unchanged. E70 removed all old local panorama/technician backgrounds and retired unused, empty hero--panorama g-708f717 after a site-wide usage scan (111 classes/36 variables). Draft970 and Media973 retain the static design experiment. No new class, Variable, library Component, JS, plugin or dependency; no Header/Footer/Core/903/production edits. [Current exact owners, QA and rollback](hero-main-beaf.md).

**Historical E69 (superseded by E70/E71),2026-10-20:** Separate **Draft Page970 — Hero Concept B — Restoration Transformation**, root78418107, duplicates the source12-node Atomic structure with fresh IDs and existing286/53/103 instances. New illustrative Media973:1440×1080 WebP/250,828bytes. Native navy split layout, copy/CTAs first on mobile/tablet,8px visual corners; Canvas/Hide Title isolates preview. No new classes/Variables/library Components/custom code/dependencies. Existing Homepage Hero remains active; only separately owner-requested project&nbsp;information wrapping changed in154/7de610a7. No Header/Footer/BEAF/production edits. [Preview, exact owners, QA and activation/discard](hero-concept-b.md).

**Historical E68 (superseded by E70),2026-10-20:** Homepage154 Hero a62cdd3 uses supplied Media961 and native brand-navy gradient layers. Local e-7cfcd182-d44a owns bounded1440px canvas/+80px center offset/top framing and responsive75%/80% cover composition CSS. Old hero--panorama detached, definition retained. Tablet native single-column/max600px copy; mobile placeholder hidden;12 nodes/content/links retained. No new class/Variable/Component/JS/dependency; one requested image asset. Footer/Header/Core/903/BEAF/production unchanged. [Exact owners, saved values, nine-width QA and rollback](../audits/2026-10-20-hero-technician.md).

**E58,2026-10-20:** Homepage Hero Actions6092e1ab gains empty gcpro-cta-origin g-b9ab0d8. It signals the global Mobile Emergency CTA after the introductory actions leave the usable viewport; no Hero visual/content/link changes. Shared Hero74 Copy also has this hook for reusable consumers. [Global controller and editing contract](smart-navigation.md). Audience cards are unchanged.

Two distinct native Homepage sections; no detached HTML composition.

## Hero

**Purpose/location:** Homepage154/main46c3aad4 → hero **a62cdd3** → container20ff6df0 → layout1514b1c. Copy6cc20521 holds eyebrow instance4af4b551 →286, H1 **7941b532**, supporting paragraph7de610a7 and actions6092e1ab (18a239c4 →53; a7bcc76 →103). Mobile media17c26181 still contains placeholder label708a5ff2.

**Styles/tokens:** hero--panorama g-708f717, section/section--dark, container, hero-layout,stack,cluster,text-lead,hero-media--mobile. Existing navy/white/accent,fonts,container/gutter/spacing tokens. Native class backgrounds own photograph/blends; the class's Custom CSS owns no-repeat and desktop background-size1500px layers/position calc(50% - 80px). [Non-enqueued mirror](../../integrations/hero-panorama-composition.css) covers only that composition rule, not all backgrounds.

**Code/dependencies:** no Hero JS, Custom Code, shortcode or HTML widget. Native Components286/53/103, image/background assets and Elementor. Desktop panorama hides/replaces with the mobile media layout; current mobile remains an explicit placeholder, not a finished photograph. H1 exists once; mobile/text wrap checked at requested widths.

**Edit/reuse/limits:** content through native controls/Component overrides, background in hero--panorama; do not hardcode generated element selectors or turn intentional one-off panorama dimensions into sitewide tokens. Current CALL is tel:+18476563322; REQUEST SERVICE#. Preserve informational286 as a DIV, not a second nested link.

## Residential and commercial audience cards

**Purpose/location:** section **7b416658**, container1b98920a, heading instance300decb5 →71, paths1a13f287. Residential anchor **4c8810dc** → media6e5afc98/image295bf90e (attachment629), body6b95719 → copya575649 and action5c2d4dca/SVG658b1119. Commercial anchor **2066a26** → media4c8bb651/image27ec40d5 (630), body687ff42f → copy6066a3bb and action5b9bc8c3/SVG6773a91b. Both arrows use asset464.

**Styles/tokens:** audience-card g-38b29fb,audience-card__body g-19a0c6f,audience-card__image g-77c2a17,card-action g-a5c0d65,card-action__icon g-8a7dd36,layout-reset,stack/stack--compact,grid-2 and existing fonts/navy/accent/border/spacing. White section surface is local native configuration.

**CSS/JS/dependencies:** audience-card class owns the scoped parent-hover/focus/media/reduced-motion block; [mirror](../../integrations/audience-card-hover.css) is not enqueued. Zoom1.025 stays within the clipped media child; action turns orange. No custom JavaScript, Custom Code, shortcode, HTML widget or extra plugin. Native image library supplies alt text.

**Responsive/edit/reuse:** two desktop cards become one mobile column. Edit each image/copy/destination locally, repeated presentation in existing classes. Both anchors remain#. Do not add a nested action anchor inside the card link. Current DOM scan finds no nested anchors; native main images have alt attributes. Preserve keyboard focus and reduced-motion gates when modifying hover. No new asset upload or hover refactor occurred.
