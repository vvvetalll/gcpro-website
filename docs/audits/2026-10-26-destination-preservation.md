# Destination preservation — 2026-10-26

Canonical editing location: [SEO_URL_INVENTORY.csv](../SEO_URL_INVENTORY.csv). This audit is evidence and implementation history, not a competing inventory. [Sanitized verification and new-object locators](../evidence/2026-10-26-destination-preservation.json).

## Result

- All **321 existing register rows and their original URL/query identities retained**; four discoveries added, total **325**. Nine preservation columns record purpose, sources, dependencies, readiness, next action, exception and actual staging preview URL. Earlier redirect proposals/history remain intact.
- **133 source content objects reconciled:** 90 Pages (88 published, 2 drafts), 30 articles, 13 portfolio projects. **82 existing staging counterparts reused; 51 missing objects created.** This is a count of source content objects, not 325 authored Pages.
- **51 new objects:** 8 Pages (six formerly published source destinations plus two source drafts), 30 native WordPress article drafts, 13 native Page drafts under the existing `/portfolio/` parent1132. Only the complete `/thank-you/` confirmation copy is published on staging; the other **50 remain Draft**.
- Register resolution counts: **95 matched-published rows, 54 matched-draft rows, 176 explicit exceptions**. Counts include preserved aliases and staging-only records. Exceptions are not working staging routes: technical/plugin endpoints, templates, archives/feeds, unresolved variants and unevidenced proposals remain concrete launch dependencies.

## QR and print evidence

**`https://gcprochicago.com/connect/` — production15438** explicitly says “Thank you for scanning our QR code!” and asks the visitor to save the GCPRO contact, call or use the footer contact form. Its exact-path staging counterpart is Draft2040. The original Save-to-phone link contains backslashes; its normalized resource `https://gcprochicago.com/wp-content/uploads/gcpro/GCPRO.vcf` returns HTTP200, `text/x-vcard`. Staging retains a native link to that verified production resource and the verified `tel:+18476563322` link. The original footer message form was not restored on this landing. Existing Contact/Request forms were not modified or submitted. The unsupported “form below” sentence is omitted from the Draft. **This QR flow is preserved for completion, not launch-ready.**

Local `BRANDBOOK/BAIDGE/qr.jpg` and `qr-600.jpg` decode to **`https://gcprochicago.com/testimonials/`**, whose existing staging counterpart is retained. `qr_code_review.png` decodes to **`https://g.page/r/Cdb2XI1wTDVjEBM/review`**. That external review destination is recorded without an unnecessary WordPress copy. No reviewed local artwork was proven to encode `/connect/`; its QR purpose is established by its live content, not inferred from these other codes.

100 brandbook business-card and marketing-kit PDFs were inspected for text and link annotations; extracted printable domain was `gcprochicago.com`. Selected back/flyer embedded images yielded no additional decoded QR destination. This does not exhaust vector/image-only print artwork, campaign accounts or externally hosted QR management records.

## Newly preserved special Pages

Draft links require a logged-in WordPress editor. Original intended paths are in the canonical register; Draft query URLs do not activate those public paths.

