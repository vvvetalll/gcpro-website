# Testimonials

Actual Trustindex integration, separate from Why GCPRO.

| Field | Current implementation |
| --- | --- |
| Location/parent | Homepage154/main46c3aad4 → section10a34543 → inner7d037e04 |
| Children | Heading wrapper629e394d: eyebrow31825a3f,H2 3d727826,divider41bcab5a; Shortcode **02441ff** |
| Saved shortcode | [trustindex data-widget-id=3c3f6b184e520136de76f94fefa] (current 2026-10-24 read; supersedes the earlier widget identifier) |
| Classes/tokens | section,container,stack,layout-reset,section-eyebrow; native H2 uses font-heading/color-text; light surface-alternate #EFF6FF |
| CSS owner | Native section/heading controls; Trustindex plugin/CDN owns review presentation and Poppins font |
| JavaScript / Custom Code | Vendor Trustindex runtime; no GCPRO-developed Testimonials JS or Custom Code entry |
| Dependency | Widgets for Google Reviews14.2; external cdn.trustindex.io assets/data |
| Responsive behavior | Review carousel manages responsive cards inside its own clipped track; offscreen slides are not by themselves page overflow |
| Interactions | Vendor next/previous/read-more and review source links; no custom carousel reimplementation |
| Limits | Plugin Poppins is a design-system exception; review/source approval and structured-data consistency need owner review |
| Safe editing/reuse | Change widget/layout/data in Trustindex configuration, shortcode in02441ff, native heading/surface in Homepage; do not copy review HTML or edit vendor files |

The current closed-page width scan passes360/393/430/768/1440 despite offscreen carousel slides. Runtime JSON-LD's aggregate review count differs from the visible widget's count; treat this as a source/configuration consistency question, not proof of false reviews. No review content, schema settings or typography was changed by this audit.



## Service-page integration — 2026-10-24

Implemented on staging: all 17 existing service Pages now have exactly one native review section immediately before FAQ, after projects where present. No service page had an existing Trustindex embed before this task. Header/Footer, Homepage, Heroes, CTAs, existing service copy, URLs, states, SEO settings, projects and unrelated elements were preserved. All 17 Pages were already Published and remain Published. No production changes.

The existing **Reviews on Page** widget, admin840137/public3c3f6b184e520136de76f94fefa, is the template actually used by Homepage154. It and all12 older widgets remain unchanged. Created9 copies through Trustindex Clone Widget; source selection is exclusively Google GCPRO Restoration498308, never the dental source498314. New names use `GCPRO | Service Reviews | [Service Name]`. Readback of all9 copies' named design/display controls matches the original template; original named controls also match their before snapshot.

### Design and edit locations

Native section10a34543 → inner7d037e04 → heading629e394d (eyebrow31825a3f, H2 3d727826, divider41bcab5a) + standard Elementor **Shortcode**02441ff. These page-local locators repeat across the copied sections; scope every lookup to its Page ID. No shared definition was changed and no CSS selector or business logic was added based on Page IDs.

Reused the existing Homepage review-section structure, native section/container/stack/layout-reset classes and local background/gap/heading/accent styles. H2 is **What GCPRO Customers Say** on every service page, so mixed service/general and shared Commercial selections do not imply that every review concerns that exact task or property type. Existing section typography, light-blue surface and mobile gutters remain native editable values. Trustindex owns carousel/Read More styles and JavaScript, including its existing Poppins exception. No plugin installation, custom HTML/JS/PHP/CSS, Global Class, Variable or reusable Component was added.

The Elementor MCP schema reports `Unknown widget type: shortcode`; its V3 content is not exposed by the lean tree read. Used the existing registered WordPress REST Elementor document metadata integration to insert the already working native Shortcode section, followed by a fresh native MCP subtree read, native H2 save and document publication. Exact saved shortcodes were read back. Water514's actual Elementor editor exposes **Edit Shortcode → Enter your shortcode** with the correct generated value; Publish is disabled after loading the saved result. This is a native Shortcode widget, not an HTML-widget/script workaround.

### Selection and mapping

[Canonical Page → widget name → Trustindex ID → generated shortcode → filters/fallback mapping](../integrations/2026-10-24-trustindex-service-review-mapping.csv). All shortcodes were copied from Trustindex's generated WordPress code field and matched to the saved Page and rendered `data-pid`; none were guessed.

