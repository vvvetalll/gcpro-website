# GCPRO Resources — native Posts system

## Editorial pilot and quiet menu actions — 2026-10-30

Implemented on staging with ui-ux-pro-max guidance. Single Post123 and synced core pattern3159 remain the existing owners. Pale-blue full-width opening uses the site container, breadcrumb, white rounded topic chip, gray Montserrat700 H1, excerpt, two compact native publication/modified-date chips with decorative calendar/clock glyphs, and one4:3 featured image to the right; core Columns stack on narrow screens. Dates remain actual Post Date blocks; no invented byline, reading time, buttons, reviews or emergency mark. Body remains white with a centered760px reading column, Inter body text, gray Montserrat H2/H3, blue ordinary-weight links without orange underlines, and retained visible focus. User requested photo in the opening rather than duplicated below it.

Pilot Post2046 [Water Damage at Home: What to Do First](https://vitaliiv1.sg-host.com/what-to-do-if-you-notice-water-damage-in-your-home/) retains reviewed wording, URL, publication status, SEO fields, original date and featured media. Safety guidance is a warm#FFF7ED native Group with8px corners and NO colored side rule; existing factual observations form a pale-blue checklist. All six headings have native anchors with180px scroll offset. No TOC inserted because the short article does not need one. Three unsynced native patterns3435 Safety note,3442 Key points and3443 On this page are available in WordPress Patterns; inserted copies remain independently editable. Adjust TOC links to the actual article anchors when useful on a longer article. Other article bodies were not decorated or rewritten.

Single123 Post Content3307e90b is the sole scoped CSS owner for reading width, headings, links, anchor offset and opening alignment; superseded rules replaced there. Pattern3159 owns native dynamic header layout/typography/chips. No plugin, new field, per-post stylesheet or JS added. Final inset CTA80 unchanged. Archives124/2232 and SingleProject2231 protected settings compare unchanged. BeforeAfter493 Elementor data differs from the initial snapshot; this task made no writes to493, so the concurrent difference was preserved and not reverted.

Header113 primary Nav Menu7983af36 retains its existing sole Custom CSS owner. Removed decorative orange active inset and action outlines per owner steering; actions now have a very pale orange#FFF7ED fill, subtly stronger#FFEDD5 hover/focus, navy text and6px corners. Existing native links, order, main CTA and functional focus outline preserved. Ordinary menu items unchanged. This is not a claim of an exhaustive sitewide border audit. Source mirror is recovery documentation, not separately enqueued.

Verification: native saved settings and guest HTTP/HTML checks on pilot2046 and longer-title2050:200, one H1, noindex, self-canonical, one opening photograph, actual date fields; protected article fields unchanged. Archive124/2232 and SingleProject2231 settings unchanged;493 concurrent data difference preserved. Pilot AIOSEO differences are only updated/scan timestamps, not SEO title/description/canonical values. Saved menu rules checked. Actual Chrome screenshot observed the earlier split opening; final desktop/mobile screenshots, computed overflow, anchor-under-sticky and keyboard acceptance remain incomplete: the user stopped Computer Use with physical Escape after repeated simultaneous-input guards. No further Computer Use calls made. Settings/HTML checks are not browser acceptance.

Private recoverable pre-change snapshots remain outside Git in outputs/article-pilot-2026-10-30. Roll back native3159/123/113 settings and pilot2046 body from those snapshots through the supported editor/REST. No credentials, raw admin responses or private backups committed. Existing30-article SEO decisions and canonical URL inventory remain unchanged. Owner rejected the illustrative wall-staining cover as a weak visual choice; replacement selection remains outstanding and no uninspected replacement was silently substituted.


## Archive Hero and metadata badges — 2026-10-30 follow-up

Archive124 now begins with shared Archive Hero3421/instance4e42b37b, title **Restoration Resources**, concise introduction and inspected existing kitchen photograph3007 in the established blue masked design. Removed redundant6a876bcc heading block; native Menu43/6eb3c3c0 and automatic query/paginationa6bffe2 are byte-for-byte unchanged. Category pages use the same existing archive owner. Standard section96/56px spacing and photo sizing match the owner follow-up; no buttons/emergency/reviews or empty action wrappers in this Hero. [Component/Overrides/rollback](shared-hero.md#archive-hero3421--current-2026-10-30).

Single articles remain white. Existing synced3159 now styles actual topic and dates as compact native pale-blue badges: color-surface-alternate, color-border1px,6px topic/8px date radius,6×10px topic and8×12px date padding. Actual category/date fields remain dynamic; no invented dates.13px metadata, natural flex wrapping. Native core block attributes/inline serialization own these controls; **no additional CSS/JS**, new plugin or per-article styling. H1/excerpt/photo/body/finalCTA unchanged by this refinement.

Owner screenshot demonstrated category buttons painting over Header dropdown. Archive root29d73bf4 now uses native position:relative/z-index:0 to contain its descendants; removed unnecessary isolation declaration. No Header code/style/height change. Native readback verifies the stacking context, but controlled dropdown regression is still unverified due concurrent Chrome navigation/input guard. Do not claim this visual fix browser-accepted.

Guest HTTP checks: archive/representative article200/oneH1/noindex; topic navigation retained; two actual date fields inside two tinted groups. Prior editorial selection remains14Published/16Draft; no Post, SEO or status changes. Actual Chrome Projects layout observed; current Resources desktop/mobile acceptance incomplete. [Evidence](../evidence/2026-10-30-archive-hero-checks.json).

## Current owners and unfinished acceptance — 2026-10-30

The latest owner direction replaces the earlier split/pale-blue article masthead experiments below. Single Post123 and native synced pattern3159 now give a white editorial opening: breadcrumb, Resources/topic, original/modified dates, normal-case H1, concise excerpt, then one featured photograph. No emergency mark, review loader or sales action in the opening; final inset Component80 remains. Archive124/Card3133/Menu43 remain the existing automatic archive owners.

Pattern3159 uses native core Group (vertical Flex), Paragraph, Post Terms, Post Date, Post Title, Post Excerpt and Featured Image blocks. The original default Group emitted an additional inner-container, preventing the intended direct-child spacing; corrected to native vertical flow after the owner's screenshot demonstrated cramped metadata. Metadata is13px, H1 fluid28–40px/600, reading text18px desktop/16px mobile, reading measure760px. Photograph follows the introduction, max1040px wide and fluid220–360px high with cover fit/12px corners. Original media preserved, no duplicated cover widget. Long titles wrap naturally; no forced breaks/truncation.

Existing V3 Post Content3307e90b > Advanced > Custom CSS is the single scoped owner for native WordPress body typography, group spacing, captions, branded links and focus. Use `selector`, not a top-level ampersand: an earlier unscoped ampersand experiment was corrected in this task. H2 fluid22–24px, H3 20–21px; body760px, gray text, navy links with orange underline, visited consistent. Native Atomic101b691d uses existing container/page gutters,63c8b0fa owns responsive body size. No theme stylesheet, per-Post CSS/JS, new plugin or framework.

The complete30-article editorial review is implemented:6 Keep/8 Improve/6 Merge/10 excluded,14 Published/16 Draft. [Decision/evidence/launch proposal](../seo/2026-10-29-resources-selection.md#current-decision--full-30-article-review-2026-10-30). Original dates/URLs retained.2062 alone changed from legacy Atomic body to native Post body using supported WordPress fields; original Atomic tree and source body retained privately. Other excluded source content remains recoverable. AIOSEO remains sole title/description/canonical/schema owner.

Image review: original-site inline media are absent from all14 retained public pages. Inspected existing WebPs reused; no uploads or file replacements. Updated alt/title only for inspected3270/3293/3320. Replaced misleading humidifier, dense-smoke and imagined-worksite covers with relevant existing actual project photographs. Winnetka2056 uses2987 (Downers Grove wall staining), Mold2057 uses2852 (Carol Stream attic); captions now match.2047 caption accurately identifies boarded openings/fire damage. Shared cover use is illustrative and does not imply those projects occurred in the article city.

**Verification:** authenticated native readback plus unauthenticated HTTP/HTML for14 articles and4 project configurations; all200, exactly one H1, self-canonical, noindex, one opening photograph below H1 and no opening sales widgets. Archive12+2/14unique, populated categories8/2/3/1, affected internal links and proposed equivalent targets checked.52 Published project records compare unchanged for content, IDs, dates, status, URLs, featured media, ACF and taxonomies. [Machine-readable checks](../evidence/2026-10-30-editorial-template-checks.json).

**Not browser-accepted:** repeated Chrome simultaneous-input guard rejects navigation/input even after owner hands-off authorization. Current responsive styles/HTML checks do not prove actual mobile wrapping/crops, overflow, hover/focus, keyboard or gallery/lightbox runtime. Owner screenshots are visual evidence of the earlier defect, not acceptance of the final correction. No claim that this design is fully visually approved. No security bypass or alternate hidden browser automation. Single123 native editor preview (login required): https://vitaliiv1.sg-host.com/?p=131&preview=1&theme_template_id=123 ; use a retained article URL for real post-context review.

Rollback: restore private pre-change pattern3159/Single123 settings and source Post snapshots through native editors/REST; no recovery archive or credentials committed. Footer remains unchanged in this task; the separately requested Resources/legal separators/Back-to-top refinement is still pending.

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


## 2026-10-29 — Owner-directed Resources visual redesign

Staging only. Owner rejected the prior Resources appearance and authorized a full redesign of the archive, topic navigation, article cards and Single Post presentation. Dwell recent stories and This Old House supplied editorial references (large lead story, photography, clear hierarchy); no external content or assets copied. Existing post IDs, text, dates, URLs, categories, publication state, Header113, Footer114, shared service Hero1318 and Projects preserved.

Archive124 now shows a single automatic current-query loop: first item spans the grid with a 1.3:1 photo/text split, followed by three desktop columns, two tablet columns and one mobile column. Seven items per page; native reload pagination verified as seven plus five distinct articles. No second query or hand-picked duplicated feature. Existing Section Heading71 remains the archive introduction on a white surface. Menu43 stays native category/Page object links; topic chips wrap visibly on mobile instead of a hamburger. Article Card3133 has a full-bleed 16:9 photo, 24px/21px title, padded content, restrained action and native whole-card post link. Only Resource Card3133 changed; Project Card2233 was not modified in this redesign.

Single123 retains one Post Content3307e90b and native synced header pattern3159. ReadingContainer101b691d expands within the existing1200px boundary; the header becomes an inset pale-blue split composition with the actual featured image, while ordinary article text is centered at760px and inherits18px/1.75 body type. Mobile stacks the header content and image. Article titles, actual category and publication/update dates remain native core blocks. Existing inset CTA80 and native Resources/Request Service bindings preserved.

Native container/card controls remain the layout/style owners wherever supported. No new Global Classes, Variables, Components, media, JS, PHP, plugins or dependencies. Two demonstrated native gaps require scoped CSS: V3 topic-menu visual controls through the connector, and descendant layout of the core synced header emitted inside V3 Post Content. Archive first-item styling is a local, scoped layout exception on its existing loop layout, not global theme CSS. See CUSTOM_CODE.md for exact owners and a connector caveat.

Verification: live browser at1280px desktop and390px mobile; archive/topic links, category40 showing seven relevant posts, article one-H1/image/native dates,760px desktop text with31.5px line height and no horizontal overflow. Native Next click returned the remaining five distinct posts. Actual CSSOM checked: no bare top-level ampersand selectors remain. Final default viewport restored. Authenticated browser checks are not anonymous-delivery, physical-device, exhaustive keyboard or final owner visual acceptance. Production untouched. No cache purge claimed; ordinary browser reloads delivered current output after MCP publish.

Editing: Elementor Theme Builder Archive124 and Single Post123; shared Resource Card3133; Posts body/header pattern3159 stays editable with WordPress core blocks. MCP edits on published documents stage autosaves; publish-document is required to promote them. Readback performed after publication. Scoped pre-change tool snapshots kept privately in audit-temp/blog-redesign; older rollout recovery remains documented above. Reverting documentation alone does not restore WordPress.


### Final owner correction — 2026-10-29

Owner requested removing the oversized first feature and keeping the rest. Archive124 now uses an ordinary uniform3/2/1 card grid, six articles per page. Removed all first-item spanning and split-layout rules from380a3746; the first article remains a normal card, no post was deleted. Existing introduction/topic navigation, card design and Single123 remain unchanged. Browser1280px confirmed six cards, three equal378.7px columns, first grid-column auto and no horizontal overflow. Earlier lead-story/seven-per-page statements describe the superseded checkpoint. No new photo or hero was inserted; no new CSS owner or dependency. Native responsive rules retained.


### 2026-10-30 — Published service badges on card images

Owner explicitly approved scoped CSS after the native Post Terms/loop styling gap was demonstrated. Archive124 > Article Query a6bffe2 > Grid380a3746 > Item5485f36b contains Card4b582bfe (Component3133) and sibling classic Post Info2ef8cf7. Post Info displays Category terms, no icon, and uses CSS class `resource-category-badge`; native category destinations remain intact.

**Authoritative style owner:** Archive124 > Archive Settings > Advanced > Custom CSS. This is template CSS, not Custom Code903 and not theme CSS. The semantic selector `.elementor .resource-category-badge` survives Atomic loop cloning, which changes classic widget IDs and causes its original per-widget generated styling to miss clones. No scripts, custom fields or new plugins were added.

Rules: absolute inset12px auto auto12px; z-index2; inline-flex, widthauto, margin0; padding6px10px;1px color-border (#E5E7EB fallback); radius6px; white background; color-text; font-body/Inter12px600 with16px line height. Scoped icon-list items have zero margin/padding, and items/text/links inherit font and color; badge links have no text decoration. Native keyboard focus remains. Each badge is a sibling of the whole-card link, avoiding nested anchors.

Verification: native Publish completed/disabled; public blog rendered12 categories in white badges at photo top-left, with correct first-row Water Damage/Water Damage/Fire & Smoke values. Mobile Elementor preview showed the badge within a305px card (badge97.375px wide,12px offsets). Staging cache was purged; physical-device and anonymous-delivery checks were not performed. Source images and card action geometry were unchanged by this correction.

Earlier temporary Paragraphs1187540/89fc620, wrapperf1382b1 and root duplicate46fa232 were removed. Global class g-0d21740 was created during the unsuccessful native approach; it is not an active styling owner for the final rendered badges. Do not attach a duplicate rule to it. Rollback: remove only the service-badge block from Archive124 custom CSS (and the Post Info widget if removing badges entirely).

Remaining separate work: numeric pagination, estimated reading time and18 draft covers remain pending. Single article layout was deferred by the owner; reported mobile rendering issues on About/Signs of Hidden Water Damage were not reproduced in the desktop check.


### 2026-10-30 — Publish all legacy articles and source photos: checkpoint

Owner requested all articles and photos. Reused existing30 posts and already uploaded optimized original-site images; no duplicate posts/media created. Twelve additional drafts were published through the native WordPress editor with original featured images and source alt text:

| Post | Featured media |
|---|---|
|2048|3310|
|2049|3333|
|2050|3270|
|2051|3315|
|2052|3300|
|2053|3329|
|2054|3277|
|2055|3284|
|2058|3313|
|2059|3301|
|2060|3271|
|2061|3319|

Existing12 published posts were preserved. Thus24/30 are now published. Native publication state checked for each completed record; a public REST inventory verified the first19 published records and their correct featured-media IDs before the last5 were published. Legacy bodies/excerpts were retained; this was publication/photo work, not an editorial fact-check. Newly published records use WordPress's publication date at publish time. Original URLs/slugs/categories retained. Inline source-image URLs on2059 were replaced with their already-uploaded staging counterparts; earlier newly published2051–2053 still reference original-site inline images and require localization. Some legacy text still needs editorial review for unsupported statistics/company claims, outdated costs, safety statements and unresolved links before production launch.

**Unfinished6 drafts and intended covers:**2062→3276,2063→3328,2065→3334,2071→3304,2073→3305,2074→3281. Text and uploaded photo assets already exist. Do not recreate them.

Blocker: SiteGround served a Robot Challenge on opening2062. One reload led to an explicit image CAPTCHA. No CAPTCHA interaction attempted; per-action owner confirmation requested before solving. Do not evade it with alternate routes/network or disable security. Last publication2061 showed Published; no writes attempted to2062. Final30-item inventory, cache purge, blog pagination/frontend/photo checks remain pending until access resumes. Existing native12-per-page archive and image badges were preserved. No production changes.

A stale editor handle initially retained the prior published record; automatic review rejected retrying the publish routine until state was reconciled. Fresh URL/title/status and public inventory checks confirmed completed records; subsequent writes used an explicitly passed tab plus URL/title identity checks, avoiding mutable shared editor handles.

### 2026-10-30 — Whole-card interaction and editorial masthead

Read current native3133 rather than replacing owner edits: current16:10 image,20px title, grid details and separate Read article/arrow retained. Root4cc99b32 already has dynamic post-url; removed empty nested link configuration from label9ee7f6e (now span). Root hover/focus-visible now moves arrow014d067 by4px through the existing local native style owner; removed arrow-only hover. No JS, overlays or second anchor. Guest archive emits12 whole-card links,12 distinct URLs and zero nested anchors. Generated local3133 CSS contains both group states; keyboard focus outline retained.

Pattern3159 now uses native WordPress Columns55/45: category/title/excerpt/dates left,4:3 featured image right; native Columns stack below782px. Fluid28–40px title, restrained metadata; published/updated label and date stay grouped. Existing Single123 Post Content3307e90b CSS owner simplified: removed fragile legacy inner-container grid rules, retained body measure/spacing and focus styling. No duplicated template or article-body rewrites. Current saved card/image changes made since the previous checkpoint preserved.

Guest Winnetka sample returns one H1, two actual dates, native columns and noindex. Actual browser hover/mobile visual acceptance remains pending; emitted CSS/HTML is not a browser interaction test. Private native pre-change snapshots are in outputs/resources-2026-10-30 outside Git. Native template preview (editor login required): https://vitaliiv1.sg-host.com/?p=131&preview=1&theme_template_id=123 . Use the public Winnetka article for actual article-context review.


2026-10-30 owner correction: Single123/PostContent3307e90b explicitly aligns article paragraphs, headings and lists left. Existing centered760px reading-column position/width and opening structure retained. Native saved CSS readback checked; no body/URL/SEO changes.


2026-10-30 clarification: previous text-align change was visually ineffective because paragraphs were already left aligned. Owner meant the reading-column position. Single123/PostContent3307e90b now aligns the760px article body to the opening/site-container left edge using the existing container-max and fluid gutter, rather than centering that column. Saved setting verified; final computed browser alignment not certified.


2026-10-30 corrective fix: owner reported broken article layout. Saved readback demonstrated malformed nested selector wrappers/unbalanced braces introduced by reusing the connector style projection. Repaired the sole existing123/3307e90b CSS owner using complete generated widget-scoped selectors; native saved readback now39 balanced rule pairs. Left reading-column alignment retained. Future edits must read raw existing custom_css rather than reconstructing it from the tool style projection. No body, media, URL or SEO writes. Guest cache-busted article request returned403; final generated CSS delivery and browser visual acceptance are unverified.


2026-10-30 editor preview correction: Single123 still selected restricted starter demo Post131, explaining the ROBYLO text/emergency block visible in owner editor screenshot. Native document preview_id now2046, preview_type single/post. Saved readback verified. No demo, published article, frontend conditions or body content changed. Reload Elementor to apply the preview context. This corrects preview selection; the native3159 header remains block-editor-owned rather than independently selectable Elementor widgets.
