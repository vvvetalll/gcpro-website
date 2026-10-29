# Service availability popup — 2026-10-23

## Current delivery and coverage gap

Native Elementor Pro Popup **1801 — GCPRO — Check Service Availability**, opened by the existing button in shared Service Areas Component1140 / instance4e418401 / Outline Orange100. Trigger appearance, URLs and page content are preserved. The trigger action alone changes from Request492 to native Popup Open1801. Popup has no automatic triggers. [Edit popup](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1801&action=elementor).

**Owner-provided provisional scope (2026-10-23):** Chicago and surrounding Chicagoland communities. Cook, DuPage, Lake (Illinois), Will, Kane and McHenry counties are candidate boundaries pending review, not confirmation for every address. Northwest Indiana and Wisconsin remain unconfirmed. Owner confirms that no neighborhood or ZIP exclusion list has yet been approved. No demographic inference, blanket South/West Side exclusion, radius or city-page inventory is used.

Exact city/ZIP/address confirmation remains disabled. All valid input now displays the owner's exact neutral message: “GCPRO serves Chicago and surrounding Chicagoland communities. Call us to confirm service at your address.” with verified `tel:+18476563322`. The single editable review table distinguishes `confirmed`, `proposed`, `requires_call`, future `excluded` and `partial` statuses. Its13 city rows are review candidates/call-required entries, not automatic confirmations; six Illinois counties are proposed; two neighboring regions require a call. No ZIP or exclusion has been invented. Request492 remains empty and is omitted.

## Native owner and authorized exception

Elementor owns modal creation/loading, overlay, close button and Escape. Native Atomic Panel31e30fea owns responsive32px/24px padding, white surface,8px radius and Inter body typography. H2 340918b7 and paragraph362b1f70 remain native. Native Form51db3f70 → Row45e6d7a9 → Field397d339a → Label23516055/Input468d958, alongside Submit2e121b1a. Native Call Now60ce072e uses existing button-primary. Desktop/tablet row:12px gap, bottom aligned, input flex-grow1/basis0/min-width0, button natural width/no shrink, both48px high. Native mobile breakpoint stacks full-width input/button. No custom field/button layout CSS remains.

One HTML widget7a5e1801 now contains only live validation/result slots, notice, JSON registry and the authorized local script/result-slot CSS. Owner explicitly allowed custom code inside the native popup after the native geographic-matching limitation was reported. No plugin, PHP, framework, global Custom Code entry or external API. Existing Elementor jQuery popup events are reused, with a staging-host guard.

Native Form actions-after-submit and submission metadata are explicitly empty; the custom handler intercepts submit in document capture phase with preventDefault/stopImmediatePropagation, so native sending does not run. Validation, matching and result updates remain local; there is no lookup endpoint, storage or analytics call. Native inputs retain label/id association; custom handler supplies max length, aria-describedby, inline role=alert validation and role=status result announcements. It handles Enter, keeps modal open, resets on reopen, supplements Tab containment and returns focus after native close.

## Single editing location

Live authority: **Popup1801 → Local Coverage Form and Single Coverage Registry → HTML → application/json block**. Repository `integrations/service-coverage.json` is its source mirror, not another active list. JS/CSS mirrors: `integrations/service-availability.js` and `.css`, compiled into that same widget rather than separately enqueued. Edit/sync the registry in one place, publish native popup and check the new render. Do not duplicate lists/logic in triggers.

Registry schema: `approved` gates exact positive matching; `provisionalMessage` contains the owner's current wording; `locations` is the single review table. Each record has `kind` (city/zip/county/region/area), `location`, `status`, `verified`; optional `city`, `aliases`, `state` and `ambiguous`. Only approved, verified exact city/ZIP entries can confirm coverage. Verified exact exclusions take precedence; proposed/unverified/ambiguous entries remain uncertain. A city with subarea exclusions cannot get blanket confirmation. Partial cities request ZIP only if reviewed ZIP entries can actually resolve coverage. County/region boundaries never imply ZIP/address coverage. Do not add operational exclusion reasons to public JSON; keep any future reasons in internal records with neutral public wording.

## Actual verification

Water514 native trigger opens popup; shared1140 action is not a per-page copy. Actual browser: empty input,1234,123456 and markup rejected inline; mixed-case/whitespace city, five-digit ZIP and unknown city return the owner's provisional message with Call Now. Enter and button submission keep popup open and page unchanged. Close/reopen resets input/results; Escape closes; explicit focus return to trigger passes; Tab from final Call Now wraps to accessible close control. At394CSSpx input/button stack at full width,48px high with12px gap and no horizontal overflow. Desktop input/button share the same top/bottom at48px height with measured12px gap. Native dialog wrapper gets role=dialog and accessible name. Telephone href checked without placing call. No lead transmission test is needed because there is no submission endpoint.

