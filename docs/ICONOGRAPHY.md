# GCPRO iconography

## 2026-11-01 — Canonical used-icon registry and completion limits

**Site standard remains Uicons Regular Rounded (fi-rr), medium weight.** The owner additionally requested two comparable sets, thicker and thinner, to find a balanced weight. The second set below is **Thin Rounded (fi-tr), reference only**; it is not installed on staging. Regular Rounded remains the recommendation at the existing32/40/48px roles. Do not synthesize an intermediate stroke weight, force fill:none onto expanded paths, or substitute an unrelated concept.

| Meaning / icon | Regular Rounded source (`fi-rr`) | WP attachment | Actual owner / use | Thin Rounded comparison (`fi-tr`) |
|---|---|---|---|---|
|Water damage — raindrops|[raindrops](https://www.flaticon.com/free-icon-font/raindrops_5068885)|1438|Home154 Core; Service Card62 default; Residential484/Commercial499 icon Overrides|[raindrops](https://www.flaticon.com/free-icon-font/raindrops_11767035)|
|Fire / smoke — flame|[flame](https://www.flaticon.com/free-icon-font/flame_3916980)|1439|Home154 Core; Residential484/Commercial499 service Overrides|[flame](https://www.flaticon.com/free-icon-font/flame_16675772)|
|Mold remediation (approved generic disease metaphor) — disease|[disease](https://www.flaticon.com/free-icon-font/disease_9856315)|1440|Home154 Core; Residential484/Commercial499 service Overrides|[disease](https://www.flaticon.com/free-icon-font/disease_9856387)|
|Reconstruction — wrench-simple|[wrench-simple](https://www.flaticon.com/free-icon-font/wrench-simple_8778079)|1441|Home154 Core; Residential484/Commercial499 service Overrides|[wrench-simple](https://www.flaticon.com/free-icon-font/wrench-simple_8778140)|
|Storm damage — thunderstorm|[thunderstorm](https://www.flaticon.com/free-icon-font/thunderstorm_6854083)|1442|Home154 Core; Residential484 service Override|[thunderstorm](https://www.flaticon.com/free-icon-font/thunderstorm_7434914)|
|Personal property / contents — box-open|[box-open](https://www.flaticon.com/free-icon-font/box-open_9238295)|1443|Home154 Core; Residential484/Commercial499 service Overrides|[box-open](https://www.flaticon.com/free-icon-font/box-open_9239283)|
|Homes / condos; residential and commercial property — house-building|[house-building](https://www.flaticon.com/free-icon-font/house-building_9239740)|1425|Home154 audience58725369; Why1149 default benefit1|[house-building](https://www.flaticon.com/free-icon-font/house-building_9239302)|
|Comprehensive restoration — shield-check|[shield-check](https://www.flaticon.com/free-icon-font/shield-check_3917603)|1428|Why1149 default benefit2|[shield-check](https://www.flaticon.com/free-icon-font/shield-check_17495350)|
|Coordinated process — diagram-project|[diagram-project](https://www.flaticon.com/free-icon-font/diagram-project_8778033)|1429|Why1149 default benefit3|[diagram-project](https://www.flaticon.com/free-icon-font/diagram-project_8778104)|
|Clear / adjuster communication — comments|[comments](https://www.flaticon.com/free-icon-font/comments_5070422)|1435|Why1149 default benefit4; Insurance3796 SVG12e1e959|[comments](https://www.flaticon.com/free-icon-font/comments_10484786)|
|Cleanup to rebuild; general contracting — tools|[tools](https://www.flaticon.com/free-icon-font/tools_11270161)|3857|Home154 Why instance60cdf058 benefit1; Commercial499 c290c54d icon Override|[tools](https://www.flaticon.com/free-icon-font/tools_11270107)|
|24/7 emergency contact — timer-clock-call|[timer-clock-call](https://www.flaticon.com/free-icon-font/timer-clock-call_16310024)|3858|Home154 Why instance60cdf058 benefit2|Unmatched: source page exposes no fi-tr variant|
|Local Chicagoland team — map-marker-home|[map-marker-home](https://www.flaticon.com/free-icon-font/map-marker-home_5074065)|3859|Home154 Why instance60cdf058 benefit3|[map-marker-home](https://www.flaticon.com/free-icon-font/map-marker-home_19030085)|
|Restoring property and belongings — warehouse-alt|[warehouse-alt](https://www.flaticon.com/free-icon-font/warehouse-alt_9240018)|3860|Home154 Why instance60cdf058 benefit4|[warehouse-alt](https://www.flaticon.com/free-icon-font/warehouse-alt_9239366)|
|Commercial audience — building|[building](https://www.flaticon.com/free-icon-font/building_3914425)|3977|Home154 audience13cb5d39|[building](https://www.flaticon.com/free-icon-font/building_15399591)|
|Damage documentation — file-image|[file-image](https://www.flaticon.com/free-icon-font/file-image_10469600)|3863|Insurance3796 SVG349eab2e; Home154 consumer4ebf7d5d|[file-image](https://www.flaticon.com/free-icon-font/file-image_10470549)|
|Restoration estimates — calculator|[calculator](https://www.flaticon.com/free-icon-font/calculator_3914400)|3864|Insurance3796 SVGbd9087e; Home154 consumer4ebf7d5d|[calculator](https://www.flaticon.com/free-icon-font/calculator_15399600)|

**Insurance correction completed:** component3796, the registered “GCPRO / Insurance Support” (uid component-22774a7b-c32c-433e-9f6b-79ef52d247eb), now uses3863/3864/1435 in place of3894/3895/3896. File Image3863 and Calculator3864 path data exactly matched the verified fi-rr source SVGs. Comments1435 reuses the approved fi-rr asset. All three retain native40px boxes, color-text-muted and65% opacity; component layout/content and consumer Home154 remain intact. The saved values were read back after native component publication. The first publish attempt was incorrectly rejected by automatic review as a non-component; list-components confirmed its registered type and the subsequent publish succeeded. No permission or configuration changes were made.

**Sources and reuse:** all17 Regular Rounded source pages and their variant metadata were checked in the open authenticated Flaticon tab. Existing Home benefit assets3857–3860 also matched the original fi-rr path data exactly. The16 Thin Rounded links above were obtained from those same source pages; Timer Clock Call has no fi-tr variant exposed there. No duplicate WordPress uploads or new downloads were needed for this finishing pass. Original licensed Building3977 and earlier approved source files remain in their existing private locations.

**Representative checks:** Elementor Clear Files & Data reported success, then SiteGround Purge SG Cache was used. Authenticated staging frontend Insurance rendered all three expanded SVGs at40×40, muted rgb(91,101,117), opacity0.65, stroke none; desktop and390px mobile-emulation visual checks confirmed visibility and alignment. The temporary viewport override was cleared. Previous completed checks cover the two audience substitutions and General Contracting Tools. This is a targeted icon check, not an unrelated site audit, physical-device test or blanket anonymous-delivery claim.

**Flaticon collections remain BLOCKED, not complete:** existing “GCPRO - Regular Rounded fi-rr” collection68865866 is empty (0/17). Earlier native SVG import raised “Uncaught TypeError: Cannot read properties of null (reading 'value')” in fi-base at2026-11-01T20:04:05.597Z/20:04:05.849Z. The requested native-source fallback was inspected: Uicons detail pages expose no active Add to collection action, and their editor’s Save to collection button (#save_into_active) is disabled/hidden. The normal free-icon route for this Uicons ID returned404; it is not a usable alternative. No hidden control was forced and no further import/reconnect loop was attempted. No usable collection URL is available. Every one of the17 regular items above remains to be added; the thinner collection remains uncreated/unpopulated with16 sourced candidates plus the unmatched Timer Clock Call. These source lists are NOT Flaticon collections. Do not claim sitewide task completion until the collection deliverables are usable.

The prior Insurance-family exception is superseded. Preserved exclusions are brand/certification/social logos, Google stars, third-party widget controls and the coherent functional arrow/menu/close/contact-control families. Unused Feature Card65 is outside the actually-used set. Reused targeted saved-configuration inventory established shared consumers; no additional page crawl or website audit was performed.

## 2026-11-01 — Current standard and confirmed corrections

**Owner-approved current standard: Flaticon Uicons Regular Rounded (fi-rr), medium visual weight.** This supersedes the October 31 thin-outline trial below. Do not mix Thin, Bold, solid artwork, icon fonts or an additional CDN. Reuse approved SVG attachments through native controls and supported Overrides; preserve expanded outline path fill.

| Location | Replaced | Current attachment |
|---|---|---|
| Home154 Residential SVG58725369 | ROBYLO Home204 | House-building1425 (existing approved asset; homes/condos) |
| Home154 Commercial SVG13cb5d39 | ROBYLO Building205 | Building3977, fi-rr-building |
| Commercial499 General Contracting instance c290c54d | ROBYLO Tools207 | Tools3857 (existing asset), native icon Override |

Home artwork remains48px desktop/32px mobile, graphite contextual treatment. Removed only the two local SVG fill:none/stroke rules; all audience layout, spacing, text, links and functional arrows remain unchanged. Service-card badge sizing and orange treatment remain unchanged. Shared62 defaults were not changed; its12 live hub consumers were inspected before editing only the General Contracting Override. Why1149's15 known live consumers retain their existing native defaults/Overrides; no Thin replacements were introduced.

Building source: https://www.flaticon.com/free-icon-font/building_3914425 — Flaticon/Uicons Regular Rounded, downloaded2026-11-01 through the authenticated browser. One missing SVG uploaded through Elementor's supported SVG control/sanitizer as3977; no duplicate site uploads. Original building.svg and individual license PDF retained privately in Downloads. Ordinary WordPress media upload rejected SVG; no upload/security settings were changed.

**Verified on staging:** published native settings read back; Elementor Tools > Clear Files & Data returned success, followed by SiteGround Purge SG Cache. Actual frontend then rendered the new House-building/Building expanded paths with graphite fill and no stroke; General Contracting rendered Tools with orange fill. Earlier frontend checks showed cached ROBYLO markup until Elementor's HTML/data cache was cleared. Desktop frontend/paint verified; mobile dimensions are preserved in native settings, but a new mobile visual check is not claimed.

Intentional exceptions: coherent functional arrows/menu/close, contact phone/email/location group935–937, brand/certification/social logos, Google stars and third-party controls. Unused Feature Card65 was not changed. Inventory was limited to icons and their consumers; a few About/Testimonials/BeforeAfter roots failed transport reads, so full sitewide visual completion is not claimed.

Flaticon collection **GCPRO - Regular Rounded fi-rr** was created; SVG import failed with a page JavaScript error and the collection remained empty. Do not report it as populated. No purchases or subscription changes.

Header hover correction in the existing gcpro-smart-header global class: scoped normal-header secondary-button hover/focus-visible uses primary blue fill and white text. Actual pointer hover was verified; floating-header orange treatment remains.

## 2026-10-31 — Lighter outline direction and homepage trial

**Owner-approved visual direction:** use thin rounded outline artwork with a consistent apparent line weight,40px for large benefit icons and20–24px beside compact text. Preserve the established GCPRO color tokens and simple recognizable concepts. This updates the earlier Regular Rounded weight preference; historical asset/license records below remain intact. Exact thin-variant source pages and SVG paint still require verification before import; no new external family, download or license is claimed verified here.

Requested first replacement is limited to **Home154 > Why1149 instance60cdf058**:

| Role | Current attachment | Current supported Override |
| --- | --- | --- |
| From Cleanup to Rebuild |3857 tools.svg |prop-1792719457799-sbydh70 |
| 24/7 Emergency Contact |3858 timer-clock-call.svg |prop-1792719460379-4twr4eg |
| Local Chicagoland Team |3859 map-marker-home.svg |prop-1792719463290-7ztj8s7 |
| Restoring Your Property & Belongings |3860 warehouse-alt.svg |prop-1792719466312-9j3p4yk |

**Pending, not implemented:** fresh MCP reads confirm these four attachments remain assigned through native Homepage Overrides. No thinner matching files were found by the targeted Media Library searches. Local command execution failed before process startup (`sandbox provisioning failed: helper_sandbox_lock_failed … Access is denied`); the exposed Elementor tools support selecting existing SVG IDs but not uploading new assets, and browser control is unavailable. No replacement IDs exist, no WordPress edits were made, and thinner-icon browser verification remains pending. Do not report this documentation commit as a completed icon replacement.

Once asset upload is available, retain original files/IDs for recovery, select coherent thinner equivalents, change only these four Homepage Overrides, publish Home154 and perform one focused render check. Preserve shared1149 defaults, other page instances, current40px boxes, text, numbers visibility, grid, spacing and colors. Existing brand marks and functional arrows are excluded from the decorative-icon standard.

## Status and permanent direction

2026-10-23: Owner approved **Flaticon Uicons Regular Rounded** and subsequently reported that the four Why icons were already applied. This session researched assets and documented that decision only; no WordPress/Elementor changes, downloads or purchases were made. Actual attachment IDs, exported SVG contents, current installed mappings and site-wide icon replacement were not independently verified and must not be inferred from this record.

Follow the [approved style contract](DESIGN_SYSTEM.md#approved-icon-family--flaticon-uicons-regular-rounded). All links below were opened in the connected authenticated Flaticon browser; the selected pages displayed SVG and Premium Flaticon License, and the Uicons variants were checked as fi-rr. Author/publisher for all approved/proposed Uicons below: **Flaticon / Uicons**.

## Why Choose GCPRO — owner-selected

| Role | Exact icon | Direct page |
|---|---|---|
|Residential & Commercial|House-building|[Flaticon](https://www.flaticon.com/free-icon-font/house-building_9239740)|
|Comprehensive Restoration|Shield-check|[Flaticon](https://www.flaticon.com/free-icon-font/shield-check_3917603)|
|Coordinated Process|Diagram-project|[Flaticon](https://www.flaticon.com/free-icon-font/diagram-project_8778033)|
|Clear Communication|Comments|[Flaticon](https://www.flaticon.com/free-icon-font/comments_5070422)|

**Comments** supersedes the earlier **Comment-check** proposal. Its two speech bubbles avoid repeating Shield-check's checkmark. Preserve the earlier icon references only as historical research, not as the current approved fourth selection.

## Remaining twelve concepts — proposed, NOT approved for implementation

| Role | Candidate | Direct page | Status / semantic limits |
|---|---|---|---|
|Water Damage|Raindrops|[Flaticon](https://www.flaticon.com/free-icon-font/raindrops_5068885)|Water metaphor; not a literal damage scene.|
|Fire & Smoke|Flame|[Flaticon](https://www.flaticon.com/free-icon-font/flame_3916980)|Flame; smoke is conveyed by the service label.|
|Mold Remediation|Biohazard|[Flaticon](https://www.flaticon.com/free-icon-font/biohazard_9856287)|OPEN GAP. Biohazard was inspected but is visually heavy and signifies biological hazard generally. Do not use as an approved exact mold symbol. Bacterium was rejected as biologically inaccurate for mold.|
|Storm Damage|Thunderstorm|[Flaticon](https://www.flaticon.com/free-icon-font/thunderstorm_6854083)|Weather metaphor.|
|Reconstruction & Repairs|Wrench simple|[Flaticon](https://www.flaticon.com/free-icon-font/wrench-simple_8778079)|One simple wrench.|
|Contents Restoration|Box open|[Flaticon](https://www.flaticon.com/free-icon-font/box-open_9238295)|Packing/contents metaphor.|
|24/7 Emergency|Clock-three|[Flaticon](https://www.flaticon.com/free-icon-font/clock-three_7602696)|Clock;24/7 belongs in the accompanying label.|
|Property Assessment|Search|[Flaticon](https://www.flaticon.com/free-icon-font/search_3917132)|Magnifying glass; inspection context comes from the label.|
|Restoration Planning|Clipboard list|[Flaticon](https://www.flaticon.com/free-icon-font/clipboard-list_7857307)|Simple list/plan.|
|Quality & Completion|Check circle|[Flaticon](https://www.flaticon.com/free-icon-font/check-circle_10469499)|Plain check circle, no decorative medal.|
|Property Managers|Building|[Flaticon](https://www.flaticon.com/free-icon-font/building_3914425)|Building; management is specified by label.|
|Trade Partners|Handshake|[Flaticon](https://www.flaticon.com/free-icon-font/handshake_7653230)|Collaboration/handshake.|

Exact `mold` and `fungus` searches within Regular Rounded returned no matching interface icons on2026-10-23. This is a search observation, not proof that the entire evolving catalog has no usable symbol. Leave this concept unresolved until the owner approves a truthful generic remediation symbol or an explicitly permitted alternative; do not force a mismatch for16/16 completeness.

## Licensing and file handling

Primary terms: [Flaticon Terms, sections8–9](https://www.flaticon.com/legal), inspected2026-10-23. The authenticated session is Premium. Uicons pages call these “free interface icons”; Premium license availability does not make them Premium-only content. Premium removes attribution for eligible content downloaded during an active subscription; other restrictions remain. After an authorized download retain the asset's exact URL, author/style, date and license certificate privately with the project assets. Do not commit account details, signed CDN URLs, raw admin/browser responses or licensed source bundles indiscriminately.

All current research previews are screenshots of real Flaticon pages, stored locally outside this repository; no SVG/PNG download buttons, Copy SVG, collection save, purchase or asset installation was used. No licensed previews or source assets were committed. SVG internal structure, exported recoloring and final32/40/48px site render require validation after the corresponding implementation approval. Do not deploy an entire icon font for a small SVG set without a demonstrated need.

## Research assessment

Compared Uicons Regular Rounded, Regular Straight and Thin Rounded as consistent style packs. Regular Rounded was chosen by the owner; do not continue offering the others as interchangeable defaults. Eucalyp Meticulous Line/Rental Property Investing, HAJICON Black Outline/Property Business and Slameticon Black Outline/Property Management were also inspected as author-pack alternatives; their more detailed compound property motifs were less suitable for the owner's minimal direction. No claim of complete16-concept coverage or Premium-only status was established for those alternatives.

## Future workflow

1. Read the approved style contract and this registry; search the same family first.
2. Verify actual page, visual form, fi-rr variant and license; never invent an icon URL.
3. Present the exact icon and a genuine preview, identifying any semantic substitute.
4. Obtain approval for that selection and download/implementation scope.
5. Use native SVG controls and existing per-instance Overrides; test paint, size, color, keyboard/semantic treatment and all affected consumers as applicable.
6. Record verified attachment IDs, owners and results after implementation; preserve owner-reported vs independently verified status.

## Approved Core rollout — 2026-10-23

Owner approved and authorized original SVG downloads and staging replacement, including **Disease** for Mold. It is a generic microorganism/disease metaphor, not a literal fungal spore. This implemented record supersedes the earlier proposed status for these six concepts.

| Role | Exact Flaticon source | Media ID |
|---|---|---|
|Water Damage|[Raindrops](https://www.flaticon.com/free-icon-font/raindrops_5068885)|1438|
|Fire & Smoke|[Flame](https://www.flaticon.com/free-icon-font/flame_3916980)|1439|
|Mold Remediation|[Disease](https://www.flaticon.com/free-icon-font/disease_9856315)|1440|
|Reconstruction|[Wrench Simple](https://www.flaticon.com/free-icon-font/wrench-simple_8778079)|1441|
|Storm Damage|[Thunderstorm](https://www.flaticon.com/free-icon-font/thunderstorm_6854083)|1442|
|Personal Property|[Box Open](https://www.flaticon.com/free-icon-font/box-open_9238295)|1443|

All six are Flaticon/Uicons fi-rr, original SVG paths, single-color outline artwork. Downloaded from the verified detail-page original SVG media through the authenticated Premium browser. Original files and individual license PDFs retained privately in work/icon-rollout-1023/originals, outside this repository. Uploaded through the existing Elementor-aware WordPress media handler and sanitizer; no upload/security settings changed. Filenames gcpro-fi-rr-{slug}.svg. Do not upload copies per page.

Targets: Home154 Core section3fd180bb SVGs5071b7ac/2de7976c/7971ab6/16d7e4c2/1acc89e6/55d70b59. Native32px dimensions and color-accent (#F05A29). Residential484 service-card instances170443ba/3ed0e60b/dedb673/740bef0f/44127e7c/16d63af0. Commercial499 instances08061908/6b3576ff/d9949af5/0159b3bb/d7701a35. Existing Service Card62 SVG4a4396ac defaults to1438 and retains icon/title/description/cta_text/cta_link exposures. Its56px badge remains; native12px inset provides32px artwork. No content/link/layout edits intended.

Legacy icon-svg has a fill:none descendant rule incompatible with expanded Uicons paths. Removed that class only from the six Home SVGs and Service Card62 SVG; retained service-card__icon and added local native paint/sizing. Shared icon-svg, Why1149 and other Global Classes unchanged. No new classes, Variables, Components, custom code, fonts/CDNs, plugins or dependencies. Six unique media uploads only.

**Pending approval:** Commercial General Contracting instance c290c54d retains207; do not assume the Reconstruction approval covers that distinct concept. Feature Card65 retains203; no approved equivalent selected for its generic feature role. Other proposed registry concepts remain unapproved. Certification/brand/social marks, BEAF controls, navigation arrows and functional FAQ arrows excluded. Existing individual service pages and reusable components were included in saved-configuration inventory; no blanket all-page visual sign-off claimed.

**Verification/stop:** Home actual Chrome1440/768/393: six32px orange SVGs, no overflow, desktop/tablet40px track/24px gap and existing mobile32px/16px preserved; row-arrow hover responds. Owner explicitly stopped further verification. Residential/Commercial/individual-page final visual verification and full final preservation diff remain unverified. Owner owns final visual acceptance; routine future work gets only a minimal technical sanity check unless more QA is requested.

**Rollback:** Private all-posts-before.json and components-before.json under work/icon-rollout-1023 retain exact settings. Home prior IDs596/597/607/599/600/601, class icon-svg, no local icon styles. Restore hub icon Overrides from snapshots. Service Card62 previously defaulted192, classes service-card__icon + icon-svg, no local style. Restore its original SVG/classes/local style and all five exposed properties together; publish the component and affected pages through native lifecycle. Keep new media for recovery until unused references are established; no deletions authorized. No production changes.

