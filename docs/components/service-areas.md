# Service Areas

## Highland Park and reusable card design — 2026-11-03

Existing Interactive Card68 now owns the approved whole-card hover/focus/pressed/reduced-motion design for its66 direct instances across11 GEO pages, following the owner's explicit shared-component correction. Native city-specific title/description/link Overrides and grids remain;527's duplicate local interaction CSS removed.528 finalized with authentic licensed City Hall Hero, two-column local experience/real Lombard office, Northbrook/Glenview links, full Reviews section, Affiliations, FAQ/final CTA and one AIOSEO Service. Four projects preserved. Actual1440/390 and six service navigations on both527/528 checked; anonymous HTTP403 and unconfirmed roofing responsibilities documented. [Implementation, IDs, tests and recovery](../seo/2026-10-26-geographic-implementation.md#highland-park-finalization-and-shared-interactive-card68--2026-11-03).

## Downers Grove527 approved layout and interactions — 2026-11-03

Downers Grove now uses the approved Lombard Local Team composition with local copy, natural373.042px desktop office card/equal left span, nearby Lombard/Oak Brook/Elmhurst/Naperville links and mobile single-column layout. Existing Reviews4051 is inside full sectionff2490a2; Affiliations1886 follows. Six shared68 card instances retain whole-card native links; only page-local grid46bb8f70 owns pointer/lift/shadow/focus/active/reduced-motion styling, with no orange hover line. [Exact IDs, scope, tests, limitations and rollback](../seo/2026-10-26-geographic-implementation.md#downers-grove-finalization-and-card-interactions--2026-11-03).



## Lombard Local Team height correction — 2026-11-03

**Final owner-approved follow-up:** restored meaningful left copy in two paragraphs: heading instance68a1fb0e description is “Our Lombard office at 220 Eisenhower Lane North is a local contact point for homeowners and businesses.”; restored paragraph ad6af6d reads “Tell us about the damage to discuss restoration options and service availability. Please call ahead to arrange an office visit.” Only the two office text links remain removed, alongside the now-redundant second paragraph4411a461. Grid237e8357 uses existing24px desktop gap (mobile32px preserved), retaining original column ratio and natural card height. At1440px final left copy245.073px + nearby navigation94px within a373.042px complete left span; right card373.042px; top/bottom align within0.001px, no horizontal overflow. Four city links fit one desktop row. Owner visually approved this exact version. Final expanded-copy mobile wrapping was not rechecked; the preceding mobile layout/card check remains recorded below. This paragraph supersedes the intermediate copy-removal and desktop3+1 descriptions below.

Supersedes the width-only change in bb46889. Owner clarified equal desktop visual boundaries, then explicitly requested shortening/removing the left prose and removing both Office Map & Contact Details / View Service Areas links. Final staging Page526 keeps the original natural-height office card; it is not stretched to accommodate copy.

- Grid237e8357: restored1.35fr/1fr, native stretch alignment and rows `auto 1fr`; mobile remains one column with automatic rows. Nearby nav40142c moved from container109161ab into this grid, desktop column1/row2 aligned to the bottom; mobile automatic placement retains heading → office card → nearby navigation and the former48px card/navigation separation.
- Card3dff6bfa: removed the463px limit; spans desktop rows1–2 but uses `align-self: start`, original flex layout and24px internal gaps. No fixed height, content distribution trick, custom CSS or shared-definition change. Original padding/colors/type/buttons remain intact.
- Heading instance68a1fb0e: cleared its local description Override to remove the duplicated address (address stays in the office card). Removed paragraphs ad6af6d and4411a461 and, at the owner's explicit later request, link container39ae4c81 with links6fb1d101/65eb3a2a. Main heading, eyebrow, all four city links, office address and both card buttons remain. City-link styling and destinations are unchanged; existing wrapping yields3+1 at this desktop column width and2×2 on mobile.
- Native layout writes used direct Elementor MCP. The description Override used registered WordPress metadata after the MCP setting merge did not persist an empty Override; saved native data was reread. Temporary instance styling was restored; no new custom CSS remains.

Measured in authenticated Chrome at1440px (document Y coordinates): before, complete left span4020.635–4550.896 =530.260px and card4028.240–4401.281 =373.042px. After, complete left span4020.635–4393.677 =373.042px and card4020.635–4393.677 =373.042px; top difference0, bottom difference<0.001px. Card width462.979px; overall container1200px unchanged. At390px, heading108.188px, card334.667×367.844px (same natural card size as before), navigation154px; natural single-column stacking and2×2 city links. Visual checks passed, horizontal scroll/client widths1425/1425 and375/375. Scope limited to this section at those two sizes, not other browsers or a sitewide audit.

Private before/final Page526 backups remain outside Git. Recovery requires restoring the affected native elements/parents from the before backup; do not revert unrelated sections or shared components. Production untouched.

## Lombard local navigation refinement — 2026-11-03

Published staging Page526 only, following the owner's focused follow-up and clarification: ordinary text links have **no resting underline**, orange underline on hover/keyboard focus; outlined city links never acquire an underline. Existing text-link class and native destinations are preserved. Local Team buttons `6fb1d101` (Contact496) and `65eb3a2a` (Service Area495) retain their text, arrows, 44px targets and existing24px wrapping gap. Their local styles own the2px orange interactive underline,0.3em offset and visible orange keyboard outline.

Nearby links `1c198e33` (Elmhurst530), `3befddf1` (Oak Brook536), `3c0d2a21` (Downers Grove527), `282e738c` (Carol Stream543) retain text/arrows and native page selectors. Native local controls add44px minimum height, white background, color-border outline, space-xs radius,8px/16px padding and orange-border/color-surface hover. Existing container `6f4487a9` retains wrapping desktop flex and uses space-sm gap; mobile is two equal minmax(0,1fr) columns with8px horizontal padding. Heading61530d23 and all other content untouched. No new component/global class/token/plugin; no global templates, review configuration, map or production edits.

Storage: existing text-link owns typography; the seven affected elements own only this page's local presentation. Native Atomic styles store geometry, colors, borders, hover and mobile grid. Converter-retained local Custom CSS handles underline color/thickness/offset, focus-visible and nowrap (unsupported native conversions); no page-ID selector or separately deployed stylesheet. Recovery: restore only these seven elements' local styles/class attachments from private `work/lombard-audit-2026-11-03/links-before.json`, retaining later edits. Do not restore the whole page.

Verification: saved before/after comparison confirms exactly these seven elements changed, identical element set and unchanged texts/native links. Actual authenticated Chrome1440px: one compact row,44px targets, document scroll/client1425px;390px:2×2 grid,159.33px items,44px heights, no text clipping or overflow (scroll/client375px). Actual pointer hover: office underline rgb(240,90,41); city border same orange, background rgb(248,250,252), no underline. Tab focus confirmed orange2px outline and correct link treatment. Screenshots visually inspected. Six unchanged destinations independently returned anonymous HTTP200 and appropriate H1. Browser emulation, not physical-device or screen-reader certification; no broader regression or Reviews4051 repair claimed. This focused follow-up does not certify completion of the preceding broader audit.


## Technical optimization — 2026-11-03

**Current task/status and handoff.** Supersedes the rollout's sitewide delivery/observer/accessibility descriptions below. Staging only; existing1140,4134 and21 published consumers. No production, page-definition, global-template, map-CSS, CTA-style, Popup1801 or coverage edits. GEO01–GEO04 remain OPEN.

### Confirmed findings and implementation

- Saved4134 matched the pre-change compiled source after newline normalization. Default branch `main` and remote head checked before changes. Private recoverable backup: `gcpro-map-optimization-20261103/4134-before.html` outside Git; former display condition was Entire Site. Existing1140 was inspected in the native in-context editor: semantic root hook,11 native city links, heading/content Overrides and both CTA fields retained; no native definition write.
- Entire Site really delivered the214,733-byte inline artifact to Contact Us, which has no map. Replaced it with21 explicit **Include → Singular → Pages** conditions, exactly the page IDs in the consumer inventory below. Reopened/saved native conditions and confirmed Contact Us contains neither the map script nor a map. Future consumers must be added to4134's native conditions. Draft4104 remains unpublished/native and is outside this allowlist; use a published consumer for the enhanced preview.
- Existing compiler now simplifies only decorative land rings, starting each time from unchanged `map-panel.html`. Maximum Hausdorff deviation0.45 SVG units (asserted≤0.451); ring count retained. Featured municipalities and everything from the Lake Michigan group onward compare byte-for-byte identical. Existing coordinates already use0.1 precision; indiscriminate rounding or removal of islands was rejected. Shapely was already used by the Census builder; no new runtime dependency, request, plugin or build system.
- Runtime1.1.0 matches same-origin verified native destination paths to GEOIDs, not visible city names or an exact link count. Each pair continues to use the actual native link's URL. Unknown destinations remain native links; unmatched polygons become noninteractive; zero matches leave the native component intact. Diagnostics are restricted to Elementor preview URLs.
- Native links are the primary accessible navigation. Removed11 polygon tab stops and the SVG tab stop. The SVG is one descriptive image identifying Chicago, ten suburbs, Lake Michigan and the eligibility caveat; decorative polygons are hidden from the accessibility tree. List focus highlights its municipality, preserves the existing focus outline and recenters it when zoomed. Arrow keys on the existing zoom controls pan; native Enter navigation is untouched.
- Published consumers have their native component in the initial rendered document; startup runs once at DOM readiness with singleton/per-root guards. Removed persistent public body observation. The active Atomic editing canvas owns/replaces its native tree, so the enhancement intentionally skips that canvas instead of reparenting nodes while Elementor renders them. Native editing remains available; use frontend Preview Changes to test the map. No public dynamic insertion was observed/required on these21 consumers; future AJAX-inserted consumers require a specific lifecycle integration rather than restoring unconditional body observation.
- Removed empty `positionInfo()`, never-assigned reference branches, hidden-info coordinate writes and obsolete polygon keyboard handlers. Path center coordinates remain used for zoomed keyboard-focus recentering. Pointer/touch selection, drag suppression and controls remain intact.
- Arrow audit: all11 rendered arrows use the same `→`, Inter20px/20px and the same51.6004px desktop row height. Fractional positions exist, but no inconsistent CSS/font fallback was demonstrated. No speculative arrow replacement or style change; cross-browser rasterization remains unverified.

### Measurements

UTF-8 sizes normalize CRLF to LF to match WordPress delivery. gzip values are reproducible local gzip level9 compression, **not measured server transfer sizes**.

| Metric | Before | After |
|---|---:|---:|
| Compiled map source, bytes | 214,733 | 199,353 |
| Local gzip, bytes | 73,463 | 70,430 |
| Map script contribution on Contact Us | 214,733 bytes | 0 |
| Duplicate SVG keyboard stops | 12 | 0 |
| Dedicated map/geometry requests introduced by runtime | 0 | 0 |
| Public initialization | DOM-ready plus persistent body observer | DOM-ready once; no body observer |
| Actual document response bytes / compressed wire transfer | Not captured | Not captured |
| Cold/repeat transfer and numeric CLS | Not measured reliably | Not measured reliably |

Raw reduction15,380 bytes (7.16%); local gzip reduction3,033 bytes (4.13%). Original source panel199,123 bytes dominates payload; scoped CSS6,713 bytes. Featured geography was preserved rather than chasing a larger reduction. Script remains inline on map pages and cannot be cached independently of HTML. Conditional native emission avoids the whole payload on unrelated pages without adding a runtime asset dependency.

Read-only DOM serialization on Contact Us was457,454 characters before and242,970 after; this is a rendered, dynamically changing DOM observation, **not an HTML response/transfer measurement**. Browser network capture did not yield usable response/transfer records. Independent anonymous homepage/Contact Us requests returned SiteGround202 challenge responses (167/180 bytes), not website HTML. No Lighthouse score, wire compression ratio, cache-hit improvement or quantified CLS improvement is claimed. Existing scoped layout CSS is byte-unchanged; responsive visual checks found no new overflow.

### Actual verification and limits

- Authenticated Chrome: all21 inventory consumers showed their expected heading Override, one root/one initialized panel,11 matched native destinations and zero SVG/polygon tab stops; no horizontal overflow at the inspected viewport. This is a structural21-page pass, not a full interaction suite on every page. No direct page edits.
- Integrated homepage at1440px: all11 list→map and11 map→list pointer hover cases matched; all11 focused links highlighted the matching polygon with solid visible outlines. Existing15 available controls at default zoom are11 native links, two CTAs, Zoom in and Reset; disabled Zoom out is skipped. One Zoom click gives150%, keyboard ArrowRight pans, pointer drag changes transform without navigation, Reset returns100%. No duplicated map or repeated zoom increment observed; this is not a browser-wide listener census.
- Direct desktop polygon click opened Lombard; no map-runtime error was observed in the captured frontend error log. All11 native city links were actually opened in browser tabs and their destination titles checked, including Chicago→directory495. Actual Tab moved through the11 native cities in order; Enter on Chicago opened directory495. Both desktop CTAs tested: directory opened and availability opened Popup1801. No form submitted.
- Integrated touch emulation at768px and390px: first tap selects, choosing another city updates selection, second same-city tap opens Lombard; at150% touch dragging changes transform without navigating, clears selection, and Reset returns100%. At both widths there is no horizontal overflow, controls fit, and actions follow the map.390px CTA buttons have equal334.667px widths and52.531px heights. A single touch on the native Chicago list link opened directory495; mobile availability also opens1801. Ordinary scrolling/scroll-to-element works; no physical-device test is claimed.
- Modified-label/partial-list test runs the actual initializer's route-resolution section in a local Node fixture: all11 renamed display labels still match; one unknown route retains10 pairs and disables only its polygon; zero valid routes leaves native fallback. This is a source-level initialization test, not a persisted content experiment on staging.
- Source checks: JavaScript syntax, deterministic compilation, ring retention, bounded geometric deviation, exact featured/water preservation and whitespace diff check. Saved4134 reread in chunks equals the final compiled artifact after newline normalization. Existing polygon title removal is retained to avoid reintroducing native hover tooltips. Native editing canvas retains11 links and both CTA fields; no editor Publish action performed.
- Actual screen reader, other browsers, physical touch devices, guest rendering, reliable cold/repeat network/CLS profiling and arbitrary future dynamically inserted components remain unverified. Elementor/AIOSEO editor diagnostics were observed; they are not represented as a clean global-console pass. No production or coverage change.

### Recovery and next handoff

To revert only this optimization, restore `integrations/service-areas-map/{map.js,compile.py,custom-code.html}` from pre-optimization commit `cbdb67133b77ad0a80b1d25c7e355f856f268ab3`, paste that artifact into4134, and restore its former Entire Site condition if sitewide delivery is intentionally desired. Recheck saved code and relevant staging cache. Do not revert1140, native links/Overrides, button sweeps, unrelated work or GEO01–GEO04. The private4134 backup is an additional recovery copy, never committed. Owner visual acceptance and the explicitly unverified checks above remain separate from implementation completion.

## Shared interactive map rollout — 2026-11-03

**Current implementation; supersedes prototype-only restrictions below.** Owner authorized integrating the approved Draft4104 revision from `main` at `13b0b2aae463483f6108410b064b55e180a26215` into existing Atomic Component1140 on staging. No second component, production deployment, unrelated page content, global templates, Popup1801 or eligibility rules changed. GEO01–GEO04 remain OPEN.

### Ownership and saved structure

Component1140 root `e4ea1bc` retains its original section class and gains semantic hook `gc-service-areas-map` (Global Class `g-d1611dc`, position:relative). Native Chicago link `e5f4570` with paragraph `5167cca3` is first in existing column `470681c9`; its native Internal URL points to directory495. Existing ten links, both CTA elements (`73ee7e7e`, `4591c8e0`), container/intro/headings and Override envelopes remain intact. Saved-tree comparison:31 original nodes preserved,33 after adding Chicago; original settings unchanged except the root class assignment. Native component revision was explicitly **published** using the component API; merely saving a revision does not update consumers.

Elementor Custom Code **4134**, “GCPRO / Shared Service Areas Map”, owns the central progressive SVG/CSS/vanilla-JS enhancement: published, Body End, priority10, Entire Site. Sources and deterministic compiler: [integrations/service-areas-map](../../integrations/service-areas-map/README.md). Compiled artifact matches the rendered script after newline normalization. Host guard restricts runtime to `vitaliiv1.sg-host.com`; styling is scoped to the semantic component hook. Singleton global, per-root ready flag and unique touch-label IDs prevent repeated initialization; a MutationObserver supports newly rendered instances. Native links/actions remain available without JavaScript. No new plugin, library, remote geometry fetch, per-page implementation or duplicated URL registry.

Atomic's available schema does not provide the interactive municipal SVG primitive. The approved prototype code is therefore centrally owned by Custom Code rather than hidden in individual pages. Native copy, links and CTA Overrides remain editable in Elementor; polygon geometry and interaction code require the documented source files. The inline artifact is approximately215KB and is delivered sitewide by the Entire Site condition, although it initializes only component roots. This is a delivery/performance limitation, not a claim of conditional network loading.

Draft4104 remains unpublished and reuses1140. Removed its old prototype HTML widget `a4104def` to avoid a second runtime; native instance `a1140abc` retained. The historical prototype source is preserved in Git. Final authenticated Draft4104 preview confirmed one root, one map,11 links and ready state. Relevant staging SG/Elementor render caches cleared.

### Approved presentation and interaction

Preserve the latest actual prototype: full-width native heading/intro above36/64 columns, left list plus bottom-aligned intrinsic-width CTAs with a24px minimum flex gap; map/footer right. No fixed heights or stretched rows. At1024px and below: natural list → map → actions flow. SVG640:580 proportions remain unchanged.

Eleven cities, Chicago first. Default labels graphite; active row uses orange text/arrow and full-width orange bottom separator, transparent background, no vertical accent. Keyboard outline retained. Desktop bidirectional hover has no floating popup and click/Enter navigates directly. Touch polygon first tap selects and exposes a compact named destination, second same-city tap navigates; list links remain single-tap. Drag threshold suppresses accidental navigation; zoom/pan/Reset retained.

Chicago uses official Census1714000 polygon with passive permanent label/point and directory495 destination, not an invented Chicago page. Existing ten municipal links/geometry unchanged. Lake Michigan remains blue with its label inside water. Geography comes from the approved prototype manifest:2026 Census TIGER/Line Illinois PLACE plus Cook17031/Lake17097 AREAWATER; source URLs/checksums remain in `prototypes/service-areas-map/geography.json`. Municipal geography does not establish address-level service eligibility. Disclaimer and attribution retained.

### Consumer inventory and verification

**21 published direct consumers**, one instance each, plus Draft4104. Full ID/path/heading/check results: [consumers.json](../../integrations/service-areas-map/consumers.json).

| Page ID | Page | Staging path |
|---|---|---|
| 154 | GCPRO Homepage — Phase 1 Atomic Wireframe | `/` |
| 484 | Residential Restoration Services in Chicago | `/residential-services/` |
| 487 | Water extraction | `/water-extraction/` |
| 488 | Board Up | `/board-up/` |
| 489 | Odor Removal | `/odor-removal/` |
| 490 | Moisture mapping | `/moisture-mapping/` |
| 491 | Dehumidification | `/dehumidification/` |
| 495 | Service Area | `/service-area/` |
| 499 | Commercial Restoration Services in Chicago | `/commercial-services/` |
| 514 | Water Damage | `/residential-services/water-damage/` |
| 515 | Water Damage | `/commercial-services/water-damage/` |
| 516 | Mold Removal | `/residential-services/mold-removal/` |
| 517 | Fire & Smoke | `/residential-services/fire-smoke/` |
| 518 | Reconstruction | `/residential-services/reconstruction/` |
| 519 | Mold Removal | `/commercial-services/mold-removal/` |
| 520 | Fire & Smoke | `/commercial-services/fire-smoke/` |
| 521 | Personal Property Restoration | `/residential-services/personal-property-restoration/` |
| 522 | General Contracting | `/commercial-services/general-contracting/` |
| 523 | Storm Damage | `/residential-services/storm-damage/` |
| 524 | Reconstruction | `/commercial-services/reconstruction/` |
| 525 | Personal Property Restoration | `/commercial-services/personal-property-restoration/` |

Representative Residential Water514 tested first, followed by all21 authenticated browser pages at1440px: one root, one map,11 native city links, ready flag set, no horizontal overflow, individual section heading Overrides rendered. No direct edits were made to the21 page definitions. A final bulk REST comparison could not be completed because SiteGround returned challenge HTML, so byte-for-byte post-rollout page-tree equality is not claimed.

Focused browser verification on514 at1440/768/390px: approved layout, compact controls/footer, natural narrow-screen stacking, no horizontal overflow or overlap. All11 city destinations visited and correct page headings/no404 verified. Chicago Enter opened `/service-area/`; desktop polygon click opened Lombard. All22 list→map/map→list hover checks passed with popup hidden; visible focus and direct keyboard navigation checked. All Service Areas button actually opened directory495. Existing Check Service Availability button opened Popup1801 and its City/ZIP form; no form submission or popup change.

Chrome touch emulation390px: first Schaumburg tap selected without navigation; switching to Naperville changed selection; second Naperville tap opened its city page. At150%, touch drag changed transform without navigation and cleared selection; Reset restored100%. No physical-device testing claimed. Desktop/mobile screenshots saved as local delivery artifacts. No duplicate initialization observed across consumers. No map-script console error observed; one browser ViewTransition/opt-in navigation error was seen during navigation and is not represented as a map failure or a clean global-console pass.

Anonymous delivery: Home returned200 with hook,11 city links/Chicago and central script. Remaining anonymous automated requests returned403 or202 SiteGround challenge; full unauthenticated rendering is **not verified**. Authenticated browser checks are distinct from that limitation. No security protection bypassed.

### Rollback

Pre-change readable1140 definition, global-class registry, Draft4104 content and consumer inventory are retained outside Git in local `gcpro-map-rollout-20261103` backups. To revert only this rollout: disable/unpublish Custom Code4134; remove Chicago link `e5f4570` and only the `g-d1611dc` root assignment (retain original `g-d3248b3` section class); publish Component1140 and clear relevant staging render caches. Existing ten links, Overrides and both CTAs need no recreation. Restore Draft4104's backed-up HTML widget only after disabling the shared enhancement, to avoid double rendering. Do not revert concurrent page edits or geographic verification records.


**2026-10-27 focused content/URL review:** no component/layout/navigation rebuild. Page-owned Overrides shorten six-card/local copy and ten Process instances; Northbrook/Oak Brook FAQs now answer real repair questions. Six native AIOSEO title/description pairs added; original canonical/robots/schema preserved. All ten link targets remain Published; thirty deferred routes are individually registered as preservation recommendations awaiting owner approval,not migration deletions. Lombard1596 location remains owner-supplied rather than independently corroborated. [Review and30-URL register](../seo/2026-10-26-geographic-implementation.md#focused-content-and-url-preservation-review--2026-10-27).


**Current,2026-10-27 research-led revision:** ten published local pages (the nine independent-SERP research candidates plus completed Oak Brook); six former shells now contain useful source-backed local guidance rather than requiring a photograph. Shared1140 owns ten native city routes/27 Overrides, two columns of five, mobile one column.495 remains the wider directory. The four completed city bodies are unchanged. All36 queued objects were Published before the previous task and were changed to Draft by the agent; six now republished,30 remain unchanged from this task's start. No new unpublishing. [Current decision, owners, exact deferrals and tests](../seo/2026-10-26-geographic-implementation.md#current-decision-and-completed-first-rollout--2026-10-27-supersedes-four-only-selection). Earlier four-only entries below are historical, superseded.


**2026-10-27:**495 now reuses actual Homepage1140, then Chicago-neighborhood and municipal groups. Same1140 now owns four ready-city links with15 active Overrides; Footer114 has six compact geographic destinations. Four local pages Published/36 unsupported inherited shells Draft; no coverage change. [Current owners/statuses/tests](../seo/2026-10-26-geographic-implementation.md#completed-execution--2026-10-27).

## Lombard design pilot — 2026-10-26

Owner authorized one geo-page design based on existing SEO reports, for visual acceptance before any city rollout. Existing526 `/service-area/lombard/` is updated and Published on staging; same ID/path/status, original SEO metadata/canonical and noindex retained. Production and other city bodies unchanged.

**SEO basis:** [K061 brief](../seo/PAGE_SEO_BRIEFS.md#k061--lombard-service-area), [local architecture](../seo/2026-10-22-deep-competitive-research/GCPRO_ARCHITECTURE.md) and [conditional Lombard priority](../seo/2026-10-22-deep-competitive-research/IMPLEMENTATION_ROADMAP.md). This implements the owner's present Lombard-only request; it does not approve the remaining draft strategy or service×city expansion. One cross-service local landing connects verified office/local evidence to existing specialist pages. Broad-city query demand remains unmeasured in the cited research; no ranking/lead forecast, invented ZIP coverage, radius, neighborhoods, office hours or local projects.

**Current structure and owners:**

| Section | Native owner / locator |
| --- | --- |
| Hero | Existing Shared1318 instance1f8dbd0f, H1 Restoration Services in Lombard, IL; original media/mask/button design retained, content Overrides only |
| Six services | Section6f144ba6/container b524748; grid a56ae12 uses existing grid-3, six Interactive Card68 instances; Water/Fire/Mold/Reconstruction/Storm/Contents; native Internal URL→Content page bindings |
| Local proof | Section d5676df/container3b49e7d4, two-column copy/comparison, mobile stack; existing card fba213a6 and Shortcode b36bbb88 `[bafg id="1596"]` moved intact, no new slider or media |
| Process | Existing How We Work1152 instance19b8c6e, four content Overrides describing enquiry, assessment, restoration and repairs |
| Lombard office | Section54858021/container109161ab; confirmed address, directions, contact route; white copy area/navy contact panel using existing White Outline103 |
| FAQ | Existing full-section Service Questions1354 instance35b640f2, six independent local Q/A Overrides; approved two-column accordion/chevrons, not starter83 |
| Final CTA | Existing inset CTA80 instance25934c18; verified phone and named Content→Service Request492 |

Shared Heading71/accent wrapper, navigation59, text-link, existing container/grid classes and Variables reused. Text headings use graphite; navy panels retain white text. All specialist destinations verified against actual Published WordPress objects; saved labels use the exact current titles. No generic Chicago target reassignment, service route changes, schema changes or additional SEO plugin settings.

**Owner corrections:** FAQ now uses the actual1354 standard. Removed page-container padding resets that caused the local sections to start32px left of Hero/Process/FAQ. Existing global container g-68fb534 owns the same1200px maximum and32px desktop/20px mobile gutters. Shared1152 container466f7a12 and1354 container3969ecc5 now explicitly use native text-align:left, as requested for the components themselves; both retain the same global container class and unchanged layout/content. These two alignment-only shared edits affect their consumers; no other geo-page content/design rollout occurred. CTA inner copy retains the intentional inset-card padding.

**Focused verification:** Actual staging desktop and393px browser simulation: one H1; Hero and five primary section-heading left edges match at275px desktop/20px mobile in the observed viewport. Six services form3×2 desktop/one column mobile; proof and office split layouts stack, no horizontal document overflow. Native FAQ Enter opens the correct question. All six service hrefs rendered to the verified existing Residential pages; Commercial remains a separate hub action. Comparison images render, and the saved shortcode widget equals its pre-edit version byte-for-byte; plugin records/files untouched. Body has zero custom_css. Shared definitions1318/68/71/80, Header/Footer, media and SEO settings not edited. No new code, classes, variables, plugins or dependencies. Physical mobile/screen reader and every shared-component consumer not exhaustively retested; owner visual acceptance remains pending.

**Recovery and editing:** Private526 before/after snapshots remain outside Git. Edit pilot copy through page Overrides; shared FAQ/process design in1354/1152; grid geometry via existing grid-3/container classes. Restore only526 for page rollback, retaining later owner edits. The shared alignment rollback removes only native text-align from the two named containers. Do not copy this pilot to other cities until owner acceptance and their local evidence are confirmed.


**2026-10-24:**Directory495 and Lombard526/Glenview533/Northbrook556/Oak Brook536 completed at existing routes with real approved project comparisons. Shared1140 unchanged.47 other published city shells need distinct verified local source material; existing links retain correct objects rather than substituted routes. [Current coverage/content record](page-completion-2026-10-24.md).

**2026-10-23 — service availability popup:** Native Popup1801, shared1140 trigger; owner-authorized local form code. Submit stays open, accessible close/focus/reset and mobile checked. Owner supplied provisional Chicagoland scope; no ZIP/neighborhood exclusions are approved. Exact confirmation remains disabled; valid input shows the owner’s call-to-confirm message. Field/button layout is native Atomic,48px high,12px gap, inline desktop/tablet and stacked mobile. No invented coverage or Request492 form claim. [Editing, gap and recovery](service-availability-popup.md).


**E77 current:** Shared Component1140 now owns the unchanged Homepage design, with Homepage10feca9e and Residential5ced3ca1 consumers.12 city links and both actions are native real Page references. Former inactive availability action becomes Outline Orange100→492. Source7d8c17ad is historical. [Current exact locations and checks](residential-services.md).

Twelve community links and a directory action, followed by the separate [unfinished ZIP prototype](zip-search.md).

## Location and structure

Homepage154/main46c3aad4 → section **7d8c17ad** → container585624a1 → intro **3dc285eb**. Eyebrow1e3e2129; heading instance2554ebe8 →71; city grid **d6dbbe2**. Directory wrapper62862a3a contains link instance **2b5f493 →59** and prototype button5350691e.

All12 displayed-city/row/text locators and current destinations are maintained once in the [link register](../audits/2026-10-19-elementor-state-sync.md#current-service-areas-link-register). Several Navigator titles are stale; use displayed text plus actual IDs.

## Style/code ownership

Atomic native/local grid is3/2/1 columns; native **city-link g-9a26448** owns repeated layout/color, and **city-link__text g-efb17e3** owns typography. Standard section/container/stack, section-heading--accent and section-eyebrow apply. Tokens: font-heading/body, color-primary/accent/text, space-xs/sm and existing container/gutter values.

City-link's one class-owned Custom CSS block owns pseudo-arrow, focus outline, per-side border/transition limitations and reduced-motion rules. [Exact owner/exception](../CUSTOM_CODE.md); no page IDs or per-city copies are needed. Some border values remain literal approved visual values, not newly introduced tokens.

No Service Areas JavaScript, Custom Code, shortcode, HTML widget or external lookup API. Component71 supplies heading/description;59 supplies the directory button.

## Behavior, limitations and reuse

Hover/focus turns text/arrow orange and moves the pseudo-arrow0.2rem; reduced motion removes movement. Actual rendered width checks pass360/393/430/768/1440. All12 destinations and All Service Areas remain literal#; they are explicitly unresolved routes, not verified working navigation.

Edit content in Homepage native controls; repeated styles in the two existing classes. Bind intended existing published destination objects through supported Internal URL/page selectors when routes are approved. Preserve independent destinations, avoid duplicate location pages and retest native bindings after migration. Do not connect this layout to an invented ZIP backend. No visual refactor was performed.

## 2026-10-24 — Seventeen service-page consumers

All17 now use native1140 immediately before Reviews; retained514, added16 references with heading Overrides only. Central12 cities, native links, directory, availability Popup1801 and matching are unchanged. Earlier literal# / inactive-action descriptions above are historical. Current full chain: Service Areas → Reviews → Affiliations1886 → FAQ → Final CTA. [Coverage, actual checks and remaining limitations](../audits/2026-10-24-service-consistency.md). Five supporting-page background trials were removed after the renderer ignored them; no ineffective style left deployed.

## Lombard semantic follow-up — 2026-10-26

Read-only recheck found the current local landing role distinct from Chicago service owners, but three preserved production Lombard articles mix local informational and service-selection intent. Their staging counterparts remain Draft. Actual ranking cannibalization is unconfirmed without Lombard query×page data; resolve article roles and local evidence before rollout. [Evidence, boundaries and recommendations](../seo/2026-10-26-lombard-semantic-review.md).


---

## PROPOSED — NOT APPROVED: interactive Chicagoland map modernization (research, 2026-11-02)

**Status:** RESEARCH / PROPOSAL ONLY. **No WordPress, Elementor, site assets, plugins, CSS or JS were changed.** This section is not authorization to implement, publish, add locations, replace links or redraw claimed service coverage. Owner approval is required before any staging change.

### 1. Existing implementation audit and evidence

**Verified from existing project records (not a fresh live MCP read):**

- The section is **one native Elementor Atomic shared Component, GCPRO Service Areas (1140)**, not seventeen independently copied city sections or a conventional Theme Builder template. All 17 service pages reference the same definition; page-specific section headings use supported instance Overrides. The established service-page order is **Service Areas1140 → Reviews → Affiliations1886 → FAQ1354 → Final CTA80**. See [17-page rollout audit](../audits/2026-10-24-service-consistency.md) and [component reuse](residential-services.md). The source also has documented Home154, Residential hub484 and directory495 consumers; confirm the complete *current* consumer set before any shared-definition edit.
- Current geographic records supersede historical 12-city, 3/2/1 layouts and literal `#` links recorded earlier in this file. The **2026-10-27** source-of-truth record says **ten active native city routes and 27 Overrides**, displayed in **two columns of five on desktop and one column on mobile**, with directory page495 as a wider index. Ten current central city links lead to existing published local landing pages, rather than a generic map or search endpoint. Directory and “Check Service Availability” use the existing navigation/action setup; the latter involves **Popup1801** and is not an eligibility polygon lookup. See [geographic implementation](../seo/2026-10-26-geographic-implementation.md#current-decision-and-completed-first-rollout--2026-10-27-supersedes-four-only-selection), [popup record](service-availability-popup.md).
- Existing city rows retain native HTML links and shared `city-link` / `city-link__text` styling; the documented class-owned exception provides arrows, borders, hover/focus and reduced-motion behavior. Historic responsive testing covered 17 desktop instances and five mobile samples on 2026-10-24, **before** the later ten-city reduction, so it is not a new current-state visual certificate.
- Do **not** treat old twelve-city names, inactive `#` actions, 3/2/1 columns, or earlier Homepage-native section7d8c17ad as the current shared implementation. Dates in the earlier paragraphs are historical.
- **2026-10-30 wrinkle:** Elk Grove Village529 was separately published after the ten-city cohort. Its **inclusion in the current Component1140 city list is not verified** by the available record. Do not silently add it to map geometry or links without owner-approved alignment of current displayed city choices.

**Current documented ten displayed destination pages (the canonical map *candidate set*, pending live confirmation):**

| City | Existing WP object | Existing relative page route |
| --- | ---: | --- |
| Carol Stream | 543 | /service-area/carol-stream/ |
| Downers Grove | 527 | /service-area/downers-grove/ |
| Schaumburg | 558 | /service-area/schaumburg/ |
| Glenview | 533 | /service-area/glenview/ |
| Northbrook | 556 | /service-area/northbrook/ |
| Highland Park | 528 | /service-area/highland-park/ |
| Naperville | 532 | /service-area/naperville/ |
| Elmhurst | 530 | /service-area/elmhurst/ |
| Lombard | 526 | /service-area/lombard/ |
| Oak Brook | 536 | /service-area/oak-brook/ |

These are **existing city landing URLs**, not proposed new pages. The rendered link target must come from the existing *native Elementor links*, not from a second hard-coded staging-domain URL table. Confirm all hrefs, visible text, ordering, section-heading Overrides, buttons, current tablet/mobile layout and all shared consumers through a fresh MCP read and focused browser test before any approval-based implementation. Do not infer service eligibility from a clickable municipality.

**Verification limit for this research session:** GitHub `main`/AGENTS and documented 2026-10-24/27/30 audits were readable. Native Elementor MCP bindings were not exposed in the current toolset, the connected browser had no originating browser context, and direct staging page opens did not provide verifiable rendered page content. Therefore the exact live November 2 saved tree, schema for adding a map slot/attribute, currently rendered hrefs, all consumers and current responsive geometry **were not freshly inspected**. This is a **document-based implementation audit**, not a completed live Elementor audit.

### 2. One technical recommendation

**Recommend a lightweight, self-hosted, data-driven inline SVG map generated from simplified authoritative GeoJSON, with one small progressive-enhancement JavaScript interaction module.** Do **not** add a full tiled-map SDK.

| Candidate | Bidirectional city/polygon interaction | Weight / dependencies | Suitability here |
| --- | --- | --- | --- |
| **SVG paths derived from GeoJSON (RECOMMENDED)** | Native path hover/focus/click and DOM linking; one key per municipality | No tile requests, API key or mapping SDK; static geometry and small local JS | Best for a fixed, curated set of ~10 municipalities and exact highlight behavior; no pan/zoom requirement |
| Leaflet + OpenStreetMap | `L.geoJSON`, per-feature styles/events | Requires Leaflet CSS/JS, tile provider/attribution and network tile requests if using a background | Good if freely pannable street map is essential, but unnecessary for a fixed bounded diagram |
| MapLibre GL JS | GeoJSON fill layers + feature-state hover | WebGL renderer, style/tiles and additional asset/network complexity | Best for frequent zoom/pan, large feature counts and vector basemaps, not this limited shared section |
| Google Maps JavaScript API | Data layer loads GeoJSON, supports `mouseover`/`click` | API key, billing-enabled Google Cloud project, Dynamic Maps requests and third-party loading | Technically feasible, but higher vendor/billing/dependency burden without a needed Places/roads feature |

References: [Leaflet GeoJSON](https://leafletjs.com/examples/geojson/), [MapLibre GL hover states](https://maplibre.org/maplibre-gl-js/docs/examples/create-a-hover-effect/), [Google Maps Data layer](https://developers.google.com/maps/documentation/javascript/datalayer), [Google Maps pricing](https://developers.google.com/maps/billing-and-pricing/pricing) and [OSM tile use policy](https://operations.osmfoundation.org/policies/tiles/). No tile licensing/billing is needed for the recommended Census-derived SVG; display an appropriate data-source credit nevertheless.

### 3. Geographic data: factual boundaries, not a service-coverage claim

- **Primary source:** [US Census 2026 TIGER/Line, Illinois “Place” boundaries](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.2026.html) (legal names/boundaries as of **2026-01-01**, released **2026-10-14**). Use Illinois state FIPS17, exact incorporated-place names and **stable place GEOIDs** (not inferred centroids, ZIP codes, service radii or handmade city polygons). Resolve each of the ten displayed names to one authoritative record; check multipart polygons, adjacency, islands and names carefully.
- Optional faint, non-interactive geography for reader orientation (e.g., county lines / Lake Michigan shoreline) may be derived from authoritative Census geographic files **and compiled into the same one versioned map artifact**. Do not add separate runtime map/tile datasets. [Census cartographic boundary guidance](https://www.census.gov/geographies/mapping-files/time-series/geo/cartographic-boundary.html) explains simplified boundaries for small-scale maps.
- **Build-time pipeline only:** download the source once; validate city-to-GEOID list; reproject to a single fixed planar SVG coordinate space; topologically simplify at the intended viewport while retaining meaningful area shapes; clip/layout for Chicagoland; generate one checked-in, optimized SVG/compiled geometry artifact and manifest with source date, GEOIDs and labels. A generated SVG is a derivative of the **one canonical spatial registry**, not a second independently maintained city dataset. No full Illinois shapefile is sent to visitors.
- **Critical distinction:** colored polygons show **municipal geography for existing linked featured locations**, **not** the full boundaries of GCPRO’s service eligibility. Do not shade an invented metropolitan service area, imply geographic exclusions for uncolored places, or assert municipal-border service rules. Include a modest label such as “Featured locations — map for orientation; call to confirm availability.” Preserve current popup language; do not connect the SVG to eligibility logic.

### 4. Layout and behavior (proposal)

**Desktop (>= existing approved breakpoint):** Retain the existing shared section eyebrow/heading, intro, city-link design and two established actions. Below the heading, one Elementor-native two-column parent: **left ~40–45%** has the **existing ten city HTML anchors** in their established editorial order (choose one/two subcolumns only if readability supports it); **right ~55–60%** has a bounded Chicagoland vector map. Match shared max-width, gutters, graphite/navy/orange tokens and subtle lines; no heavy cards, shadows or competing CTA buttons. Align list and map tops; the map has stable aspect ratio/min-height without forced tall whitespace. Do not replace the current footer CTA or availability action.

**Tablet:** Use the actual shared Elementor breakpoints. Stack at the breakpoint where a usable list and map no longer fit side-by-side; avoid squeezed labels and map polygons.

**Mobile:** Natural full-width stacking, **city link list first** as reliable primary navigation, map after it with an accessible short heading/caption; cap vector height to avoid a huge scroll and allow labels to remain readable. Native anchor hit area >=44px high with consistent focus. If the map becomes too dense, provide a simple “Explore map” disclosure that is keyboard/touch accessible; the native list is always present, not hidden behind JS.

**Shared interaction contract:**
1. The selected/hovered **city list item** changes its native link emphasis and highlights the **one matching SVG municipal feature** by the same stable `place/GEOID` key. Moving to another city clears the prior transient highlight.
2. Hover/focus/touch selection of **map polygon** updates both corresponding city link and polygon, with a visible accessible city name. Keyboard **Tab** reaches map feature links; **Enter/Space** activates them; Escape clears a temporary selection if relevant. Highlight is not color-only (add stroke weight, emphasis/label), and respect `prefers-reduced-motion`.
3. Clicking a city anchor navigates to its **existing native page destination**. On desktop, clicking the corresponding map feature navigates to exactly that same href. On touch, first tap may select/highlight and reveal a clear **“View [City] services”** native-equivalent link; the link then navigates. Avoid unintended navigations when exploring polygons.
4. Use one per-instance scoping root, one initialized controller, and a matching `data-place-id` on the existing row and generated SVG geometry **only if supported by the live Atomic schema**. Otherwise match the current native anchor's *exact approved city label* to the GEOID registry during initialization (with unmatched-item reporting), without brittle Elementor generated IDs or page-specific CSS selectors. Destination href must be read from the actual live anchor, never manufactured from a slug.
5. With blocked/disabled JavaScript or a failed geometry load, the ten server-rendered city links, heading, directory link and Popup1801 trigger remain fully usable. No map feature should misleadingly act as a link without a resolved destination.

### 5. Reusable WordPress/Elementor architecture

Keep **Component1140 as the single presentation and content owner**, with **existing per-page heading Overrides** and native city links/buttons intact. Elementor controls should continue owning colors, typography, spacing, columns and responsive order; the mapping module should own only feature geometry, selected/highlight state and list↔polygon synchronization.

Since native Atomic V4 has no demonstrated municipal-polygon interaction primitive in the records, **propose one narrowly scoped reusable integration only after live capability validation**: a small GCPRO-owned WordPress integration (lightweight plugin or documented existing code owner, chosen during approval) serving the compiled SVG and a single scoped JS/CSS bundle. Prefer a server-rendered accessible vector slot in the shared1140 definition; if native slots cannot render/attach SVG features, a **single explicitly approved shortcode/custom widget** inside1140 is the fallback, **never 17 HTML-widget copies**. Load JS/CSS only on pages actually containing1140; initialize each instance independently and only once; preserve compatibility with Elementor editor preview/re-render. No map service, secret, Google key, or production deployment required.

Do not modify **BEAF Pro**, the global Header/Footer, service availability popup logic, SEO plugin settings, or the 17 page instances merely to introduce map layout. Ensure no duplicate section on Odor Removal or other service. A shared-definition change will affect other confirmed consumers (Home, Residential, directory), so their presentation must be reviewed and, if necessary, the design variant must be handled by supported Overrides rather than copied definitions.

**New-code approval gate:** AGENTS §5 requires an explicit authorization before adding custom JS/CSS/plugin/shortcode; the owner is being asked to approve this proposed exception, not being told it is already allowed.

### 6. SEO, accessibility, security and performance acceptance criteria

- Keep the original **server-rendered crawlable `<a href>` city links**, their native WP object URLs, ordering and contextual text. The map is **supplementary**, not a replacement and not a new sitemap/navigation/SEO landing-page system.
- No service×city pages, extra city pages, redirects, canonical changes, fake coverage or unsupported Schema.org `areaServed` expansion. Do not map Draft-only/old placeholder links as clickable destinations. Keep Page495 directory and Popup1801 action intact.
- Avoid SVG script and `foreignObject`, unsafe inline markup, foreign runtime assets and untrusted GeoJSON properties. Compile/sanitize at build time; escape all labels/attributes; resolve hrefs from site-owned native anchors; no arbitrary `window.location` from raw geometry. Respect site CSP and keyboard focus order.
- One local cacheable geometry/SVG asset and one small JS controller; compress/minify and self-host. Do not import Leaflet, MapLibre, Google SDK or OSM tiles in this version. Reserve the map's width/height to avoid CLS, lazy-initialize **below the fold** with `IntersectionObserver` and provide a non-JS city-list fallback. Measure transferred bytes and Core Web Vitals relative to baseline (LCP/INP/CLS), rather than promising unsupported performance numbers. Limit event handlers to delegation/per-instance listeners; no hover-driven layout measurement/reflow.
- Check keyboard screen-reader descriptions, visible focus, readable contrast, 44px mobile touch targets, `pointer` and touch selection, zoomed text, low-motion mode; city labels should stay accessible even for small/irregular polygons.

### 7. Approval-gated implementation plan

1. **Fresh read-only baseline:** reconnect the **existing** staging Elementor MCP (do not recreate it), read Component1140 saved definition/schema and its actual consumers; inspect representative desktop/tablet/mobile render and current city hrefs, heading Overrides, buttons, Popup1801, keyboard focus. Reconcile ten-city list versus 2026-10-30 Elk Grove529 and any later owner changes; obtain any coverage/content decision *separately* before including a new location. Save recovery reference/backup only once implementation is approved.
2. **Build off-site proof of concept:** extract authoritative 2026 Census Illinois Place geometries for **only the confirmed displayed linked cities**, validate GEOIDs and topology, simplify and generate one SVG artifact. Test bidirectional focus/hover, touch selection, native href resolution, density/visibility and disconnected/disabled-script fallback outside staging. No published change.
3. **After explicit approval:** add just one map slot and a responsive two-column layout **inside definition1140**; hook up the single minimal reusable scoped integration. Keep all existing links/actions/Overrides intact. Record the true CSS/JS location and rollback in [custom-code register](../CUSTOM_CODE.md) if any custom code is introduced.
4. **Targeted staging QA:** read back1140, verify a representative Residential service, Commercial service, one supporting service and each distinct shared consumer variant (Home154, Residential484, directory495). Then run one **presence + link + responsive smoke pass across the actual 17 service-page instances** (inventory below), including city-to-polygon parity, keyboard, touch simulation, and popup/directory CTA; do not redo unrelated site-wide QA. Verify accurate semantic HTML/no duplicate sections, no console errors, correct native links and no CLS/overflow. Owner visual approval follows.
5. **Rollback:** remove the single map slot/integration or restore the backed-up1140 shared definition while preserving later independent component revisions; the preexisting HTML city links and actions remain functional. No URL changes/deletions required. Update this record from PROPOSED only **after** approved implementation and verification.

**The 17 documented service-page consumers** (source: [2026-10-24 coverage table](../audits/2026-10-24-service-consistency.md); current status requires a fresh read): Residential Water514, Fire517, Mold516, Reconstruction518, Storm523, Contents521, Water Extraction487, Board-Up488, Odor Removal489, Moisture Mapping490, Dehumidification491; Commercial Water515, Fire520, Mold519, Reconstruction524, Contents525 and General Contracting522. Their current Component1140 instances were documented under native locator `5e152b1b` at the rollout; never use that as a global CSS selector or assume it is unchanged without re-reading staging.

**Decision requested of owner:** Approve *or decline* the **single shared SVG/GeoJSON + small JS integration** and the two-column enhancement after the live audit precondition; **no implementation approval has been given yet**.


## Interactive map prototype — 2026-11-03

**Implemented for owner review; not deployed to the shared component.** Current/default approved Git branch: `main`. Staging Draft **4104**, “GCPRO — Interactive Service Areas Map Prototype”: [editor-authenticated preview](https://vitaliiv1.sg-host.com/?page_id=4104&preview_id=4104&preview=true). Requires an editor session. Saved status `draft`; preview robots `noindex, nofollow`. No navigation/sitemap insertion or publication performed. Existing unrelated drafts were not suitable for this isolated prototype.

### Architecture and ownership

Root `a4104abc` holds the existing Component1140 instance `a1140abc` and prototype-only HTML widget `a4104def`. One source implementation under `prototypes/service-areas-map/`: build.py, map.css, map.js, map.svg, geography.json, prototype-widget.html and README.md. The compiled fragment embeds SVG/CSS/vanilla JS and runs only in this draft. No global Custom Code, plugin, stylesheet, template or production edit. Native1140 links, heading overrides and directory495/Popup1801 actions remain the source of content and navigation. Actual1140 content/style tree is byte-identical to the pre-task tool snapshot.

Explicit task exception: an isolated HTML widget is used for authorized prototype code, written through authenticated staging REST because the native Atomic tools cannot author legacy HTML widgets. Native document save refreshes Elementor's cached render. No new Hero1318 is added: this is a section-review sandbox, not a service/marketing page. The existing header/footer only frame the preview and were not edited.

Published direct consumers confirmed by current page-tree inventory:154,484,499,495,487,488,489,490,491,514,515,516,517,518,519,520,521,522,523,524,525. None changed. Draft4104 is the only new consumer.

### Geographic source and mapping

Official [US Census TIGER/Line2026 Illinois PLACE archive](https://www2.census.gov/geo/tiger/TIGER2026/PLACE/tl_2026_17_place.zip), listed2026-10-06. Source checksum is recorded in geography.json. NAD83 geography projected to EPSG26916; featured shapes simplified45m preserving topology, context90m. All ten resulting geometries valid; area change below0.31% each. Neutral context is nearby real municipalities clipped to the extent, not a fabricated service area. No extra featured city or invented boundary/radius.

| Featured city | Census GEOID | Existing published page |
|---|---|---|
| Lombard | 1744407 | 526 |
| Glenview | 1729938 | 533 |
| Northbrook | 1753481 | 556 |
| Oak Brook | 1754534 | 536 |
| Carol Stream | 1711332 | 543 |
| Downers Grove | 1720591 | 527 |
| Schaumburg | 1768003 | 558 |
| Highland Park | 1734722 | 528 |
| Naperville | 1751622 | 532 |
| Elmhurst | 1723620 | 530 |

`geography.json` is the canonical generated mapping. No duplicated destination registry: runtime resolves the original native city anchors, compares labels with SVG city names, and reads href from those anchors. A mismatch leaves native content untouched. Before future shared integration, stable native GEOID/page-ID keys should replace label matching so editorial renaming cannot break pairing.

### Behavior and visual layout

Existing heading/introduction precede a42/58 desktop grid inside the existing approved container. Original links left, real municipality geometry right, existing actions below the list. Mobile DOM/visual order: intro, ten city links, map, existing actions. Map height caps at340px on mobile and510px desktop; widths never force horizontal scrolling. Native typography/buttons retained; muted blue geography, orange active fill, emphasized navy boundary, city label and inset list indicator provide more than color alone.

Pointer hover and keyboard focus synchronize both directions. Map selection exposes “View city page” using the corresponding native href. Enter/Space selects and focuses that link; Escape clears selection. First touch selects without navigating. Original list links navigate directly. Reduced-motion disables transitions. All original HTML links remain usable without JS; in that fallback the styled static map follows the unmodified list/actions rather than the enhanced two-column arrangement. Availability popup still depends on its existing JS.

### Actual verification

- Official-name matching and unique GEOIDs checked for10/10 cities; all ten linked WordPress pages have `publish` status.
- Real pointer input:20/20 bidirectional hover checks passed (ten list-to-map and ten map-to-list).
- Real keyboard Enter selection:10/10 generated visit href values equal the original native href. Focus outline visible; Escape hides the visit action. Keyboard-driven actual city-list navigation reached Naperville; map visit navigation reached Lombard.
- Touch emulation at390px: tapping the actual Schaumburg polygon selects Schaumburg, exposes its correct href and keeps the draft URL unchanged.
- Actual Chrome1440px and390px visual checks: no horizontal overflow; original links, map and actions visible with the intended mobile order. Desktop screenshot and mobile full-section screenshot delivered to owner locally; no authenticated toolbar screenshots committed.
- JS-disabled reload: ten original city links present, no overflow, correctly styled static map, no enhanced initialization. Reduced-motion computed transition duration0s. Browser console error log empty during tested interactions.
- Original directory href retained; Check Service Availability actually opened Popup1801, then closed without form submission. Full unchanged-popup regression intentionally omitted.
- Final draft readback confirmed draft status and current widget content; shared1140 readback equals its pre-task tree. No existing consumers modified.
- Asset check: SVG158,018 bytes; compiled fragment about166KB uncompressed /55.5KB gzip estimate; CSS4.6KB, JS2.7KB uncompressed. No runtime map network requests/dependencies. Local build-time Python packages only.

### Limits, removal and next approval

This is a working reviewed-browser prototype, **not approved production integration**. Browser testing used Chrome desktop/mobile emulation, not a physical phone or full screen-reader audit. Tiny real municipal parts are not enlarged into false geometry; the comfortably sized native city list supplies an equivalent navigation target. Native labels must remain unchanged for current matching. Preview requires editor login. No-JS retains original link/action order, with a static map afterwards. Actual compressed HTTP transfer was not measured;55.5KB is a local gzip estimate.

Owner reviews the layout/behavior at4104. Only after explicit approval: back up1140 and its override schema, add a single shared SVG/integration owner, retain native city links and current heading/action Overrides, attach stable geography keys, test representative service/hub consumers, then authorize rollout. Do not copy HTML widgets into17 service pages. Popup1801 remains independent.

Rollback/removal is confined to draft4104: remove its local HTML widget and1140 instance, or trash the draft when authorized. No existing page, shared definition or global code needs restoration. Source files are recoverable in Git. Outstanding: owner visual/behavior approval and separately authorized shared integration; no rollout performed.


### Owner map visual refinement — 2026-11-03

Draft4104 only: extended real geographic context across the full right map viewport without stretching city shapes. Removed desktop510px height cap; mobile340px retained. Active municipality now orange fill only, no dark stroke; native list indicator and city label preserved. Saved/readback and390/1440 overflow checks passed; computed active fill rgb(240,90,41), stroke none. Existing1140 unchanged. Expanded SVG194KB / compiled fragment202KB raw supersede initial sizes. Implementation commit fcb6db4.


### Owner zoom, hover and geographic-context follow-up — 2026-11-03

Draft4104 only. Added100–300% zoom in50% steps, Reset, bounded mouse/touch dragging and arrow-key panning. Six-pixel drag threshold suppresses accidental city clicks; default-scale touch scrolling retained. Controls are created only with JS. No wheel/pinch zoom. Actual150% mouse drag and390px touch drag changed the transform; Reset returned100%. Native destinations preserved.

Final owner visual decision supersedes earlier light-orange-fill/underline instructions: city text and arrow turn orange with a thin orange separator across the full row; no background fill, left stripe or text underline. Default city/map/control labels use graphite text token; focus retains2px navy outline. List dimensions/spacing and original inactive separators preserved. Browser computed checks confirmed transparent background, no box shadow, no text decoration, orange active text/arrow/border and visible focus. Scoped prototype color rules override native link specificity without editing1140.

Owner authorized Chicago as a non-navigation geographic landmark (Census1714000 internal point41.8370453,-87.6849386), not an11th city link. Lake Michigan uses official2026 AREAWATER Cook17031/Lake17097 data, named lake faces plus adjoining H2030 water faces (including channel-named offshore faces); source URLs/checksums in geography.json. Real shoreline, muted-blue fill, graphite labels. Initial lake-face naming gaps corrected. All10 featured municipalities unchanged. Both landmark and lake move with zoom. No runtime downloads.

Actual1440/390 overflow checks passed; final desktop geographic context inspected and screenshot delivered locally. Source JS/CSS decoding explicitly UTF-8. Draft status/readback confirmed. Shared1140/global resources/production untouched. Physical-device/pinch testing not claimed. Rebuild now also requires the two AREAWATER ZIPs beside the PLACE ZIP. Remove draft-local widget to roll back; no rollout authorized.


### Final compact prototype — 2026-11-03

Owner-approved visual foundation preserved on unpublished Draft4104 only. Removed separate header row and permanent selection footer. Chicagoland is a compact in-map upper-left label; existing minus/plus/Reset controls float upper-right. Removed100% indicator and Zoom to explore. A city name and existing View city page link appear only during selection/focus/hover in a compact floating panel positioned opposite the city's projected reference point; positioning updates during zoom/pan. No empty panel, new controls, shadows or aspect-ratio/geographic-shape changes. Readable13px disclaimer and12px attribution directly below the map. Lake label wraps to avoid clipping; mobile geographic labels increased. Existing native CTA buttons retained.

**Final owner correction:** preserve the earlier city-row effect: transparent background, orange city text/arrow and thin orange full-width bottom separator; no text underline, orange left accent or fill. This explicitly supersedes the pasted brief's light-orange background/navy-active request. Visible2px keyboard outline retained; default labels graphite. Original row sizing and inactive separators retained.

**Chicago decision:** stays a non-interactive geographic reference with label/marker; never added to the ten-city list or given hover/navigation. Latest explicit owner instruction supersedes the earlier Chicago-interactive brief. Published-page search found Chicago Heights573/Chicago Ridge576 and general hubs, but no dedicated approved Chicago city destination. Lake Michigan remains non-interactive blue geography. Shared1140 tool tree compares identical to the baseline; no existing service pages, production, global templates or Popup1801 changed.

Final verification:1440px desktop and390px mobile have no horizontal overflow; default/selected/zoom states visually reviewed.20/20 real pointer bidirectional checks passed.10/10 keyboard selections expose the matching original href and keep the selected reference point clear of the floating panel. Keyboard focus solid2px, reduced-motion transition0s. Touch at390 selects Schaumburg without redirect; its floating-panel link actually opened the existing Schaumburg page. Lombard actual list navigation passed. All ten original native hrefs also match current WordPress published-page URLs/status. Browser automation detached after the first item in a full navigation sweep; anonymous fallback requests returned403 for all ten. Therefore actual browser opening of every destination is NOT claimed. JS-disabled reload confirmed ten native city anchors, no enhancement and no overflow. Zoom150%, upper bound300%/disabled plus and Reset100% verified; earlier mouse/touch pan preserved. Browser console errors empty during checks.

Updated source: build.py, map.css, map.js, generated map.svg/prototype-widget.html. Recovered original source geometry/path data; no municipality boundary changes. CSS state owners consolidated. Desktop default/selected and mobile screenshots delivered locally. Rollback: restore the draft HTML widget from commit682b10a (or private pre-compact snapshot) and refresh its Elementor document cache; do not roll back1140/global resources. Owner review remains the next step; no publication or rollout.


### Desktop direct navigation, touch two-tap and Chicago directory exception — 2026-11-03

Latest owner instructions supersede prior hover/navigation decisions. Isolated Draft4104 only. Desktop pointer hover now synchronizes row/polygon without any city popup; temporary hover clears on leave, retaining a separate keyboard focus state. Direct municipality click and keyboard Enter navigate to the href of the existing native city link. Map targets expose role=link and accessible city names; no touch-only gate for keyboard users. Active rows use the newly requested light-orange background, navy name and orange arrow, with no left stripe; municipalities remain orange. Approved compact geometry, zoom controls and footer remain.

Touch/pen: first tap selects and exposes the city/destination; second tap on the same polygon navigates. Another polygon switches selection only. Outside tap clears. Existing list anchors remain single-tap links. Pan movement suppresses click and disarms selection; zoom/reset disarm it too. Selection state is separated from keyboard/pointer state. To avoid covering a different municipality with a tappable link, the existing compact city/destination label appears immediately BELOW the map only during touch selection, not as an overlay. No empty label or desktop panel. This targeted placement correction prevents accidental navigation when switching cities.

**Owner-approved Chicago navigation exception:** Chicago is now first in the list and links to verified published Service Areas495 (`https://vitaliiv1.sg-host.com/service-area/`), never an invented Chicago URL. Existing point/label remains non-interactive; no Chicago polygon, hover or map navigation added.11 list destinations, original10 interactive municipalities. Other ten links unchanged. The draft-only HTML anchor is moved to the top of the existing rendered list and reads the native directory action's href; its no-JS relative-directory fallback remains available after the original component. Native1140 definition untouched. Future approved integration should expose this extra link natively rather than copy prototype HTML.

Recorded the navigation-only exception on Chicago's existing entry in `integrations/service-coverage.json`; pre-existing operational statuses, ZIP/coverage records and destinations remain unchanged. The note is not deployed to Popup1801/runtime. Chicago market representation does not imply new address guarantees. Existing geographic verification remains authoritative; source credit/disclaimer retained.

Verification:1440px desktop and390px mobile no overflow. Desktop list→map and map→list sync without popup confirmed; direct mouse selection reached Schaumburg; Enter reached Lombard. Real emulated touch first tap selected Schaumburg without navigation, another tap selected Naperville without navigation, second tap reached Naperville. Outside tap cleared;150% drag changed transform without URL change and cleared selection; Reset restored100%. Touch label no longer covers map targets. Eleven list entries/ten polygons and Chicago495 href verified; Chicago row spacing matches native rows after removing inherited paragraph margin. No physical-device test claimed. Screenshots delivered locally. Only draft content and source/docs changed; no shared1140, existing services, global templates, production or Popup1801 edits.

Source: build.py (single Chicago fallback anchor), map.js (input-specific navigation/state), map.css (approved active colors and conditional touch label), compiled widget. Rollback to107b3fd for prior interaction mode, scoped to draft widget; restore the added navigation-note field separately if needed. No public rollout or new city page.

Concurrent geographic verification work preserved: exact serviceable Chicago/address boundaries, exclusions and dispatch questions remain in [SERVICE_CAPABILITY_QUESTIONS.md, GEO01–GEO04](../SERVICE_CAPABILITY_QUESTIONS.md). This navigation exception resolves none of those operational questions.


Chicago hover correction — 2026-11-03: owner now requests synchronized hover for the existing Chicago point/label and first city row; keyboard focus on the list link also highlights the marker. No boundary, marker navigation, touch two-tap target or new destination added; the earlier no-hover decision above is superseded. Scoped to Draft4104.
Targeted authenticated-preview check passed: list-to-marker and marker-to-list hover, orange point/text, clear on pointer leave, and keyboard focus on Chicago. Other municipality handlers and shared1140 unchanged.


Chicago area hover correction — 2026-11-03: owner explicitly supersedes the point-only/no-boundary decision. Chicago now uses its official Census1714000 municipal polygon, clipped to the unchanged map viewport, with synchronized list/area highlight and the existing directory495 destination; its permanent point and label stay passive orientation references in their original colors. Existing interaction handlers apply to the area (desktop direct navigation, keyboard and touch two-tap); no new page, service-eligibility boundary or shared1140 edit. Municipal geography does not settle coverage questions in GEO01–GEO04.

Owner reiterated list styling: active/hover/focus rows use orange text/arrow and a full-width orange bottom separator, transparent background, no left accent; visible keyboard outline retained. This supersedes the light-orange row-fill instruction.
Lake Michigan label moved right and upward into open water to separate it from the shoreline. Authenticated desktop preview verified Chicago area/list hover synchronization, orange full-width separator/text without fill, unchanged landmark color, and visible lake-label clearance; no full regression repeated.


### Balanced prototype columns — 2026-11-03
Draft4104 only: group the existing rendered list/actions in one lightweight flex wrapper (`gc-map-left`); actions use `margin-top:auto` with a 24px minimum flex gap, intrinsic individual desktop button widths and left alignment. Right map/footer stretches to the same grid row. No fixed heights, spacers, absolute CTA positioning or stretched city rows. To fit eleven unchanged rows and both buttons without blank map-panel space, minimally rebalance desktop columns from42/58 to36/64; SVG keeps its640:580 aspect ratio and unchanged geometry. At1024px and below the wrapper uses display:contents and natural stacked list→map→actions flow; existing mobile button widths/touch styles remain.
Authenticated browser checks:1440px columns share top181.96 and bottom891.35, equal709.40px heights; list-to-CTA gap24px, row height51.67px unchanged, individual buttons216.99/300.84px with identical left edges and unchanged directory/popup destinations. At768px and390px stacked sections have24px gaps, no overlaps or horizontal overflow; mobile zoom buttons remain44px. Desktop/mobile screenshots saved locally and delivered. Interaction handlers, map colors/geometry, Chicago, attribution and disclaimer unchanged; no repeat of full two-tap regression or physical-device test. Shared1140, service pages and production untouched. Rollback only the prototype JS wrapper/CSS and compiled draft widget to09db116.


### CTA column width — 2026-11-03 (verification incomplete)
Shared Component1140 saved through Homepage154 → select Service Areas → Edit Component; direct standalone component editor remained on Loading, while in-context editing worked. Area actions73c11252 local Style → Custom CSS now contains `width: 100%; & a { width: 100%; }` (Elementor supplies the outer element.style wrapper); previous custom CSS was empty, so clearing this field rolls back the change; no global/button-definition, link, popup or visual-token changes were made. Authenticated frontend at1440px confirms both CTA widths394.55px with the same left/right edges as city rows and heights52.53px, and Check Service Availability opens Popup1801; browser control timed out during the directory-action check and then recovery, leaving directory navigation,768/390px, anonymous delivery and final visual acceptance unverified.


### CTA hover sweep — 2026-11-03

Later owner correction expanded this animation to the five existing global button variants; see [global sweep record](interaction-transitions.md#global-button-fill-sweep--2026-11-03). The compatible local rules below remain. Follow-up verified actual1440/768/390 CSS widths, equal CTA widths,390 buttons below map, click/keyboard Popup1801 and mobile directory navigation. The earlier outstanding768px layout check is now complete; anonymous/physical-device checks remain unperformed.
Published on staging only through Homepage154 → Edit Service Areas1140 → Area actions73c11252 → local Style/Custom CSS. Added the following nested rules, preserving all pre-existing CSS (including width rules); remove only this addition to roll back. Existing default transparent backgrounds, primary #1A327D / accent #F05A29, hover white text, border/radius, typography, spacing, destinations and Popup1801 remain owned by their existing definitions. No global CSS, JS, dependencies or component additions.

```css
/* CTA hover sweep */
& a { position: relative; isolation: isolate; }
& a::before { content: ""; position: absolute; inset: 0; border-radius: inherit; background-color: var(--color-primary); transform: scaleX(0); transform-origin: left center; transition: transform 280ms ease; z-index: -1; pointer-events: none; }
& a.button-outline-orange::before { background-color: var(--color-accent); }
& a:is(:hover, :focus-visible) { background-color: transparent; }
& a:is(:hover, :focus-visible)::before { transform: scaleX(1); }
@media (prefers-reduced-motion: reduce) { & a::before { transition: none; } }
```

Authenticated desktop default-style before/after comparison matched widths394.552px, heights52.5312px, padding16px24px, Montserrat60016px/19.2px,8px radius, colors/borders and hrefs. Browser-forced hover/focus states verified both original fill colors, white text, scale0→1→0,280ms duration and preserved focus outlines; emulated reduced-motion gives0s. Actual keyboard Tab focus and Enter popup open passed. Actual390px viewport verified both334.667px-wide/52.5312px-high buttons below the map, Popup open/close, and directory navigation; desktop directory navigation also reached /service-area/. Screenshot visually confirms text above fill. Emulation overrides cleared. Anonymous delivery, physical-device testing and final owner visual acceptance are not claimed; the earlier width-task768px check remains outstanding.


### Selected-city link underline — 2026-11-05

Owner-requested small visual correction on staging Service Areas495. Inspection found `text-decoration:underline` on the inline-flex selection anchor decorated both its text and separate arrow. Wrapped its existing first text node in `span[data-map-visit-text]`; moved the underline/4px offset to that span and restricted the existing orange rule to the aria-hidden arrow. Anchor now has no decoration. Existing firstChild text updates still work; map.js, URLs, selection handlers, colors, minimum target height and focus-visible outline are unchanged. All selectors remain scoped to `.gc-service-areas-map .gc-map-selection`.

Updated map.css/map-panel.html and rebuilt custom-code.html with compile.py. Deployed only existing staging Custom Code4134 meta; retained location, priority and conditions. Live pre-change code matched the repository after CRLF normalization; private full snippet backup retained outside Git. Shared1140 structure and production untouched. Existing map consumers receive this same narrowly scoped link correction.

Verification: authenticated Chrome at390px, emulated touch selected Lombard and preserved its existing href; inspected text underline/graphite color and undecorated orange aria-hidden arrow, visually observed single text underline, document width390 (no horizontal overflow). At1440px desktop, no overflow (scroll width1425); selection link remained hidden in mouse mode and Lombard map hover activated. Browser emulation restored. Existing focus-visible rule verified unchanged in source; attempted keyboard focus on the touch-only footer did not remain visible, so no successful keyboard-focus interaction or physical-device test is claimed. No navigation or broad consumer regression claimed. Rollback: restore this change's parent versions of the three map source/artifact files and redeploy prior Custom Code4134, or restore the private snippet code backup; no component rollback required.
