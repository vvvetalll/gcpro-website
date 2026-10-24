# Measurement methodology, access and limitations

## Current sources and access

GitHub MCP read main instructions, current context/changelog/workflows, October23 rollout and approved-ownership record, plus October22 architecture, SERP observations and research limitations. October22 `SERP_TOP10.csv` was reused from a local copy only after its Git blob hash exactly matched current remote `00eb82cb000cc81f15a4b0270e22777eb37f0395`; other dated page-content exports were not used as current staging content.

Current WordPress REST `GET /wp-json/wp/v2/pages?include=...&per_page=100&context=edit` returned all17 IDs, current URLs and `publish` statuses. The connected Chrome frontend then rendered all17 actual routes in its existing authorized WordPress session. Authenticated rendering is not proof of identical anonymous delivery. Public HTTP for Water514 returned403; no cache purge, protection bypass or page mutation was performed. All requested page content was accessible in the browser, so there is no zero-content or missing-page row. No target requires a Draft preview today. A separate read-only MCP structure check of Draft970 earlier established draft-object access, but that design concept is not one of these17 services and is not audited here.

The remote Elementor endpoint successfully handled initialize and session-bound tools/list plus tools/call for Homepage154 and Draft970. This was a direct MCP protocol client, **not** automatically installed ChatGPT tool bindings. Initial tools/list without session returned HTTP400; initialize plus the returned session header resolved it. WordPress status reads and rendered page reads are separate evidence, not inferred from tool availability.

## Counting rules

1. Read the current rendered DOM in Chrome, at its normal desktop viewport; no cached exports/templates used as page content. For GCPRO select the inner page main within the theme main. For competitors select main, role=main, #content, or body when no main exists. Include a service hero containing H1 outside main when needed (notably Romexterra). A header/footer label alone is not allowed to erase an editorial hero.
2. Traverse each included element’s direct text nodes once, rather than summing nested container text. Collapse whitespace. Exclude scripts/styles/noscript, iframes, forms, site banner/nav/footer, admin toolbar, modal/dialog/popup regions and hidden responsive versions. Do not use whole-document source word counts. Browser innerText was not used by itself because it drops collapsed FAQ answers.
3. Use computed display/visibility to remove hidden responsive duplication. Include the text of relevant native details accordions and recognized FAQ/accordion content even while collapsed. Count the question once and its answer once, including lists. Do not append answer text a second time after counting its DOM nodes. GCPRO has six native details answers per page:102 answers total. Other competitor accordion formats were inspected; RestoPros, McMahon and Zaba were re-extracted with FAQ/accordion containers included because initial counts omitted their hidden answers. ATI hidden FAQ answers were also included in the final reads. Empty answers are not fabricated.
4. Tokenize normalized text with Unicode letter/number sequences, allowing internal apostrophes and hyphens. Numbers, visible button labels and task-related conversion copy inside main count as words. Punctuation/icons do not. Word counts are descriptive measurements, not a quality score.
5. Remove unrelated global regions that appear inside main using observed boundaries. GCPRO: exclude the generic shared Why GCPRO block and Water’s global coverage block. Retain task-related CTAs, project captions, service links with explanatory copy, substantive safety guidance and FAQ. Competitors: remove menus, unrelated service/article promotions, global contact/footer material, generic franchise bios, unrelated review widgets and large coverage lists. Keep task-related process, proof captions, useful task FAQs and relevant service handoffs. GCPRO raw-versus-adjusted deltas and competitor raw-versus-adjusted deltas are recorded. A proof widget may be observed as a credibility element without all its unrelated testimonial text inflating editorial depth.
6. Exact-shared counts: normalize each GCPRO H1/H2/H3, paragraph/list and summary block; exclude standalone numbering. Count a block as shared when identical text of at least4 words occurs on at least2 different target pages. Sum occurrences on that page. Other blocks are “non-repeated,” not automatically service-specific. Their sum covers editorial blocks only and excludes much link/UI text; it is intentionally not forced to equal the main total. Semantic review separately identifies paraphrased generic content, e.g. “describe/review/agree” processes, which exact-match counting cannot detect.
7. Retained H1/H2/H3 counts exclude removed global regions. FAQ questions rendered as summary/paragraph are not incorrectly promoted to H3. Project captions actually using H2 are recorded as such; their heading level is not proof of greater substance. Original structures remain in GCPRO evidence for traceability. Assessment of substance uses actual words/answers, not the number of planned components.

## Manual exclusion boundaries and reproducibility

The evidence JSON preserves final counts, initial DOM counts, exclusion deltas, date, URL, heading level order and H1 and main-text hash for competitor pages. Full competitor bodies remain private scratch analysis and are not republished. GCPRO’s current rendered text/blocks/FAQ and status metadata are included so its measurements and shared-text analysis are inspectable. A new extraction can change because a site changes, widgets load differently or desktop visibility differs.

Observed removal boundaries:

