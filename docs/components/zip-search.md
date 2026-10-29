# ZIP / service availability prototype

**Current2026-10-29:** Working native Popup1801 plus GCPRO Service Coverage1.2.1;14 owner-approved cities enabled,115 ZIPs unapproved. [Current configuration and checks](service-availability-popup.md#staging-coverage-bridge-and-owner-approved-cities--2026-10-29). All older prototype/inactive descriptions below are historical.

**2026-10-29:** [Current owner-review register and implementation](service-availability-popup.md#coverage-proposal-for-owner-review--2026-10-29). Earlier inactive homepage prototype descriptions below are historical.

**2026-10-23 — service availability popup:** Native Popup1801, shared1140 trigger; owner-authorized local form code. Submit stays open, accessible close/focus/reset and mobile checked. Owner supplied provisional Chicagoland scope; no ZIP/neighborhood exclusions are approved. Exact confirmation remains disabled; valid input shows the owner’s call-to-confirm message. Field/button layout is native Atomic,48px high,12px gap, inline desktop/tablet and stacked mobile. No invented coverage or Request492 form claim. [Editing, gap and recovery](service-availability-popup.md).


**Status: unfinished, not a working ZIP search.** Do not infer a backend from the visible button.

## Actual saved location and structure

Homepage154 → Service Areas7d8c17ad → container585624a1 → intro3dc285eb → directory wrapper **62862a3a** → **5350691e**, “Check Area — Inactive Prototype”, Atomic e-form-submit-button. Text: “Check Service Availability”. There is **no ZIP input, label or native form in the current Homepage subtree**, and the button has no saved interactions. Earlier prototype/form descriptions are historical.

## Styles, code and dependencies

Existing button-outline-orange g-563da68 plus local style e-57f07b94-b3f5; global button tokens/typography. Native Elementor Atomic form-submit widget; no custom CSS/JavaScript, Custom Code ID, shortcode, external API, lookup table or integration endpoint is deployed for this control.

## Behavior and limitations

The surrounding directory stacks responsively with Service Areas. Runtime inspection finds an enabled BUTTON with type=submit, no disabled/aria-disabled state and no surrounding form. It does not establish successful availability lookup; its Navigator word “Inactive” is not a functional disabled state.

This is a verified misleading affordance and a pending product decision. The audit did not enable it, fabricate results or silently change the approved visual design. Before activation define service-area data/ownership, accessible ZIP input/validation, no-results/error states, supported native form/popup behavior, backend and privacy requirements, then test mobile/keyboard/anonymous flows.

For safe reuse, copy the documented requirements, not the claim that this prototype is operational. Decide whether to disable/hide the affordance or implement the real flow in an explicitly scoped follow-up.

## Owner approval of all existing ZIPs — 2026-10-29

Supersedes the ZIP approval gate described above: after checking60026 and60148, the owner explicitly instructed enabling all ZIPs in the existing register. All115 existing ZIP rows are individually approved/served;14 city records are unchanged, total129 records. No new ZIPs, county rules, aliases or exclusions were added. Unknown/unlisted ZIPs still return unresolved, not rejection or blanket nationwide coverage.

The exact-ZIP decision is now approved for the entire record, so operational ambiguous/partial flags are off. Original geographic intersections, associations and boundary flags remain in the sanitized snapshot; private runtime notes retain the owner decision and boundary context. Census2020 provenance is not represented as current USPS verification. Multi-city ZIPs receive the generic served message instead of claiming a single municipality.

Readback verified all115 ZIP approvals and exact preservation of14 city rows. Actual lookup checks:60026,60148,60026-1234 and whitespace60148 return served; Glenview/Lombard still served;99999 and00123 remain unresolved. Only registry data changed, no plugin/popup code or layout changes. Browser verification was unavailable in this follow-up; actual server responses were verified. Sanitized evidence: `docs/evidence/2026-10-29-all-zips-approved.json`. The seed remains unapproved on a fresh installation and never replaces runtime records.