Initial submit regression: binding to a popup's temporary DOM did not survive Elementor's cached/cloned content. Fixed with one guarded delegated submit listener; native cache regenerated after writes. Native popup did not reliably restore trigger focus, so a popup-hide listener returns it on the next animation frame. Checks above are after fixes. Physical devices, guest delivery and all-page matrices not claimed. Nine synthetic matcher fixtures check exact confirmed/excluded, partial, ambiguous ZIP, subarea exclusion precedence and disabled-gate behavior. Fixtures are not real coverage data and are not deployed. Real covered/excluded/partial/verified-ZIP outcomes await reviewed data; none are claimed as live verified results.

## Recovery and preservation

Private pre-change1140 MCP snapshot and popup shell/page492 snapshots remain outside Git. Restore only1140's availability link to its prior native Request492 value and unpublish Popup1801 to remove the feature. Preserve subsequent owner content. No Service Request body, SEO, page URLs, Hero, other sections, media or production changes. Popup1801 is the only new document; no popup component duplication.


## Popup finish and viewport behavior — 2026-10-23

Native Popup settings now own16px outer radius, restrained shadow, fadeIn/fadeOut300ms,24px margins,560px desktop width and86vw mobile width. Actual394px mobile render has about28px side gutters. Native `prevent_scroll=yes` is the real Disable Page Scrolling control; the earlier guessed `disable_page_scrolling` key was ineffective and is removed. Native close placement/colors are retained. Minimal popup-document Custom CSS provides the44px circular close target with20px SVG, hover/focus treatment and reduced-motion guard; native close controls cannot independently size the glyph and hit area. Source mirror: integrations/service-availability-popup-polish.css, not another enqueue.

The native a11y-navigation focus owner is disabled to avoid competing restoration; existing local handler retains dialog ARIA, Tab containment, Escape via Elementor and focus return. Native hide/unlock work still caused a measured page-position shift, so the handler preserves the trigger-time viewport and restores it immediately and after the300ms native close lifecycle (340ms completion check), using instant scrolling and preventScroll focus. No new scroll library or document-wide persistent style. Actual mobile open/close: scroll10698.667 before and after; focus returned to trigger.

Opening/reopening focuses the dialog container, **never the text input**, so it does not request the mobile software keyboard. Input receives focus only on user interaction or correction of an explicitly submitted invalid value. Actual browser reports active DIV, not INPUT. Physical phone keyboard behavior was not device-tested. Coverage, destinations, local validation, form layout and unrelated sections unchanged. Private pre-polish snapshot remains outside Git. Rollback only this popup's settings and focus-handler changes; preserve current coverage records. Owner final visual approval remains pending.


## Compact result and header overlay — 2026-10-23

Owner requested shorter text: native intro is now “Enter your city or ZIP code.”; provisional response “GCPRO serves Chicagoland. Call to confirm your address.”; note “Geographic coverage only.” Native panel gap reduced to16px. No automatic ZIP confirmation or new coverage decision.

Popup-document CSS now raises only #elementor-popup-modal-1801 above the existing smart Header's10000 stacking layer. The modal/backdrop covers navigation too. Card/message maximum height is calc(100dvh -48px); excess content scrolls inside the message region, preserving the native margin and16px radius. No Header/903/other popup CSS changed. Existing popup-polish source mirror updated, not separately enqueued.

Actual394x640 browser render afterZIP entry: card left27.57px, top81.53px, bottom558.47px, height476.94px; no horizontal overflow. Computed popup z-index2147483647; elementFromPoint in the Header area resolves to Popup1801's overlay. Owner remains final visual reviewer.


### Quiet result and label refinement

Owner removed the repeated visible input label: native Label23516055 now has display:none while its for/id association remains; the actual browser still resolves the textbox by its accessible name City or ZIP code. Result text is14px/400 muted #5B6575 on existing pale surface #EFF6FF,8px radius,12×16px padding, applied only when nonempty through existing popup-scoped CSS. Native label layout and existing matching/validation unchanged. Rendered styles and named input/Enter checked.


## Coverage proposal for owner review — 2026-10-29

**Execution order: list first. No coverage decisions deployed.** The one editable proposal register is still [`integrations/service-coverage.json`](../../integrations/service-coverage.json), enriched in place. The tables below are its read-only review rendering, not a second list to maintain. No CSV/database/plugin list was activated. The live Popup1801 JSON and matcher remain unchanged, `approved:false`,21 provisional records and zero ZIP records. No coverage-named plugin was found in the installed-plugin list; the currently recorded implementation is popup-local. No geo-page, status, route or eligibility was changed.

### Recommendation and approval boundary

