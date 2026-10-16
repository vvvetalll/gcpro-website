# GCPRO design system

Observed 2026-10-16 through read-only Elementor MCP on staging (E3 in [PROJECT_CONTEXT](../PROJECT_CONTEXT.md#evidence-register)). These are saved resource values and class identities, not a new design proposal or proof of rendered use. Re-read resources before editing.

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
