# GCPRO design system

## Current audience photo presentation — E31

Existing audience-card__image g-77c2a17 uses native16:9 (supersedes historical4:3 below), same cover/center/full-width rules. Final images1152×648 match the frame with no default composition crop. No new design resource in E31. Existing E30 hover uses native280ms transitions plus scoped parent→child CSS in audience-card Global Class; [exact location, source mirror and motion limitation](milestones/2026-10-16-final-audience-images.md#e30-carryover--existing-audience-hover-documented-without-new-deployment). No theme/shared-repository change.

## Audience photography trial — E28

New native Global Class **audience-card__image g-77c2a17**: display block, width100%, height auto, aspect ratio4:3, object fit cover, object position50%50%. Current consumers: only native Images295bf90e/27ec40d5 on154. All values are native Atomic properties, custom_css:null; no local styles. Existing media-placeholder is a padded/background/bordered flex placeholder, image-led-card styles a parent, header-logo is logo-specific; none fits a full-bleed photograph. This single shared class is required to preserve symmetry without affecting other media. Edit Image → Style → select audience-card__image → Size/Show more for ratio/fit/position. Images themselves remain independently selected in General → Content. Existing audience-card owns24px clipping/corners/border; layout-reset removes obsolete placeholder frame presentation. Classes90→91; Components16/Variables36 unchanged. [Assets, trial/QA and limitations](milestones/2026-10-16-audience-card-images.md).

## Current optional H2 accent — E26

Use section-heading--accent g-a537304 on the existing native container directly holding Section Heading71 (.stack > h2). One scoped GLOBAL class pseudo-element rule adds40×3px/radius2 orange line,16px below H2 via color-accent/space-sm. Apply selectively; current five are Audience/Core/Process/Projects/Areas on154, all start-aligned. No global H2 default or71 definition change. Attach/remove via native container Classes; geometry lives in that selected global class's documented Custom CSS, not local widget CSS. [Canonical mirror](../integrations/section-heading-accent.css) is not separately enqueued; [editing/limits/map/QA](milestones/2026-10-16-section-heading-system.md).

E26 owner correction removes E25's H3 line and copy wrapper from62; retires heading-accent and stack--tight after usage/16-component checks. Global Classes now90, Variables36, Components16. The following E25 description is historical and superseded.

E25: Component62 uses new reusable heading-accent g-01bd1bd (36×3px, radius2px, color-accent) and stack--tight g-19f58a6 (space-xs8px, desktop/mobile) with existing stack. Native copy grouping keeps icon/CTA spacing unchanged and adds only3px mobile height. Classes89→91; no new Variables/Components/code/local styles. Native controls and custom_css:null verified. [Editing/QA](milestones/2026-10-16-service-heading-accent.md).

E24: service-card__icon g-b759e84 native padding10px (previous12), same56px square/14px radius/light-blue Variable/margins; inner SVG36px, +12.5%. No transform/local/custom CSS. B Mold source now spore/cleaning sparkle; same48×48/2.25 stroke, Media607. Other five designs unchanged. [QA and editing](milestones/2026-10-16-icon-refinement.md).

E23: owner selected B; navy/orange service SVGs now applied through existing instance icon Overrides on Homepage154. Media596–601, same badge classes/geometry; no new styles/components/code. Both color channels and intended fills verified in actual frontend. Source-level colors remain explicit; native per-channel color controls not claimed. [Integration/QA](milestones/2026-10-16-icon-b-integration.md).

E22 **proposed, not deployed**: [original Core Services SVG family](../assets/icons/core-services/README.md), A/currentColor outline and B/navy-orange accent.48×48,2.25 rounded strokes, six service meanings per treatment. No new Global Classes/Variables/Components or site code. Use existing SVG Icon Override only after visual approval and native color/instance tests. [Study/QA](milestones/2026-10-16-core-service-icon-concepts.md).

E21 supersedes E19 CTA colors: existing button-outline-orange g-563da68 supplies transparent/orange default and orange/white hover. service-card__action g-d0416c8 keeps compact dimensions/bottom alignment/native200ms transition; its redundant navy color and state overrides removed. Orange Outline unchanged; no new resources/custom code. [Editing, contrast and QA](milestones/2026-10-16-core-orange-cta.md).

E20: Code590 remains Homepage154-only and now includes the color-only `gcpro-process-number` keyframe in existing integrations/process-timeline-mobile.css. Reuses current hover/played triggers and stagger; no JS, theme, global typography or Atomic structure changes. [Source, timing, accessibility and QA](milestones/2026-10-16-timeline-number-color.md).

E19: Global Classes87→89. Existing service-card g-f569734 now controls full bordered surface/card height/padding/hover. New service-card__icon g-b759e84 is the56px SVG badge modifier (priority before icon-svg); new service-card__action g-d0416c8 is the compact Montserrat600 outline CTA/bottom alignment. Three classes use native Atomic properties only, custom_css:null; Variables36 unchanged. grid3 reused without grid--flush. [Details/editing/QA](milestones/2026-10-16-service-cards.md).

## Touch sequence — E17, 2026-10-16

Desktop E16 rules unchanged. On hover:none/pointer:coarse/no-reduced-motion, [mobile CSS](../integrations/process-timeline-mobile.css) reuses `gcpro-process-ripple` with step delays0/400/800/1200ms and second-ring+160ms. It applies only after native Custom Code590's observer sets `data-gcpro-ripple="played"` on the existing root. Before that, no rings are generated. Mobile uses forwards fill so future delayed rings remain invisible. Pseudo-element geometry is explicitly touch-gated because E16's equivalent definitions are fine-pointer-only; no theme refactoring or duplicated base typography/layout tokens. Same2px accent-token rings; no new Atomic Class/Variable/Component. [Controls, native gap and QA](milestones/2026-10-16-mobile-sequence.md).

## Process ripple — E16, 2026-10-16

Supersedes only E15's static hover outline: existing client CSS block now uses `.process-timeline__number::before/::after`, triggered by `.process-timeline__step:hover`, and scoped keyframes `gcpro-process-ripple`. Two **2px** orange rings expand/fade once,1000ms duration/160ms stagger, without transforming the circle. Generation/animation requires fine hover pointer and no reduced-motion preference; reduced motion also disables the existing native background transition. Classes87/Variables36 and Component582 remain unchanged. [Native gap, exact CSS, editing and QA](milestones/2026-10-16-process-ripple.md); no Elementor Custom CSS or shared starter edits.

## Process timeline — E15, 2026-10-16

Current register: **87 Global Classes, 36 Variables**. Four added native classes support Component582: `process-timeline` (`g-a12d836`, four-column zero-gap grid→one column at1024px), `process-timeline__step` (`g-07d3365`, column→row step layout), `process-timeline__number` (`g-e17507d`, 64→56px navy/white circle), `process-timeline__connector` (`g-261ecb6`, 2px horizontal→vertical segment). Existing `process-step-number` provides Montserrat600 24/24/22px; stack/compact/reset and color/spacing Variables are reused. Circle class has priority over existing number typography color; other existing class priority relationships are unchanged.

Base properties and the 200ms background transition are native Atomic Global Class settings, editable through the selected class in Style controls; no retained local styles or Elementor Custom CSS. Three native connector divs meet centers continuously; no pseudo-elements. Owner-approved minimal external exception supplies whole-step hover → circle color/outline and reduced motion: [canonical CSS](../theme-overrides/process-timeline.css), deployed in existing ROBYLO Starter `assets/css/fallback.css`. No typography/base-size duplication, plugins, dependencies or shared repository changes. [E15](milestones/2026-10-16-process-timeline.md) contains IDs, capability findings, measured responsive results, editing and recovery. This supersedes only earlier process-grid/card descriptions below.

Observed 2026-10-16 through read-only Elementor MCP on staging (E3 in [PROJECT_CONTEXT](../PROJECT_CONTEXT.md#evidence-register)). These are saved resource values and class identities, not a new design proposal or proof of rendered use. Re-read resources before editing.

## ZIP UI and Homepage refinements — E8

Current class total is 83. The 71-class register below is the earlier baseline. Existing variables and classes were reused; no tokens or duplicate Components were created. These additions use native Global Class controls, with no retained Custom CSS:

| Class | ID | Purpose |
| --- | --- | --- |
| form-panel | g-ecfd56c | Light-blue panel, 1px token border, 12px radius, 32px padding / 24px mobile, 16px gap |
| form-controls | g-a9bac3a | Input/action row; stacked at tablet breakpoint 1024px and below |
| form-input | g-4a008b9 | Inter 16px, 52px control, native border/radius/background; navy 2px focus border |
| button--inactive | g-bf5bb9b | Montserrat 600, 14px, 52px control and muted disabled presentation; disabled is a native attribute, not CSS |
| form-label | g-f760e1c | Inter 14px/600 with text-color token |
| form-field | g-7a37771 | Native vertical field layout with 8px gap and zero padding |
| form-note | g-77663f6 | Inter 14px normal-case muted help text |
| process-step-number | g-af5ab08 | Montserrat 600, 24px desktop/tablet and 22px mobile, 1.3 line height |
| audience-card | g-38b29fb | Rounded white linked card with token border, clipped placeholder and no underline |
| audience-card__body | g-19a0c6f | Copy/action grid, 32px padding / 24px mobile |
| card-action | g-a5c0d65 | Navy circle, 64px desktop/tablet / 52px mobile |
| card-action__icon | g-8a7dd36 | 24px white SVG glyph |

Only process-step-number was moved ahead of card-icon; other existing classes retain relative priority. Step Number keeps card-icon and hide-empty because the existing icon-svg rule hides an SVG immediately followed by a nonempty card-icon. Changing that contract requires an explicit supported visibility design. This is a documented pre-existing selector, not new code introduced here.

Heading capitalization remains H1/H2 uppercase, H3/H4 capitalize, H5/H6 none. Sizes, weights, colors and responsive defaults match the pre-task snapshot. Audience copy reuses stack--compact plus stack; placeholders reuse media-placeholder.

The converter initially retained unsupported cursor/white-space and a focus-visible border as Custom CSS. These declarations were removed in the visual editor; ordinary link keyboard focus remains provided by the existing HTML Default. No new custom styling remains in the added classes. See [milestone](milestones/2026-10-16-zip-and-homepage-refinements.md) for verification and limitations.

## Global conventions

- Keep reusable values in native Global Variables, base typography in tag defaults, shared styling/layout in Global Classes, repeated structures in Components and instance content in supported overrides.
- Reuse the existing labels. Component names are human-readable; class labels use lower-case role names, with existing `--modifier` and `__part` conventions. Do not rename existing classes merely to impose a new convention.
- Inspect actual class declarations, priority, local overrides and tag defaults before diagnosing the cascade. The resource says earlier classes have higher priority; do not reorder casually.
- Preserve native responsive controls, meaningful headings, readable contrast, visible focus and usable menu/touch controls. Record the actual breakpoints and values inspected, rather than assuming defaults.
- Document new labels, scope, consumer effects and the editor location after each milestone. Avoid duplicated local settings and hidden theme rules.

## Observed Global Variables — 36

Source: discovered `elementor://global-variables`, active kit, read 2026-10-16. Values are transcribed as returned, including px units and formulas. Their existence does not prove every heading or layout currently references them. Internal variable IDs are omitted; labels are the useful editing reference.

| Label | Type | Saved value |
| --- | --- | --- |
| `color-primary` | color | `#1A327D` |
| `color-primary-hover` | color | `#142862` |
| `color-secondary` | color | `#334155` |
| `color-accent` | color | `#F05A29` |
| `color-text` | color | `#334155` |
| `color-text-muted` | color | `#5B6575` |
| `color-background` | color | `#FFFFFF` |
| `color-surface` | color | `#F8FAFC` |
| `color-surface-alternate` | color | `#EFF6FF` |
| `color-border` | color | `#CBD5E1` |
| `color-white` | color | `#FFFFFF` |
| `color-success` | color | `#15803D` |
| `color-error` | color | `#B91C1C` |
| `font-body` | font | `Inter` |
| `font-heading` | font | `Montserrat` |
| `space-xs` | size | `8px` |
| `space-sm` | size | `16px` |
| `space-md` | size | `24px` |
| `space-lg` | size | `32px` |
| `space-xl` | size | `48px` |
| `space-2xl` | size | `64px` |
| `space-3xl` | size | `96px` |
| `container-max` | size | `1200px` |
| `content-max` | size | `800px` |
| `page-gutter` | size | `32px` |
| `page-gutter-mobile` | size | `20px` |
| `section-spacing` | size | `96px` |
| `section-spacing-mobile` | size | `56px` |
| `font-size-h1` | custom-size | `clamp(2.5rem, 1.75rem + 3vw, 3rem)` |
| `font-size-h2` | custom-size | `clamp(2rem, 1.5rem + 2vw, 3rem)` |
| `font-size-h3` | custom-size | `clamp(1.5rem, 1.25rem + 1vw, 2rem)` |
| `font-size-h4` | custom-size | `clamp(1.25rem, 1.125rem + 0.5vw, 1.5rem)` |
| `font-size-h5` | custom-size | `clamp(1.125rem, 1rem + 0.5vw, 1.25rem)` |
| `font-size-h6` | size | `1rem` |
| `font-size-body` | size | `1rem` |
| `font-size-lead` | custom-size | `clamp(1.125rem, 1rem + 0.5vw, 1.25rem)` |

## Observed Global Class register — 71

Source: discovered `elementor://global-classes`, read 2026-10-16. Full returned order is preserved below, highest priority first. This resource returned IDs and labels, not a complete declaration audit. Locate these in Elementor Global Classes; inspect the native controls and affected consumers before changing them.

| Priority | Class label | Internal ID |
| --- | --- | --- |
| 1 | `section--dark` | `g-43edd01` |
| 2 | `service-card` | `g-f569734` |
| 3 | `text-link` | `g-f85f475` |
| 4 | `image-led-card` | `g-f382380` |
| 5 | `grid--four` | `g-aadf7b4` |
| 6 | `grid--flush` | `g-5e84b20` |
| 7 | `feature-summary` | `g-8333fe1` |
| 8 | `project-summary` | `g-3eb7605` |
| 9 | `testimonial-card` | `g-c51baa3` |
| 10 | `section--strip` | `g-8f39284` |
| 11 | `split-row` | `g-5f7b649` |
| 12 | `hero-layout` | `g-c4cc431` |
| 13 | `comparison-media` | `g-05670b8` |
| 14 | `comparison-panel` | `g-637b3ac` |
| 15 | `city-links` | `g-6ebef89` |
| 16 | `city-link` | `g-9a26448` |
| 17 | `cta-panel` | `g-e1d4327` |
| 18 | `site-footer` | `g-a9afb6b` |
| 19 | `footer-columns` | `g-fb9219a` |
| 20 | `footer-column` | `g-3f96b71` |
| 21 | `text-measure--short` | `g-d480b26` |
| 22 | `heading-label` | `g-0526546` |
| 23 | `text-meta` | `g-2f5e3b0` |
| 24 | `footer-meta` | `g-11ba71a` |
| 25 | `navigation--primary` | `g-be97fc2` |
| 26 | `navigation-links` | `g-683eaef` |
| 27 | `panel` | `g-b691ab0` |
| 28 | `align-start` | `g-63e627b` |
| 29 | `stack--compact` | `g-3bac536` |
| 30 | `media-placeholder--dark` | `g-710713a` |
| 31 | `media-placeholder--neutral` | `g-dc38375` |
| 32 | `media-placeholder--project` | `g-09f1205` |
| 33 | `media-placeholder--badge` | `g-7b4239a` |
| 34 | `media-placeholder` | `g-7242622` |
| 35 | `card-icon` | `g-2c25e20` |
| 36 | `hide-empty` | `g-dea53d0` |
| 37 | `text-emphasis` | `g-3c6116d` |
| 38 | `section--light` | `g-1834399` |
| 39 | `layout-reset` | `g-0152925` |
| 40 | `section--compact` | `g-4225410` |
| 41 | `section--large` | `g-d5b53ca` |
| 42 | `section` | `g-d3248b3` |
| 43 | `container--narrow` | `g-0013c25` |
| 44 | `header-row` | `g-eeaa1f2` |
| 45 | `info-row` | `g-bf95de4` |
| 46 | `container` | `g-68fb534` |
| 47 | `stack` | `g-6f5f11a` |
| 48 | `cluster` | `g-0e529a5` |
| 49 | `grid-2` | `g-9b8782d` |
| 50 | `grid-3` | `g-2f37dc0` |
| 51 | `card--interactive` | `g-d63edc0` |
| 52 | `card` | `g-8ca905f` |
| 53 | `button-primary` | `g-92745fa` |
| 54 | `button-secondary` | `g-e47e377` |
| 55 | `button-outline` | `g-b5f3969` |
| 56 | `text-lead` | `g-8c1a9a9` |
| 57 | `text-muted` | `g-68bba82` |
| 58 | `button-outline-orange` | `g-563da68` |
| 59 | `button-outline-white` | `g-c8eb142` |
| 60 | `icon-svg` | `g-b84ed52` |
| 61 | `site-header` | `g-34b5e46` |
| 62 | `header-brand` | `g-fba6f58` |
| 63 | `header-logo` | `g-a59f4e5` |
| 64 | `info-bar` | `g-1f9d3da` |
| 65 | `info-links` | `g-f94864f` |
| 66 | `info-text` | `g-e2b178b` |
| 67 | `emergency-mark` | `g-d54b228` |
| 68 | `emergency-mark__numbers` | `g-bdc93ca` |
| 69 | `emergency-mark__number` | `g-5d6cddf` |
| 70 | `emergency-mark__slash` | `g-1529654` |
| 71 | `emergency-mark__label` | `g-32c8e95` |

## HTML Defaults read during integration — E6

These are fresh saved tag-default values, not changes made by this documentation task. Tablet rules use max-width 1024px; mobile rules use max-width 767px. All headings reference `font-heading` (Montserrat), use `color-text` at the default layer, and have zero margin. Dark-section foreground treatment is a separate shared-class concern.

| Tag | Desktop / tablet / mobile size | Weight | Line height | Transform |
| --- | --- | --- | --- | --- |
| H1 | `var(--font-size-h1)`; existing clamp token | 700 | 1.1 | uppercase |
| H2 | 32 / 28 / 24px | 700 | 1.15 | uppercase |
| H3 | 24 / 22 / 20px | 600 | 1.3 | capitalize |
| H4 | 20 / 19 / 18px | 600 | 1.3 | capitalize |
| H5 | 18 / 17 / 16px | 600 | 1.4 | none |
| H6 | 16 / 15 / 14px | 600 | 1.4 | none |

The retained `font-size-h2` through `font-size-h5` variable formulas above do not describe these explicit HTML Default sizes. Do not overwrite defaults merely to make them match unused or differently scoped tokens.

## Homepage V2 class roles — 17 additions in the implementation record

Current identities/order are confirmed by E6; the roles below are corroborated by saved class assignments and the historical E7 implementation. This is not a fresh audit of every class declaration.

| Classes | Role / native editing location |
| --- | --- |
| `service-card`, `text-link` | Shared Component 62 layout and understated action; Global Classes layout, spacing and typography/state controls |
| `image-led-card` | Unified audience/project image-and-body wrapper |
| `grid--four`, `grid--flush` | Four-step responsive grid and compact service-grid gaps |
| `feature-summary`, `project-summary`, `testimonial-card` | Lighter shared definitions for 65, 68 and 86 |
| `section--strip`, `split-row` | Compact emergency strip and responsive copy/action layout |
| `hero-layout` | Native grid column proportions, gaps and responsive stacking |
| `comparison-media`, `comparison-panel` | Static 4:3 Before/After placeholders; no slider |
| `city-links`, `city-link` | Wrapping compact location links, without normal/hover underline |
| `cta-panel` | Inset navy CTA layout within a light section |
| `media-placeholder--dark` | Legible dark Hero placeholder variant |

Existing `section`, `container`, `stack`, `cluster`, grids, icon and button classes were reused. No new design-token set or duplicate Component ID was introduced. The temporary `eyebrow`, `header-navigation` and `menu-control` classes were removed and are not part of the final 71-class register.

Final E7 refinements: existing emergency-mark classes give the caption 12px desktop/tablet and 11px mobile with an 8px gap after the numbers. Component 286 has a DIV root, so the informational mark has no anchor underline. `button-secondary` prevents shrinking/wrapping; recorded Header CTA size is about 204×53px on desktop and hidden on tablet/mobile. The mobile Header grid reserves a 44px toggle column. Native Full Width replaced the conflicting legacy dropdown right/min-width rule; other pre-existing legacy navigation styling remains. These class behavior values are historical rendered checks, not remeasured here.

## Reported conventions and limits

E4 reports one Homepage H1, Montserrat headings, a compact navy Hero, 16:9 Hero/audience placeholders and 4:3 project placeholders. It reports core service grids at 3/3/2/1 columns and process grids at 4/4/2/1 for 1440/1200/900/390 px. Those viewport checks are historical, not configured breakpoint values verified here.

The older E5 component artifact contains typography/default/style definitions that may be stale. Do not replay it over the current kit. The full saved tag-default settings, all class declarations, responsive breakpoints and any legacy custom CSS still need a current audit.

E4 reports white text on orange `#F05A29` around 3.39:1 and leaves the treatment unresolved. Preserve the issue in the next design review; no palette or styling was changed in this documentation task.

## Editing locations

| Change | Native location / scope |
| --- | --- |
| Reusable colors, fonts, spacing | Global Variables; inspect references before changing |
| Base heading/body typography | Atomic tag defaults; inspect class/local overrides |
| Shared layout, buttons and states | Global Classes; check order and responsive/state controls |
| Reusable structure | Component definition; affects consumers |
| Individual title, icon or destination | Component instance's exposed overrides; do not detach |
| Header/footer assignment | Separate Theme Builder document and display conditions |

Actual controls and persistence must be verified on the installed Elementor version. No hidden CSS/JS or new styling was added by documentation initialization.
