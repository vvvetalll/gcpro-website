# GCPRO Resources — native Posts system

Implemented on staging, 2026-10-29. Owner requested a clean editorial design first, publication for review, and a visual language consistent with Projects. Production unchanged.

## Configuration owners

| Owner | Editing location and responsibility |
| --- | --- |
| Existing Page2043, Restoration Resources | `/blog/`; reused original Draft object and slug. WordPress Reading → Posts page. Its body is not the archive layout. |
| Existing Archive124 | Elementor Theme Builder; one automatic current-query article archive and category presentation. Existing `include/archive`, `exclude/archive/search` conditions retained. Project Archive2232 remains the more specific separate owner; actual `/portfolio/` still renders2232. |
| Existing Single Post123 | Elementor Theme Builder → Single Post; `include/singular/post`. Editorial header through native synced pattern3159,800px left-aligned reading column, one Post Content slot, back-to-Resources Content binding and existing inset CTA80. |
| New Component3133, GCPRO — Resource Article Card | One reusable article card:4:3 cover, Inter18px/500 title, short16px excerpt, restrained Read article action. Root is the only native post-URL link; no nested links. Existing card/card--interactive classes, native focus outline and Variables. Projects Card2233 shares the restrained action treatment; project content and destinations are unchanged. |
| New native WordPress synced pattern3159 | “GCPRO — Editorial Article Header”: Resources label, native Post Title H1, excerpt, category, publication/modified dates and4:3 featured image. Referenced from each migrated body. Dates come from actual Post fields; formatting has one shared owner. No PHP/shortcode/custom date calculation. |
| New WordPress Menu43, GCPRO Resources Topics | All articles → existing Page2043; categories40 Water Damage,41 Fire & Smoke,42 Mold,44 Reconstruction. Native category object links. Nav Menu in Archive124: horizontal desktop; native mobile dropdown; current-item semantics supplied by WordPress. No location/sector filters or filtering framework. |
| Header113 / Primary Menu5 | New native Page menu item3153 Resources, child of existing About243. Existing items, URLs and ordering preserved. |
| Footer114 | One added Resources link in the existing wrapping legal/navigation group; native Internal URL → Content selects Restoration Resources2043. Existing footer structure/logo/contact links preserved. |
| Resources hub1007 | Existing `/resources/` retained as a broader reference hub. One existing Button59 instance added linking to Blog2043; no duplicate article query. |

Archive124 uses Section Heading71 inside the existing orange-accent wrapper, container/stack/grid-3 classes, approved Variables and native3/2/1 grid settings. Pagination is native Previous/Next with page reload; no AJAX/Load More code. Per-loop limit6, normal Reading limit10 preserved. Only populated categories are currently linked. When changing publication/category membership, remove any now-empty category from Menu43; automatic empty-category hiding is not claimed.

No new plugins, JS/PHP, HTML widgets, classes or variables. V3 Nav Menu6eb3c3c0 uses one scoped Custom CSS owner for branded controls because its visual styling controls are unavailable through the connector. Existing Header113 Custom CSS owns native ancestor/hover styling. Native Kit6 Theme Style owns ordinary link colors/font and article H2 typography. See CUSTOM_CODE.md. Shared service Hero definitions remain unchanged.

## Editorial workflow and style

1. Reuse the existing Draft Post and original path. Edit body in the WordPress block editor, not Edit with Elementor. Inactive legacy Elementor data remains recoverable privately; it is not the active body renderer.
2. Write a useful informational title, brief excerpt, relevant category and approved featured image. Put a reference to synced pattern3159 at the start of the body. It reads publication/modified dates automatically.
3. Use connected short paragraphs: the visible problem → implications for materials/building → decisions before cleanup/repair → appropriate next step. Use descriptive headings, concrete verbs and natural US English. Explain a technical term only when it helps a decision.
4. Remove invented experience, generic reassurance, location trivia, repetitive service sales copy, unsourced prices and unsupported operational claims. GCPRO does not perform mold testing. Do not imply storage/return logistics are confirmed.
5. Link informational guidance to its service/geo intent owner and relevant real cases. Do not reproduce full case narratives or convert articles into generic local-provider pages. Ordinary WordPress body links are native editorial links; Elementor navigation/CTA destinations use Content object bindings.
6. Preserve actual original dates from production. Update only when content changes. Do not invent authors or credentials. Current AIOSEO administrative author attribution remains a launch-review item; no visible unverified personal byline was added.
7. Use meaningful photographs, truthful location captions, and existing descriptive alt. A photograph from Carol Stream, Downers Grove or Tinley Park is labeled accordingly, never relabeled Glenview/Winnetka. Existing WebP assets1589/2987/2852 reused; inspected images, files/crops/metadata unchanged; no uploads or duplicates.