- **Proposed served, subject to owner approval:60201 and60202 (Evanston, IL).** These are the only ordinary ZIP candidates in this selected set with a single-place/no-outside-place land relationship in the2020 mapping; city sources corroborate the city/ZIP association. They are candidates for whole-ZIP approval, not a claim that GCPRO already serves every property. Current USPS delivery-boundary verification is still unavailable. Evanston remains a Draft geo object; the recommendation does not authorize publishing it or adding a geo link.
- **Proposed requires_call:113 remaining ZIPs**, all14 city-name records and six candidate counties. A postal/ZCTA boundary crossing several cities, outside-place areas, or an unapproved Chicago subarea needs address confirmation. Two ZCTAs overlap Kendall County, outside the six candidate counties; neither is rejected automatically.
- **Explicitly approved exclusions: none.** Zero `not_served` proposals. Unknown input is `unresolved`, never an implied rejection. Northwest Indiana and Wisconsin remain unresolved regions, with a call path. Southern places intersecting Chicago data stay call-required: being outside the current SEO expansion task is not a business exclusion.
- **Unresolved decisions:** approve/amend whole-ZIP scope for60201/60202; review the primary ZIPs for the ten priority municipalities below including all mapped neighboring/unincorporated parts; define any Chicago subarea scope; confirm neighboring-state extent; obtain current USPS ZIP delivery/type/alias data before any positive matcher rollout. No blanket city approval is requested from SEO page existence or a past case. No exclusion reasoning, demographics or reputation is used.

The ten priority cities retain operational review priority. The two Evanston proposals reflect lower mapping ambiguity, not an SEO priority change.60208 also maps entirely to Evanston, but Northwestern documents it for non-residential university addresses; keep requires_call. Do not treat it as an ordinary residential ZIP.

### Sources, dates and interpretation