| Production ID | Original path | Staging counterpart / ID | Status |
| --- | --- | --- | --- |
| 21723 | `/service-area/service-area-bridgeview/` | [Bridgeview](https://vitaliiv1.sg-host.com/?page_id=2039&preview=true) — 2039 | draft |
| 15438 | `/connect/` | [Welcome to GCPRO Restoration](https://vitaliiv1.sg-host.com/?page_id=2040&preview=true) — 2040 | draft |
| 8136 | `/test2/` | [test2](https://vitaliiv1.sg-host.com/?page_id=2041&preview=true) — 2041 | draft |
| 2406 | `/corporate-signatures2/` | [Corporate signatures](https://vitaliiv1.sg-host.com/?page_id=2042&preview=true) — 2042 | draft |
| 2187 | `/blog/` | [Blog](https://vitaliiv1.sg-host.com/?page_id=2043&preview=true) — 2043 | draft |
| 456 | `/thank-you/` | [Thank you](https://vitaliiv1.sg-host.com/thank-you/) — 2044 | publish |
| 15553 | `(unpublished; no proven path)` | [Elementor #15553](https://vitaliiv1.sg-host.com/?page_id=2088&preview=true) — 2088 | draft |
| 11856 | `(unpublished; no proven path)` | [Barlett](https://vitaliiv1.sg-host.com/?page_id=2089&preview=true) — 2089 | draft |

The 30 article and 13 project titles, original URLs, native object IDs and Draft preview links are recorded individually in the canonical CSV and evidence JSON. The native post permalink template was verified as `/%postname%/`; project Page drafts retain `/portfolio/%pagename%/`. The staging portfolio CPT is absent: using native child Page drafts preserves original paths and content without installing a plugin or pretending that source taxonomy/lightbox behavior has been restored.

## Remaining readiness gaps

- `/connect/`: VCF migration/approved resource destination and verified message-form route.
- `/blog/`: native posts index, archive/pagination behavior and article publication/taxonomy/date/SEO review. Existing `/resources/` is preserved and is not treated as an exact replacement.
- `/corporate-signatures2/`: public business-signature text/images retained, email-client template/copy fidelity not recreated.
- `/test2/`: experimental source, placeholder heading/countdown, unconfirmed claims and alternate phone; retained as Draft for owner review.
- `/service-area/service-area-bridgeview/`: exact source route retained in Draft2039 while existing `/service-area/bridgeview/`531 remains unchanged. Historical MERGE/301 proposal has not been executed.
- Source Drafts15553 and11856 (`Barlett`): authenticated list confirmed both empty saved slugs; previews have no authored page body. Titles and parent identities retained without inventing historical public URLs or content.
- Articles/projects: source text and available images/galleries retained in editable native elements; image URLs still reference production. Gallery interactions, image migration and historical claims require review before publication.
- `/team/`: independently returns production404 and has no evidenced source object. No invented team placeholder.
- Legacy BEAF/query/template/taxonomy/archive/feed endpoints: see each row's explicit exception and next action. Existing plugin objects and working galleries were not altered or claimed to be equivalent solely from appearance.

## Verification, scope and rollback

Production was read-only. Fresh unauthenticated REST returned88 Pages,30 Posts and13 portfolio projects. Authenticated production Pages administration showed90 total/88 published/2 drafts. Production robots/sitemap index was reachable: Page sitemap83 URLs, Post sitemap31 URLs. Homepage plus public rendered content yielded138 unique internal links; only the bare-host root variant was absent from the original register. Historical administrator/content inventories supplement current discovery. No fresh authenticated non-Page draft/private inventory or external campaign-console inventory was obtained; **this inventory is not claimed exhaustive**.

All51 new records were read back: expected native Atomic content, status, slug and parent verified. The **94 pre-existing staging Pages are byte-for-byte unchanged in the captured fields, including Elementor metadata**, after creation. No existing form, component, navigation, redirect, Reading Setting, SEO or staging noindex setting was modified. `/thank-you/` returns200; browser confirms exact confirmation copy, one H1, no horizontal overflow and `noindex, nofollow`. QR Draft browser confirms welcome/contact content and both native destinations; no call, contact import or form submission was performed. The 50 Drafts intentionally are not public links or navigation items.

Implementation uses existing native section/container styles and reusable Section Heading71, native paragraphs, buttons and images. No new component, CSS/JS/PHP, dependency, plugin or duplicate WordPress media upload. Private source captures and temporary discovery tools remain outside Git; committed evidence omits raw admin responses, credentials and signature contact lists.

Rollback: use the evidence JSON's `created` IDs2039–2089 to move **only these newly created objects** to WordPress Trash if required; no destructive operation was performed. Existing94 Pages/shared components require no rollback. Inventory/documentation can be reverted through this commit while preserving dated history; never restore by modifying production.

Remote integration: retained the parallel Oct24 page-completion/policy/enquiry documentation and CSV field changes; reused its existing SMS1952 inventory row instead of creating a duplicate. Fresh Oct26 observation timestamps and preservation columns are additive.
