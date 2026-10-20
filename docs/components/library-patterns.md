# Additional Atomic library patterns

**E58,2026-10-20:** Shared Hero74's Copy2bd621f1 gains empty gcpro-cta-origin g-b9ab0d8, ending at its existing CTA. Native styles, content, component overrides and links unchanged. This configures future Hero consumers for the one global navigation controller903; no script is stored in Hero74. [Reuse instructions](smart-navigation.md#responsive-behavior-and-configuration).

Saved definitions and override schemas freshly inspected on2026-10-20. These nine entries complete the16-definition discovery inventory alongside [shared primitives](shared-components.md), [CTA](final-cta.md) and [timeline](how-we-work.md). They are not current Homepage section implementations unless a consumer is named. “Not used in Homepage main” never means safe to delete.

Common ownership: Elementor Pro Components, existing Global Classes/Variables and each definition's local native controls. No HTML widgets, shortcodes, GCPRO JavaScript or Custom Code reference occurs inside these nine saved definitions. Inherited class exceptions are in [CUSTOM_CODE](../CUSTOM_CODE.md); no library source file is separately enqueued. Native tag defaults supply responsive typography; exact unused-library rendering and all-consumer graph are **not newly browser-validated**. Inspect Style Guide/consumer pages before changing shared definitions.

## Secondary Blue button56

**Purpose/structure:** single e-button root7d7dc767,button-secondary g-e47e377 and local style e-3fda4fee-d967. Overrides text/link. Header113 instancecd66895 uses this definition; no such instance occurs in current Homepage main.

**Styles/responsiveness:** native class/default/button controls; existing fonts/primary/hover/white/border/spacing tokens. Class Custom CSS owns border-box,wrapping,focus halo and final nowrap. Button hover/focus are CSS states, no JS. Review narrow-width label wrapping before reuse. Use native link overrides; prototype default #robylo-content is not a destination for every consumer.

## Outline Orange button100

**Purpose/structure:** single e-button root2b6a23b3,class button-outline-orange g-563da68; overrides text/link. No current Homepage main instance; availability5350691e uses the same class on a different widget, not this Component.

**Ownership/behavior:** native class/default controls, existing accent/font/spacing tokens and class focus-halo exception. Responsive button wrapping/focus/hover inherit class behavior; no instance-specific code. Check intended object link and keyboard focus before use; default #robylo-content remains a starter reference.

## Service Card62

**Purpose/structure:** article/flexbox6cd5ab9f → icon4a4396ac,title4a877e1a,description295090e4,action210ecf0d. Overrides icon,title,description,cta_text,cta_link. Defaults include SVG attachment192 and# link.

**Styles:** service-card g-f569734,service-card__icon g-b759e84,icon-svg,button-outline-orange,service-card__action g-d0416c8; existing fonts/navy/accent/border/surface/spacing tokens. Native card/class layout; icon-svg fill fallback; inherited button focus states. No custom card JS/Custom Code.

**Responsive/reuse/limits:** self-contained flexible article; parent grid controls column count and tag defaults adjust typography. Original Core A/template703 is historical; current Homepage uses Core B articles instead of62. Supply real SVG/media references and independent destinations; test parent grid/mobile card height and never reinsert archived service layouts automatically.

## Feature Card65

**Purpose/structure:** article60a7235a → SVG663703ef,optional number77fda46a,H3 681f7c76,description2400437e. Overrides icon,step_number,title,description; SVG203 default,number empty.

**Styles/behavior:** feature-summary g-8333fe1,icon-svg,card-icon g-2c25e20,process-step-number g-af5ab08,hide-empty; existing fonts/colors/spacing. Native class/default presentation; :empty hides blank number,icon-svg adjacency rule avoids double fallback icon. No JS,Custom Code or shortcode.

**Responsive/reuse/limits:** follows parent layout and native type breakpoints. This is not timeline582 and does not independently deploy590. Populate number/icon deliberately, verify empty/hide behavior and parent-grid fit; no current Homepage main instance or fresh standalone browser QA.

## Interactive Card68

