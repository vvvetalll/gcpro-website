# Service schema audit — 2026-11-11

Status: **AUDIT COMPLETE; CORRECTION PLAN AWAITING OWNER APPROVAL.** Issue [#2](https://github.com/vvvetalll/gcpro-website/issues/2) remains open. Default branch: `main`. Staging only: https://vitaliiv1.sg-host.com. No WordPress, AIOSEO, Elementor, plugin, theme, cache, indexing or production changes were made.

## Outcome and severity

All 17 requested service landings were checked against their current AIOSEO per-page configuration and anonymous frontend JSON-LD. **1 OK, 16 ADD, 0 confirmed FIX, 0 page-specific REVIEW.** ADD denotes useful, supported, optional semantic enrichment; it is not a critical error, a prerequisite for indexing, or evidence of lost rankings. No critical syntax, entity-link, duplicate-emitter or Residential/Commercial mismatch was found in the inspected output.

The existing work on Residential Water Damage **514** is retained: its saved Service graph exactly matches its emitted Service. The other 16 pages have WebPage but no separate Service. WebPage and Service describe different things and can legitimately coexist.

## Evidence and method

- Read current default-branch [AGENTS.md](../../AGENTS.md), [SEO_AIOSEO.md](../SEO_AIOSEO.md), [SEO_STRATEGY.md](SEO_STRATEGY.md), and Issue #2, including its empty comment history. The E79/E80 AIOSEO and Trustindex work is historical evidence, not assumed current output. Residential/Commercial hubs **484/499** are separate from these 17 individual service landings; their previously recorded Service graphs are not counted here. The semantic strategy remains a draft awaiting approval: no proposed URL/audience restructuring is adopted by this audit.
- Read each current page's registered `aioseo_meta_data` through authenticated WordPress REST GET, limited to schema fields; fetched each actual public page anonymously (HTTP 200). Parsed every `application/ld+json` block and checked canonical, types, definitions/references, Service properties, descriptions and audience against page text. No admin response, credential or private customer record is included here.
- All 17 public responses contain exactly **one `script.aioseo-schema` JSON-LD block**, valid JSON, with the types listed below. No additional server-rendered JSON-LD emitter or HTML `itemtype` microdata was found. Browser DOM checks explicitly confirmed the same single-emitter pattern on 514, 515, 516 and supporting pages 487–491, including loaded review widgets; no Product/rating or other added JSON-LD was observed on those eight pages. The remaining nine rely on current anonymous HTML plus saved configuration, not a claimed completed browser-render pass.
- Schema.org Validator URL tests completed for **514, 517 and 515**: each reported **0 errors, 0 warnings**. Its connected-entity presentation lists Service for 514 and WebPage for the others, plus `hentry` (theme microformat, not a second JSON-LD emitter). These result item counts are not the count of all nodes in AIOSEO's graph. A supporting-page test was initiated but its completed result was not captured; no pass is claimed for it. External validation was representative, not 17 separate validator runs. All 17 received direct JSON parsing and relationship checks.
- [Google Rich Results Test for 514](https://search.google.com/test/rich-results/result?id=3BA8bTRIs_WLoLCtt5hCqQ), November 11 around 10:12 America/Chicago: page fetch **Successful**, crawl allowed **Yes**, indexing allowed **No: noindex detected in robots meta tag**. It reports valid Breadcrumbs, Organization and a Local businesses category, but the expanded latter item is explicitly `type Organization`, ID `/#organization`. That UI category does **not** prove an additional LocalBusiness graph. Overall result is “URL is not available to Google”; this is intentional staging indexing protection, not a schema correction request. Do not remove noindex for this audit.
- Browser navigation later timed out; no further dynamic-emitter coverage or Google URL tests are claimed. No live Google ranking/indexing, Search Console property, physical-device or production schema audit was performed. Tool result links can expire; the recorded observations above are the evidence, not a promise that a later retest is identical.

## All 17 service pages

**Base** = BreadcrumbList + Organization + WebPage + WebSite. Nested types include ImageObject, PostalAddress and Country; 514 additionally has City entries under Service.areaServed. No LocalBusiness/HomeAndConstructionBusiness, FAQPage, Product, Review or AggregateRating appears in the inspected 17 server graphs. Absence of those optional types is not itself an error.

| Page | URL / ID | Existing schema | Problem / classification | Recommended action |
|---|---|---|---|---|
| Residential Water Damage | [514](https://vitaliiv1.sg-host.com/residential-services/water-damage/) | Base + Service | **OK** — no confirmed issue | Retain existing page-level Service and WebPage. |
| Residential Fire & Smoke | [517](https://vitaliiv1.sg-host.com/residential-services/fire-smoke/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for residential fire and smoke damage restoration, after owner approval; retain WebPage. |
| Residential Mold | [516](https://vitaliiv1.sg-host.com/residential-services/mold-removal/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for residential mold remediation, after owner approval; retain WebPage. |
| Residential Reconstruction | [518](https://vitaliiv1.sg-host.com/residential-services/reconstruction/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for residential reconstruction after property damage, after owner approval; retain WebPage. |
| Residential Storm Damage | [523](https://vitaliiv1.sg-host.com/residential-services/storm-damage/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for residential storm damage restoration, after owner approval; retain WebPage. |
| Residential Personal Property | [521](https://vitaliiv1.sg-host.com/residential-services/personal-property-restoration/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for residential contents restoration, after owner approval; retain WebPage. |
| Commercial Water Damage | [515](https://vitaliiv1.sg-host.com/commercial-services/water-damage/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for commercial water damage restoration, after owner approval; retain WebPage. |
| Commercial Fire & Smoke | [520](https://vitaliiv1.sg-host.com/commercial-services/fire-smoke/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for commercial fire and smoke damage restoration, after owner approval; retain WebPage. |
| Commercial Mold | [519](https://vitaliiv1.sg-host.com/commercial-services/mold-removal/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for commercial mold remediation, after owner approval; retain WebPage. |
| Commercial General Contracting | [522](https://vitaliiv1.sg-host.com/commercial-services/general-contracting/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for commercial general contracting, after owner approval; retain WebPage. |
| Commercial Reconstruction | [524](https://vitaliiv1.sg-host.com/commercial-services/reconstruction/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for commercial reconstruction after property damage, after owner approval; retain WebPage. |
| Commercial Personal Property | [525](https://vitaliiv1.sg-host.com/commercial-services/personal-property-restoration/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for commercial contents restoration, after owner approval; retain WebPage. |
| Water Extraction | [487](https://vitaliiv1.sg-host.com/water-extraction/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for water extraction, after owner approval; retain WebPage. |
| Board-up | [488](https://vitaliiv1.sg-host.com/board-up/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for emergency board-up and temporary property protection, after owner approval; retain WebPage. |
| Odor Removal | [489](https://vitaliiv1.sg-host.com/odor-removal/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for property-damage odor removal and deodorization, after owner approval; retain WebPage. |
| Moisture Mapping | [490](https://vitaliiv1.sg-host.com/moisture-mapping/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for moisture mapping after water damage, after owner approval; retain WebPage. |
| Structural Drying / Dehumidification | [491](https://vitaliiv1.sg-host.com/dehumidification/) | Base | **ADD** — optional Service entity absent; base graph valid on direct inspection | Add one AIOSEO-managed Service for structural drying and dehumidification, after owner approval; retain WebPage. |

## Configuration, identity and relationships

Every page has `schema_type=default`; default output is enabled and emits WebPage. All have no explicitly selected additional `schema.graphs` or block graphs. Pages 522/524 have an empty saved default graph name but correctly inherit and emit WebPage: this is not a confirmed fault. Only 514 has a custom graph in AIOSEO: `#aioseo-custom-mvyar4wwrlnd`, named “Water Damage Restoration — Chicago”. This is an existing graph managed by AIOSEO's emitter, not Elementor Custom Code.

Common relationships, verified on all 17:

- WebPage `@id` = own canonical URL + `#webpage`; WebPage.url and canonical equal the actual page URL. `isPartOf` resolves to root `#website`; `breadcrumb` resolves to own `#breadcrumblist`.
- WebSite publisher resolves to root `#organization`. All `@id`-only references resolve to definitions in the same document, including nested logo/address definitions. No unresolved reference was found. Repeated references or nested expansion of a single ID are not duplicate business entities.
- Organization ID is `https://vitaliiv1.sg-host.com/#organization`, name GCPRO Restoration, phone `+18476563322`, email `restore@gcprochicago.com`, address **220 Eisenhower Lane North, Lombard, IL 60148, US**. These match verified project records and the read-only [official contact page](https://gcprochicago.com/contact-us/). No separate branch addresses are asserted.
- Organization logo is the existing `GCPRO_BLACK.svg` ImageObject, with page-specific `#organizationLogo` definition and a resolving image reference. The historical E80 homepage LocalBusiness `/#logo` vendor limitation is **not present in these 17 graphs**; it is not assigned to all service pages or claimed resolved globally.
- Breadcrumbs maintain the existing hierarchy (Residential/Commercial parent for the corresponding landings; Home → service for supporting pages). No hierarchy correction is needed merely because a page also acquires Service.

Existing 514 Service:

| Property | Current verified value / finding |
|---|---|
| `@id` / `url` | Own water-damage URL + `#service` / own canonical URL |
| `name` | Residential Water Damage Restoration in Chicago |
| `serviceType` | Residential water damage restoration |
| `provider` | `https://vitaliiv1.sg-host.com/#organization` — resolves |
| `mainEntityOfPage` | Own `#webpage` — resolves |
| `description` | Emergency water extraction, structural drying, household contents restoration and repairs for homes in Chicago and surrounding suburbs; consistent with current page scope |
| `areaServed` | City names Chicago, Lombard, Glenview, Northbrook, Oak Brook, Carol Stream, Downers Grove, Schaumburg, Highland Park, Naperville, Elmhurst (each Illinois); consistent with documented coverage/current visible service-area section; these are coverage locations, not offices or guaranteed dispatch eligibility |

For the other 16 pages, Service `@id`, `provider`, `areaServed`, `serviceType` and Service.url are **not applicable because no Service entity exists**. Their WebPage.url and shared Organization relationships are present and correct; missing Service properties must not be reported as malformed WebPage fields.

## Content accuracy, claims and conflicts

The six Residential WebPage descriptions identify homes/household contents and their actual damage or rebuilding scope. The six Commercial descriptions identify business premises, commercial repairs/general contracting or business contents. Commercial Fire 520 describes a business fire-loss discussion and explicitly avoids operating-time guarantees; it is not a Residential description. The five supporting descriptions distinguish extraction, temporary board-up, odor cleanup, moisture mapping and drying/dehumidification. No audience swap or service-description conflict was found. Keep the proposed Service scopes in the table equally specific; do not copy 514's residential wording to every page.

The common Organization description says Chicago/Chicagoland restoration with 24/7 emergency services. Project records support this geography and emergency contact. No inspected graph asserts physical office reception hours, prices, credentials, awards, guarantees or review/aggregate ratings. Visible review counts or credential logos are not independently verified structured-data facts and should not be copied into new Service graphs. Existing records explicitly distinguish 24/7 emergency contact from unconfirmed physical-office hours. No new branch, statewide/nationwide coverage or guaranteed response time is justified.

The actual output identifies AIOSEO as the JSON-LD owner; no competing Elementor/theme/Trustindex JSON-LD was found in anonymous responses, and the browser sample confirms that loaded review widgets did not add a second emitter. No plugin-source audit or proof of every possible delayed/conditional script state is claimed. FAQ sections do not require FAQPage, and absence of FAQ schema does not make Service invalid. Do not add self-serving Product/review markup to obtain stars.

## Prioritized plan — approval required before website edits

1. **P0 — no critical schema repair identified.** Retain 514 and all valid WebPage/Organization/WebSite/BreadcrumbList output. Keep staging noindex. No emergency schema deployment is warranted.
2. **P1 — optional main-service enrichment:** after owner approval, pilot Residential Fire **517**, then verify an explicit Commercial Service on **520** before applying the same AIOSEO-native method to **515, 516, 518, 519, 521, 522, 523, 524, 525**. Create exactly one distinct Service per page using the scopes in the table; retain 514 unchanged. Priorities are implementation convenience/coverage, not an unsupported traffic forecast.
3. **P2 — optional supporting-service enrichment:** **487, 488, 489, 490, 491**, describing only each documented task. Do not turn this into the draft strategy's URL consolidation or site redesign. Keep all 17 current URLs, copy, metadata, layouts and existing emitter ownership.
4. **P3 — verification/launch review:** finish browser dynamic-emitter checks for the other nine and external validation of each changed page when implementing. Before any separate production launch, verify final host/IDs/canonicals and indexing with owner authorization. Independently reconfirm credential/rating/office-hour claims only if a later task proposes encoding them; they are not required for this plan.

### Simplest native implementation

Use **AIOSEO → page Schema → Generate Schema → Service** in the installed native UI. Start with the pilot; confirm the native controls can retain the existing Organization reference and WebPage linkage. Use current-page canonical + `#service` as the unique ID, current URL, precise audience-specific name/serviceType, a short factual description, provider root `#organization`, `mainEntityOfPage` own `#webpage`, and supported Chicago/Chicagoland coverage. A simple text areaServed is permitted by Schema.org; there is no need to invent geographic geometry or repeat eleven cities everywhere.

If a required reference/property is not exposed by the installed generator, first inspect its saved/emitted pilot graph. Only if necessary, reuse the **existing page-level AIOSEO Custom Schema route demonstrated by 514**, inside the same plugin emitter. Do not add a global custom JSON-LD engine, plugin, theme filter, Elementor HTML widget or second Organization/LocalBusiness. This is a proposed fallback within AIOSEO, not a claim that the native Service UI has already been tested for writes.

For each approved edit: preserve its prior schema configuration for recovery; save only that page's schema; re-read configuration and anonymous/rendered JSON-LD; confirm exactly one Service, its intended audience, own URL/ID and resolving provider/page links; validate Schema.org and applicable Google-supported features; verify no duplicate rating/entity output. Do not alter unrelated content or remove staging noindex to obtain a green Google URL result.

## Validation meaning and next step

[Schema.org Service](https://schema.org/Service) defines the general vocabulary, including provider, serviceType and areaServed. [Google's supported structured-data gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) does not provide a general Service rich-result feature; [Rich Results Test documentation](https://support.google.com/webmasters/answer/7445569?hl=en) concerns Google-supported features. Valid markup neither guarantees display nor improved rankings; see [Google's structured-data policies](https://developers.google.com/search/docs/appearance/structured-data/sd-policies).

Owner decision requested by the task: approve or revise the optional AIOSEO additions and implementation order. **No schema implementation has been performed; Issue #2 must remain open.** Documentation and the issue update are the only authorized external writes in this audit.