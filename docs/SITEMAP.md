# Complete GCPRO hierarchical sitemap

Current E76, 2026-10-21. **321 migration-register records; 93 actual staging Pages: 88 Published / 5 Draft.** Business/Partner Pages: 86 Published / 2 Draft; five unrelated fixtures: 2 already Published / 3 Draft, unchanged. Publication is for staging structure review, not finished content or production launch. Source-only tables below retain E73 production observations; no new production inspection or mutation was performed in E74/E75.

[Canonical migration register](SEO_URL_INVENTORY.csv) · [Staging Pages](https://vitaliiv1.sg-host.com/wp-admin/edit.php?post_type=page&orderby=title&order=asc) · [Primary menu5](https://vitaliiv1.sg-host.com/wp-admin/nav-menus.php?action=edit&menu=5) · [Utility menu15](https://vitaliiv1.sg-host.com/wp-admin/nav-menus.php?action=edit&menu=15)

## Current Header hierarchy

Primary: Residential → Commercial → Service Areas → Projects → About. Desktop utility: Partner Programs (four existing children), Careers, **Blog pending migration**, Contact Us. Mobile/tablet: one native hamburger menu containing the five primary sections plus Partner Programs, Careers and Contact Us. About contains About GCPRO and Testimonials; **Our Team has no staging destination and stays pending**. Apply is available from Careers. These navigation choices do not change Page parents or URLs.

| Section | Actual staging destination | Placement |
|---|---|---|
| Residential | [Residential Services](https://vitaliiv1.sg-host.com/residential-services/) | Primary |
| Commercial | [Commercial Services](https://vitaliiv1.sg-host.com/commercial-services/) | Primary |
| Service Areas | [Service Area](https://vitaliiv1.sg-host.com/service-area/) | Primary |
| Projects | [All Projects](https://vitaliiv1.sg-host.com/portfolio/) | Primary and All Projects child; Before & After second child |
| About | [About Us](https://vitaliiv1.sg-host.com/about-us/) | Primary |
| Partner Programs | [Partner Programs](https://vitaliiv1.sg-host.com/partner-programs/) | Utility desktop; hamburger mobile |
| Resources | [Resources](https://vitaliiv1.sg-host.com/resources/) | Retained page; removed from Header; not a Blog substitute |

Staging Reading → Discourage search engines checked before publication; anonymous pages emit noindex,nofollow. This is not access protection. E74 anonymous HTTP checks:84/85 business URLs return200 with one H1 and noindex; `/contact-us/` returns nginx403 to that client. New E76 `/portfolio/` also returns403 to the external anonymous client, while the connected admin browser opens its page. No security bypass/change was attempted.

## Actual staging Page hierarchy

ACTUAL means a saved WordPress object; Published routes link to the frontend, Drafts link to admin only. Unrelated fixtures/experiments and legal Drafts remain outside navigation. Native shared structural template1008 supplies one H1 and a development notice to80 Pages; Partner Pages982–986 retain their own Atomic shells.

- **ACTUAL [All Projects](https://vitaliiv1.sg-host.com/portfolio/)** — ID1132, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1132&action=edit); E76 structural index only, no project records imported

- **ACTUAL [About Us](https://vitaliiv1.sg-host.com/about-us/)** — ID497, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=497&action=edit)
  - **ACTUAL [Careers](https://vitaliiv1.sg-host.com/about-us/careers/)** — ID534, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=534&action=edit)
- **ACTUAL [Apply](https://vitaliiv1.sg-host.com/apply/)** — ID486, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=486&action=edit)
- **ACTUAL [Before And After](https://vitaliiv1.sg-host.com/before-and-after/)** — ID493, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=493&action=edit)
- **ACTUAL [Board Up](https://vitaliiv1.sg-host.com/board-up/)** — ID488, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=488&action=edit)
- **ACTUAL [Commercial Services](https://vitaliiv1.sg-host.com/commercial-services/)** — ID499, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=499&action=edit)
  - **ACTUAL [Fire & Smoke](https://vitaliiv1.sg-host.com/commercial-services/fire-smoke/)** — ID520, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=520&action=edit)
  - **ACTUAL [General Contracting](https://vitaliiv1.sg-host.com/commercial-services/general-contracting/)** — ID522, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=522&action=edit)
  - **ACTUAL [Mold Removal](https://vitaliiv1.sg-host.com/commercial-services/mold-removal/)** — ID519, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=519&action=edit)
  - **ACTUAL [Personal Property Restoration](https://vitaliiv1.sg-host.com/commercial-services/personal-property-restoration/)** — ID525, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=525&action=edit)
  - **ACTUAL [Reconstruction](https://vitaliiv1.sg-host.com/commercial-services/reconstruction/)** — ID524, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=524&action=edit)
  - **ACTUAL [Water Damage](https://vitaliiv1.sg-host.com/commercial-services/water-damage/)** — ID515, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=515&action=edit)
- **ACTUAL [Contact Us](https://vitaliiv1.sg-host.com/contact-us/)** — ID496, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=496&action=edit)
- **ACTUAL [Copyright](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=494&action=edit)** — ID494, **draft**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=494&action=edit)
- **ACTUAL [Dehumidification](https://vitaliiv1.sg-host.com/dehumidification/)** — ID491, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=491&action=edit)
- **ACTUAL [Elementor #7](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=7&action=edit)** — ID7, **draft**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=7&action=edit) — unrelated existing fixture/experiment
- **ACTUAL [GCPRO Homepage — Phase 1 Atomic Wireframe](https://vitaliiv1.sg-host.com/)** — ID154, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=154&action=edit)
- **ACTUAL [GCPRO — Coming Soon](https://vitaliiv1.sg-host.com/gcpro-%d0%bd%d0%b5%d0%b7%d0%b0%d0%b1%d0%b0%d1%80%d0%be%d0%bc/)** — ID12, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=12&action=edit) — unrelated existing fixture/experiment
- **ACTUAL [Hero Concept B — Restoration Transformation](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=970&action=edit)** — ID970, **draft**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=970&action=edit) — unrelated existing fixture/experiment
- **ACTUAL [Moisture mapping](https://vitaliiv1.sg-host.com/moisture-mapping/)** — ID490, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=490&action=edit)
- **ACTUAL [Odor Removal](https://vitaliiv1.sg-host.com/odor-removal/)** — ID489, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=489&action=edit)
- **ACTUAL [Partner Programs](https://vitaliiv1.sg-host.com/partner-programs/)** — ID982, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=982&action=edit)
  - **ACTUAL [Commercial Partnership Programs](https://vitaliiv1.sg-host.com/partner-programs/commercial-partnership-programs/)** — ID986, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=986&action=edit)
  - **ACTUAL [Condominium / HOA Program](https://vitaliiv1.sg-host.com/partner-programs/condominium-hoa-program/)** — ID985, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=985&action=edit)
  - **ACTUAL [Insurance Agent Program](https://vitaliiv1.sg-host.com/partner-programs/insurance-agent-program/)** — ID984, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=984&action=edit)
  - **ACTUAL [Plumber Support Program](https://vitaliiv1.sg-host.com/partner-programs/plumber-support-program/)** — ID983, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=983&action=edit)
- **ACTUAL [Privacy Policy](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=3&action=edit)** — ID3, **draft**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=3&action=edit)
- **ACTUAL [Residential Services](https://vitaliiv1.sg-host.com/residential-services/)** — ID484, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=484&action=edit)
  - **ACTUAL [Fire & Smoke](https://vitaliiv1.sg-host.com/residential-services/fire-smoke/)** — ID517, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=517&action=edit)
  - **ACTUAL [Mold Removal](https://vitaliiv1.sg-host.com/residential-services/mold-removal/)** — ID516, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=516&action=edit)
  - **ACTUAL [Personal Property Restoration](https://vitaliiv1.sg-host.com/residential-services/personal-property-restoration/)** — ID521, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=521&action=edit)
  - **ACTUAL [Reconstruction](https://vitaliiv1.sg-host.com/residential-services/reconstruction/)** — ID518, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=518&action=edit)
  - **ACTUAL [Storm Damage](https://vitaliiv1.sg-host.com/residential-services/storm-damage/)** — ID523, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=523&action=edit)
  - **ACTUAL [Water Damage](https://vitaliiv1.sg-host.com/residential-services/water-damage/)** — ID514, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=514&action=edit)
- **ACTUAL [Resources](https://vitaliiv1.sg-host.com/resources/)** — ID1007, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1007&action=edit)
- **ACTUAL [ROBYLO — Atomic Foundation Validation (Temporary Draft)](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=50&action=edit)** — ID50, **draft**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=50&action=edit) — unrelated existing fixture/experiment
- **ACTUAL [Sample Page](https://vitaliiv1.sg-host.com/sample-page/)** — ID2, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=2&action=edit) — unrelated existing fixture/experiment
- **ACTUAL [Service Area](https://vitaliiv1.sg-host.com/service-area/)** — ID495, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=495&action=edit)
  - **ACTUAL [Algonquin](https://vitaliiv1.sg-host.com/service-area/algonquin/)** — ID550, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=550&action=edit)
  - **ACTUAL [Alsip](https://vitaliiv1.sg-host.com/service-area/alsip/)** — ID560, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=560&action=edit)
  - **ACTUAL [Antioch](https://vitaliiv1.sg-host.com/service-area/antioch/)** — ID535, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=535&action=edit)
  - **ACTUAL [Arlington Heights](https://vitaliiv1.sg-host.com/service-area/arlington-heights/)** — ID559, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=559&action=edit)
  - **ACTUAL [Aurora](https://vitaliiv1.sg-host.com/service-area/aurora/)** — ID537, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=537&action=edit)
  - **ACTUAL [Bartlett](https://vitaliiv1.sg-host.com/service-area/bartlett/)** — ID561, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=561&action=edit)
  - **ACTUAL [Batavia](https://vitaliiv1.sg-host.com/service-area/batavia/)** — ID554, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=554&action=edit)
  - **ACTUAL [Bellwood](https://vitaliiv1.sg-host.com/service-area/bellwood/)** — ID567, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=567&action=edit)
  - **ACTUAL [Bensenville](https://vitaliiv1.sg-host.com/service-area/bensenville/)** — ID577, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=577&action=edit)
  - **ACTUAL [Berwyn](https://vitaliiv1.sg-host.com/service-area/berwyn/)** — ID549, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=549&action=edit)
  - **ACTUAL [Blue Island](https://vitaliiv1.sg-host.com/service-area/blue-island/)** — ID569, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=569&action=edit)
  - **ACTUAL [Bolingbrook](https://vitaliiv1.sg-host.com/service-area/bolingbrook/)** — ID557, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=557&action=edit)
  - **ACTUAL [Bridgeview](https://vitaliiv1.sg-host.com/service-area/bridgeview/)** — ID531, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=531&action=edit)
  - **ACTUAL [Broadview](https://vitaliiv1.sg-host.com/service-area/broadview/)** — ID575, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=575&action=edit)
  - **ACTUAL [Brookfield](https://vitaliiv1.sg-host.com/service-area/brookfield/)** — ID568, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=568&action=edit)
  - **ACTUAL [Buffalo Grove](https://vitaliiv1.sg-host.com/service-area/buffalo-grove/)** — ID551, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=551&action=edit)
  - **ACTUAL [Burbank](https://vitaliiv1.sg-host.com/service-area/burbank/)** — ID564, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=564&action=edit)
  - **ACTUAL [Calumet City](https://vitaliiv1.sg-host.com/service-area/calumet-city/)** — ID548, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=548&action=edit)
  - **ACTUAL [Carol Stream](https://vitaliiv1.sg-host.com/service-area/carol-stream/)** — ID543, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=543&action=edit)
  - **ACTUAL [Carpentersville](https://vitaliiv1.sg-host.com/service-area/carpentersville/)** — ID539, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=539&action=edit)
  - **ACTUAL [Cary](https://vitaliiv1.sg-host.com/service-area/cary/)** — ID544, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=544&action=edit)
  - **ACTUAL [Channahon](https://vitaliiv1.sg-host.com/service-area/channahon/)** — ID574, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=574&action=edit)
  - **ACTUAL [Chicago Heights](https://vitaliiv1.sg-host.com/service-area/chicago-heights/)** — ID573, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=573&action=edit)
  - **ACTUAL [Chicago Ridge](https://vitaliiv1.sg-host.com/service-area/chicago-ridge/)** — ID576, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=576&action=edit)
  - **ACTUAL [Deerfield](https://vitaliiv1.sg-host.com/service-area/deerfield/)** — ID563, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=563&action=edit)
  - **ACTUAL [Des Plaines](https://vitaliiv1.sg-host.com/service-area/des-plaines/)** — ID572, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=572&action=edit)
  - **ACTUAL [Downers Grove](https://vitaliiv1.sg-host.com/service-area/downers-grove/)** — ID527, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=527&action=edit)
  - **ACTUAL [Elk Groove Village](https://vitaliiv1.sg-host.com/service-area/elk-grove-village/)** — ID529, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=529&action=edit)
  - **ACTUAL [Expert Restoration Services in Addison](https://vitaliiv1.sg-host.com/service-area/addison/)** — ID538, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=538&action=edit)
  - **ACTUAL [Expert Restoration Services in Barrington](https://vitaliiv1.sg-host.com/service-area/barrington/)** — ID552, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=552&action=edit)
  - **ACTUAL [Expert Restoration Services in Elmhurst](https://vitaliiv1.sg-host.com/service-area/elmhurst/)** — ID530, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=530&action=edit)
  - **ACTUAL [Expert Restoration Services in Evanston](https://vitaliiv1.sg-host.com/service-area/evanston/)** — ID565, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=565&action=edit)
  - **ACTUAL [Expert Restoration Services in Glen Ellyn](https://vitaliiv1.sg-host.com/service-area/glen-ellyn/)** — ID542, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=542&action=edit)
  - **ACTUAL [Expert Restoration Services in Glencoe](https://vitaliiv1.sg-host.com/service-area/glencoe/)** — ID547, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=547&action=edit)
  - **ACTUAL [Expert Restoration Services in Glenview](https://vitaliiv1.sg-host.com/service-area/glenview/)** — ID533, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=533&action=edit)
  - **ACTUAL [Expert Restoration Services in Kenilworth, IL](https://vitaliiv1.sg-host.com/service-area/kenilworth/)** — ID571, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=571&action=edit)
  - **ACTUAL [Expert Restoration Services in Lake Forest](https://vitaliiv1.sg-host.com/service-area/lake-forest/)** — ID553, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=553&action=edit)
  - **ACTUAL [Expert Restoration Services in Lombard](https://vitaliiv1.sg-host.com/service-area/lombard/)** — ID526, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=526&action=edit)
  - **ACTUAL [Expert Restoration Services in Long Grove, IL](https://vitaliiv1.sg-host.com/service-area/long-grove/)** — ID545, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=545&action=edit)
  - **ACTUAL [Expert Restoration Services in Naperville](https://vitaliiv1.sg-host.com/service-area/naperville/)** — ID532, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=532&action=edit)
  - **ACTUAL [Expert Restoration Services in Northbrook](https://vitaliiv1.sg-host.com/service-area/northbrook/)** — ID556, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=556&action=edit)
  - **ACTUAL [Expert Restoration Services in Oak Brook](https://vitaliiv1.sg-host.com/service-area/oak-brook/)** — ID536, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=536&action=edit)
  - **ACTUAL [Expert Restoration Services in Skokie](https://vitaliiv1.sg-host.com/service-area/skokie/)** — ID541, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=541&action=edit)
  - **ACTUAL [Expert Restoration Services in Villa Park](https://vitaliiv1.sg-host.com/service-area/villa-park/)** — ID546, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=546&action=edit)
  - **ACTUAL [Expert Restoration Services in Wilmette](https://vitaliiv1.sg-host.com/service-area/wilmette/)** — ID555, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=555&action=edit)
  - **ACTUAL [Expert Restoration Services in Winnetka](https://vitaliiv1.sg-host.com/service-area/winnetka/)** — ID566, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=566&action=edit)
  - **ACTUAL [Fox Lake](https://vitaliiv1.sg-host.com/service-area/fox-lake/)** — ID570, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=570&action=edit)
  - **ACTUAL [Highland Park](https://vitaliiv1.sg-host.com/service-area/highland-park/)** — ID528, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=528&action=edit)
  - **ACTUAL [Hinsdale](https://vitaliiv1.sg-host.com/service-area/hinsdale/)** — ID540, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=540&action=edit)
  - **ACTUAL [Niles](https://vitaliiv1.sg-host.com/service-area/niles/)** — ID562, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=562&action=edit)
  - **ACTUAL [Schaumburg](https://vitaliiv1.sg-host.com/service-area/schaumburg/)** — ID558, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=558&action=edit)
- **ACTUAL [Service Request](https://vitaliiv1.sg-host.com/service-request/)** — ID492, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=492&action=edit)
- **ACTUAL [Testimonials](https://vitaliiv1.sg-host.com/testimonials/)** — ID498, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=498&action=edit)
- **ACTUAL [Water extraction](https://vitaliiv1.sg-host.com/water-extraction/)** — ID487, **publish**, [admin](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=487&action=edit)

## Articles — native post source records

These30 published production articles are not30 staging Pages. Existing migration decisions and future import holds remain.

### All source articles

SOURCE ONLY; preserve approved source paths. No article imported/published during E73.

| Record | Source/status | Staging | Future action |
| --- | --- | --- | --- |
| [Black Mold vs. Regular Mold: Understanding the Difference](https://gcprochicago.com/black-mold-vs-regular-mold-understanding-the-difference/) | post 13555 / publish | **Not created** | UPDATE |
| [Bouncing Back from Fire and Smoke Damage in Glenview: A Quick Guide](https://gcprochicago.com/bouncing-back-from-fire-and-smoke-damage-in-glenview-a-quick-guide/) | post 7341 / publish | **Not created** | UPDATE |
| [Breathe Easy: Preventing Mold in Your Home](https://gcprochicago.com/breathe-easy-preventing-mold-in-your-home/) | post 4660 / publish | **Not created** | UPDATE |
| [Choosing the Right Water Damage Restoration Service: A Buyer&#x27;s Guide](https://gcprochicago.com/choosing-the-right-water-damage-restoration-service-a-buyers-guide/) | post 6948 / publish | **Not created** | UPDATE |
| [Water Damage Restoration Guide for Chicago Businesses](https://gcprochicago.com/comprehensive-guide-to-commercial-water-damage-restoration-in-chicago/) | post 10338 / publish | **Not created** | UPDATE |
| [Comprehensive Rebuild: Full-Service Reconstruction Explained](https://gcprochicago.com/comprehensive-rebuild-full-service-reconstruction-explained/) | post 4671 / publish | **Not created** | UPDATE |
| [Comprehensive Smoke Cleanup Strategies for Effective Restoration](https://gcprochicago.com/comprehensive-smoke-cleanup-strategies-for-effective-restoration/) | post 5300 / publish | **Not created** | UPDATE |
| [Financial Fury: The Astonishing Cost of Water Damage](https://gcprochicago.com/financial-fury-the-astonishing-cost-of-water-damage/) | post 4437 / publish | **Not created** | UPDATE |
| [Fire and Smoke Damage Restoration in Lombard: A Comprehensive Guide by GCPRO](https://gcprochicago.com/fire-and-smoke-damage-restoration-in-lombard-a-comprehensive-guide-by-gcpro/) | post 9625 / publish | **Not created** | UPDATE |
| [Flooded Basement: A Step-by-Step Guide to Water Damage Control](https://gcprochicago.com/flooded-basement-a-step-by-step-guide-to-water-damage-control/) | post 4855 / publish | **Not created** | UPDATE |
| [How Board-Up Services Save Chicago Businesses After a Disaster](https://gcprochicago.com/how-board-up-services-save-chicago-businesses-after-a-disaster/) | post 20286 / publish | **Not created** | UPDATE |
| [Mold Remediation in Glenview: A Comprehensive Guide](https://gcprochicago.com/mold-remediation-in-glenview-a-comprehensive-guide/) | post 7541 / publish | **Not created** | UPDATE |
| [Navigating Fire and Smoke Restoration in Glencoe with GCPRO Restoration](https://gcprochicago.com/navigating-fire-and-smoke-restoration-in-glencoe-with-gcpro-restoration/) | post 11336 / publish | **Not created** | UPDATE |
| [Navigating Water Damage in Lombard, IL: A Thorough Guide from GCPRO](https://gcprochicago.com/navigating-water-damage-in-lombard-il-a-thorough-guide/) | post 7356 / publish | **Not created** | UPDATE |
| [Reviving Treasures: A Guide to Personal Property Restoration](https://gcprochicago.com/reviving-treasures-a-guide-to-personal-property-restoration/) | post 4663 / publish | **Not created** | UPDATE |
| [Safeguarding Your Sanctuary: Essential Tips to Fireproof Your Home](https://gcprochicago.com/safeguarding-your-sanctuary-essential-tips-to-fireproof-your-home/) | post 4656 / publish | **Not created** | UPDATE |
| [Signs of Hidden Water Damage in Your Home](https://gcprochicago.com/signs-of-hidden-water-damage-in-your-home/) | post 21140 / publish | **Not created** | UPDATE |
| [The Complete Guide to Sewage Cleanup: Safety, Steps, and Services](https://gcprochicago.com/the-complete-guide-to-sewage-cleanup-safety-steps-and-services/) | post 6638 / publish | **Not created** | UPDATE |
| [Top 5 Reasons You Need Emergency Board-Up Services in Chicago](https://gcprochicago.com/top-5-reasons-you-need-emergency-board-up-services-in-chicago/) | post 20280 / publish | **Not created** | UPDATE |
| [Understanding and Addressing Ceiling Water Damage: A Comprehensive Guide](https://gcprochicago.com/understanding-and-addressing-ceiling-water-damage-a-comprehensive-guide/) | post 6664 / publish | **Not created** | UPDATE |
| [Understanding Mold Remediation in Lombard, IL: A Resident&#x27;s Guide](https://gcprochicago.com/understanding-mold-remediation-in-lombard-il-a-residents-guide/) | post 7371 / publish | **Not created** | UPDATE |
| [Understanding Water Damage Restoration in Villa Park: A Must-Read Guide](https://gcprochicago.com/understanding-water-damage-restoration-in-villa-park-a-must-read-guide/) | post 12696 / publish | **Not created** | UPDATE |
| [Water Damage and Restoration Services in Glenview: A Comprehensive Guide](https://gcprochicago.com/water-damage-and-restoration-services-in-glenview-a-comprehensive-guide/) | post 7331 / publish | **Not created** | UPDATE |
| [Water Damage Floor Repair: A Homeowner&#x27;s Guide to Restoration](https://gcprochicago.com/water-damage-floor-repair-a-homeowners-guide-to-restoration/) | post 4829 / publish | **Not created** | UPDATE |
| [Water Damage Restoration 101: What You Need to Know](https://gcprochicago.com/water-damage-restoration-101-what-you-need-to-know/) | post 6879 / publish | **Not created** | UPDATE |
| [Comprehensive Water Damage Restoration Services in Glencoe by GCPRO Restoration](https://gcprochicago.com/water-damage-restoration-in-glencoe-expert-insights-from-gcpro/) | post 11214 / publish | **Not created** | UPDATE |
| [Water Damage Restoration in Winnetka: Expert Insights from GCPRO](https://gcprochicago.com/water-damage-restoration-in-winnetka-expert-insights-from-gcpro/) | post 8726 / publish | **Not created** | UPDATE |
| [What to Do If You Notice Water Damage in Your Home](https://gcprochicago.com/what-to-do-if-you-notice-water-damage-in-your-home/) | post 21121 / publish | **Not created** | UPDATE |
| [When and Why You Need Emergency Board-Up Services](https://gcprochicago.com/when-and-why-you-need-emergency-board-up-services/) | post 20267 / publish | **Not created** | MERGE |
| [Why Professional Sewage Cleanup is Essential for Health and Safety](https://gcprochicago.com/why-professional-sewage-cleanup-is-essential-for-health-and-safety/) | post 6642 / publish | **Not created** | UPDATE |

## Portfolio / projects

SOURCE ONLY:13 published production CPT items; no duplicate staging Pages. Portfolio CPT/model/template/import work remains separate.

| Record | Source/status | Staging | Future action |
| --- | --- | --- | --- |
| [Fire Damage Restoration on West School Street in Chicago](https://gcprochicago.com/portfolio/fire-damage-restoration-on-w-school-street-in-chicago/) | portfolio 11008 / publish | **Not created** | UPDATE |
| [From Ashes to Excellence: Tinley Park Home Restoration](https://gcprochicago.com/portfolio/from-ashes-to-excellence-tinley-park-home-restoration/) | portfolio 12428 / publish | **Not created** | UPDATE |
| [Frozen Facade: Complete Exterior and Window Renovation in Chicago](https://gcprochicago.com/portfolio/frozen-facade-complete-exterior-and-window-renovation-in-chicago/) | portfolio 11351 / publish | **Not created** | UPDATE |
| [Green Oaks Apartments in Palos Hills](https://gcprochicago.com/portfolio/green-oaks-apartments-in-palos-hills/) | portfolio 8236 / publish | **Not created** | UPDATE |
| [Helen Berkun - Bathroom Reveal](https://gcprochicago.com/portfolio/helen-berkun-bathroom-reveal/) | portfolio 8300 / publish | **Not created** | UPDATE |
| [Helen Berkun - The Entire Facade Of The House](https://gcprochicago.com/portfolio/helen-berkun-the-entire-facade-of-the-house/) | portfolio 8186 / publish | **Not created** | UPDATE |
| [Home Remodeling in Oak Brook](https://gcprochicago.com/portfolio/home-remodeling-oakbrook/) | portfolio 22663 / publish | **Not created** | UPDATE |
| [Reconstruction After Water Damage on Montana Street, Chicago](https://gcprochicago.com/portfolio/reconstruction-after-water-damage-on-montana-street-chicago/) | portfolio 10625 / publish | **Not created** | UPDATE |
| [Transforming the Boys and Girls Club in Chicago](https://gcprochicago.com/portfolio/reconstruction-in-boys-and-girls-clubs-of-chicago/) | portfolio 11388 / publish | **Not created** | UPDATE |
| [Restoring Elegance: Water Damage Reconstruction of a Wonder Lake Residence](https://gcprochicago.com/portfolio/restoring-elegance-water-damage-reconstruction-of-a-wonder-lake-residence/) | portfolio 11471 / publish | **Not created** | UPDATE |
| [Transforming Spaces: Glenview Home Reconstruction](https://gcprochicago.com/portfolio/transforming-spaces-glenview-home-reconstruction/) | portfolio 11268 / publish | **Not created** | UPDATE |
| [Transforming spaces into modern and elegant interiors in St. Charles](https://gcprochicago.com/portfolio/transforming-spaces-into-modern-and-elegant-interiors-in-st-charles/) | portfolio 9882 / publish | **Not created** | UPDATE |
| [Water Damage Restoration in Western Spring](https://gcprochicago.com/portfolio/water-damage-restoration-in-western-spring/) | portfolio 14989 / publish | **Not created** | UPDATE |

## Production Pages not mapped to an actual staging Page

SOURCE ONLY. Includes2 newly discovered Drafts with no saved slug; their admin identity is not a historical public URL.

| Record | Source/status | Staging | Future action |
| --- | --- | --- | --- |
| [Welcome to GCPRO Restoration](https://gcprochicago.com/connect/) | page 15438 / publish | **Not created** | REVIEW |
| [Corporate signatures](https://gcprochicago.com/corporate-signatures2/) | page 2406 / publish | **Not created** | REVIEW |
| [Bridgeview](https://gcprochicago.com/service-area/service-area-bridgeview/) | page 21723 / publish | **Not created** | MERGE |
| [test2](https://gcprochicago.com/test2/) | page 8136 / publish | **Not created** | REVIEW |
| [Thank you](https://gcprochicago.com/thank-you/) | page 456 / publish | **Not created** | REVIEW |
| [Elementor #15553](https://gcprochicago.com/wp-admin/post.php?post=15553&action=edit) | page 15553 / draft | **Not created** | REVIEW |
| [Barlett](https://gcprochicago.com/wp-admin/post.php?post=11856&action=edit) | page 11856 / draft | **Not created** | REVIEW |

## Archive, taxonomy, index and remaining content proposals

INVENTORY ONLY unless an actual staging ID is shown. Taxonomy terms have no Page publication status; empty counts/public URL candidates do not prove indexability.

| Record | Source/status | Staging | Future action |
| --- | --- | --- | --- |
| [News](https://gcprochicago.com/./news/) | taxonomy:category 49 / not_applicable_taxonomy_term | **Not created** | REVIEW |
| [https://gcprochicago.com/2024/01/24/](https://gcprochicago.com/2024/01/24/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/01/25/](https://gcprochicago.com/2024/01/25/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/01/26/](https://gcprochicago.com/2024/01/26/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/02/01/](https://gcprochicago.com/2024/02/01/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/02/02/](https://gcprochicago.com/2024/02/02/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/02/05/](https://gcprochicago.com/2024/02/05/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/02/06/](https://gcprochicago.com/2024/02/06/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/02/12/](https://gcprochicago.com/2024/02/12/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/02/15/](https://gcprochicago.com/2024/02/15/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/03/04/](https://gcprochicago.com/2024/03/04/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/03/26/](https://gcprochicago.com/2024/03/26/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/03/27/](https://gcprochicago.com/2024/03/27/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/05/02/](https://gcprochicago.com/2024/05/02/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2024/05/16/](https://gcprochicago.com/2024/05/16/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2025/01/20/](https://gcprochicago.com/2025/01/20/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/2025/02/19/](https://gcprochicago.com/2025/02/19/) | date_archive  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [Blog](https://gcprochicago.com/blog/) | page 2187 / publish | **Not created** | UPDATE |
| [https://gcprochicago.com/commercial-services/storm-damage/](https://gcprochicago.com/commercial-services/storm-damage/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REVIEW |
| [Portfolio](https://gcprochicago.com/portfolio/) | page 8929 / publish | **Not created** | UPDATE |
| [https://gcprochicago.com/sewage-cleanup/](https://gcprochicago.com/sewage-cleanup/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REVIEW |
| [board-up](https://gcprochicago.com/tag/board-up/) | taxonomy:post_tag 89 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Construction](https://gcprochicago.com/tag/construction/) | taxonomy:post_tag 65 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Fire Damage](https://gcprochicago.com/tag/fire-damage/) | taxonomy:post_tag 61 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Glencoe](https://gcprochicago.com/tag/glencoe/) | taxonomy:post_tag 85 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Glenview](https://gcprochicago.com/tag/glenview/) | taxonomy:post_tag 59 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Lombard](https://gcprochicago.com/tag/lombard/) | taxonomy:post_tag 66 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Mold Removal](https://gcprochicago.com/tag/mold-removal/) | taxonomy:post_tag 62 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Property Restoration](https://gcprochicago.com/tag/property-restoration/) | taxonomy:post_tag 64 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Smoke Damage](https://gcprochicago.com/tag/smoke-damage/) | taxonomy:post_tag 63 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Villa Park](https://gcprochicago.com/tag/villa-park/) | taxonomy:post_tag 87 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Water Damage](https://gcprochicago.com/tag/water-damage/) | taxonomy:post_tag 60 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [Winnetka](https://gcprochicago.com/tag/winnetka/) | taxonomy:post_tag 77 / not_applicable_taxonomy_term | **Not created** | UPDATE |
| [https://gcprochicago.com/team/](https://gcprochicago.com/team/) | page_unverified  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [Fire Damage](https://gcprochicago.com/project-type/fire-damage/) | taxonomy:project-type 71 / not_applicable_taxonomy_term | **Not created** | REVIEW |
| [Mold Removal](https://gcprochicago.com/project-type/mold-removal/) | taxonomy:project-type 73 / not_applicable_taxonomy_term | **Not created** | REVIEW |
| [Reconstruction](https://gcprochicago.com/project-type/reconstruction/) | taxonomy:project-type 70 / not_applicable_taxonomy_term | **Not created** | REVIEW |
| [Water Damage](https://gcprochicago.com/project-type/water-damage/) | taxonomy:project-type 72 / not_applicable_taxonomy_term | **Not created** | REVIEW |
| [Commercial](https://gcprochicago.com/bafg_gallery/commercial/) | taxonomy:bafg_gallery 81 / not_applicable_taxonomy_term | **Not created** | REVIEW |
| [Fire Damage](https://gcprochicago.com/bafg_gallery/fire-damage/) | taxonomy:bafg_gallery 82 / not_applicable_taxonomy_term | **Not created** | REVIEW |
| [Reconstruction](https://gcprochicago.com/bafg_gallery/reconstruction/) | taxonomy:bafg_gallery 84 / not_applicable_taxonomy_term | **Not created** | REVIEW |
| [Residential](https://gcprochicago.com/bafg_gallery/residential/) | taxonomy:bafg_gallery 80 / not_applicable_taxonomy_term | **Not created** | REVIEW |
| [Water Damage](https://gcprochicago.com/bafg_gallery/water-damage/) | taxonomy:bafg_gallery 83 / not_applicable_taxonomy_term | **Not created** | REVIEW |

<details>
<summary>Technical source integration/template objects — not business Pages</summary>


### BEAF and Elementor source objects

95 source objects recorded for dependency preservation only;3 were already inventoried by URL and now receive observed IDs/types without duplicate rows. No plugin, shortcode, template or BEAF record modified/imported.

| Record | Source/status | Staging | Future action |
| --- | --- | --- | --- |
| [Fasade 21-0495-CND](https://gcprochicago.com/?bafg=10347) | bafg 10347 / publish | **Not created** | REMOVE |
| [Mold Removal](https://gcprochicago.com/?bafg=mold-removal) | bafg 22092 / publish | **Not created** | REMOVE |
| [Default Kit](https://gcprochicago.com/?elementor_library=default-kit) | elementor_library 562 / publish | **Not created** | REMOVE |
| [Property-restoration](https://gcprochicago.com/?bafg=property-restoration) | bafg 18061 / publish | **Not created** | REVIEW |
| [Mold-2](https://gcprochicago.com/?bafg=mold-2) | bafg 17892 / publish | **Not created** | REVIEW |
| [Mold-1](https://gcprochicago.com/?bafg=mold-1) | bafg 17882 / publish | **Not created** | REVIEW |
| [The Fire Damage Restoration in Tinley Park 8](https://gcprochicago.com/?bafg=the-fire-damage-restoration-in-tinley-park-8) | bafg 13663 / publish | **Not created** | REVIEW |
| [Fire-Damage-Tinley-7](https://gcprochicago.com/?bafg=fire-damage-tinley-7) | bafg 12730 / publish | **Not created** | REVIEW |
| [Fire-Damage-Tinley-6](https://gcprochicago.com/?bafg=fire-damage-tinley-6) | bafg 12656 / publish | **Not created** | REVIEW |
| [Fire-Damage-Tinley-5](https://gcprochicago.com/?bafg=fire-damage-tinley-5) | bafg 12569 / publish | **Not created** | REVIEW |
| [Fire-Damage-Tinley-3](https://gcprochicago.com/?bafg=fire-damage-tinley-3) | bafg 12503 / publish | **Not created** | REVIEW |
| [Fire-Damage-Tinley-2](https://gcprochicago.com/?bafg=fire-damage-tinley-2) | bafg 12496 / publish | **Not created** | REVIEW |
| [Tinley-fire-damage-1](https://gcprochicago.com/?bafg=tinley-fire-damage-1) | bafg 12486 / publish | **Not created** | REVIEW |
| [Glenvie-house-2](https://gcprochicago.com/?bafg=glenvie-house-2) | bafg 11840 / publish | **Not created** | REVIEW |
| [Glenview-House-1](https://gcprochicago.com/?bafg=glenview-house-1) | bafg 11834 / publish | **Not created** | REVIEW |
| [Wonder-Lake-Entrance](https://gcprochicago.com/?bafg=wonder-lake-entrance) | bafg 11540 / publish | **Not created** | REVIEW |
| [Wonder-Lake-Kitchen-2](https://gcprochicago.com/?bafg=wonder-lake-kitchen-2) | bafg 11529 / publish | **Not created** | REVIEW |
| [Wonder-Lake-Stairs](https://gcprochicago.com/?bafg=wonder-lake-stairs) | bafg 11526 / publish | **Not created** | REVIEW |
| [Wonder-Lake-Fireplace](https://gcprochicago.com/?bafg=wonder-lake-fireplace) | bafg 11519 / publish | **Not created** | REVIEW |
| [The Water Damage Restoration](https://gcprochicago.com/?bafg=wonder-lake-corner) | bafg 11515 / publish | **Not created** | REVIEW |
| [The Water Damage Restoration of a Kitchen](https://gcprochicago.com/?bafg=11464) | bafg 11464 / publish | **Not created** | REVIEW |
| [The Fire Damage Garage Restoration](https://gcprochicago.com/?bafg=garage) | bafg 11048 / publish | **Not created** | REVIEW |
| [The Commercial Roof Reconstruction](https://gcprochicago.com/?bafg=roof2) | bafg 10948 / publish | **Not created** | REVIEW |
| [The Commercial Interior Reconstruction](https://gcprochicago.com/?bafg=jordan-bg-club2) | bafg 10838 / publish | **Not created** | REVIEW |
| [The Door Reconstruction](https://gcprochicago.com/?bafg=door1) | bafg 10769 / publish | **Not created** | REVIEW |
| [The Damaged Wall Reconstruction](https://gcprochicago.com/?bafg=roof1) | bafg 10766 / publish | **Not created** | REVIEW |
| [Fire Damage Restoration of a Kitchen](https://gcprochicago.com/?bafg=fire-damage-1) | bafg 10661 / publish | **Not created** | REVIEW |
| [19-0255-CNI-3](https://gcprochicago.com/?bafg=19-0255-cni-3) | bafg 10537 / publish | **Not created** | REVIEW |
| [Berkun door](https://gcprochicago.com/?bafg=berkun-door) | bafg 10468 / publish | **Not created** | REVIEW |
| [19-0255-CNI-2](https://gcprochicago.com/?bafg=19-0255-cni-2) | bafg 10380 / publish | **Not created** | REVIEW |
| [19-0255-CNI-1](https://gcprochicago.com/?bafg=19-0255-cni-1) | bafg 10374 / publish | **Not created** | REVIEW |
| [Back 21-0495-CND](https://gcprochicago.com/?bafg=10353) | bafg 10353 / publish | **Not created** | REVIEW |
| [Restroom](https://gcprochicago.com/?bafg=9862) | bafg 9862 / publish | **Not created** | REVIEW |
| [Kitchen1](https://gcprochicago.com/wp-admin/post.php?post=8152&action=edit) | bafg 8152 / draft | **Not created** | REVIEW |
| [Entrance](https://gcprochicago.com/?bafg=entrance) | bafg 8132 / publish | **Not created** | REVIEW |
| [newest_serv_area_template_4](https://gcprochicago.com/?elementor_library=newest_serv_area_template_4) | elementor_library 21903 / publish | **Not created** | REVIEW |
| [area_template_2](https://gcprochicago.com/?elementor_library=area_template_2) | elementor_library 21468 / publish | **Not created** | REVIEW |
| [area_template](https://gcprochicago.com/?elementor_library=area_template) | elementor_library 21426 / publish | **Not created** | REVIEW |
| [Elementor Footer #21217](https://gcprochicago.com/?elementor_library=elementor-footer-21217) | elementor_library 21217 / publish | **Not created** | REVIEW |
| [Elementor Footer #21215](https://gcprochicago.com/wp-admin/post.php?post=21215&action=edit) | elementor_library 21215 / draft | **Not created** | REVIEW |
| [Elementor Header #21168](https://gcprochicago.com/?elementor_library=elementor-header-21168) | elementor_library 21168 / publish | **Not created** | REVIEW |
| [Reviews_wide_slider](https://gcprochicago.com/?elementor_library=reviews_wide_slider) | elementor_library 20674 / publish | **Not created** | REVIEW |
| [Counter_live](https://gcprochicago.com/?elementor_library=counter_live) | elementor_library 20001 / publish | **Not created** | REVIEW |
| [Counter](https://gcprochicago.com/?elementor_library=counter-2) | elementor_library 19958 / publish | **Not created** | REVIEW |
| [Elementor Loop Item #18952](https://gcprochicago.com/?elementor_library=elementor-loop-item-3) | elementor_library 18952 / publish | **Not created** | REVIEW |
| [Insurance](https://gcprochicago.com/?elementor_library=insurance-3) | elementor_library 18922 / publish | **Not created** | REVIEW |
| [Insurance](https://gcprochicago.com/wp-admin/post.php?post=18921&action=edit) | elementor_library 18921 / draft | **Not created** | REVIEW |
| [Fire Damage Types](https://gcprochicago.com/?elementor_library=fire-damage-types-2) | elementor_library 17614 / publish | **Not created** | REVIEW |
| [Insurance](https://gcprochicago.com/?elementor_library=insurance-2) | elementor_library 17444 / publish | **Not created** | REVIEW |
| [Insurance](https://gcprochicago.com/?elementor_library=insurance) | elementor_library 17425 / publish | **Not created** | REVIEW |
| [List](https://gcprochicago.com/?elementor_library=list) | elementor_library 17270 / publish | **Not created** | REVIEW |
| [Advantages](https://gcprochicago.com/wp-admin/post.php?post=16219&action=edit) | elementor_library 16219 / draft | **Not created** | REVIEW |
| [Advantages](https://gcprochicago.com/?elementor_library=advantages-3) | elementor_library 16215 / publish | **Not created** | REVIEW |
| [Advantages](https://gcprochicago.com/wp-admin/post.php?post=16214&action=edit) | elementor_library 16214 / draft | **Not created** | REVIEW |
| [Service Area Page](https://gcprochicago.com/?elementor_library=service-area-page) | elementor_library 15029 / publish | **Not created** | REVIEW |
| [New Servise Area](https://gcprochicago.com/?elementor_library=new-servise-area) | elementor_library 14551 / publish | **Not created** | REVIEW |
| [Water Related Services](https://gcprochicago.com/?elementor_library=water-related-services-2) | elementor_library 13438 / publish | **Not created** | REVIEW |
| [Water Related Services](https://gcprochicago.com/?elementor_library=water-related-services) | elementor_library 13430 / publish | **Not created** | REVIEW |
| [Related Services](https://gcprochicago.com/?elementor_library=related-services) | elementor_library 13344 / publish | **Not created** | REVIEW |
| [Elementor Loop Item #11576](https://gcprochicago.com/?elementor_library=elementor-loop-item-2) | elementor_library 11576 / publish | **Not created** | REVIEW |
| [Elementor Loop Item #11568](https://gcprochicago.com/?elementor_library=elementor-loop-item) | elementor_library 11568 / publish | **Not created** | REVIEW |
| [Reconstruction-portfolio](https://gcprochicago.com/?elementor_library=portfolio-2) | elementor_library 10874 / publish | **Not created** | REVIEW |
| [Fire Damage Types](https://gcprochicago.com/?elementor_library=fire-damage-types) | elementor_library 10749 / publish | **Not created** | REVIEW |
| [Water Danage Categories](https://gcprochicago.com/?elementor_library=water-danage-categories) | elementor_library 10595 / publish | **Not created** | REVIEW |
| [Water Damage Steps](https://gcprochicago.com/?elementor_library=water-damage-steps) | elementor_library 10556 / publish | **Not created** | REVIEW |
| [Certificates](https://gcprochicago.com/?elementor_library=certificates) | elementor_library 10070 / publish | **Not created** | REVIEW |
| [Tags Archive PAge](https://gcprochicago.com/?elementor_library=tags-archive-page) | elementor_library 9612 / publish | **Not created** | REVIEW |
| [Area page](https://gcprochicago.com/?elementor_library=area-page) | elementor_library 9540 / publish | **Not created** | REVIEW |
| [logos_slider](https://gcprochicago.com/?elementor_library=logos_slider) | elementor_library 9426 / publish | **Not created** | REVIEW |
| [Logos_intro](https://gcprochicago.com/?elementor_library=logos_intro) | elementor_library 9413 / publish | **Not created** | REVIEW |
| [Related Articles](https://gcprochicago.com/?elementor_library=related-articles) | elementor_library 9253 / publish | **Not created** | REVIEW |
| [Portfolio Archive Page](https://gcprochicago.com/?elementor_library=elementor-archive-8412) | elementor_library 8412 / publish | **Not created** | REVIEW |
| [PORTFOLIO](https://gcprochicago.com/?elementor_library=portfolio) | elementor_library 8415 / publish | **Not created** | REVIEW |
| [Elementor Single Page #8121](https://gcprochicago.com/?elementor_library=elementor-single-page-8121) | elementor_library 8121 / publish | **Not created** | REVIEW |
| [Portfolio item page](https://gcprochicago.com/?elementor_library=portfolio-item-page) | elementor_library 7996 / publish | **Not created** | REVIEW |
| [Call Us Vertical Right](https://gcprochicago.com/?elementor_library=call-us-vertical-right) | elementor_library 7652 / publish | **Not created** | REVIEW |
| [Elementor Search Results #7495](https://gcprochicago.com/?elementor_library=elementor-search-results-7495) | elementor_library 7495 / publish | **Not created** | REVIEW |
| [BLOG](https://gcprochicago.com/?elementor_library=blog) | elementor_library 6858 / publish | **Not created** | REVIEW |
| [Call Us Vertical](https://gcprochicago.com/?elementor_library=call-us-vertical) | elementor_library 5972 / publish | **Not created** | REVIEW |
| [GCPRO Single Page](https://gcprochicago.com/?elementor_library=gcpro-blog-page) | elementor_library 5897 / publish | **Not created** | REVIEW |
| [Reviews](https://gcprochicago.com/?elementor_library=reviews-2) | elementor_library 5872 / publish | **Not created** | REVIEW |
| [Membership](https://gcprochicago.com/?elementor_library=membership) | elementor_library 3365 / publish | **Not created** | REVIEW |
| [Service Area](https://gcprochicago.com/?elementor_library=service-area-2) | elementor_library 3213 / publish | **Not created** | REVIEW |
| [Counter 24](https://gcprochicago.com/?elementor_library=counter-24) | elementor_library 3076 / publish | **Not created** | REVIEW |
| [Counter commercial](https://gcprochicago.com/?elementor_library=counter-commercial) | elementor_library 2318 / publish | **Not created** | REVIEW |
| [Counter](https://gcprochicago.com/?elementor_library=counter) | elementor_library 2280 / publish | **Not created** | REVIEW |
| [Advantages_white](https://gcprochicago.com/?elementor_library=advantages_white) | elementor_library 1670 / publish | **Not created** | REVIEW |
| [Elementor Error 404 #1372](https://gcprochicago.com/?elementor_library=elementor-error-404-1372) | elementor_library 1372 / publish | **Not created** | REVIEW |
| [Elementor Error 404 #1358](https://gcprochicago.com/?elementor_library=elementor-error-404-1358) | elementor_library 1358 / publish | **Not created** | REVIEW |
| [Advantages Commercial White](https://gcprochicago.com/?elementor_library=advantages-2) | elementor_library 1303 / publish | **Not created** | REVIEW |
| [Advantages](https://gcprochicago.com/?elementor_library=advantages) | elementor_library 1195 / publish | **Not created** | REVIEW |
| [Reviews](https://gcprochicago.com/?elementor_library=reviews) | elementor_library 1086 / publish | **Not created** | REVIEW |
| [Call Us](https://gcprochicago.com/?elementor_library=call-us) | elementor_library 1075 / publish | **Not created** | REVIEW |
| [Slider logo](https://gcprochicago.com/?elementor_library=slider-logo) | elementor_library 1044 / publish | **Not created** | REVIEW |
| [Logo slider](https://gcprochicago.com/?elementor_library=logo-slider-2) | elementor_library 1022 / publish | **Not created** | REVIEW |

</details>

<details>
<summary>Remaining historical, redirect-variant, operational and disposition records</summary>


### Complete residual URL history

These are URL/history records, not instructions to manufacture Pages. Future MERGE/301/REMOVE proposals remain unexecuted.

| Record | Source/status | Staging | Future action |
| --- | --- | --- | --- |
| [http://gcprochicago.com/](http://gcprochicago.com/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | 301 REDIRECT |
| [http://www.gcprochicago.com/](http://www.gcprochicago.com/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | 301 REDIRECT |
| [https://gcprochicago.com/*](https://gcprochicago.com/*) | administrative_pattern  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/?elementor_library=fire-damage-new](https://gcprochicago.com/?elementor_library=fire-damage-new) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REMOVE |
| [https://gcprochicago.com/?elementor_library=fire-damage-old](https://gcprochicago.com/?elementor_library=fire-damage-old) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REMOVE |
| [https://gcprochicago.com/?elementor_library=parent-page](https://gcprochicago.com/?elementor_library=parent-page) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REMOVE |
| [https://gcprochicago.com/?elementor_library=property-old](https://gcprochicago.com/?elementor_library=property-old) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REMOVE |
| [https://gcprochicago.com/?elementor_library=service-page](https://gcprochicago.com/?elementor_library=service-page) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REMOVE |
| [https://gcprochicago.com/?elementor_library=testimonials](https://gcprochicago.com/?elementor_library=testimonials) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REMOVE |
| [https://gcprochicago.com/?tid=EPD86ss00Q0J9dndxqr3gD_QvZj2gTmoi2Y](https://gcprochicago.com/?tid=EPD86ss00Q0J9dndxqr3gD_QvZj2gTmoi2Y) | parameter_variant  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/?tid=EPD86ss00Q0J9dndxqr3gD_wZWINOybdBeO](https://gcprochicago.com/?tid=EPD86ss00Q0J9dndxqr3gD_wZWINOybdBeO) | parameter_variant  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/?tid=EPdnd9J0Q00ss68DlCxw07_I4WZw43NVPAQ](https://gcprochicago.com/?tid=EPdnd9J0Q00ss68DlCxw07_I4WZw43NVPAQ) | parameter_variant  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/blog/page/2/](https://gcprochicago.com/blog/page/2/) | pagination  / unverified_no_exact_public_object_match | **Not created** | UPDATE |
| [https://gcprochicago.com/blog/page/3/](https://gcprochicago.com/blog/page/3/) | pagination  / unverified_no_exact_public_object_match | **Not created** | UPDATE |
| [https://gcprochicago.com/blog/page/4/](https://gcprochicago.com/blog/page/4/) | pagination  / unverified_no_exact_public_object_match | **Not created** | UPDATE |
| [https://gcprochicago.com/bouncing-back-from-fire-and-smoke-damage-in-glenview-a-quick-guide/feed/](https://gcprochicago.com/bouncing-back-from-fire-and-smoke-damage-in-glenview-a-quick-guide/feed/) | feed  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/cdn-cgi/l/email-protection](https://gcprochicago.com/cdn-cgi/l/email-protection) | resource  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/elementskit-content/dynamic-content-widget-21b4cd74-3f9a71f/](https://gcprochicago.com/elementskit-content/dynamic-content-widget-21b4cd74-3f9a71f/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REMOVE |
| [https://gcprochicago.com/elementskit-content/dynamic-content-widget-21b4cd74-fa4c5d3/](https://gcprochicago.com/elementskit-content/dynamic-content-widget-21b4cd74-fa4c5d3/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REMOVE |
| [https://gcprochicago.com/financial-fury-the-astonishing-cost-of-water-damage/feed/](https://gcprochicago.com/financial-fury-the-astonishing-cost-of-water-damage/feed/) | feed  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/fire-and-smoke-damage-restoration-in-lombard-a-comprehensive-guide-by-gcpro/feed/](https://gcprochicago.com/fire-and-smoke-damage-restoration-in-lombard-a-comprehensive-guide-by-gcpro/feed/) | feed  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/home/e28nhlyahv8x/public_html/wp-content/plugins/beaf-before-and-after-gallery/](https://gcprochicago.com/home/e28nhlyahv8x/public_html/wp-content/plugins/beaf-before-and-after-gallery/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REMOVE |
| [https://gcprochicago.com/navigating-fire-and-smoke-restoration-in-glencoe-with-gcpro-restoration/feed/](https://gcprochicago.com/navigating-fire-and-smoke-restoration-in-glencoe-with-gcpro-restoration/feed/) | feed  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/navigating-water-damage-in-lombard-il-a-thorough-guide/feed/](https://gcprochicago.com/navigating-water-damage-in-lombard-il-a-thorough-guide/feed/) | feed  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/portfolio/feed/](https://gcprochicago.com/portfolio/feed/) | feed  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/portfolio/page/2/](https://gcprochicago.com/portfolio/page/2/) | pagination  / unverified_no_exact_public_object_match | **Not created** | UPDATE |
| [https://gcprochicago.com/residential-services/lake-forest/](https://gcprochicago.com/residential-services/lake-forest/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | 301 REDIRECT |
| [https://gcprochicago.com/search/【Buy+at+36b.net】+longchamp+le+pliage+pre-owned+20251108_035456/feed/rss2/](https://gcprochicago.com/search/【Buy+at+36b.net】+longchamp+le+pliage+pre-owned+20251108_035456/feed/rss2/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | REMOVE |
| [https://gcprochicago.com/service-area/alsip](https://gcprochicago.com/service-area/alsip) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | 301 REDIRECT |
| [https://gcprochicago.com/service-area/bartlett](https://gcprochicago.com/service-area/bartlett) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | 301 REDIRECT |
| [https://gcprochicago.com/service-area/batavia](https://gcprochicago.com/service-area/batavia) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | 301 REDIRECT |
| [https://gcprochicago.com/service-area/hinsdale](https://gcprochicago.com/service-area/hinsdale) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | 301 REDIRECT |
| [https://gcprochicago.com/tag/property-restoration/feed/](https://gcprochicago.com/tag/property-restoration/feed/) | feed  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/tag/water-damage/page/2/](https://gcprochicago.com/tag/water-damage/page/2/) | pagination  / unverified_no_exact_public_object_match | **Not created** | UPDATE |
| [https://gcprochicago.com/top-5-reasons-you-need-emergency-board-up-services-in-chicago/feed/](https://gcprochicago.com/top-5-reasons-you-need-emergency-board-up-services-in-chicago/feed/) | feed  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/water-damage-restoration-in-glencoe-expert-insights-from-gcpro/feed/](https://gcprochicago.com/water-damage-restoration-in-glencoe-expert-insights-from-gcpro/feed/) | feed  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/water-damage-restoration-naperville-6/](https://gcprochicago.com/water-damage-restoration-naperville-6/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | 301 REDIRECT |
| [https://gcprochicago.com/wp-*.php](https://gcprochicago.com/wp-*.php) | administrative_pattern  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/wp-admin/*](https://gcprochicago.com/wp-admin/*) | administrative_pattern  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://gcprochicago.com/wp-includes/js/wp-emoji-release.min.js?ver=20f7f8b9f1023a9fc8a0054f0b1273bc](https://gcprochicago.com/wp-includes/js/wp-emoji-release.min.js?ver=20f7f8b9f1023a9fc8a0054f0b1273bc) | parameter_variant  / unverified_no_exact_public_object_match | **Not created** | KEEP |
| [https://www.gcprochicago.com/](https://www.gcprochicago.com/) | non_page_or_unverified  / unverified_no_exact_public_object_match | **Not created** | 301 REDIRECT |

</details>

## Source inspection coverage and limitations

Production read-only admin:90 Pages(88 Published/2 Draft),30 Posts(all Published),13 Portfolio(all Published),34 BEAF(33 Published/1 Draft),61 Elementor templates(57 Published/4 Draft),0 Post Grid records. No Private/Pending/Future/Trash status counts were exposed in these All lists. This is current visible admin inventory, not deleted/revision/database history.

Taxonomies inspected:1 News category,12 post tags,4 Project Types,5 BEAF categories. Elementor library-category route redirected to the template library; its term inventory is not certified. CPT UI lists one registered custom type portfolio and one custom taxonomy project-type; plugin-owned types are separately inventoried.

Current AIOSEO sitemap index advertises only post-sitemap.xml(31 URLs) and page-sitemap.xml(83 URLs). Four published Pages and all13 portfolio items are absent from their combined URL set. Draft visibility/previous public history and current anonymous HTTP/indexability remain separate facts.

[Detailed production audit and all source record locators](audits/2026-10-21-production-admin-and-partners.md) · [Partner Programs editing/activation/recovery](components/partner-programs.md)

Reading Settings read-only verification confirms Front Page40 and Posts Page2187: Blog is the native posts index. The canonical model is now posts_index; older E13 candidate wording is historical. Source Page8929 does not replace Portfolio CPT archive. No routing/template change was made.
