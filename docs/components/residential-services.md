# Residential Services — E77, 2026-10-21

**Current,2026-10-22:** The page-owned Hero described below has been replaced by a complete instance of [GCPRO — Shared Hero1318](shared-hero.md), using a native Image and independent content/link Overrides. Earlier Hero element IDs, slider instructions and layout descriptions below are historical. Other page sections and BEAF galleries are preserved.

**E83:** Results cards25d5b401/14e979f now use the shared [approved A design](before-after.md#e83--approved-a-card-design-2026-10-21), matching Home/gallery. Two caption divs group the original headings/paragraphs;723/742 captions now identical to Home with City, IL in titles only. Hero, service-card buttons and Solid Blue assessment CTA remain unchanged.

## E81/E82 — image and contextual CTA

Existing77 instance26c8a5b5 now uses technician WebP1243 (1448x1086,4:3) in the assessment section. Attachment alt: "GCPRO technician cleaning debris from an interior with exposed wall framing during home restoration." Descriptive title/description supplied; no visible caption added. Original724 retained for rollback.

E82 now uses existing Solid Blue button-secondary styling on a native Atomic Button; the temporary Orange Outline treatment was superseded, preserving Discuss Your Home Restoration and Internal URL Page492. No new library Button/Global Class/custom CSS; one native visibility/wrapping override keeps the existing blue variant visible on mobile. [Canonical hierarchy, exact component owners, responsive evidence and contrast limitation](../DESIGN_SYSTEM.md#cta-button-hierarchy--e82-2026-10-21). Existing77 root now62ef2b5; shared53/100 definitions untouched. No Residential body change for the CTA; existing overrides continue to resolve. Image rollback: restore724 in this instance only.

## E79 — complete SEO content through existing Overrides

Full Residential visible copy, H1, intros,8 H2/16 H3, six service cards, four process/Why items, six FAQs and CTA copy now optimized. Existing design/styles/classes/destinations retained;53 native nodes after separately requested Hero reuse of Glenview742, compact intro and balanced process copy. Plugin and original comparisons unchanged; no shared definition changed. Exact instances/keys/final text, AIOSEO fields, keyword evidence, QA and rollback: [complete content brief](../seo/2026-10-21-residential-services.md). [Global AIOSEO configuration](../SEO_AIOSEO.md).

## E78 — numbered heading consistency and native Residential entry link

2026-10-21, staging only. Seven main content sections now use the established numbered-eyebrow/H2/orange-line/intro system:

| Number / editable label | Existing owner |
| --- | --- |
| 01 / RESIDENTIAL SERVICES | Page484 Section Heading71 instance48d8e79c |
| 02 / RESTORATION SOLUTIONS | Page484 Image+Text77 instance26c8a5b5 → existing nested71 |
| 03 / OUR PROCESS | Page484 shared1152 instance5412e337, existing eyebrow Override |
| 04 / WHY GCPRO | Page484 shared1149 instance225936ef, existing ebd1102 eyebrow Override |
| 05 / REAL RESULTS | Page484 Section Heading71 instance5cd7bb8a |
| 06 / LOCAL COVERAGE | Page484 shared1140 instance5ced3ca1, existing eyebrow Override |
| 07 / HOMEOWNER QUESTIONS | Page484 Section Heading71 instance44dce85e |

Hero retains its single uppercase H1. Final conversion CTA80 retains the approved shared Homepage format and animation; it is separate from the numbered content sequence. All H2/H3 titles, descriptions, images, links, service/project/FAQ content and layouts are preserved.

**Shared settings:** existing Section Heading71 now exposes one optional `eyebrow` content field (empty default). Root1c84f24b: existing stack → paragraph using existing section-eyebrow + hide-empty, H2 and optional description. Original title/heading_tag/description keys/defaults retained. Empty eyebrows render display:none on Homepage consumers, so its visible numbering/design is unchanged. No new heading Component or style variant.

Existing Image+Text77 root1a39a5fc forwards `eyebrow` to its existing nested71; original title/tag/description/image/CTA Overrides remain independent. Its native Copy wrapper reuses section-heading--accent; no new CSS rule. Existing image/split layout/conditional image hiding rules preserved. No Homepage77 instance exists. Component internals received regenerated native IDs when the existing definitions were updated; component IDs/UIDs and original public Override keys remain stable.

Page484 native containers1c714b47, the Results heading container and FAQ heading container gain existing section-heading--accent g-a537304. This reuses its existing `.section-heading--accent > .stack > h2::after` rule. Shared Why retains its original native orange Divider; Process/Service Areas retain their original accent-class ownership. Only instance labels and these three existing-class assignments change in the saved Page tree.52 Page nodes retained. No new Global Class, Global Variable, Atomic Component, Custom Code, CSS/JS/PHP file, plugin or dependency. Existing590/847/903, BEAF records/shortcodes/styles, Header113/Footer114 and other shared section definitions are unchanged.

**Homepage native link:** existing whole Residential card154/4c8810dc now uses native Dynamic Tags → Internal URL → Page484. Previously `#`; no manual staging/production URL. The existing child heading remains within the single anchor; zero nested anchors. Existing WordPress menu item109 is already `type=post_type`, `object=page`, `object_id=484`, reused by desktop/mobile Header renderings; verified both resolve to `/residential-services/`. No new duplicate menu items or links on explanatory body text. No other Homepage saved field changed, confirmed after excluding only this card's link from comparison. No URL, parent, publication, redirect or inventory-row changes.

**Verification:** Chrome viewport simulation360/393/430/768/1024/1280/1440 shows exact01–07 sequence, existing font/uppercase behavior, orange line on all seven content H2s, no text clipping/horizontal overflow, one uppercase H1 and two initialized Residential comparisons. Existing Page body destinations are unchanged. Homepage visible eyebrows remain01 WHO WE HELP /02 RESTORATION SERVICES /03 OUR PROCESS /04 OUR WORK /05 WHY GCPRO /TESTIMONIALS /06 COVERAGE AREA; all added optional eyebrow nodes are empty/hidden. Four Homepage comparisons initialize after load. Actual click on the Residential card navigates to Page484. Header/Footer native settings exactly match the pre-E78 backups. Source comparison proves all Residential content/links/BEAF nodes unchanged except approved eyebrow Overrides and accent-class assignments. Desktop/mobile screenshots saved for owner review.

Elementor Tools Clear Files & Data completed successfully. No new editor-session certification, physical-device test or anonymous/incognito certification is claimed; prior editor-loading/external403 limits remain. This heading-only change did not retest every BEAF drag/popup state; prior E77 interaction evidence remains dated.

**Editing:** [Section Heading71](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=71&action=elementor), [Image+Text77](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=77&action=elementor). Set page-specific labels through supported content Overrides; do not edit shared defaults for one Page or add per-page CSS. Maintain sequence when inserting/reordering content sections. Keep Homepage's optional eyebrow values empty where it already supplies an outer label.

**Rollback:** restore only Page484 pre-E78 eyebrow Overrides/classes and Homepage card's previous link from private backups. Restore pre-E78 definitions71/77 (original exposed keys, styles and defaults) together if removing the new optional control. Preserve other Pages/Components/menus; clear Elementor rendering cache and verify both consumers. Public sanitized final native state and responsive evidence: `docs/evidence/2026-10-21-residential-headings/`. Raw admin backups remain outside Git.

Implemented on staging only: [Residential Services](https://vitaliiv1.sg-host.com/residential-services/), existing Published Page484, unchanged slug/parent. This supersedes the initial E77 trial variants: the independently assembled cities and white benefit cards were removed. Shared section types retain the Homepage design; only content differs through native Overrides.

## Exact owners and reuse

Page484 → main **b1c1ff0**, 52 saved native nodes, nine sections. Elementor Full Width (`elementor_header_footer`), Hide Title=yes. Existing structural Single Page1008 no longer includes484:79 conditions remain, also saved through native Theme Builder conditions UI. No other Page status/path changed;93 Pages remain88 Published/5 Draft.

| Section | Native owner / reusable definition | Content and links |
| --- | --- | --- |
| Residential Hero | 5357c5f3; H1 12e30c52; existing286/53/103 | Uppercase inherited H1; real restored living room Media747; Call847-656-3322; Request492; existing `gcpro-cta-origin` |
| Six residential services | 305c8aa; six existing Service Card62 instances | Water514, Fire517, Mold516, Storm523, Reconstruction518, Personal Property521; existing SVG596/597/607/600/599/601 |
| Solutions | 26c8a5b5 → Image+Text77 | Real damaged interior Media724; request492; native copy/image/action overrides |
| How We Work | instance5412e337 → **1152** | Source-copy of Homepage4681b8f5, including existing71/582, original spacing/classes/z-index0; residential step descriptions overridden |
| Why homeowners choose GCPRO | instance225936ef → **1149** | Source-copy of Homepage5b2c6d3c; same navy editorial split/four benefits/dividers/icons; residential headings/copy overridden |
| Real restoration results | 264c58b4; two native Shortcodes | Original `[bafg id="723"]` and `[bafg id="742"]`; same vendor comparison presentation and approved descriptions; View All Projects→1132 |
| Service Areas | instance5ced3ca1 → **1140** | Original Homepage7d8c17ad design:12 city rows, native3/2/1 grid, shared arrow/divider/focus classes; residential intro overrides |
| FAQ | 564749dd; three existing FAQ Group83 instances | Six native details/summary questions; supported copy overrides; schema remains off |
| Final emergency CTA | 728c4896 → existing **80** | Residential copy, call phone and native Request492; same shared video/background/radius/responsive behavior |

Homepage now references **6d0939b9→1152**, **60cdf058→1149**, **10feca9e→1140** in the original section positions. All other Homepage child subtrees are byte-for-byte unchanged, including Hero, Core B, BEAF results, emergency support and testimonials. Header113/Footer114 trees and page settings are byte-for-byte unchanged.

### New shared definitions — existing designs promoted, not redesigned

- **1140 GCPRO / Service Areas Section**: [editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1140&action=elementor). Existing source design promoted because two real consumers need one owner. Root/child locators, complete settings/styles in component-1140.json.31 native exposed properties: eyebrow, heading, introduction,12 city labels and12 destinations, two action labels and destinations. Existing city-link/city-link__text/section/container/stack/classes reused. Whole native anchor row contains its text and pseudo-arrow; no nested anchors or stranded arrow grid items. Directory→495; Check Service Availability now uses existing Outline Orange100→492 rather than copying the inactive submit-button prototype. No ZIP lookup is claimed.
- **1149 GCPRO / Why Choose Section**: [editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1149&action=elementor). Exact source copy retains native local styles, Global Classes, icons205/206/210/211 and four-benefit design. Exposes existing heading/paragraph content with descriptive editor labels. Existing numeric override keys are native metadata/location references, not runtime selectors.
- **1152 GCPRO / How We Work Section**: [editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1152&action=elementor). Exact source copy wraps existing Section Heading71 and Timeline582; exposes eyebrow/heading/intro plus12 step fields. Does not duplicate Timeline582 or its styling.

No new Global Class, Variable, plugin, library, media asset, stylesheet or JS file. Existing definitions reused:286,53,103,71,62,77,582,59,100,83,80. Trial Feature Card65 alternatives are absent from final Page. Three new shared definitions are justified by actual reuse on both Pages; don't create another variation merely for different copy. Saved public native evidence is in this milestone's evidence directory; raw admin responses/private recovery backups are excluded from Git.

## Shared motion and radius

**Existing Custom Code847** renamed “GCPRO / Shared Final CTA Video (staging only)”; Published, Entire site, Body End, priority1, jQuery opt-in off. One source remains in its Custom Code editor; `integrations/cta-video-experiment.html` is a source mirror, never separately enqueued. Removed `.gcpro-homepage` selector dependency; initialize each `.cta-panel` idempotently. Preserved original masked MP4 attachment846, opacity, mobile treatment, lazy proximity load, offscreen pause, muted/inert/aria-hidden handling, Save-Data/reduced-motion and staging-host guard. No script copied into Pages or Components. One panel on each tested Page means one active controller per Page.

Component80 → panel **5ec4592**, native local style now owns radius `var(--space-xs)`=8px. Removed only the obsolete Homepage main local Custom CSS `& .cta-panel { border-radius:8px; }`; other Homepage settings unchanged. Existing847 mobile square corners/padding preserved. Shared code is still a documented native-video gap, not falsely described as an Elementor video widget.

**Existing Code590** source unchanged, its native condition broadened from154 to Entire site so the shared `.process-timeline` gets the same touch animation. Body End priority10; one existing IntersectionObserver for timelines, no duplicated script. Desktop theme hover and reduced-motion gates preserved. Existing Code903 unchanged; Hero origin configures it automatically. No new numeric runtime dependency.

## Internal links and content

All Page484 internal actions use native InternalURL post-object references. No empty/# body links.21 unique body destinations visited in the connected browser: six services,12 cities, Request492, Portfolio1132, Service Areas495. All resolve to existing Published routes; the linked child pages/index/form remain structural placeholders, not completed content or a working submission form. The preserved Elk Grove Village path is `/service-area/elk-grove-village/`; no spelling/URL restructuring performed.

Real Media724/747 and BEAF723/742 are approved existing project evidence. No invented credentials, reviews, response-time, pricing or insurance claims. H1 is uppercase, unique and follows native site typography. Title is Residential Property Restoration in Chicago; canonical retains the exact route. Relevant description saved as native excerpt; **no rendered meta-description currently exists**, so SEO-plugin/meta integration remains pending rather than adding custom head code. Staging robots remain noindex,nofollow. Migration register still321 rows; only484's implementation observation changes, original production/history/performance/action fields retained.

## Verification and limitations

- Final viewport simulation360/393/430/768/1024/1280/1440: zero horizontal overflow, one uppercase H1, six services, four benefits,12 full clickable64px city rows, six FAQ controls, all six raster images loaded with alt text. Native3/2/1 grids and compact wrapping actions verified. No body/html overflow workaround.
- Runtime Home/Residential city, Why, Timeline and CTA fingerprints agree for display/gap/padding/font/color/background/radius. Native copied local styles preserve the original design.
- Desktop CTA video readyState4/playing/muted/inert;393px mobile also plays; reduced motion removes video. One847 style/script owner per document. Mobile Timeline waiting→played, Call Now remains available.
- Smart Header down1150 hides/up990 shows; Call Now visible in both directions, hidden while native mobile menu is open. Menu expansion/close preserved.
- FAQ Enter opens/Space closes; city rows keyboard reachable with visible2px outline. Existing class arrows/hover styling retained.
- BEAF desktop divider changed723 from278 to357.667px and742 from278 to377.667px; mobile723 from176.667 to241.323px. Both fullscreen popups open/close; mobile popup fits viewport and suppresses Call Now. Actual touch scrolling moves the Page over an image. No plugin/global BEAF CSS/JS edits; vendor handle/close keyboard semantics remain vendor limitations.
- All21 body routes were actually opened in the connected Chrome session. Physical Android/iOS and screen-reader testing not performed. No form submitted/phone call placed.
- Independent anonymous external HTTP attempts return existing nginx403 for all10 tested routes. Connected browser frontend works. No security/settings bypass attempted; anonymous/incognito/cache-HIT delivery is **not certified**.
- Native saved trees, Overrides and frontend persistence verified. Elementor484 visual editor shell stays LOADING/about:blank and offers Can't Edit/Safe Mode; did not enable Safe Mode or change settings. Full visual-editor interaction remains unverified.

## Safe reuse and rollback

Future Commercial/service/location pages should place existing shared1152/1149/1140/80 and adjust supported content Overrides. Use62/77/83 where suitable, preserving native styles. Keep unique Hero content independent; don't copy Global Classes or scripts. Page count/content differences do not justify a second visual design. BEAF remains third-party content integration.

Rollback: restore private pre-E77 Page484 body/title/excerpt/template/featured media/settings and its one1008 include condition; restore only the three source Homepage sections and removed radius rule from private pre-E77 backup if reverting shared adoption. Restore Component80's prior empty local panel style, Code847 source/title/Page154 condition and590 Page154 condition. Save native conditions and clear Elementor files/data + relevant staging cache. Remove/archive new definitions only after removing both consumers; do not delete media, plugins, city/service Pages or alter Header/Footer. Component80/590/847 affect shared consumers, so rollback these together. No production changes or redirects.


2026-10-22 Trust Logos: [current shared1149 media,classes,label,mobile order,hover,verification limits and rollback](why-gcpro.md). This record supersedes earlier Why media descriptions.
