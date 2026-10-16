# Process timeline water ripple — E16

Verified2026-10-16, America/Chicago, staging Homepage154 only. Builds on [E15](2026-10-16-process-timeline.md) / commit1922207022c6d924ba7e88be5ce86c1d56d31ac7. Owner authorized minimal centrally managed CSS when native controls are insufficient, then requested final **2px** ring strokes. No other sections, production or shared ROBYLO repository changes.

## What changed / native-first decision

Replaced the existing static orange outline with two thin concentric ripple rings. Native Atomic Effects exposes transitions/element transforms, but not a parent-hover-triggered pair of decorative pseudo-elements. Targeting the actual circle with native transforms would violate the stationary-circle requirement; new decorative elements/wrappers would be unnecessary. Continued the previously approved minimal external CSS exception without adding another component or styling system.

The existing process structure/Component582, Homepage instance79a67ca3,12 content overrides,87 Global Classes,36 Variables and native200ms background transition remain unchanged. Feature65 and its unrelated consumers receive no selectors. Numbers/titles/descriptions/connectors/typography/spacing are preserved. No JavaScript, PHP, Elementor Custom CSS, inline styles, plugins or external dependencies.

## Exact code / future editing

Canonical source: **[theme-overrides/process-timeline.css](../../theme-overrides/process-timeline.css)**, modified in place. Deployed block: **`/wp-content/themes/robylo-starter/assets/css/fallback.css`**, existing active staging ROBYLO Starter stylesheet. Native WordPress Theme File Editor saved the replacement and exact reload text matched; existing fallback rules are unchanged. Existing content-MD5 cache versioning picks up the change; no enqueue/PHP edit. Shared ROBYLO source and other websites untouched.

| Selector / name | Purpose |
| --- | --- |
| `.process-timeline__step:hover .process-timeline__number` | Existing whole-step background change via existing primary-hover Variable; static outline removed. |
| `.process-timeline__number::before`, `::after` | Two empty absolute/inset0, circular2px accent-token borders; opacity0 and pointer-events:none. No DOM nodes or actual circle-size rule. |
| `.process-timeline__step:hover .process-timeline__number::before`, `::after` | One1000ms ease-out iteration; second delayed160ms, total1160ms. Leave clears animation; re-entry starts it again. |
| `@keyframes gcpro-process-ripple` | Only pseudo-elements scale1→1.55 and fade0.55→0. No numbered-circle transform. |
| `.process-timeline .process-timeline__number` under reduced motion | Retains transition:none; ring generation/animation exists only under no-preference plus hover/fine pointer. |

New technical elements: the two CSS-generated pseudo-elements and one namespaced keyframe in the **existing** code file, justified by the exact effect. No new class, Variable, Component, code file, markup wrapper, plugin or dependency. Pseudo-elements reuse the existing circle radius and accent Variable; no duplicated typography/base sizes/colors. Animation duration/stagger/scale/stroke are cosmetic settings in this explicit exception, not a parallel design system.

Edit normal circle/content/layout and background-transition duration in Elementor as before. Edit only ring stroke/timing/expansion in the canonical CSS block, then apply that block to staging's existing stylesheet through supported deployment/editor access. No automatic Git→WordPress deployment exists. Client-specific block must be preserved during future theme updates; do not copy into shared starter without permission.

## Verification

- Fresh pre-edit theme text exactly matched E15; private local before-file backup retained. Saved final block matched intended file text, including final2px stroke. Real staging stylesheet URL acquired a new content version.
- Real pointer over the description: parent:hover=true while circle:hover=false. Both pseudo-elements used `gcpro-process-ripple`, duration1s, iteration-count1, delays0s/0.16s. Mid-cycle samples showed different growing scales and decreasing opacity. Both ended at opacity0/scale1.55 while parent remained hovered; leaving/re-entering restarted them. No infinite animation.
- Circle stayed64×64, transform:none, same document coordinates within0.001px rounding; no static outline. Only decorative rings expand. They use pointer-events:none and informational text remains non-clickable.
- Reduced-motion emulation: both pseudo-elements content:none/animation:none; native background transition suppressed by retained rule. Touch390px emulation: hover=false/pointerFine=false, pseudo-elements absent; all four steps remain complete through normal scrolling.
- Final CSS viewport checks1440/1200/900/390 retain4/4/vertical/vertical layouts, correct Montserrat, original content and continuous connector alignment. Zero horizontal overflow or inline style attributes. No key information depends on hover.
- Elementor remains natively editable: no element/override/class writes during E16; E15 actual editor checks remain applicable. No physical-device, screen-reader or performance benchmark is claimed.

[QA samples/final geometry](../evidence/2026-10-16-process-ripple/qa.json), [desktop during ripple](../evidence/2026-10-16-process-ripple/desktop-ripple.jpg), [mobile default](../evidence/2026-10-16-process-ripple/mobile-390.jpg). Animation samples were first captured at1px before the owner's final stroke refinement; final saved CSS/stroke and four-width checks are2px. Geometry is unchanged by this pseudo-border refinement.

## Complexity / outstanding / recovery

Removed obsolete static outline/offset; reused the existing file, parent trigger, native transition and tokens. Two pseudo-elements avoid extra DOM and JavaScript; only transform/opacity animate, one-shot, no dependencies. No duplicate hover component/class or hidden widget styles.

Visual approval pending; no remaining implementation blocker. Screenshots are static samples; hover the actual staging step to review motion. Roll back only the marked client CSS block to commit1922207 for the previous static treatment; preserve existing fallback rules and native timeline. Private before-file snapshot exists; no full database/files restore was tested. Git revert alone does not deploy the stylesheet.