The style shares brand typography, spacing, restrained borders, image proportions, links and focus language with Projects. Content types, cards and navigation retain their distinct purposes: Projects taxonomy facets remain in Projects; Resources uses topic navigation. No universal filter layer was added.

## Demonstrated native limitation and correction

Atomic `post-date` inside Single123 output the template date (October29,2026) even when Post2057 correctly stored February6,2024. Both publish/modified variants were tested against actual HTML. Removed those incorrect template widgets. Core WordPress Post Date blocks through Post Content correctly render the article context, so synced pattern3159 now owns metadata. Actual `<time>` dates match source Posts and existing AIOSEO BlogPosting dates.

Initial new Page3136 collided with existing Draft Blog2043 and became `/blog-2/`. Corrected by publishing/reusing2043, assigning it as the Posts page, updating bindings, and trashing only the newly created duplicate3136. New template3135 was removed after consolidating the design into existing Archive124. Neither is an active implementation owner. No pre-existing page or legacy URL was deleted, redirected or renamed.

## Verification and limits

Anonymous HTTP checks: `/blog/`200/3 cards; each category200/1 correct card; all three original article paths200, correct title/H1/self-canonical, Single123, native body, WebP photo and source publication date;27 legacy Draft articles excluded. Native WordPress menu and Content bindings read back. All11 inspected internal service/geo/project/CTA paths200. Portfolio remains Archive2232. Existing noindex/nofollow and disabled sitemap generation retained.

Controlled pagination: temporarily2 articles per page, first page2 and next page1, with three distinct titles and no duplicate/skipped article. Actual relative native Next URL followed successfully. Restored normal Reading10 and loop6 afterward; no test content created or published.

Browser control could not reliably focus/navigate the intended Chrome tab through the available Windows tool. No completed desktop/mobile screenshots, actual overflow, hover, keyboard, dropdown or physical-device certification is claimed. Saved native responsive/focus settings and HTTP output are distinct from browser acceptance. Owner visual review remains pending.

Related automatic article cards deferred: current three selected articles cover distinct topics; useful contextual links are present. No duplicate query or manual article-ID selection introduced. Historical GA4 attribution, fuller GSC query joins and backlink verification remain in the selection record.

Private backups: `outputs/resources-2026-10-29/` outside Git, including original Posts, templates, Reading settings, menus and source content. Use native Theme Builder/Posts restore routes; do not paste raw Atomic JSON into REST. Reverting this rollout should restore the backed-up124/123/114, remove only newly added navigation/card/date-pattern items, and restore Reading assignment and selected Posts from backups. Do not touch Projects, BEAF or production.

See [article decisions](../seo/2026-10-29-resources-selection.md), [canonical inventory](../SEO_URL_INVENTORY.csv) and [actual HTTP/readback evidence](../evidence/2026-10-29-resources-verification.json).

## Current follow-up — 2026-10-29

Owner authorized useful-original-content expansion beyond the initial three and requested editorial metadata instead of sales actions.12 original Posts are now Published;18 legacy articles remain Draft, plus two preserved ROBYLO demos131/133 changed Private→Draft. No original URL changed.

Single123 no longer renders the service Hero. Breadcrumb27e07130 precedes ReadingSection7389f778; ReadingContainer101b691d is800px, left-aligned within the existing content boundary. Pattern3159 supplies the only article H1, excerpt, category, actual publication/update dates and featured photograph. Each body references this one native synced pattern. Existing bottom CTA80 remains; no reviews,24/7 mark or conversion buttons in the article masthead. No author or reading-time estimate invented.

Article Card3133 action65a5a25b and Project Card2233 action3b612ec are non-link spans inside their existing whole-card anchor: Inter14/500, no frame/underline, native180ms color/translate hover. No nested links. Kit6 native Theme Style links use primary/primary-hover and Inter; ordinary H2 uses24px Inter600. Archive124 uses heading61abce59 and native Menu43; light surface/topic-active navy styling is scoped to its V3 menu. Header113 existing CSS owner removes orange active lines and styles WordPress current_page_parent so Resources can indicate article ancestry.

All12 article ordinary guest URLs returned200 with exactly one H1, native featured image, both article dates and noindex. Shared pattern reference verified in every saved body. See resources-followup evidence. This is HTTP/readback verification; desktop/mobile appearance, browser focus/hover and overflow remain unverified because available browser control was unreliable. No claim that CSS readback proves visual acceptance.

Existing WebPs reused after full-size review:1589,2852,2868,2979,2980,2981,2987,2991,3014,3016,2721,2724. Captions distinguish initial damage, mitigation and completed finishes; no unrelated-room Before/After claim. Contents2071 remains Draft: insufficient confirmed scope and relevant approved photograph.