- **P20:** [Census2020 ZCTA/place relationship file](https://www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/tab20_zcta520_place20_natl.txt), [record explanation](https://www2.census.gov/geo/pdfs/maps-data/data/rel2020/zcta520/explanation_tab20_zcta520_place20_natl.pdf).
- **C20:** [Census2020 ZCTA/county relationship file](https://www2.census.gov/geo/docs/maps-data/data/rel2020/zcta520/tab20_zcta520_county20_natl.txt). Both datasets were downloaded and parsed2026-10-29; hashes are recorded in the existing JSON.
- [Census ZCTA limitations](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/zctas.html): generalized2020 geography; not all postal ZIPs exist as ZCTAs, and this is not a2026 USPS delivery boundary. [USPS versus municipal cities](https://www.census.gov/programs-surveys/geography/guidance/geo-areas/usps_census_city.html).
- [Evanston city reference to60201/60202](https://cityofevanston.org/departments/prcs/lakefront_beaches/boat_launches.php), checked2026-10-29; [Northwestern60208 restriction](https://www.northwestern.edu/living/services/mail/mail-faq.html), checked2026-10-29. These sources support geographic/postal interpretation only.

Selection is reproducible: preserve the existing13 city candidates and add Carol Stream from the accepted ten-city plan; include every five-character ZCTA having positive land intersection with one of these14 Illinois places. Preserve every positive overlap, including tiny slivers; no invented ZIP ranges, radius or one-city-per-ZIP assumption. Empty PLACE means land outside2020 incorporated/CDP places, not necessarily empty land. Land shares are not shares of addresses, customers or population. County crossing and outside-envelope flags are geographic warnings, not operational exclusions. The file includes all115 discovered ZCTAs, including56 Chicago-majority ones; it is not an exhaustive2026 USPS Chicago/Chicagoland postal inventory.

**Existing operational approval per row: none for a whole ZIP/city.** Only the owner's2026-10-23 provisional Chicago/Chicagoland statement and six candidate Illinois counties exist. Registry legacy `status` and `verified:false` remain conservative; use the separate `recommended_status` and `operational_approval` columns. `approved:false` is preserved. Current live21-record JSON equals the repository pre-proposal snapshot; do not paste this proposal into the popup.

Private operational notes must stay outside public GitHub. No such notes are included. The future WP administration can own a private-notes field; public HTML/JS, responses and sanitized exports must omit it. This proposal has no runtime settings or private-note implementation.

### City review summary

Primary geographic ZIPs below mean >50% of the2020 ZCTA land overlaps that city. This is a display aid, not a postal-city alias or eligibility rule. All city-name recommendations remain requires_call until whole-city/address exceptions are approved.

|City / IL|Primary geographic ZIPs (text)|Review priority|Existing geo object (separate from eligibility)|
|---|---|---|---|
|Chicago|60601, 60602, 60603, 60604, 60605, 60606, 60607, 60608, 60609, 60610, 60611, 60612, 60613, 60614, 60615, 60616, 60617, 60618, 60619, 60620, 60621, 60622, 60623, 60624, 60625, 60626, 60628, 60629, 60630, 60631, 60632, 60633, 60634, 60636, 60637, 60638, 60639, 60640, 60641, 60642, 60643, 60644, 60645, 60646, 60647, 60649, 60651, 60652, 60653, 60654, 60655, 60656, 60657, 60659, 60660, 60661|Preserved provisional city candidate|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|Lombard|60148|Current ten-city priority|[Lombard #526](https://vitaliiv1.sg-host.com/service-area/lombard/)|
|Arlington Heights|60004, 60005|Preserved provisional city candidate|Arlington Heights #559 Draft|
|Elmhurst|60126|Current ten-city priority|[Elmhurst #530](https://vitaliiv1.sg-host.com/service-area/elmhurst/)|
|Naperville|60540, 60563, 60564, 60565|Current ten-city priority|[Naperville #532](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|Northbrook|60062|Current ten-city priority|[Northbrook #556](https://vitaliiv1.sg-host.com/service-area/northbrook/)|
|Downers Grove|60515, 60516|Current ten-city priority|[Downers Grove #527](https://vitaliiv1.sg-host.com/service-area/downers-grove/)|
|Oak Brook|60523|Current ten-city priority|[Oak Brook #536](https://vitaliiv1.sg-host.com/service-area/oak-brook/)|
|Glenview|60025, 60026|Current ten-city priority|[Glenview #533](https://vitaliiv1.sg-host.com/service-area/glenview/)|
|Highland Park|60035|Current ten-city priority|[Highland Park #528](https://vitaliiv1.sg-host.com/service-area/highland-park/)|
|Schaumburg|60173, 60193, 60194, 60195|Current ten-city priority|[Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|Evanston|60201, 60202, 60208|Preserved provisional city candidate|Evanston #565 Draft|
|Elk Grove Village|60007|Preserved provisional city candidate|Elk Grove Village #529 Draft|
|Carol Stream|60188|Current ten-city priority|[Carol Stream #543](https://vitaliiv1.sg-host.com/service-area/carol-stream/)|

### All ZIP rows — generated review view of the existing register

All values in ZIP columns are five-character strings. State IL for this set. Associated city names are2020 geographic overlaps, not a list of USPS-approved mailing names. Every row uses P20/C20, data vintage2020, checked2026-10-29, and has **no documented whole-ZIP operational approval**. Full source IDs, place/county GEOIDs and precise land shares are in the JSON.

Flags: **M** multiple places; **U** land outside incorporated/CDP places; **C** multiple counties; **B** outside the candidate six-county envelope; **CHI** Chicago subarea undecided; **I** institutional ZIP. Other associated municipalities outside the14-city review seed remain listed; their inclusion is not a proposed service expansion.

|ZIP (text)|Associated municipalities/CDPs|Recommended status|Boundary / type flags|Available geo object(s)|
|---|---|---|---|---|
|`60004`|Arlington Heights, Buffalo Grove (0.07% land), Palatine (0.05% land), Prospect Heights, Wheeling (0.66% land)|requires_call (proposal)|M, U|Arlington Heights #559 Draft; Buffalo Grove #551 Draft|
|`60005`|Arlington Heights, Mount Prospect, Rolling Meadows (0.56% land)|requires_call (proposal)|M, U|Arlington Heights #559 Draft|
|`60007`|Arlington Heights (0.00% land), Chicago (0.33% land), Des Plaines (0.37% land), Elk Grove Village, Rolling Meadows (0.06% land), Schaumburg|requires_call (proposal)|M, U, C, CHI|Arlington Heights #559 Draft; [Chicago #154](https://vitaliiv1.sg-host.com/); Des Plaines #572 Draft; Elk Grove Village #529 Draft; [Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|`60008`|Palatine (0.09% land), Rolling Meadows, Schaumburg|requires_call (proposal)|M, U|[Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|`60015`|Bannockburn, Buffalo Grove (0.20% land), Deerfield, Highland Park (0.01% land), Lincolnshire (0.54% land), Northbrook (0.15% land), Riverwoods|requires_call (proposal)|M, U, C|Buffalo Grove #551 Draft; Deerfield #563 Draft; [Highland Park #528](https://vitaliiv1.sg-host.com/service-area/highland-park/); [Northbrook #556](https://vitaliiv1.sg-host.com/service-area/northbrook/)|
|`60016`|Des Plaines, Glenview, Niles (0.03% land), Park Ridge (0.41% land)|requires_call (proposal)|M, U|Des Plaines #572 Draft; [Glenview #533](https://vitaliiv1.sg-host.com/service-area/glenview/); Niles #562 Draft|
|`60018`|Chicago, Des Plaines, Elk Grove Village (0.41% land), Rosemont, Schiller Park (0.89% land)|requires_call (proposal)|M, U, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/); Des Plaines #572 Draft; Elk Grove Village #529 Draft|
|`60022`|Glencoe, Northbrook (0.48% land)|requires_call (proposal)|M, U|Glencoe #547 Draft; [Northbrook #556](https://vitaliiv1.sg-host.com/service-area/northbrook/)|
|`60025`|Glenview, Morton Grove (0.29% land), Niles (0.02% land)|requires_call (proposal)|M, U|[Glenview #533](https://vitaliiv1.sg-host.com/service-area/glenview/); Niles #562 Draft|
|`60026`|Glenview|requires_call (proposal)|U|[Glenview #533](https://vitaliiv1.sg-host.com/service-area/glenview/)|
|`60035`|Highland Park, Highwood (0.07% land), Lake Forest|requires_call (proposal)|M, U|[Highland Park #528](https://vitaliiv1.sg-host.com/service-area/highland-park/); Lake Forest #553 Draft|
|`60040`|Highland Park, Highwood, Lake Forest (0.06% land)|requires_call (proposal)|M, U|[Highland Park #528](https://vitaliiv1.sg-host.com/service-area/highland-park/); Lake Forest #553 Draft|
|`60056`|Arlington Heights (0.04% land), Des Plaines (0.04% land), Mount Prospect, Prospect Heights (0.01% land)|requires_call (proposal)|M, U|Arlington Heights #559 Draft; Des Plaines #572 Draft|
|`60062`|Glencoe, Glenview, Northbrook, Northfield (0.07% land), Prospect Heights (0.99% land)|requires_call (proposal)|M, U|Glencoe #547 Draft; [Glenview #533](https://vitaliiv1.sg-host.com/service-area/glenview/); [Northbrook #556](https://vitaliiv1.sg-host.com/service-area/northbrook/)|
|`60067`|Hoffman Estates (0.59% land), Inverness, Palatine, Rolling Meadows, Schaumburg (0.32% land)|requires_call (proposal)|M, U|[Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|`60070`|Arlington Heights (0.62% land), Prospect Heights, Wheeling (0.20% land)|requires_call (proposal)|M|Arlington Heights #559 Draft|
|`60074`|Arlington Heights (0.24% land), Deer Park, Kildeer (0.45% land), Palatine, Rolling Meadows (0.05% land)|requires_call (proposal)|M, U, C|Arlington Heights #559 Draft|
|`60090`|Arlington Heights (0.41% land), Buffalo Grove (0.11% land), Prospect Heights (0.03% land), Wheeling|requires_call (proposal)|M, U, C|Arlington Heights #559 Draft; Buffalo Grove #551 Draft|
|`60093`|Glencoe, Glenview (0.79% land), Northfield, Wilmette (0.83% land), Winnetka|requires_call (proposal)|M, U|Glencoe #547 Draft; [Glenview #533](https://vitaliiv1.sg-host.com/service-area/glenview/); Wilmette #555 Draft; Winnetka #566 Draft|
|`60103`|Bartlett, Carol Stream (0.05% land), Hanover Park (0.02% land), Streamwood|requires_call (proposal)|M, U, C|Bartlett #561 Draft; [Carol Stream #543](https://vitaliiv1.sg-host.com/service-area/carol-stream/)|
|`60106`|Addison (0.11% land), Bensenville, Chicago, Wood Dale|requires_call (proposal)|M, U, CHI|Addison #538 Draft; Bensenville #577 Draft; [Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60108`|Addison (0.01% land), Bloomingdale, Carol Stream, Glendale Heights|requires_call (proposal)|M, U|Addison #538 Draft; [Carol Stream #543](https://vitaliiv1.sg-host.com/service-area/carol-stream/)|
|`60126`|Addison (0.03% land), Elmhurst, Hillside (0.00% land), Oak Brook (0.03% land), Oakbrook Terrace (0.07% land), Villa Park (0.84% land)|requires_call (proposal)|M, U, C|Addison #538 Draft; [Elmhurst #530](https://vitaliiv1.sg-host.com/service-area/elmhurst/); [Oak Brook #536](https://vitaliiv1.sg-host.com/service-area/oak-brook/); Villa Park #546 Draft|
|`60131`|Bensenville, Chicago (0.73% land), Franklin Park, Melrose Park (0.00% land), Northlake (0.13% land)|requires_call (proposal)|M, U, CHI|Bensenville #577 Draft; [Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60133`|Bartlett (0.13% land), Bloomingdale (0.04% land), Carol Stream (0.01% land), Hanover Park, Roselle, Schaumburg (0.12% land), Streamwood (0.02% land)|requires_call (proposal)|M, U, C|Bartlett #561 Draft; [Carol Stream #543](https://vitaliiv1.sg-host.com/service-area/carol-stream/); [Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|`60137`|Downers Grove (0.03% land), Glendale Heights (0.11% land), Glen Ellyn, Lombard, Wheaton (0.53% land)|requires_call (proposal)|M, U|[Downers Grove #527](https://vitaliiv1.sg-host.com/service-area/downers-grove/); Glen Ellyn #542 Draft; [Lombard #526](https://vitaliiv1.sg-host.com/service-area/lombard/)|
|`60139`|Bloomingdale (0.20% land), Carol Stream (0.01% land), Glendale Heights|requires_call (proposal)|M, U|[Carol Stream #543](https://vitaliiv1.sg-host.com/service-area/carol-stream/)|
|`60148`|Addison (0.40% land), Downers Grove (0.07% land), Glendale Heights (0.20% land), Glen Ellyn (0.18% land), Lombard, Oak Brook (0.01% land), Oakbrook Terrace (0.01% land), Villa Park (0.06% land)|requires_call (proposal)|M, U|Addison #538 Draft; [Downers Grove #527](https://vitaliiv1.sg-host.com/service-area/downers-grove/); Glen Ellyn #542 Draft; [Lombard #526](https://vitaliiv1.sg-host.com/service-area/lombard/); [Oak Brook #536](https://vitaliiv1.sg-host.com/service-area/oak-brook/); Villa Park #546 Draft|
|`60169`|Hoffman Estates, Schaumburg (0.49% land)|requires_call (proposal)|M, U|[Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|`60172`|Bloomingdale, Elk Grove Village (0.14% land), Hanover Park (0.05% land), Itasca (0.09% land), Roselle, Schaumburg|requires_call (proposal)|M, U, C|Elk Grove Village #529 Draft; [Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|`60173`|Hoffman Estates (0.02% land), Palatine (0.03% land), Rolling Meadows (0.39% land), Schaumburg|requires_call (proposal)|M, U|[Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|`60176`|Chicago (0.95% land), Schiller Park|requires_call (proposal)|M, U, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60181`|Addison (0.10% land), Oak Brook (0.32% land), Oakbrook Terrace, Villa Park|requires_call (proposal)|M, U|Addison #538 Draft; [Oak Brook #536](https://vitaliiv1.sg-host.com/service-area/oak-brook/); Villa Park #546 Draft|
|`60185`|Bartlett (0.08% land), Batavia (0.15% land), Carol Stream (0.16% land), Geneva (0.24% land), St. Charles (0.89% land), Warrenville (0.13% land), West Chicago, Winfield (0.41% land)|requires_call (proposal)|M, U, C|Bartlett #561 Draft; Batavia #554 Draft; [Carol Stream #543](https://vitaliiv1.sg-host.com/service-area/carol-stream/)|
|`60188`|Carol Stream, Glendale Heights (0.11% land), Wheaton (0.11% land), Winfield (0.35% land)|requires_call (proposal)|M, U|[Carol Stream #543](https://vitaliiv1.sg-host.com/service-area/carol-stream/)|
|`60193`|Roselle (0.04% land), Schaumburg|requires_call (proposal)|M, U|[Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|`60194`|Hoffman Estates (0.19% land), Schaumburg|requires_call (proposal)|M|[Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|`60195`|Hoffman Estates (0.89% land), Schaumburg|requires_call (proposal)|M, U|[Schaumburg #558](https://vitaliiv1.sg-host.com/service-area/schaumburg/)|
|`60201`|Evanston|served (proposal)|No mapped boundary overlap; operational approval pending|Evanston #565 Draft|
|`60202`|Evanston|served (proposal)|No mapped boundary overlap; operational approval pending|Evanston #565 Draft|
|`60208`|Evanston|requires_call (proposal)|I|Evanston #565 Draft|
|`60440`|Bolingbrook, Naperville, Woodridge (0.48% land)|requires_call (proposal)|M, U, C|[Bolingbrook #557](https://vitaliiv1.sg-host.com/service-area/bolingbrook/); [Naperville #532](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|`60504`|Aurora, Naperville (0.42% land)|requires_call (proposal)|M, U, C, B|Aurora #537 Draft; [Naperville #532](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|`60515`|Downers Grove, Lisle (0.08% land), Westmont (0.02% land)|requires_call (proposal)|M, U|[Downers Grove #527](https://vitaliiv1.sg-host.com/service-area/downers-grove/)|
|`60516`|Darien (0.68% land), Downers Grove, Westmont, Woodridge (0.41% land)|requires_call (proposal)|M, U|[Downers Grove #527](https://vitaliiv1.sg-host.com/service-area/downers-grove/)|
|`60517`|Bolingbrook (0.37% land), Darien (0.63% land), Downers Grove (0.08% land), Lisle (0.57% land), Woodridge|requires_call (proposal)|M, U, C|[Bolingbrook #557](https://vitaliiv1.sg-host.com/service-area/bolingbrook/); [Downers Grove #527](https://vitaliiv1.sg-host.com/service-area/downers-grove/)|
|`60521`|Hinsdale, Oak Brook (0.10% land), Westmont (0.13% land)|requires_call (proposal)|M, U, C|Hinsdale #540 Draft; [Oak Brook #536](https://vitaliiv1.sg-host.com/service-area/oak-brook/)|
|`60523`|Downers Grove (0.03% land), Elmhurst (0.27% land), Lombard (0.05% land), Oak Brook, Oakbrook Terrace (0.87% land), Westmont|requires_call (proposal)|M, U, C|[Downers Grove #527](https://vitaliiv1.sg-host.com/service-area/downers-grove/); [Elmhurst #530](https://vitaliiv1.sg-host.com/service-area/elmhurst/); [Lombard #526](https://vitaliiv1.sg-host.com/service-area/lombard/); [Oak Brook #536](https://vitaliiv1.sg-host.com/service-area/oak-brook/)|
|`60532`|Downers Grove (0.16% land), Lisle, Naperville (0.12% land), Woodridge (0.02% land)|requires_call (proposal)|M, U|[Downers Grove #527](https://vitaliiv1.sg-host.com/service-area/downers-grove/); [Naperville #532](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|`60540`|Lisle (0.15% land), Naperville, Woodridge (0.57% land)|requires_call (proposal)|M, U|[Naperville #532](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|`60555`|Aurora, Naperville (0.01% land), Warrenville|requires_call (proposal)|M, U|Aurora #537 Draft; [Naperville #532](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|`60561`|Darien, Downers Grove (0.00% land), Willowbrook (0.05% land), Woodridge (0.11% land)|requires_call (proposal)|M, U|[Downers Grove #527](https://vitaliiv1.sg-host.com/service-area/downers-grove/)|
|`60563`|Aurora, Lisle (0.08% land), Naperville, Warrenville, Wheaton (0.02% land)|requires_call (proposal)|M, U|Aurora #537 Draft; [Naperville #532](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|`60564`|Aurora, Naperville|requires_call (proposal)|M, U, C|Aurora #537 Draft; [Naperville #532](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|`60565`|Bolingbrook (0.05% land), Naperville, Woodridge|requires_call (proposal)|M, U, C|[Bolingbrook #557](https://vitaliiv1.sg-host.com/service-area/bolingbrook/); [Naperville #532](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|`60585`|Aurora (0.01% land), Bolingbrook, Naperville (0.02% land), Plainfield|requires_call (proposal)|M, U, C, B|Aurora #537 Draft; [Bolingbrook #557](https://vitaliiv1.sg-host.com/service-area/bolingbrook/); [Naperville #532](https://vitaliiv1.sg-host.com/service-area/naperville/)|
|`60601`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60602`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60603`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60604`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60605`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60606`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60607`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60608`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60609`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60610`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60611`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60612`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60613`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60614`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60615`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60616`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60617`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60618`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60619`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60620`|Chicago|requires_call (proposal)|U, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60621`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60622`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60623`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60624`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60625`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60626`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60628`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60629`|Bedford Park, Chicago|requires_call (proposal)|M, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60630`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60631`|Chicago|requires_call (proposal)|U, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60632`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60633`|Burnham, Chicago|requires_call (proposal)|M, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60634`|Chicago, Norridge (0.03% land), Schiller Park|requires_call (proposal)|M, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60636`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60637`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60638`|Bedford Park, Bridgeview (0.12% land), Burbank (0.05% land), Chicago, Forest View|requires_call (proposal)|M, U, CHI|[Bridgeview #531](https://vitaliiv1.sg-host.com/service-area/bridgeview/); [Burbank #564](https://vitaliiv1.sg-host.com/service-area/burbank/); [Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60639`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60640`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60641`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60642`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60643`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60644`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60645`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60646`|Chicago, Skokie (0.13% land)|requires_call (proposal)|M, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/); Skokie #541 Draft|
|`60647`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60649`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60651`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60652`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60653`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60654`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60655`|Chicago|requires_call (proposal)|U, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60656`|Chicago|requires_call (proposal)|U, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60657`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60659`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60660`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60661`|Chicago|requires_call (proposal)|CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60707`|Chicago, Elmwood Park|requires_call (proposal)|M, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60804`|Chicago, Cicero, Stickney|requires_call (proposal)|M, CHI|[Chicago #154](https://vitaliiv1.sg-host.com/)|
|`60827`|Blue Island, Calumet Park, Chicago, Dixmoor (0.77% land), Dolton, Riverdale|requires_call (proposal)|M, U, CHI|[Blue Island #569](https://vitaliiv1.sg-host.com/service-area/blue-island/); [Chicago #154](https://vitaliiv1.sg-host.com/)|

### Existing runtime and next implementation stage

Read-only staging inspection2026-10-29 confirmed native Popup1801 still has21 provisional rows, no ZIP rows, and approved=false. No WordPress write, positive/negative matching, search storage or external lookup was introduced. The proposal contains137 rows:14 cities,115 ZIPs,6 counties,2 regions. Recommendation totals for ZIPs:2 served proposals/113 requires_call/0 not_served/0 unresolved ZIP rows; unlisted input and unconfirmed neighboring regions remain unresolved.60 ZIPs have multiple place overlaps;17 cross counties.60504 and60585 overlap Kendall County; retain call-required, not rejected.

Reference review for phase2: https://github.com/vvvetalll/cm default branch is claude/chicago-mounting-zip-review-szeoup, inspected at52b4344a6f3071173cdb2c282b44d63db3b651a4. Reference clone is read-only; its geographic coverage, branding and contact values are not GCPRO authority. The next implementation step is a separate GCPRO adaptation, synthetic tests and disabled-by-default approvals. No approved operational list exists yet.

## Staging coverage bridge and owner-approved cities — 2026-10-29

GCPRO Service Coverage1.2.1 is active on staging. The single editable authority is WordPress option `gcpro_service_coverage_v1`, managed at `/wp-admin/admin.php?page=gcpro-service-coverage`. The owner explicitly approved all addresses within Chicago, Lombard, Arlington Heights, Elmhurst, Naperville, Northbrook, Downers Grove, Oak Brook, Glenview, Highland Park, Schaumburg, Evanston, Elk Grove Village and Carol Stream. These14 city rows are individually approved/served and the operational gate is enabled. Approval does not extend to115 ZIP records: these remain unapproved and return an uncertain call path. No exclusions are approved. County/region proposals are context, not matching rules.

The earlier proposal below is dated history. `integrations/service-coverage.json` is now a sanitized decision snapshot, not a second runtime list. `proposal-seed.json` bootstraps fresh installs only, with every approval off; it never overwrites an existing registry. Census2020 ZCTA/place intersections establish proposal provenance, not current USPS/address-level eligibility.

### Owners and editing

Native Popup1801, Atomic Form and shared1140 trigger remain in place. The plugin's documented render-content hook replaces only the existing HTML widget7a5e1801 output with one endpoint bridge; dormant saved fallback code is not executed. `popup.js` owns lookup, announcements, reset, request cancellation and supplemental focus/scroll restoration. `popup.css` owns dynamic results/actions only. Native Elementor owns heading, input, submit, panel geometry and close control. No second modal, copied CM coverage, external geocoding, analytics or entered-location storage. The public lookup allowlists output; private registry notes and audit references are admin-only.

The popup is restrained: white neutral Check Availability action; one bright orange conversion action; ordinary services text link; muted rounded result panel. Native button typography uses the site's Inter body variable,16px/600, uppercase. Heading22px desktop/20px mobile. Native560px desktop panel,86vw mobile with24px external margins,48px form controls,12px gap and mobile stacking. Opening focuses the dialog, not the input. Native overlay covers the Header. Existing call destination is `tel:+18476563322`; Request Service resolves Published object492. Draft geo destinations are suppressed.

Water514 had an instance override pointing availability to Request492. It now uses native Popup1801 action. All21 Published1140 consumers were checked on guest HTML: correct popup action, complete document, one new bridge, no old handler. Other Request Service links remain unchanged.

### Verification and recovery

Local PHP lint passed. Local and staging synthetic suites passed33/33: normalization, leading-zero/ZIP+4, ambiguous/partial/unapproved/exclusion precedence, invalid inputs, CSV validation/duplicates/formula guard, approval isolation and public/private separation. Actual14 city lookups return served; unapproved ZIP and unknown inputs remain uncertain. Anonymous management routes return401; missing approval confirmation400; stale edit409. Initial native import accepted129 unapproved rows. Actual CSV export retained129 rows,14 approved cities and115 five-character ZIP strings. Import/export round-trip edge cases were tested in memory, not by repeatedly importing the live approved register.

Desktop Enter made one lookup request, with no native form navigation. Inline validation, Escape, reopen/reset, focus containment and focus return checked.393px emulated mobile panel338.26px with27.53px left gutter, stacked controls and no overflow. Physical-device touch and assistive-technology testing remain unverified. Sanitized results: `docs/evidence/2026-10-29-coverage-verification.json`.

Full private template/settings backups and registry export are retained outside public Git. A discovered widget API incompatibility was fixed before reactivation; revision response fixed in1.2.1. Elementor page-settings updates in this connector replaced omitted fields despite merge wording: always send the complete saved settings snapshot. Full native popup settings were restored, then Clear Files & Data completed successfully and SG cache purged; responsive CSS verified. To roll back the bridge, disable it in the plugin settings or deactivate the plugin: native call-only fallback returns and the registry is retained. Restore native style/settings from the private backup if reverting appearance; do not delete registry data.
