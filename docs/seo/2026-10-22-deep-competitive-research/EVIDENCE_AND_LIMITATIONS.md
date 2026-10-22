# Evidence, methodology and limitations

## Provenance labels

**W — website evidence:** direct public HTTP GET + HTML parsing, or browser DOM reads where public GET was blocked. Metadata, headings, observed links and image URLs are facts about the returned document. They are not proof of indexing, credential validity, equipment ownership, review authenticity or ranking causality. Browser reads recovered Midway and ServiceMaster pages blocked to the HTTP collector.

**S — SERP observation:** actual Google desktop searches in the connected browser on 22 October 2026. Signed out; `hl=en`, `gl=us`, `pws=0`; footer location **60026, Glenview, IL — From your IP address**. Chicago queries used the literal Chicago modifier. No downtown Chicago GPS pin, geogrid or mobile search was used. Rankings are specific to these conditions and timestamps, not universal Chicago positions.

**A — Ahrefs observation:** authenticated Site Explorer, Organic Keywords, Top Pages, Content Gap, Link Intersect, Referring Domains and Backlinks. US, **average volume** for Site Explorer/Keywords/Top Pages/Overview; **monthly volume** for Content Gap. Current date 22 October compared with 22 September where the UI retained comparison. Root-domain DR is shown even for local-prefix targets; backlink/referring-domain totals belong to the selected target. Never compare a national root’s traffic with a local-prefix estimate as equivalent businesses.

**H — historical repository evidence:** 21 October datasets and project documentation read from main at `472b72466cf6675fd4500ed8d5692ff5d198239b`. Prior GSC and Planner data remain historical; this task did not refresh those accounts. **I — interpretation/recommendation:** reasoning derived from W/S/A/H, expressly not an observed ranking factor.

## Capture and counting

* Thirteen queries cover nine major clusters plus Glenview, commercial water, commercial mold and residential water. `SERP_TOP10.csv` keeps ten **distinct observed organic URLs** per query. Page-one collections usually contained nine standalone heading links; page two was inspected to complete ten. Duplicate URLs across pagination were collapsed. `google_page` and raw heading order are preserved. Consequently the ordinal is an observation sequence, not a claim of Google's nominal `start` offset or a rank-tracker position.
* Advertisements, Local Services Ads, map listings, AI/other modules are not counted in that organic table. Directories and forums that occur organically remain in the table and are classified separately from service companies. Glenview module notes: sponsored Independent Restoration Services and SERVPRO, sponsored Redefined/Romexterra advertising destinations, and map entries including a roofing-oriented American Elite listing. Advertising destinations do not prove ownership of another similarly named organic domain.
* Google sometimes supplied opaque `/goto` redirect URLs. Public requests resolved many to actual URLs. Unresolved links retain their Google link and visible context; actual URL, H1 and metadata are explicitly unverified. Do not guess an exact destination from a truncated display URL.
* The collector made 284 public requests across original landings, SERP results, high-traffic pages and authority sources; 239 returned HTTP 200. These are **attempts**, including repeated URLs, not 239 unique websites. Nine additional browser DOM captures include competitor fallbacks and three staging hubs. See `evidence/coverage.json` for unique counts.
* 599 Organic Keywords rows, 163 Top Pages rows and 188 Content Gap rows were captured. Rows include comparisons and Lost items; they are not 599 current keywords or 163 currently successful pages. Romexterra/Restore/CWF and small local scopes were paginated; all 188 gap rows were captured. Only first 50 rows per selected backlink/refdomain report and first 50 Link Intersect domains were sampled; no claim of exhaustive backlink analysis.
* `position_raw_old_and_current` and Top Pages comparison fields preserve the UI. A Lost row contains a historical position, **not a current rank**. When two positions appear, inspect the raw cells and change label before assigning the current one. “N/A”, missing values and uncaptured endpoints are not zero.
* Ahrefs displayed a 22 October SERP-data-update warning about inconsistent Google data. Example: water restoration Chicago may be Lost with a September update while the same company appears in this live Google observation. Keep both sources rather than overwriting either.

## Scope and sampling limits

The SERVPRO Chicago landing-prefix excludes other franchises, which nevertheless appear in the SERPs. BluSky’s Chicago-location prefix excludes its separate Chicago mold page; the latter was separately inspected in both Ahrefs and on site. ATI’s prefix includes Chicago service children. ServiceMaster’s no-www prefix reflects its current browser destination. Paul Davis is a local subdomain scope. National brand DR is inherited context, not locally earned DR.

Page inspections retain H1/H2/H3, metadata, up to 150 observed links and 16 image references. `ARCHITECTURE_LINKS.csv` retains the full deduplicated internal-link edges observed by the collector, including large menus. It is not a sitemap-based exhaustive crawl. Navigation headings, responsive duplicates and empty headings may appear; heading order alone does not establish visible main-content structure or accessibility failure. Source word count includes navigation/footer and is not editorial content depth.

No independent certification registers, project dates, original-image provenance, review authenticity, response-time performance, financial capacity or actual conversion rates were validated. Claimed certifications/years/insurance handling are labeled site claims. National case studies cannot be relabeled Chicago cases. Regulatory, mold-health and insurance explanations need qualified review; avoid copying competitors' medical claims or coverage guarantees.

Current staging Home/Residential/Commercial DOM was inspected read-only. Elementor MCP was not required for this research and was not called. Child-page status and Atomic IDs are repository facts unless a specific current page read is stated. This is not a fresh audit of every Elementor object, all city pages, production analytics, redirects or editor responsiveness. Desktop/tablet/mobile implementation testing is outside this documentation-only task.

## Files and reproducibility

`evidence/ahrefs-overviews.json` preserves the metric block and report URL for all ten primary comparators, BELFOR and GCPRO. `evidence/ahrefs-report-tables.json` preserves report cells without account chrome. `evidence/page-inspections.json` preserves structural facts without full page bodies; failed requests remain visible. `evidence/serp-observation-conditions.json` records per-snapshot timestamps/settings. CSVs provide inspectable joins; exact source URLs are preferable to an undated screenshot.

Collection is a dated research snapshot. Recheck proposed target owners against fresh GSC query→page exports and production URL/backlink evidence before any merge, redirect or URL change. Research cannot demonstrate that a particular implementation will reach a promised rank or number of leads.
