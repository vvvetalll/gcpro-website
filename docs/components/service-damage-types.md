# GCPRO — Service Damage Types

2026-10-22, staging only. **Section2 approved by owner; requested final desktop3+2 adjustment implemented.** Implements only Section2 of the Water landing page. No sections3–10, metadata rollout, new URLs, redirects or SEO research.

## Purpose and native ownership

- New native Atomic Component **1345 — GCPRO — Service Damage Types**, UID `component-505fb6a5-0caa-4a83-805b-7f65f8bb3c55`.
- [Edit the shared definition](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1345&action=elementor).
- Existing Water Damage Page514, `/residential-services/water-damage/`, main50eb9797 → new instance5777c79b **Shared Types of Water Damage**, directly after unchanged Hero29f36982 →1318.
- Complete shared tree: outer section → container → existing Section Heading71 + responsive native grid → five native article cards, each with number Paragraph, H3 and description Paragraph. Desktop shows three equal cards then two centered cards; tablet retains two columns with the fifth spanning its row; all stack on mobile. No copied page-owned section tree.
-13 native independent Overrides: `eyebrow`, `heading`, `introduction`, `type_1_title` / `type_1_description` through `type_5_title` / `type_5_description`. Heading fields expose the existing71 properties further through1345; heading level stays H2, card headings H3. Numbers01–05 are shared structure.

## Design and dependencies

Reuses existing section, container, stack, grid-2, card and section-heading--accent Global Classes. Existing color-background, color-surface, color-border, color-primary, font-size-h4 and spacing Variables supply native styling. White section, lightly tinted cards, navy headings/numbers, existing orange heading underline;32px desktop card padding/24px mobile,8px corners. Native local controls own six equal desktop tracks. Card grid-column values are1/3,3/5,5/7,2/4,4/6, producing three equal-width cards above two centered cards without wrappers or new definitions. At tablet the prior two-column layout is retained, with ordinary card placement and the fifth spanning1/-1. Mobile retains one column, original24px padding and original card placement.

Exactly one new Component,1345. No new Global Class, Variable, media, CSS, JavaScript, PHP, plugin, Custom Code entry or external dependency. MCP style inputs were converted through supported Atomic controls, with no conversion warnings. All heading accent CSS remains owned by the pre-existing global class; no new custom rule. Existing71 and1318 definitions are untouched. No card links, buttons or placeholder destinations were added; contextual service/support links belong to later separately authorized sections.

## Water content

Eyebrow: **01 / WATER DAMAGE SOURCES**. H2: **Types of Water Damage**.

Introduction: A burst pipe, a slow leak or water entering from outside can affect more than the surface you see. The source and spread of moisture help determine the right cleanup, drying and repair plan.

1. **Burst and Leaking Pipes:** A sudden pipe break can release water into walls, floors and adjoining rooms. Smaller supply-line leaks may stay hidden until staining, soft finishes or damp materials appear.
2. **Basement Flooding:** Water can collect in basements and lower levels, affecting flooring, wall materials and stored belongings. Standing water and moisture beneath finished surfaces need separate assessment.
3. **Appliance Leaks:** Washing machines, dishwashers, refrigerators and water heaters can leak at connections or supply lines. Water may travel beneath cabinets and flooring beyond the visible puddle.
4. **Ceiling Leaks:** Stains, peeling paint or a sagging ceiling may point to water from plumbing, an upstairs room or the roof. The source and condition of affected materials should be checked before cosmetic repairs.
5. **Stormwater Intrusion:** Heavy rain can bring water through damaged roofing, windows or other openings. Restoration planning needs to account for affected interiors and the building issue that allowed water in.

Sources: existing2026-10-22 SEMANTIC_ARCHITECTURE, IMPLEMENTATION_ROADMAP Water section, KEYWORD_INTENT_GCPRO_MATRIX and SERP_RESULT_REVIEW. Existing514 remains the generic Chicago water restoration/mitigation/cleanup owner; extraction487, moisture490 and drying491 remain support tasks. Saved search-volume geography, Lost/history and sampled-order limitations are unchanged. The five categories follow the owner’s explicit approved outline; no claim of new keyword research. Sewage is omitted without verified company capability. No response time, certification, equipment, insurance, project or performance claims are invented.

## Focused verification

Native component creation/placement/publication succeeded without warnings. Page has exactly two component instances: original Hero and this section. The original Hero JSON subtree compares byte-identical with its pre-section snapshot. Home, Residential, Commercial, other service pages, BEAF records/gallery, template assignments and shared definitions were not written.

Authenticated Chrome at1440px: five articles, correct H2/five H3 headings,556px +556px columns, no document/card overflow; cards use32px padding. At393px: five338px-wide cards in one column,24px padding, no overflow and original H1 retained. These are desktop browser viewport simulations, not physical-device or anonymous/incognito certification. The previous cloud anonymous403 limitation remains; no retry or security change was attempted. Elementor and staging caches were cleared for preview. Final desktop check confirms the existing40px orange heading underline (rgb240,90,41) renders correctly after adding the existing accent class to the section container. A desktop preview screenshot was shown to the owner for approval.

## Editing, approval and recovery

Edit1345 for shared structure; use the page instance’s13 Overrides for page-specific labels and copy. Keep five current cards; future optional-count requirements are a separate approved change rather than speculative controls. Do not detach, copy descendants or create a separate full definition for different text. No second page instance was created solely to test hypothetical future reuse.

Owner approved this section, including the requested desktop3+2 adjustment. Stop here; do not build Process, Project, Recovery, Why, Guidance, Areas, FAQ or Final CTA, and do not apply whole-page SEO metadata until separately instructed. Approved Hero and its current Overrides remain preserved.

Private pre-change514 backup and sanitized native input/output checkpoints remain outside Git. If rollback is requested, remove only new instance5777c79b from514 and preserve the Hero; clear native Elementor/SG caches. Do not delete the component definition or original data without authorization. Git rollback alone does not undo Elementor.

## Approved3+2 layout adjustment —2026-10-22

Only native layout properties on Types Grid3361ff5d and five Card nodes776ef1a0/20cf0bab/2a382dac/6c333626/419ef18a changed. One targeted read and one six-operation native update, followed by native publication. Content, H2/H3 hierarchy,13 Overrides, card colors/borders/type/padding and all page instances are untouched. No new Component, Global Class, Variable, CSS, JavaScript or script dependency. At1440px all five cards are362.66–362.67px wide; the first three share one row and the last two share a centered second row (centering error<0.01px), with no document overflow. At393px the original one-column layout is retained: five338px cards,24px padding,8px radius, no card/document overflow. Browser viewport overrides were reset. Earlier two-column desktop observations above are historical.