| Selection | Eligible/displayed at verification | Use |
| --- | --- | --- |
| Water Damage tag | 77 eligible /10 displayed | Water514 |
| Fire & Smoke tag | 7 /7 | Fire517, Commercial Fire520 |
| Reconstruction tag | 62 /10 | Reconstruction518, Commercial Reconstruction524 |
| Contents Restoration tag | 25 /10 | Contents521, Commercial Contents525 |
| Storm Damage tag | 11 /10 | Storm523 |
| General Contracting tag | 19 /10 | Contracting522 |
| Mold fixed selection | 2 explicit Mold +3 general /5 | Mold516, Commercial Mold519 |
| Dehumidification fixed selection | 2 explicit dehumidifier +3 related Water /5 | Dehumidification491 |
| Commercial Water fixed selection | 2 explicit business-property Water +3 related Water /5 | Commercial Water515 |
| Existing general GCPRO widget | 10 displayed; no service-specific claim | Extraction487, Board-Up488, Odor489, Moisture490 |

The business-specific Water reviews describe a restaurant and a skilled nursing facility. Other Commercial pages share the relevant service widget because a distinct, useful business-only selection was not supported; no duplicate widget with identical selections was created. The fixed-selection review locators are recorded in the canonical mapping without review text or author data.

Trustindex's tag dropdown explicitly states **all of selected**: multiple tags are an intersection, not an additive fallback. The Order control supports random/newer-sooner/older-sooner; the approved template also prioritizes photos. These controls cannot promise service reviews first in a mixed set. Kept photo-first/newer-sooner, all-rating eligibility, maximum10, minimum1 character, no translation, four-line cards with Popup Read More, desktop arrows/mobile progress,6-second loop, lazy load and rich snippets off. Fixed selections are used where supplementation is needed and do not auto-update. No inaccurate tags or review text changes were made. Rating alone was not used to exclude criticism; dynamic tag pools retain their eligible critical reviews even when the current10-item display window does not include them.

### Verification and limits

[Sanitized saved/configuration/render evidence](../evidence/2026-10-24-trustindex-service-reviews.json).

- All17 saved shortcodes, published states, URLs, parent/title/template/page settings and authored SEO fields match the intended mapping/protected baseline. AIOSEO automatically refreshed its `updated` and analyzer-scan timestamps; no authored SEO settings changed. Removing only the new section from every after tree yields exact equality with its immediately-before page tree.
- Actual authenticated Chrome frontend renders at1440×1000 and390×844:34 checks. Every page has one review section and one initialized Trustindex widget with the expected public ID, correct GCPRO source metadata, intended review selection, contained cards and no document horizontal overflow. Desktop widget width1136px; mobile widget width335px with20px left gutter (15px scrollbar accounts for the viewport difference).
- Read More opens and closes the vendor popup on all17 desktop pages. Representative mobile Dehumidification popup also opened and closed through its separate native bottom **Close** control. The desktop close selector is intentionally hidden on mobile, not a broken popup. Screenshots inspected for balanced cards and preserved section styling. These are browser simulations, not physical-device tests.
- All17 ordinary public URLs returned unauthenticated HTTP200 with the current widget identifier. No stale markup was observed, so no global cache purge was necessary. Anonymous JavaScript execution/incognito rendering was not tested; authenticated browser behavior plus unauthenticated markup is not a claim of full guest runtime certification.
- **Inherited source-link limitation:** approved template `review-linked` is off. Rendered cards/popups have no source anchors; clicking the Google icon did not open a source page. The original Google source metadata/records are correct and preserved, but clickable original-review links are not delivered by this template. No unapproved display-setting change or custom link workaround was introduced.
- The original12 widgets, including both dental widgets, retain their names/IDs; only the9 new copies were configured. Original template named settings compare equal before/after. Existing projects, service links and CTA destinations are unchanged by exact protected-tree comparison; no unrelated site-wide link audit was repeated.

### Recovery

Private scoped recoverable snapshots live in the executing workspace `work/widget-backups/`: immediately-before REST document for each Page, original Homepage section, after readbacks and verification receipts. Raw admin responses are excluded from Git. Backups are document-scoped; no full-site database restore was tested.

Rollback only the inserted page-local section10a34543 on the affected Page, after checking for later owner edits, then save through Elementor and verify. This preserves the pre-existing content, including Board-Up comparisons. Restore from the scoped snapshot only where needed; never overwrite later unrelated work. New Trustindex copies can remain unused. Do not modify/delete older widgets or change their filters as part of rollback.
