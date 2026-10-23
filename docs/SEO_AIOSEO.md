# AIOSEO global configuration — E80, 2026-10-21

**2026-10-23 — service rollout:** Authored unique native aioseo_meta_data title/description for existing487–491,515–525 excluding preserved514. Canonical/robots/schema configuration and global settings retained; native saves may label the already-existing default WebPage graph. No new schema emitter. [Exact saved titles and checks](evidence/2026-10-23-service-rollout.json).

**2026-10-22 — Water514:** Native registered `aioseo_meta_data` fields now contain title **Water Damage Restoration Chicago | GCPRO** and description **Water damage restoration in Chicago and Chicagoland. Explore extraction, drying, recovery steps and real GCPRO work. Call or request service.** Actual frontend title/description verified. Existing canonical resolves to `/residential-services/water-damage/`; staging `noindex, nofollow, max-image-preview:large` retained. Only these two authored fields were written; no robots, canonical, indexing, schema or global-option change. [Completed page and limits](components/water-damage.md).

**Semantic targeting note,2026-10-21 — DRAFT — AWAITING USER APPROVAL:** Current settings recorded here remain implementation history. Future approved page SEO/content work must use the [central semantic map and briefs](seo/SEO_STRATEGY.md); no AIOSEO setting was changed by this research task.


**E84:** [Commercial499](seo/2026-10-21-commercial-services.md) now has authored50-character title,160-character description, focus phrase, self-canonical, native Service graph and featured WebP social metadata. Browser/anonymous head verified; staging noindex/nofollow and global Organization preserved. No new global SEO changes.

## E81 image/gallery metadata

Page493 native AIOSEO title: `Restoration Before & After Photos | GCPRO`; description: `Explore GCPRO before-and-after photos of home and commercial restoration, including interiors, kitchens, bathrooms and exterior repairs.` Canonical retains staging `/before-and-after/`; featured image1248 uses optimized4:3 WebP. Staging noindex preserved. All gallery image alt fields present; Media titles/descriptions supplied. Technician1243 carries a descriptive alt and Media title/description; no filename stuffing or new custom schema. Existing Residential authored metadata unchanged. [Assets and exact owners](components/before-after.md).

