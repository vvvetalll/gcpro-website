# ZIP Checker UI and Homepage visual refinements

Date: 2026-10-16, America/Chicago. Environment: https://vitaliiv1.sg-host.com. Evidence E8. Owner visual approval is pending.

## Authorized scope and delivery

The initial scope was the existing Service Areas section of Homepage 154. Follow-up owner messages authorized a more compact modern panel, the final heading capitalization policy, smaller Montserrat process numbers without checkmarks, and reference-based Residential/Commercial cards. No other sections were redesigned. Header 113, Footer 114, production and shared ROBYLO were not changed.

Service Areas keeps heading Component 71, original copy, all eight existing city links and directory action. City parent d6dbbe2 moved into the introduction before the directory action. Right panel has H3 "Do We Serve Your Area?", the requested description, native Label/Input and a real disabled Check Area button. The visible note is "Coming soon — ZIP checker is not active." No ZIP lookup, validation, coverage result, external service or custom backend was built.

Process numbers in Component 65 use the new process-step-number class, Montserrat 600, 24px desktop/tablet and 22px mobile. The former card-icon class was retained for the existing SVG visibility rule; hide-empty is retained. The class priority was adjusted above card-icon. Four process instances show 01–04 without visible SVG checkmarks; benefit cards retain their SVG behavior.

Audience wrappers 4c8810dc and 2066a26 remain in the existing two-column grid, with their original 16:9 placeholders. They now have rounded white bordered cards, native H3/copy and navy circles with real white arrow SVGs. The two old Component 62 instances were replaced in this section only, leaving six core service instances unchanged. Native text uses the owner's reference descriptions. Existing # destinations remain; no new pages or production URLs were introduced.

Final heading policy is uppercase H1/H2, capitalize H3/H4 and none H5/H6. The temporary all-uppercase request was reversed after owner correction. All six final default strings equal the pre-task snapshot; Montserrat, sizes, weights, line heights and colors are preserved.

## Native editing and styles

Twelve reusable Global Classes were added; see [DESIGN_SYSTEM](../DESIGN_SYSTEM.md#zip-ui-and-homepage-refinements--e8). Existing container/grid/stack/city/placeholder classes and variables are reused. No new Component ID or design token was created. The total is 83 classes and 36 variables.

Native editor verification included input placeholder/type/required/read-only controls, label association, disabled button attribute, and audience H3 editing. A temporary placeholder and heading change rendered in the editor, then the exact final text was restored. New class controls expose normal native styling. Converter-generated Custom CSS in the inactive button and audience focus variant was removed through the editor; it is not a retained implementation exception.

The SVG asset is attachment 464. Standard WordPress Media upload rejected SVG with "Sorry, you are not allowed to upload this file type." Elementor's native Upload SVG → Media dialog accepted the path-only vector through its existing SVG import route. No unrestricted upload setting, plugin, PHP or security change was introduced. Original safe vector source is [archived here](../assets/robylo-arrow-right.svg). The SVG has no scripts, event handlers, external resources or embedded styles.

No new application CSS, JavaScript, PHP, HTML widget, theme modification or manual inline style remains. Elementor itself injects width/height/overflow attributes into rendered SVGs; these are renderer output rather than manually authored element styling.

## Actual verification

| Width | Service Areas | Audience cards | Process | Overflow |
| --- | --- | --- | --- | --- |
| 1440px | Two columns; input/action row | Two equal cards; 16:9 media, two SVG arrows | Four columns; 24px Montserrat | None |
| 1200px | Two columns; input/action row | Two equal cards | Four columns; 24px Montserrat | None |
| 900px | Two columns; input above button | Two columns; readable wrapping | Two columns; 24px Montserrat | None |
| 390px | Information then panel; full-width controls | Cards stacked; action stays beside copy | Steps stacked; 22px Montserrat | None |

- Native label for=gcpro-area-zip matches the input ID. Both label/input render Inter; input/button heights are 52px.
- Native disabled=true is present, not only disabled-looking styling.
- Filling 60148 and pressing Enter produced no form POST, lookup request, navigation or success/error state. Network observation showed only unrelated SiteGround GET requests. Test text was cleared afterward. No built-in WebMCP form-submission tool was invoked.
- City subtree settings/destinations are identical before/after. All nine city/directory links remain #. Audience links also remain # pending destination pages.
- Fresh saved reads show no local-style entries in Homepage 154. Seven unrelated section trees are identical to the initial snapshot. Header/Footer full returned trees match exactly.
- Desktop/mobile screenshots and the 1200/900 variants were inspected. Physical touch hardware, full-site audit, production, real ZIP lookup and migration were not tested.

## Exact limitations and activation gate

Atomic Input and Label must be descendants of Atomic Form. The builder also requires success/error slots with children, so two native hidden slots exist; their text says lookup is unavailable, never invented coverage results.

An empty actions-after-submit list did not persist: both MCP and visual clearing were tested, and the default Email chip reappeared after saving/reopening. No recipient, webhook or external lookup was configured. The form also advertises Elementor's built-in WebMCP submission tool even with Agent auto-submit off. The native disabled submit button prevents ordinary click/Enter submissions and the visible notice identifies the feature as inactive. This is not a claim of a backend-wide kill switch against programmatic submission. **Do not enable the button or advertise a working checker until this native default-action behavior and the intended functional design are deliberately resolved.**

The native SVG override could not be cleared through a guessed empty icon shape; validation rejected it, with no accepted page mutation. Existing number/icon visibility was preserved using its prior class contract, not a new selector workaround.

## Recovery and evidence storage

Private local affected-document snapshots, defaults, SVG source, screenshots and browser QA are in outputs/service-areas-zip-ui-2026-10-16 in the task workspace. before.json includes Homepage/Header/Footer plus global resource inventories; feature-card-before.json and heading-defaults-before.json cover follow-up edits. These are scoped recovery references, not a tested complete database/files backup. Full restore readiness and installed version inventory remain open.

Rollback scope: restore only the Service Areas/audience subtrees and Component 65 number classes from the snapshots, remove these new class usages before deleting unused classes, and restore class order. Heading defaults already match the initial state. Recheck all consumers; a Git revert alone cannot restore WordPress.

The repository contains sanitized evidence, source SVG and this implementation record; full snapshots, private logs and authenticated browser state are excluded. Documentation delivery requires a normal commit/push with verified matching remote main. The containing Git commit identifies this milestone.
