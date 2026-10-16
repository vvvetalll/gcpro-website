# Homepage CTA hierarchy implementation — E10

Delivered on staging Homepage **154**, 2026-10-16 (America/Chicago). Owner explicitly authorized direct CTA implementation while a separate [vertical-layout audit](../audits/2026-10-16-homepage-vertical-layout.md) was in progress. That audit's measurements/screenshots are the pre-change baseline; no proposed spacing/layout change was implemented.

## Implementation Summary

Changed **only** the two Hero button instances and the Homepage instance of Final CTA Component 80. Published through Elementor's standard Publish control and verified the staging frontend after reload. Header 113 and Footer 114 were audited and remain byte-for-byte equal in normalized MCP before/after reads. Production, other sections, page destinations, component definitions and global styles were not modified.

| Area | Before | After / decision |
| --- | --- | --- |
| Header 113 | Request Service, existing navy button; `#` | Unchanged. Distinct non-emergency entry point; existing tablet/mobile hiding preserved. No need to make another button orange. |
| Hero `a62cdd3` | Orange Request Service `#`, then white-outline Call | Orange **CALL 847-656-3322** `tel:+18476563322`, then white-outline **REQUEST SERVICE** `#` |
| Residential / Commercial | Two linked audience cards, `#` | Unchanged category discovery paths, no added request buttons |
| Core Services | Six service-specific text links, `#` | Unchanged service discovery, no added conversion buttons |
| Emergency `6cde656f` | Orange Call, white-outline Request Service | Already matches strategy; unchanged |
| How We Work | No conversion button | Unchanged |
| Projects | Three project links, View All Projects and Before & After | All retained; browsing actions, no request/call duplication added |
| Why GCPRO + Testimonials | View Testimonials; no direct conversion pair | Retained relevant proof-navigation link; no added request buttons |
| Service Areas | Eight cities, All Service Areas, disabled ZIP checker | Unchanged, including destinations and inactive notice |
| Final CTA `37feb023` | Orange Request Service, white-outline Call | Orange **CALL 847-656-3322**, white-outline **REQUEST SERVICE**, using existing nested variants |
| Footer 114 | Text telephone/email/contact and shared navigation | Unchanged; telephone destination correct |

Repeated emergency actions at Hero, Emergency strip and page end are useful at different decision points. No redundant standalone action justified deletion; the total button count is unchanged. Researchers retain category, service, project, testimonial and city paths without an added request button in each section.

## Technical Changes

Native Elementor Component Override controls were used directly in the visual editor. No Component was detached or rebuilt.

| Existing instance | Existing resource | Values edited |
| --- | --- | --- |
| Hero primary `18a239c4` | Component **53**, `button-primary` | Button label and destination: Call / telephone |
| Hero secondary `a7bcc76` | Component **103**, `button-outline-white` | Button label and destination: Request Service / `#` |
| Homepage Final CTA `37feb023` | Component **80**, nesting 53 and 103 | Primary Label/Link and Secondary Label/Link swapped to Call first, Request second |

Component 80 Title/Description, Hero heading/lead/media/layout and all button classes, spacing, tokens and responsive rules are unchanged. The saved-tree comparison contains **exactly eight leaf-value changes**, all text or link destinations under those three instances. There are no node additions, removals, reordered sections, local style changes or shared-definition edits.

**No new classes, components or custom code.** No new Global Variables, plugins, external dependencies or assets. Existing `button-primary`, `button-outline-white`, `cluster`, `cta-panel`, `section--dark`, Montserrat and brand tokens supply the presentation. Native override label/link fields remain directly editable under the named instances in Elementor Navigator.

## Complexity Audit

Kept existing DOM and shared variants; removed no useful navigation. Created no wrapper, selector, override key, abstraction or dependency. The wider audit records pre-existing nested CSS/cascade debt separately; this small CTA change does not require a global refactor. Header/Footer and unrelated Homepage subtrees are unchanged in normalized saved-state comparison.

## Verification

Actual frontend checks after publishing covered **1440×900, 1200×800, 900×900 and 390×844**.

- Hero and Final DOM order: Call first, Request Service second. Orange primary / transparent white-outline secondary normal styles confirmed by computed values and actual screenshots.
- Hero buttons sit in one row at 1440/1200, stack at 900/390; Final pair sits in one row at 1440/1200/900 and stacks at 390. Text does not wrap. Both controls remain about **52.5px** tall, **204px** wide; mobile gap **8px**. No clipping or horizontal document overflow.
- Document heights remain **6167 / 6167 / 7307 / 10413px**. All nine section positions/heights match the pre-change measurements. Hero heading and placeholder geometry remain unchanged.
- All **three Homepage call buttons plus Footer telephone link** use exactly `tel:+18476563322`. No telephone call was placed; verified HTML destination/protocol rather than a completed phone interaction.
- Keyboard Tab from Hero Call reaches Request Service; Shift+Tab returns to Call at all four widths. Final Call→Request order also tested. `:focus-visible` matches and visible white outline is present; normal inherited focus treatment gives Call a navy background and Request Service a white background/navy text. No activation of missing routes was attempted.
- Native editor override fields were actually edited and saved; saved MCP values plus reloaded frontend confirm persistence. Native Publish returned disabled after save completed.
- Header desktop Request Service remains navy and hides at tablet/mobile as before. This is preserved behavior, not a newly designed mobile Header.
- ZIP checker remains visibly inactive and its button disabled; no ZIP lookup, submission or API test was made.

The six-page WordPress inventory contains **no Request Service or Contact page**. Header/Hero/Emergency/Final Request Service destinations therefore remain explicitly unresolved `#`. Audience categories, six service links, project/index links, testimonial index, eight cities/directory and utility/navigation placeholders also remain unresolved, unchanged. No invented URL, production destination or unrelated section was substituted.

Accessibility limitation: normal white **16px/600** button text against fixed orange **#F05A29** has computed contrast about **3.39:1**. Existing brand colors/styles were deliberately preserved; an approved accessible treatment remains outstanding. Physical-device touch, screen-reader testing, anonymous-session performance and full database/files backup/restore were not performed. Local pre-change snapshots support this small reversible edit but are not a full backup.

[Sanitized saved diff / responsive and keyboard evidence](../evidence/2026-10-16-homepage-cta-strategy.json).

Actual post-change screenshots:

- [Hero desktop](../evidence/2026-10-16-homepage-cta-strategy/hero-1440.jpg)
- [Hero mobile](../evidence/2026-10-16-homepage-cta-strategy/hero-390.jpg)
- [Final CTA desktop](../evidence/2026-10-16-homepage-cta-strategy/final-1440.jpg)
- [Final CTA mobile](../evidence/2026-10-16-homepage-cta-strategy/final-390.jpg)

## GitHub

This milestone, the preceding read-only audit, their sanitized evidence/screenshots, PROJECT_CONTEXT, CHANGELOG, ELEMENTOR_MAP and DECISIONS are recorded together. The containing Git commit identifies delivery; its URL and verified remote main SHA are reported in the delivery receipt. No website code is deployed from this documentation repository.

## Outstanding Items and recovery

- Owner visual approval; missing Request Service and other internal destinations; existing orange contrast issue.
- Vertical-layout audit proposals remain unimplemented and require approval separately.
- No backend or production work authorized by this milestone.
- To reverse this change in native Elementor, restore Hero primary Request Service `#` / secondary Call telephone and Final primary Request Service `#` / secondary Call telephone. Component IDs, wrappers, global styles and layout do not need restoration.