Staging only. Existing AIOSEO Pro5.0.4 emitter; existing Lite5.0.3 also remains active. No plugin installed, replaced, deactivated or updated. Native supported options/post metadata APIs; no direct database edits or deployed custom code. [Search Appearance](https://vitaliiv1.sg-host.com/wp-admin/admin.php?page=aioseo-search-appearance#/global-settings) · [Social](https://vitaliiv1.sg-host.com/wp-admin/admin.php?page=aioseo-social-networks) · [Sitemaps](https://vitaliiv1.sg-host.com/wp-admin/admin.php?page=aioseo-sitemaps) · [Reading](https://vitaliiv1.sg-host.com/wp-admin/options-reading.php).

## Titles and defaults

| Native editing location | Exact saved value / behavior |
|---|---|
| Search Appearance → Global Settings → Title Separator; `searchAppearance.global.separator` | `|` |
| Content Types → Pages; dynamic `searchAppearance.postTypes.page.title` | `#post_title #separator_sa GCPRO` |
| Content Types → Posts; dynamic `searchAppearance.postTypes.post.title` | `#post_title #separator_sa GCPRO` |
| Pages / Posts metaDescription | `#post_excerpt`; authored per-page descriptions take precedence. Pages previously used whole `#post_content`. Blank structural excerpts can yield no description; do not invent generic page-specific copy. |
| Taxonomies → Categories / Tags title | `#taxonomy_title #separator_sa GCPRO` |
| Category / Tag description | Existing `#taxonomy_description`, retained; empty-category noindex retained |
| Archives → Author / Date / Search titles | `#author_name #separator_sa GCPRO`; `#archive_date #separator_sa GCPRO`; `#search_term #separator_sa GCPRO` |
| Page schema default | Existing WebPage |
| Post schema default | Existing Article / BlogPosting |
| Taxonomy schema | Native archive CollectionPage generation |

Literal GCPRO avoids inheriting the longer WordPress `#site_title`. Page-specific titles remain editable; no forced title-length truncation or arbitrary character quota, no automatic addition of Chicago/Restoration. E80 explicitly hides author/date archives, categories/tags and attachment search results while content is unfinished; search noindex is retained. Attachment titles now use the same short-brand pattern; attachment description and redirect behavior remain unchanged. BEAF `bafg` and `bafg_gallery` settings remain unchanged intentional third-party exceptions; global separator naturally propagates. No global keyword/meta-keyword injection (`useKeywords=false` retained).

**Portfolio:** `/portfolio/` is actual Published Page1132, All Projects; it renders **All Projects | GCPRO** through Pages defaults. No Portfolio CPT/taxonomy is registered on staging. The13 production project URLs are inventory-only until migration. No fake CPT option/plugin/record was created; when the real CPT exists, apply `#post_title #separator_sa GCPRO`, authored excerpt/metadata and appropriate project schema after checking its actual keys. Current configuration does not certify future CPT output.

## Actual page-specific exceptions

Only two Pages in the93-Page native inventory have authored SEO title/description values; other pages inherit defaults and are not claimed individually optimized.

### Homepage — Page154

- Title: **Property Restoration in Chicago | GCPRO**
- Description: GCPRO provides residential and commercial restoration in Chicago and Chicagoland. Explore water, fire, mold and storm damage services. Call 847-656-3322.
- Canonical: `https://vitaliiv1.sg-host.com/`
- Matching authored OG/Twitter title/description; OG website; `summary_large_image` using OG.

### Residential Services — Page484

- Title: **Residential Restoration Services in Chicago | GCPRO**
- Description: Water, fire, mold or storm damage at home? GCPRO offers residential restoration services in Chicago and Chicagoland. Call 847-656-3322 to discuss your project.
- Canonical: `https://vitaliiv1.sg-host.com/residential-services/`
- Matching authored OG/Twitter title/description; OG website; `summary_large_image` using OG.

Homepage authored fields remain stored on Page154; static Homepage wins over the global fallback. E80 also aligns global `siteTitle` and `metaDescription` to the approved Homepage values. Its custom OG image source is native `custom_image`, URL `https://vitaliiv1.sg-host.com/wp-content/uploads/2026/10/tinley-6-6.jpg`,1600×1200, original after-photo Media725; no visible Hero or shortcode edit. Residential uses featured747 and native Service graph; [full copy and schema](seo/2026-10-21-residential-services.md). Canonicals remain staging-self, never production by assumption. Host/canonical migration needs explicit launch review.

## Website brand versus organization identity

Knowledge Graph `websiteName=GCPRO`, `websiteAlternateName=GCPRO Restoration`; existing Organization representation and `organizationName=#site_title` retained, resolving **GCPRO Restoration**. WordPress site title and legal/official name are not renamed. Existing SVG logo remains the valid Organization logo; public phone `+18476563322` and email `restore@gcprochicago.com` added to native Knowledge Graph fields. Rendered Organization and Service provider reference verified. No founding date, employee count, credentials, ratings, prices or office hours invented.

**E80 Local SEO:** the owner activated the existing entitled Local Business addon1.3.17 after E79. Native single-location configuration is now saved and rendered; exact values, source evidence and vendor limitations follow below. E79's missing-addon observation is historical, not current. Physical office hours remain unspecified;24/7 refers to emergency restoration availability.

## Social sharing

Social Networks → Social Profiles now uses the four actual existing Footer destinations: Facebook `https://www.facebook.com/GCPRORESTORATION/`, LinkedIn `https://www.linkedin.com/company/gcpro-restoration/`, Instagram `https://www.instagram.com/gcprorestoration/`, Yelp `https://www.yelp.com/biz/gcpro-restoration-lombard-2`. Other handles remain empty. Configured profiles and rendered sameAs are distinct: observed Organization emits Instagram/LinkedIn/Yelp, but not the configured Facebook URL; no custom schema workaround was introduced.

Facebook general enabled, siteName **GCPRO**, default post image source `featured`, fallback image Media747 JPEG1600×1200; terms fallback same image. Replaces SVG-only social fallback without altering the Organization SVG logo. Twitter enabled, useOgData=true, summary_large_image, same featured/fallback image. Author attribution disabled globally for social cards rather than advertising fixture authors; Post OG type remains article, Pages and Categories/Tags now website. BEAF dynamic settings unchanged. No external sharing/debugger submission was made; actual rendered tags were verified.

## Sitemap and indexing configuration

**Staging Reading → Discourage search engines from indexing this site remains checked**; actual Page484/Home154/Portfolio1132 HTML emits `noindex, nofollow, max-image-preview:large`. No indexing enabled, robots permissions weakened, redirects created, URL restructuring or migration decisions executed.

Initially AIOSEO XML/RSS, News/Video/HTML options were enabled by default; initial XML exposed a Page sitemap despite noindex. Final staging-only state: **XML=false, RSS=false, News=false, Video=false, HTML=false**, llms=false retained. Do not advertise unpublished placeholder structures to crawlers. Prepared General XML selection remains explicit post/page, taxonomies category/post_tag; RSS selection post only. This excludes attachments, utilities and unrelated plugin types; no content objects were removed or edited. Author/date sitemap switches stay false, additional pages false, no custom priority/frequency invented. Empty terms/private/draft content follow native exclusions.

Anonymous after cache purge: Residential403; robots.txt200 with `/wp-admin/` disallow and no sitemap lines; sitemap.rss404. `/sitemap.xml` uses WordPress's existing provider fallback301→`/wp-sitemap.xml`, which404 while search engines are discouraged. This is core behavior after disabling generation, **not an authored redirect/migration rule**; no Redirection/AIOSEO redirect engine changes were made. Robots.txt does not itself block every frontend path; actual noindex and the observed access restriction remain the protection evidence, not a claim of robots `Disallow: /`.

Production launch is a separate approval: validate real content/indexing/canonical hosts, registered project CPT/taxonomies, publication statuses and intended archive policy; then explicitly enable XML/RSS if appropriate. Never enable indexing merely to obtain a plugin score. Current settings are intentionally a staging configuration, not production deployment-ready certification.

## Verification, exact storage and recovery

Native options: AIOSEO `/aioseo/v1/options` supports narrow `options` / `dynamicOptions` branches. Re-read via native options and settings export; snapshots/diffs retain exact public paths/values in sanitized evidence. Per-page AIOSEO metadata is the plugin's registered `aioseo_meta_data` field; storage is AIOSEO's own settings/post models, not Elementor Custom Code. No Custom Code ID or new runtime script exists for this task.

Actual browser output verifies static Homepage exception, Residential full metadata/schema, and Portfolio Page default. Posts currently comprise two Private ROBYLO fixtures; only category is empty Uncategorized. Post/taxonomy default values were read back, but no public migrated article/taxonomy result was available to certify. Neither fixtures nor taxonomy pages were published for a test.

Original Header113/Footer114/Home154 Atomic bodies/page settings and Page484 non-Hero structure/styles/links were compared unchanged; the later owner-authorized Hero image swap reuses742 in one native frame/shortcode. No new class, Variable, library Component, CSS, JS, PHP, plugin or dependency. One necessary Shortcode child renders the separately requested Hero comparison inside the reused native frame. Elementor53 nodes after the requested Hero reuse; global111 Classes/36 Variables retained from E78. One justified native Service graph reuses the existing plugin emitter instead of parallel custom JSON-LD. No settings/cache backups or auth data committed.

Recovery: use private pre-E79 supported settings export to restore ONLY changed AIOSEO branches after comparing current values, plus Page154/484 AIOSEO fields. Never import whole WordPress/database state or reset unrelated settings. Keep Reading noindex checked and staging XML/RSS disabled during recovery; restore old sitemap enable flags only with explicit owner indexing/launch approval. Residential copy recovery is separate. Purge staging cache and recheck real HTML. Historical production metadata/migration decisions in the CSV remain untouched.

Official reference: [AIOSEO sitemap content selection](https://aioseo.com/docs/choosing-which-content-to-include-in-your-xml-sitemap/), [indexing controls](https://aioseo.com/docs/showing-or-hiding-your-content-in-search-results/). Local behavior and supported option values were additionally verified against the installed version's native UI/schema and the owner's5.0.4 plugin archive, read only.


## E80 — completed global setup and Trustindex cleanup

[Sanitized settings and actual HTML evidence](evidence/2026-10-21-aioseo-global.json). No page/template body, shared Component, Header, Footer, BEAF or URL edit in this milestone. Native AIOSEO settings are the only SEO runtime owner. User disabled Rich Snippets in the separate staging Trustindex cloud widget; agent cleared **staging** Trustindex Advanced → Widget cache → Clear cache, then Purge SG Cache. No production/cloud widget configuration was changed by the agent.

### Local Business: exact storage and source verification

[Local SEO → Locations](https://vitaliiv1.sg-host.com/wp-admin/admin.php?page=aioseo-local-seo#/locations), native `options.localBusiness`:

| Path beneath localBusiness | Saved configuration |
|---|---|
| locations.general.multiple | false; one verified Lombard office, no synthetic city locations |
| locations.business.name / businessType | GCPRO Restoration / HomeAndConstructionBusiness |
| locations.business.address |220 Eisenhower Lane North; blank line2; Lombard; IL;60148;US |
| locations.business.contact | restore@gcprochicago.com; +18476563322; formatted (847)656-3322 |
| locations.business.areaServed | Chicago and the surrounding Chicagoland area |
| locations.business.image | Existing `/wp-content/uploads/2026/10/glenview-house-2.jpg` |
| locations.business.urls | staging root, `/about-us/`, `/contact-us/` |
| openingHours.show / alwaysOpen / timezone | false / false / America/Chicago |
| maps.mapOptions.center | lat41.8423663; lng-88.0193112, actual official GBP place marker |

Confirmed against [official production contact information](https://gcprochicago.com/contact-us/) and its [Google Business Profile destination](https://www.google.com/maps/place/GCPRO%2BRestoration/@41.8423663,-88.0193112,15z/data=!4m6!3m5!1s0x880fcd7522dd1503:0x63354c708d5cf6d6!8m2!3d41.8423663!4d-88.0193112!16s%2Fg%2F1tp0f843?entry=ttu), read only. GBP shows Open24hours all seven days; this does not verify physical office reception hours. Owner explicitly requires unspecified office hours unless confirmed. Native show=false suppresses stored default9–5 values; no openingHoursSpecification appears in rendered schema. Existing public24/7 emergency messaging stays separate. No legalName, VAT, prices, payment methods, qualifications, Google Place ID or additional offices invented.

Search Appearance → Global Settings → Knowledge Graph retains official organization identity, SVG logo and short Website name GCPRO. New `searchAppearance.global.schema.organizationDescription`: **Residential and commercial property restoration in Chicago and Chicagoland, with 24/7 emergency restoration services.** New global title fallback: `Property Restoration in Chicago #separator_sa GCPRO`; description matches the authored Homepage description above. This does not alter the approved per-page exceptions.

### Schema owners and actual limitations

Homepage now emits native BreadcrumbList, HomeAndConstructionBusiness, Organization, WebPage and WebSite in **one** AIOSEO graph. Local establishment and brand Organization have distinct IDs and a native brand reference; they are not duplicate rating graphs. Residential retains its native Service provider reference and existing authored metadata. No self-serving Product/rating markup was added to AIOSEO.

**Trustindex resolved:** Homepage154 → existing shortcode widget02441ff → `[trustindex data-widget-id=3c3f6b184e520136de76f94fefa]`, Widgets for Google Reviews14.2. After owner disabled staging Rich Snippets and native caches refreshed, authenticated browser and anonymous raw Homepage HTML both contain **no Product schema**. Ten reviews and loaded images remain; native Next carousel control clicked successfully. Prior E79/pre-refresh evidence remains dated history, not current output. Production widget untouched. There is no supported local shortcode rich-snippet flag; no CSS/JS/schema stripping hack or plugin-file edit was used.

**Vendor limitation retained:** installed Local Business1.3.17 `app/Schema/Graphs/LocalBusiness.php` generates `logo` as `https://vitaliiv1.sg-host.com/#logo`, without a matching ImageObject. Organization's actual SVG/ImageObject remains valid, and LocalBusiness.image is an actual JPEG. This was verified in installed source read only; no plugin patch/filter/parallel schema engine. No claim of external rich-result validation. Maps has no API key: saved marker center is verified, but interactive map/GeoCoordinates are not emitted. Do not invent a Place ID, enable billing or treat this as completed Maps integration.

### Archive rules, breadcrumbs and remaining modules

- Search Appearance → Archives: Author.show=false and Date.show=false; search results noindex retained. Content Types → Media attachment.show=false and short-brand title. Taxonomies → category.show=false, post_tag.show=false while only empty Uncategorized exists. Their default descriptions remain native taxonomy descriptions; no mass per-record overwrites. BEAF dynamic settings unchanged.
- [Breadcrumbs](https://vitaliiv1.sg-host.com/wp-admin/admin.php?page=aioseo-breadcrumbs): `breadcrumbs.categoryFullHierarchy=true`; existing Home link, current-item behavior and separator retained. Actual city BreadcrumbList preserves Home → Service Area → Expert Restoration Services in Lombard. No new visible breadcrumb widget or duplicated component.
- [Link Assistant](https://vitaliiv1.sg-host.com/wp-admin/admin.php?page=aioseo-link-assistant): activation gate; addon unavailable. Demo dashboard link counts are not a crawl result. No install, automated linking or replacement code.
- [Redirects](https://vitaliiv1.sg-host.com/wp-admin/admin.php?page=aioseo-redirects#/redirects): UI All0/Enabled0/Disabled0. Existing PHP method,404 and redirect logging with one-week retention retained; no automatic404 recovery, relocation, canonical redirect, htaccess writing or rule added. No IP/log data exported to Git.
- Webmaster verification fields are empty; no credentials/tokens guessed, no account connection or sitemap submission. Existing RSS after-content attribution (`The post #post_link first appeared on #site_link.`) retained; before-content empty.
- Image SEO addon absent: dormant formats are not claimed operational. No image renaming, bulk alt generation, filename or media mutation. Existing image alts retained. Native TruSEO/headline/SEO analysis settings remain enabled; no broad audit repeated. Integrated editor loading/score limitation from E79 remains, and a plugin score is not evidence of output correctness.

### Actual seven-page head verification

Every tested page has one title, one staging-self canonical, one AIOSEO script, short-brand title and `noindex, nofollow, max-image-preview:large`. OG website/GCPRO retained. Homepage and Residential authored title/descriptions/social overrides preserved.

| Actual route | Rendered title | Description status |
|---|---|---|
| `/` | Property Restoration in Chicago \| GCPRO | Authored; verified |
| `/residential-services/` | Residential Restoration Services in Chicago \| GCPRO | Authored; verified |
| `/commercial-services/` | Commercial Services \| GCPRO | Absent: structural placeholder, content work pending |
| `/service-area/` | Service Area \| GCPRO | Absent: structural placeholder |
| `/service-area/lombard/` | Expert Restoration Services in Lombard \| GCPRO | Absent: structural placeholder |
| `/portfolio/` | All Projects \| GCPRO | Absent: structural placeholder Page1132, not a CPT archive |
| `/partner-programs/` | Partner Programs \| GCPRO | Minimal placeholder excerpt; not finished SEO copy |

These unfinished pages are not certified fully optimized. Post defaults are saved/read back but two Private ROBYLO fixtures are the only Posts; no real article/published populated taxonomy or project CPT output exists to validate. No placeholder/fixture publication in E80.321 URL records and all production observations/migration decisions retained;93 Pages remain88 Published/5 Draft.

Fresh WordPress Reading checkbox verified checked. Anonymous Homepage200 after purge emits current AIOSEO graph/noindex and no Product; Residential403 means its head QA uses the authenticated browser. Existing robots/sitemap fallback behavior above unchanged. Chrome simulations:393px has scrollWidth393, reviews10 and no Product;1440px has scrollWidth1425 (no overflow), one H1 and10 reviews; physical Android/iOS not tested. No CSS/layout change requiring a new visual redesign test; protected154/484/113/114 native Atomic bodies and page settings compared exactly unchanged against pre-E80 snapshots.

### Recovery and launch gates

Recover only E80 modified native option branches using the private pre-E80 supported export after a fresh comparison; keep Reading noindex and sitemap generation disabled. Do not import whole database/options, re-enable rating snippets or touch production. Owner can restore their staging Trustindex cloud setting independently if desired, followed by staging native cache clear. No Elementor rollback needed because no component/layout fields changed.

Before production launch, separately approve final host/canonicals and real content, resolve thin archive/placeholder metadata, verify migrated Posts/projects/terms, recheck internal object links, assess addon logo vendor behavior, and enable only intended XML/RSS content/indexing with explicit authorization. Existing link destinations were preserved; seven routes opened successfully authenticated. No redirects, URL actions, production edits, new class/Variable/Component/Custom Code/plugin/dependency in E80. Existing owner-activated Local addon and Trustindex are the only relevant integrations; no new Custom Code ID.
