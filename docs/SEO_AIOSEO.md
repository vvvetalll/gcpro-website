# AIOSEO global configuration — E79, 2026-10-21

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

Literal GCPRO avoids inheriting the longer WordPress `#site_title`. Page-specific titles remain editable; no forced title-length truncation or arbitrary character quota, no automatic addition of Chicago/Restoration. Author/date visibility and all robots inheritance/search noindex remain unchanged, pending future launch/content decisions. Media title/description/redirect settings are unchanged. BEAF `bafg` and `bafg_gallery` settings remain unchanged intentional third-party exceptions; global separator naturally propagates. No global keyword/meta-keyword injection (`useKeywords=false` retained).

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

Homepage AIOSEO-only fields are stored on Page154, not global `siteTitle` fallback: static Homepage wins over that fallback. Its custom OG image source is native `custom_image`, URL `https://vitaliiv1.sg-host.com/wp-content/uploads/2026/10/tinley-6-6.jpg`,1600×1200, original after-photo Media725; no visible Hero or shortcode edit. Residential uses featured747 and native Service graph; [full copy and schema](seo/2026-10-21-residential-services.md). Canonicals remain staging-self, never production by assumption. Host/canonical migration needs explicit launch review.

## Website brand versus organization identity

Knowledge Graph `websiteName=GCPRO`, `websiteAlternateName=GCPRO Restoration`; existing Organization representation and `organizationName=#site_title` retained, resolving **GCPRO Restoration**. WordPress site title and legal/official name are not renamed. Existing SVG logo remains the valid Organization logo; public phone `+18476563322` and email `restore@gcprochicago.com` added to native Knowledge Graph fields. Rendered Organization and Service provider reference verified. No founding date, employee count, credentials, ratings, prices or office hours invented.

**Local SEO limitation:** native Local SEO screen offers “Activate Local SEO”; the separate addon is absent from installed plugin inventory. No installation authorized/performed. Dormant `localBusiness` group remains exactly unchanged; its default9–5 hours and Seattle map coordinates are not validated business data and were NOT activated or published. No LocalBusiness address/hours output claimed. The verified220 Eisenhower Lane North / Lombard, IL60148 address stays intact in the site. Completing native LocalBusiness requires the owner to provide/activate the existing entitled addon in a separate authorized step and verify office hours/coordinates; do not confuse24/7 emergency calls with physical office hours. No custom schema workaround was added.

## Social sharing

Social Networks → Social Profiles now uses the four actual existing Footer destinations: Facebook `https://www.facebook.com/GCPRORESTORATION/`, LinkedIn `https://www.linkedin.com/company/gcpro-restoration/`, Instagram `https://www.instagram.com/gcprorestoration/`, Yelp `https://www.yelp.com/biz/gcpro-restoration-lombard-2`. Other handles remain empty.

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
