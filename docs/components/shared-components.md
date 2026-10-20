# Shared Atomic component library

Native reuse contracts freshly discovered on2026-10-20. IDs locate saved definitions; instance wrappers can render different generated IDs, so do not write portable CSS against those generated wrappers.

| Definition / root | Contract and role | Current Homepage consumers |
| --- | --- | --- |
| 71 /1ba080c | Title66d8f464 + description2d2aa2b4; overrides title,heading_tag,description; stack/hide-empty, inherited typography | audience300decb5,emergency2631f818,process5494e63e,projects6b4663fc,areas2554ebe8 |
| 53 /33af2049 | Primary button; text/link overrides; button-primary | Hero18a239c4,emergency300e78c6,nested CTA80 primary699f9898 |
| 59 /74d51f09 | Outline blue; text/link overrides; button-outline | portfolio2364d92a,areas2b5f493 |
| 103 /565b18f9 | Outline white; text/link overrides; button-outline-white | Heroa7bcc76,emergency91ce6f0,nested CTA80 secondary6aa9a1a0 |
| 286 /37b7429f | Informational24/7 mark; numbers49dec30d contains410956c2/16b7ed6a/88b8274; caption15e7354d exposes label | Hero4af4b551 |
| 80 /324d9854 | CTA copy/actions and nested53/103; six overrides | [Final CTA](final-cta.md) |
| 582 /16ae2220 | Four-step timeline; twelve overrides | [How We Work](how-we-work.md) |

Classes/tokens own repeated visual roles; the definitions above contain no shortcode/HTML-widget/custom JS. Documented class-owned focus/hover exceptions apply to button consumers; color/background/font/spacing tokens remain canonical in [DESIGN_SYSTEM](../DESIGN_SYSTEM.md).71 description has a local native width/style and hide-empty; do not hardcode its default sample copy into all consumers.

Buttons wrap/use responsive class variants; heading typography follows default tag/breakpoint settings;286 is informational and not a nested anchor. Keep instance links independent. Schema supports dynamic/internal destinations, but a contract is not proof of successful migration or instance-independence tests.

Other library entries56/100/62/65/68/74/77/83/86 now have individual [catalog records](library-patterns.md), based on fresh saved definitions and schemas. They are **not automatically dead code** because not used by the current Homepage main tree. Their full consumer graphs were not deleted or refactored; consult library/Style Guide and usage tools before edits. Header CTA uses56.

Safe reuse: instantiate an existing definition; edit exposed props per instance; check all consumers before changing shared structure/classes; preserve native links and focus/motion behavior. Use definitions80/582 records for their code dependencies and reuse caveats. No new shared component was added.