| Site / family | Unrelated regions excluded |
|---|---|
| GCPRO | Why GCPRO shared brand block before next substantive section/FAQ; Water coverage block before FAQ |
| ATI | Office contact block before service introduction; Chicago Services navigation before next service section; general review block before case studies |
| Roto-Rooter | Plumbing-services navigation; metro list; related plumbing links; financing/resource promo suffix |
| GoDry | Repeated all-service marquee; shared other-disaster recovery and mismatched mold CTA/review suffix after the water-specific conversion section |
| Romexterra | All-service subtitle; site footer/nav already outside main. Hero plus main are both included |
| ServiceMaster Lincoln Park | General review widget between testimonial heading and fire-cleanup section |
| Restore storm | Global story/review block before the service FAQ |
| RestoPros | Large service-area list and unrelated four-service promotion; relevant rebuild FAQs retained |
| PuroClean | Navigation prefix, generic testimonial widget, unrelated services/blog/footer suffix; relevant current-page FAQ remains, even where its subject is generic |
| Excel | Global service promotion and water-only FAQ subsection; specific contents-cleaning answer retained |
| ServiceMaster Elite | Large shared service-area suffix |
| ServiceMaster Zaba | Generic review widget before contents-specific company explanation; relevant contents FAQs retained |
| SERVPRO | Quick Links, Services We Provide and jump navigation; generic franchise bio and unrelated review text; extraction/drying knowledge-center FAQ retained after removing the preceding review widget |
| Chicago Fire Repair | Global review/contact/city/article suffix after service/insurance section |
| Alpha | Repetitive coverage city-list block; project/offer/process/business FAQ retained |
| STOP | Generic reviews; actual service scope and journey retained |
| Am-Cat | Map, unrelated FAQ links and full services menu after Service Areas |
| Restoration Partner | Full site-menu prefix; other-services navigation; generic network bio |
| Restotech | Other-services/city-map suffix |
| SRP | Generic company slogan, useful links, news and location/footer suffix |
| ServiceMaster RCS | Global office/contact/footer block after the actual odor explanation |

Manual boundaries were applied to the current DOM strings and checked against heading/paragraph reads. These are audit measurements, not a perfect automated visual-page segmentation claim. Deferred third-party content, unrecognized hidden widgets and future frontend changes can alter counts. Whole mixed-audience pages remain explicitly labeled where no three clean business-only equivalents were established. The benchmark is not word-perfect attribution of every sentence to an audience.

## Competitor discovery, current search and rankings

Start: current October22 research, especially SERP_TOP10, SERP_RESULT_REVIEW, GCPRO_ARCHITECTURE and EVIDENCE_AND_LIMITATIONS. The latter explicitly says its old source counts include navigation/footer; those counts were **not reused**.

Current verification on24 October2026 used available search engines for Chicago water; fire/smoke; mold/commercial mold; storm/reconstruction; contents; commercial water/fire/reconstruction/contents; commercial contracting; extraction/board-up; odor; mapping/dehumidification. Stronger search was used to obtain direct commercial-fire and reconstruction service equivalents. Current service-page links also supplied narrower transactional children.49 unique competitor landing pages were successfully rendered and measured. The17 groups each reference3 inspected pages; overlap is explicit. No ranking position was inferred from search-engine return order.

No new observed Google SERP positions, fresh Ahrefs estimates or GSC metrics are claimed. October22 Google observations remain historical under their recorded signed-out desktop /60026 Glenview /hl=en/gl=us/pws=0 conditions. Its “observed distinct organic order” is not a universal rank. Ahrefs estimates are a separate historical dataset and are not substituted for live Google positions. Open Ahrefs/GSC/Ads tabs were observed, but no additional account analysis was needed for editorial depth; their presence is not a claim that current reports were read. No paid Ads work was performed.

## Access gaps and recovered extractions

- GCPRO anonymous Water HTTP403: authenticated browser read succeeded. Anonymous delivery equivalence is unverified, not zero content.
- EHC first browser navigation timed out; one later read succeeded and supplied the final measurement.
- Chicago Fire Repair first read encountered a null body during navigation; one later DOM-content-loaded read succeeded and supplied the final measurement.
- Accurate Board-Up water-extraction candidate timed out. It is excluded from all counts/medians; three other direct extraction/drying service landings were measured. No repeated retry loop.
- Some candidates were not used as primary matches: generic homepages, roofing-only pages, long mapping articles and residential-only service pages for business comparisons. Commercial contents, commercial reconstruction and moisture-mapping equivalence limits are detailed in COMPETITORS.md.

## Verification and changes

Checked17 unique IDs/current URLs/statuses,6 nonempty FAQ answers per page, group references/ranges/medians, matching main-count tokens, removal deltas, document paths and intended documentation-only file set. No page settings, content, SEO fields, designs, credentials or publication state changed. No form submitted or telephone call placed. No private response headers, credentials, session tokens or admin dumps are included. Commit/push verification is reported with the final remote commit rather than asserted in advance.
