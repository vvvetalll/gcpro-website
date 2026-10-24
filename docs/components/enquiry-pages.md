# Request Service and Contact Us — current task log

Date: 24 October 2026, America/Chicago. Staging only.

## Authorized scope and current state

Use the documented existing **GCPRO — Shared Hero1318** as the first page-content component on Request Service492 and Contact Us496. Keep content and native Atomic forms below it. The owner's latest instruction supersedes the experimental combined Hero/form layout. Preserve navigation Header113, Footer114, other pages, component definitions, URLs, publication states and SEO. Separately authorized follow-ups: remove the unintended wrapper padding; place Contact Name/Email in one desktop row.

Both pages are saved and Published on staging. Git delivery is the commit containing this record; remote verification is reported in the completion message. No new component definition, class, Variable, asset, custom code or plugin was created in this correction.

| Page | First shared header | Separate native form | Current editing location |
|---|---|---|---|
| [Request Service492](https://vitaliiv1.sg-host.com/service-request/) | instance6e88b6c4 →1318 |520dd1a8 | Page492 → Shared Page Header → content Overrides; form remains in the following page-content section |
| [Contact Us496](https://vitaliiv1.sg-host.com/contact-us/) | existing30d7e688 →1318 |22adac6 | Page496 → GCPRO Shared Contact Hero → content Overrides; form remains below it |

Edit the shared visual definition at Component1318 only under authorization for all consumers. Do not detach/copy its descendants. Use h1/description/call_text/call_link/request_text/request_link and other currently supported content/media Overrides. The page header is separate from global navigation Header113.

## Completed steps and actual changes

1. Read current instructions and the shared-Hero record; inspected the existing1318 settings and current target pages. Owner clarified that the known service-page component1318 is required; no alternative component was inserted during this correction.
2. Captured scoped private snapshots outside Git. Request received one1318 instance first. Its previous H1 and introduction now live in supported Overrides; the superseded page-owned introduction subtree was removed after transferring that content. Native Request form subtree is exactly equal to the pre-correction form.
3. Contact already had1318 first; retained that instance and its Overrides. No shared definition was edited. Restored the existing light-blue Request content surface and readable navy body heading/text after the navy experiment was superseded.
4. Elementor's generated outer wrappers had default10px padding, creating an unintended white frame. Set only wrappers7902342b /6071e484 to native padding0/margin0. Did not change padding inside1318.
5. On separate owner instruction, Contact's native form now uses two equal desktop columns with16px gap: Name | Email; Phone, Message, optional SMS, submit and native messages span the form. Mobile ≤767px is one column. Field names, requiredness, values, content, actions and messages are unchanged. Nothing outside that form changed in this layout step.
6. Recorded the mandatory shared-header, no-experiments/Allow approval, visible-progress and GitHub task-log rules in AGENTS.md. Routine authorized work needs no repeated approval; no deviation/experiment was proposed or implemented in this correction.

## Checks and results

- Fresh saved-data checks: exactly one1318 per page, first visible content component; no separate page-owned H1; forms occur after the header. Native wrappers are structural containers, not additional page-header designs. An initial validator incorrectly expected the component itself at document root; its read-only check was corrected for Elementor's generated wrapper, without another header implementation.
- Page identity/publication and authored SEO preserved. Header113/Footer114 metadata compare equal to scoped pre-change snapshots. No service page, shared visual definition or centralized controller was written.
- Actual Chrome1440px desktop and393px mobile: one rendered H1 on each page, header before the form, wrapper padding0, no horizontal document overflow. Request body headings render navy on light blue.
- Contact desktop: Name/Email have equal approximately305px widths in one row; Phone/Message approximately625px full width. Mobile: all fields248px in one column. Keyboard Tab from Name reaches Email. No extra submissions were needed for a layout-only change.
- [Request screenshot](../evidence/2026-10-24-page-headers/request-final.jpg) and [Contact form row screenshot](../evidence/2026-10-24-page-headers/contact-form-grid.jpg). These are actual viewport captures; the private WordPress toolbar is cropped out. Final visual acceptance remains with the owner.

## Preserved form implementation and unresolved work

The forms were built in earlier, then-uncommitted staging work after analysis commitf85de90. That analysis commit did not contain finished pages. This record reconciles their current state; it does not claim a new implementation or delivery test during this header correction.

Request requires Name, Phone, City/ZIP; Service defaults Not sure, Email/description optional. Contact requires Name, Email, Message; Phone optional. Both use native Collect submissions only, with honest staging status text. Prior clearly labeled tests created native records1–4, including SMS checked=yes and unchecked=empty; that is internal storage receipt, **not inbox delivery**. The existing production SMS disclosure was retained, unchecked and optional; its source linked Privacy Policy but no Terms. No RingCentral compliance certification or SMS integration is claimed.

**Open:** verified monitored notification recipients/email delivery, supported native spam protection, operational follow-up procedure and any RingCentral-specific recording/Terms requirements. These pages must not be described as fully operational enquiry delivery. No new external notification destination, email configuration or plugin was introduced. Existing native office map/contact links remain; unrelated placeholders and duplicated supporting contact actions were not removed under this task.

Private recovery snapshots and tool results: work/page-header-correction/. Raw admin data, credentials and backups are excluded from Git. Recovery must be scoped to the affected page nodes and preserve later owner work; reverting this documentation does not revert WordPress.
