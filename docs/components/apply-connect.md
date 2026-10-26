# Apply and QR Connect — 2026-10-26

Staging only. Existing Apply486 `/apply/` completed; existing QR landing2040 `/connect/` published after source and destination checks. Careers534 now offers native named Content→Apply486 actions. Production, URLs, Header113/Footer114, shared definitions and noindex remain unchanged.

## Source and form

Read-only source: `https://gcprochicago.com/apply/`, Gravity Forms6. Actual HTML inspected; its separate footer Contact form1 is not the application. Private form6 API returns401, so original notification recipient/private success configuration could not be inspected. Owner supplied a temporary recipient separately; it is configured privately in Elementor and intentionally omitted from Git.

| Field | Requirement and choices |
| --- | --- |
| First / last name | Both required |
| Email / phone | Both required; native email and telephone controls |
| Age18+ / legally eligible to work in US | Optional Yes/No |
| Positions | Optional multi-selection: Emergency Response Technician; Contents & Moving Specialist; Lead Technician; Client Services Specialist; Project Manager; General Labor / Flexible |
| Availability | Optional Full-time; Part-time; Flexible; Weekends / On-call |
| Start | Optional ASAP;1–2 weeks;2+ weeks;Not sure yet |
| Experience | Optional No experience; Construction; Restoration; Moving / Labor; Customer Service; Other |
| Additional information | Optional multiline text |

No upload or application consent field exists in source form6; none invented. The footer SMS consent was not copied. Native Atomic Select preserves single-choice behavior where the Atomic radio widget is unavailable; optional choices have a neutral Not specified state rather than preselecting eligibility. Original telephone mask is not recreated with custom code. Native Submit Application replaces the unverified speed claim in the original label.

## Configuration owners

- Apply486: root1c1edda6; Shared Hero1318 instance32a328ed first, with named Content→Careers534 secondary action. Section13e3c215, readable content2823806a; actual Section Heading71 instance6d8ce567 inside existing accent wrapper.
- Native Atomic form6df8c42a owns all fields and messages. Edit its Actions after submit→Collect Submissions + Email to change delivery. Email subject `GCPRO staging | Job application`, native `[all-fields]`, plain text; existing native sender defaults. No Email2, applicant autoresponder, CC/BCC or webhook configured. Temporary recipient needs the owner's eventual replacement.
- Existing `form-field`, `form-label`, `form-input`, `form-note`, `button-primary`, `section`/`section--light` and existing Variables reused. Field groups are two columns, one on mobile; fields naturally sized, body max800px, gutters32px/20px. Native local controls own page-specific grouping; no custom CSS/JS/PHP, extra classes, components, plugin or dependency.
- Optional controls use stable machine names and checkbox value Selected, with separate visible labels. These replace escaped human-readable names after the delivery test revealed a numeric age label and entity-encoded checkbox values. Final names/values were read back and rendered; a second email was intentionally not sent.
- Careers534: existing Hero717873b3 and action14ec7bf2 now bind by native Internal URL→Content to Apply486, label Apply. Related40c9434c/39473c66 application instructions updated. Other content/actions unchanged.

## QR Connect

Production `https://gcprochicago.com/connect/` explicitly thanks visitors for scanning its QR code. Existing2040 keeps exact `/connect/` path. Shared Hero1318 first; Section Heading71 and existing Solid Orange53/Blue Outline59 actions. Edit page content/Overrides, not shared definitions. Contact section92f2db1 uses same readable width/gutters as Apply.

Save Contact preserves normalized original `https://gcprochicago.com/wp-content/uploads/gcpro/GCPRO.vcf`: HTTP200, `text/x-vcard`,314 bytes, valid BEGIN/END VCARD markers. Phone is verified `tel:+18476563322`; office220 Eisenhower Lane North, Lombard IL60148. Send a Message uses native named Content→Contact Us496, avoiding a duplicate form; Directions uses the existing office Maps destination. No phone call or contact import performed. Production resource is linked, not copied or modified. No navigation/QR artwork changes.

## Heading color correction

Owner requests graphite headings in text sections regardless of H2/H3 level. Existing global default already uses color-text; Privacy3 had six local navy overrides. Native controls now bind these six to existing color-text #334155, matching its H2. Semantics, typography, legal copy and geometry unchanged. New Apply/Connect body headings follow this rule; white Hero/dark-surface headings preserved. No site-wide card/navigation palette change or full-site audit.

## Verification

- Actual desktop and393px mobile browser simulation: one H1 on Apply/Connect; form grouping stacks, labels remain associated,20px mobile gutters and353px controls, no horizontal overflow. Desktop screenshots inspected; physical mobile/screen-reader testing not performed.
- Empty submit focuses first required field; malformed email focuses email and reports native typeMismatch. First-name Tab advances to last-name. Native multi-select checkboxes and dropdowns operated successfully.
- Exactly one owner-authorized, clearly labeled non-applicant test submitted through staging. Success message appeared; actual Gmail inbox receipt with unique test marker and submitted field values confirmed. No automatic applicant email. The subsequent field-name cleanup was saved/read back without sending a second application.
- Error-message copy exists natively; transport failure was not deliberately injected. Upload/attachment tests not applicable. Original production private notification/success behavior remains unavailable; no production submission performed.
- Native saved trees read back: zero custom_css on affected pages; Published status and original slugs retained; noindex,nofollow remains. Privacy H2 and all six H3 compute rgb(51,65,85); Apply/Connect body headings match.
- Remaining: owner visual acceptance, eventual replacement of temporary application recipient, final email-label formatting after native machine-name cleanup not re-sent. No blocker to using the staging application.

## Recovery

Private pre-edit snapshots for486/534/496/2040 remain outside Git. Restore only affected page bodies/Overrides/settings if needed, preserving subsequent owner edits; Contact496 was not changed. Revert Privacy six local colors to color-primary only if owner explicitly changes the typography decision.
