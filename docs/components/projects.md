# Projects catalogue and detail pages — 2026-10-26

**Latest implementation:** [working ACF Free Projects prototype](projects-acf-prototype.md) supersedes the earlier no-install prerequisite block. Native CPT/service/sector queries and visitor filters now work on an isolated temporary archive. Existing manual Tabs below remain historical and unchanged; original project Pages were not migrated.

Published on staging only. Production was a read-only source; existing URLs, shared service/contact designs and BEAF records/files remain intact. The canonical register remains [SEO_URL_INVENTORY.csv](../SEO_URL_INVENTORY.csv), with325 rows preserved.

## Locations and editing

- [Projects1132](https://vitaliiv1.sg-host.com/portfolio/): existing Hero1318 preserved. Content container6ed6f7d holds Heading71 and native Atomic Tabs4fb075e2. Four Collection Loops read existing project Pages: All projects (2077/2078/2079), Fire restoration (2077), Water reconstruction (2078), Commercial reconstruction (2079). Edit each loop's native manual selection to change category membership. There is no separate project-body copy in a tab. Three published items do not warrant pagination; loops are configured for six per page with pagination off. Enable native pagination when the actual published collection grows.
- [Project Detail2125](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=2125&action=elementor): one native Theme Builder Single Page template, assigned only to2077/2078/2079. Shared Hero1318 gets dynamic Post Title, Post Excerpt and Featured Image. One Post Content slot sits between the Hero and existing Final CTA80. CTA uses native Request492 and verified telephone. Header113/Footer114 remain global owners. This narrow three-page assignment avoids changing unrelated Pages or the unassigned structural template1008.
- Individual Pages own their title, excerpt (verified city/service), featured image and unique native body. Body sections reuse section/container/stack, Heading71 with section-heading--accent, existing buttons and related-service object links. Photos are ordinary native Elementor **Gallery**, with Media File links and native lightbox/slideshow. Gallery settings remain editable in the visual editor; it is not a static-thumbnail substitute.

| Published page | Original path retained | Evidence and media |
| --- | --- | --- |
|2077 — Home Restoration — Tinley Park, IL|[Case study](https://vitaliiv1.sg-host.com/portfolio/from-ashes-to-excellence-tinley-park-home-restoration/)|Production portfolio12428 title/gallery; matching completed interiors in existing1218/1228. Gallery1218/1228/1230/1251; existing BEAF1200/1205.|
|2078 — Water Damage Reconstruction — Wonder Lake, IL|[Case study](https://vitaliiv1.sg-host.com/portfolio/restoring-elegance-water-damage-reconstruction-of-a-wonder-lake-residence/)|Production portfolio11471 title/gallery; exact kitchen/entrance/fireplace photo matches. Gallery1215/1219/1226; BEAF1199/1204.|
|2079 — Club Interior Reconstruction — Chicago, IL|[Case study](https://vitaliiv1.sg-host.com/portfolio/reconstruction-in-boys-and-girls-clubs-of-chicago/)|Production portfolio11388 title/gallery. Four distinct finished-space photographs imported as2134–2137,1600×1200 WebP,62–107KB. Existing club comparisons were not attached without an established same-project match.|

Production provided titles and galleries, not detailed narratives. Copy describes the evidenced damage, visible reconstruction and finished spaces only; no invented durations, dates, insurance outcomes, hidden methods or customer details. No review was associated with an individual project. The general company badge is inherited from the separately approved shared Hero.

## Native implementation and styling

Projects are existing preserved WordPress Pages, with no portfolio CPT or Page categories on staging. The owner approved native Tabs + Collection Loop after a working two-selection example. The example demonstrated distinct source items and dynamic links before catalogue rollout. Native Gallery was configured through the visual editor and tested with next/previous full-size navigation; connector non-support was not treated as an Elementor limitation. Temporary gallery/tab proof nodes were removed from Draft2075; its preserved original content remains Draft.

Cards reuse ba-card/ba-card__caption/ba-card__title, graphite headings and existing Blue Outline59. Images use4:3 cover crops; native grids use three/two/one columns. Tabs wrap on narrow screens. No custom CSS/JS/PHP, new plugins, dependencies or duplicate project Components were introduced for Projects. Existing vendor Elementor Gallery/lightbox and BEAF assets remain the runtime dependencies. The separately approved Header CSS exception is recorded in [Header menu refinement](header-menu-refinement.md).

Gallery layout is two columns for four photographs, three for Wonder Lake's three photographs, two tablet/one mobile. Project comparison pairs reuse grid-2. Full-size sources retain their original proportions. Page-specific related services use native object links: residential Fire517/Water514/Reconstruction518, commercial Reconstruction524/Commercial499.

## Before & After493

[Before & After](https://vitaliiv1.sg-host.com/before-and-after/) retains all20 existing shortcodes and original image pairings, using the approved BA card classes. Shared Hero1318 supplies the page H1; existing Heading71 is H2. Four native groups organize Fire Restoration (6), Residential Reconstruction (9), Commercial Renovations (3), Mold Removal & Exterior Repair (2). Card titles are H3. Five native View Project actions connect the two exact Tinley comparisons and three matched Wonder Lake comparisons. Unknown locations remain unfilled. No guessed case-study association was added for the other comparisons.

No compatible BEAF filtering was established without changing its existing integration, so the page uses explicit groups rather than a purported interactive filter. Native Tabs filter the Projects catalogue only. No BEAF files, slider settings, record media, popup code, labels or Kit styling were changed.

## Verification and limitations

Desktop browser: catalogue has three photographic cards, four category tabs return the correct selections, and native image/button destinations resolve to the three published case studies. All three project bodies and their related service/CTA URLs were read in the frontend. Native Gallery proof opened full-size images and navigated1/2→2/2; Tinley Gallery navigated1/4→2/4 and closed. BEAF fullscreen opened and closed. Automated mouse attempts did **not establish divider movement**, so drag operation is not certified by this pass; the vendor implementation was preserved. Existing BEAF keyboard-slider/dialog limitations remain.

At393px, catalogue, Before & After and all three project pages have one H1, page width378px within the393px viewport, and no horizontal overflow. Project galleries contain4/3/4 images; no broken main IMG elements were observed. Mobile navigation opens with Enter and the Residential submenu opens. This is desktop browser emulation, not physical-device or screen-reader certification. Desktop/mobile screenshots are retained in workspace outputs (`projects-catalogue-desktop.png`, `projects-catalogue-mobile.png`, `project-gallery-mobile.png`, `before-after-groups-desktop.png`). Owner visual acceptance remains pending.

Fresh anonymous HTTP requests returned200 for all five published destinations and each response contained noindex. Guest interaction was not tested separately. [Sanitized checks](../evidence/2026-10-26-projects.json). Existing AIOSEO configuration, URL slugs/hierarchy, forms and staging indexing restrictions were preserved.

## Remaining preserved drafts

Ten existing project Pages remain Draft, excluded from the catalogue:2075 Oak Brook remodeling;2076 Western Spring water restoration;2080 Chicago facade/windows;2081 Glenview reconstruction;2082 West School Street fire restoration;2083 Montana Street water reconstruction;2084 St. Charles interior renovation;2085 Helen Berkun bathroom;2086 Green Oaks Apartments/Palos Hills;2087 Helen Berkun facade. Their original paths/source galleries remain in the canonical inventory. They were outside the first three-project wave, not discarded.

Their remaining work is a verified concise account of the specific scope/result beyond the source title/gallery, selection/local optimization of source photographs, and confirmation of any proposed BEAF match. Dates, duration, exact work methods, insurance outcomes and project-review associations are not supplied by the source and must remain omitted unless verified. No invented city, project result or review is needed to fill a template slot.

## Recovery

Private pre-change snapshots are in workspace work/projects-2026-10-26, excluded from Git. To withdraw this wave: return2077/2078/2079 to Draft and remove them from native catalogue selections; unassign template2125 before restoring their old page bodies. Restore only1132's scoped content and493's original gallery grouping if needed, retaining later owner edits and existing BEAF assets. Keep the imported media for recovery; do not delete shared assets. No production rollback is required.