**Purpose/structure:** root anchor7439764a → H3 481eeb5f,paragraph4f7be4c9. Overrides title,description,link; project-summary g-3eb7605.

**Styles/behavior:** native shared card class/defaults and existing type/color/spacing tokens; CSS focus/hover inherited from its class. No custom JS. Responsive dimensions follow parent grid.

**Reuse/limits:** keep the whole-card link as the single interactive target; do not nest another anchor/button inside. Set an intended existing destination object; default #robylo-content is a placeholder. Not a current Homepage BEAF project-card definition; do not substitute it for plugin wrappers without a separate design decision.

## Hero74

**Purpose/structure:** section353a270b → container3e0dbc7f → layoutce2d5b2 → copy2bd621f1 (heading51772c3d→71,CTA226ddf87→53) and image74fdbbc9. Overrides title,heading_tag,description,cta_text,cta_link,image.

**Styles:** section,container,grid-2,stack; native color-surface-alternate,alignment and image max-width/auto-height/radius space-xs. Layout local style e-30b81e2f-f92c owns :not(:has(img[src]:not([src=""]))) single-column fallback; image local e-580e21c9-f816 hides missing/empty media. Native supported values stay in local controls; these structural selectors are scoped Custom CSS exceptions.

**Responsive/reuse/limits:** grid-2 desktop/mobile conventions plus explicit missing-image collapse; nested heading defaults toH1. No JS/Custom Code/plugin beyond Elementor. Current Homepage panorama is a distinct custom section, not74. When reusing, set appropriate heading level, real image/alt and CTA object link; test with and without image and avoid multiple page H1s.

## Image + Text77

**Purpose/structure:** section2c852678 → container41af9343 → layout26c7ace → copy16c8b360 (heading262aee15→71,CTA78eed882→53) and image27839859. Same six override keys as74; heading defaultsH2.

**Styles:** section/white color-background,container,grid-2,stack; existing spacing/font tokens. Local layout e-3cbef3d9-e4cd and image e-6bff78bc-1753 own the same scoped missing-image collapse/hide selectors as74; image otherwise native max-width100%,auto-height,radius space-xs.

**Responsive/reuse/limits:** parent two-column convention with one column on mobile or missing image; no custom JS/Custom Code/shortcode. Reuse the current definition and overrides rather than cloning HTML. Check empty-image behavior, alt, mobile order and independent CTA route. Similarity to74 is a documented small library composition pattern; merging them was not required by this audit.

## FAQ Group83

**Purpose/structure:** native e-accordion5a87e067 with items1c65de03/9716f34. Headers3590518d/51d65ec8 → title slots6628fba8/36fde7d2 → questions156c74ee/21cdefc6. Content31b1c41b/49d75a96 → answers7ff48a46/763330e. Overrides question_1,answer_1,question_2,answer_2.

**Styles:** native local gap space-sm,border color-border/surface,radius space-xs,padding space-md,font weight600/primary. Header local styles e-6fab0c7e-1ad9 and e-32802adb-5ad2 contain scoped focus-visible3px primary/offset3px exceptions. No extra shared class,custom JS,Custom Code or third-party FAQ plugin.

**Behavior/reuse/limits:** saved all_collapsed,max_expanded multiple,show_icon false,faq_schema false; native Elementor accordion runtime owns interactions and responsive flow. Schema is intentionally off; don't promise rich-result behavior. Preserve native header/content structure and test Enter/Space/focus/reduced-motion/screen reader before publication; saved contract is not fresh keyboard certification.

## Testimonial Card86

**Purpose/structure:** article2bcccf8 → quote1c8aca80,name413054d6,attribution34440383; overrides quote,name,attribution. Classes testimonial-card g-c51baa3,text-lead,text-emphasis,text-muted and name local style e-6fd4c9a8-9f90.

**Styles/behavior:** native card/type/color/spacing controls and tag breakpoints; no JS,Custom Code or vendor review dependency. Parent determines column count.

**Reuse/limits:** starter text explicitly requests a genuine quotation before publishing. This is not the current Trustindex section02441ff. Do not invent testimonials or copy vendor review HTML into86; supply owner-approved quote/name/source permission and test responsive text lengths.
