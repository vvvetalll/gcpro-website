# How We Work timeline — E15

Verified 2026-10-16, America/Chicago, staging only. Scope: existing Homepage154 section `4681b8f5`; no internal service-page design, Header/Footer, SEO routing, production or shared ROBYLO source changes.

## Implementation and editing

One native reusable **ROBYLO / Process Timeline**, Component582, UID `component-05873ba5-60ba-44ec-9fed-ffb25ced3f75`, replaces the four generic Feature65 instances only inside Process Steps `5a7e87b2`. New instance `79a67ca3`; section container `4a8f9eb5` and heading Component71 instance `5494e63e` remain unchanged. Existing Homepage was already published; its staging edits were saved/published without changing Reading Settings.

Open [Homepage editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=154&action=elementor), select **06 How We Work → Process Steps → process-timeline**. Instance panel has groups Step1–4, each with Number, Title and Description. There are 12 supported overrides (`step_1_number`, `step_1_title`, `step_1_description` through Step4). Do not detach. Use **Edit ROBYLO / Process Timeline** to edit shared structure/styles. Direct component entry: [582](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=582&action=elementor); the in-context Edit Component path was verified working.

| Step | Preserved title | Preserved description |
| --- | --- | --- |
| 01 | Contact | Share the property location and type of restoration need. |
| 02 | Assessment | Placeholder for the approved assessment process. |
| 03 | Restoration | Placeholder for the approved work and coordination process. |
| 04 | Review | Placeholder for the approved completion and review process. |

Feature65 was inspected, not modified. It is a generic feature-summary structure with shared icon/bottom-border rules and content overrides, rather than an independently selectable timeline layout. Its exposed native container schema has no class/layout override. Reworking its shared definition would affect Why GCPRO/Style Guide or need conditional/custom styling. One whole-process component preserves these consumers and encapsulates connector order; no duplicate per-number/per-icon components.

## Technical additions and reuse

All four classes are reusable and editable in the component's Style panel → named Global Class → native layout/size/spacing/position/background/border controls, with responsive device controls. These controls were checked in the actual editor, including 64px circle width/height/min-width. Existing generic grid/feature classes did not supply a connected horizontal-to-vertical process layout.

| New resource | Purpose / specific gap |
| --- | --- |
| Component582 ROBYLO / Process Timeline | Single four-step reusable structure with independent content; Feature65 cannot change layout per instance through exposed overrides. |
| `process-timeline` / `g-a12d836` | Zero-gap four-column native grid; one column at tablet/mobile, necessary for continuous connectors. |
| `process-timeline__step` / `g-07d3365` | Relative-positioned native step; desktop column, tablet/mobile row and controlled step spacing. |
| `process-timeline__number` / `g-e17507d` | Navy/white 64px circle, 56px tablet/mobile, no shrinking; existing process-step-number supplies typography only. |
| `process-timeline__connector` / `g-261ecb6` | Three native decorative divs, 2px existing border-color segments, horizontal desktop/vertical tablet-mobile; no pseudo-elements or code. |

Reused `process-step-number` (Montserrat600, 24/24/22px), `stack`, `stack--compact`, `layout-reset`, existing section/light/container classes, heading Component71 and color/spacing/font Variables. Number class precedes process-step-number in global priority to keep white foreground; relative order of existing classes is preserved. 83→87 Global Classes, 36 unchanged Variables. No new plugins or external dependencies. The subsequent owner-approved hover exception introduces one canonical CSS source file, detailed below; no local styles or Elementor Custom CSS remain.

Desktop circles 64px: connector top31px/left32px, width100% and height2px. Tablet at existing 1024px breakpoint: circles56px, connector left27px/top28px, width2px/height100%; step padding provides spacing. Circle foreground covers segment ends. Last step has no segment and reuses layout-reset. Copy wrapper is necessary to group title/description to the right on mobile. No card backgrounds, borders, shadows, sliders, entrance animations or icon placeholders.

## Simplification and capability findings

The old four Feature instances (`591dc14c`, `4074ad6a`, `7dbe04c2`, `3451936`) were removed from this section only; their obsolete grid--four class was removed from the retained parent. No unrelated shared resources were deleted. Four copy wrappers and three connector divs serve explicit responsive/decorative roles; no extra hover wrappers were added.

The owner's follow-up requires hover on the **whole step**, affecting its circle. Native self-hover/background and native 200ms transition controls exist; exposed state controls do not provide an ancestor-hover→child style binding. A trial box-shadow shorthand converted to class Custom CSS rather than native shadow controls; it was removed by restoring the complete native circle class. Do not treat a successful converter response as proof of native editability. Actual editor now shows an empty Custom CSS field and a native background-color200ms transition row. No new component/class was added for decoration.

## Approved external CSS exception

The owner explicitly authorized minimal parent→child CSS after the native capability check. New canonical source **[theme-overrides/process-timeline.css](../../theme-overrides/process-timeline.css)** is a client-specific block, not a copied shared theme or a newly enqueued stylesheet. It was appended through native WordPress Theme File Editor to **`/wp-content/themes/robylo-starter/assets/css/fallback.css`**. Active theme is **ROBYLO Starter0.2.0**; read-only `functions.php` inspection confirms existing fallback enqueue uses content-MD5 cache versioning. No PHP/enqueue changes were needed. Save success and exact reloaded file text were verified; original rules remain byte-identical except an outdated no-animation comment. Full before file is backed up privately.

Only `.process-timeline__step:hover .process-timeline__number` changes the child: existing `color-primary-hover` Variable plus 1px `color-accent` outline/4px outline offset, gated by `(hover:hover) and (pointer:fine)`. All typography, circle sizes, positioning, colors at rest, layout and 200ms background transition remain in native Global Classes. Outline does not affect box dimensions. `.process-timeline .process-timeline__number` sets transition:none only under prefers-reduced-motion:reduce. No hardcoded brand color, duplicate token, wrapper, pointer cursor or click behavior. No rule targets Feature65 or generic cards. The shared ROBYLO Git repository and other sites were not changed.

Future editing: edit ordinary circle design and duration in the existing native class; edit only ancestor-hover/reduced-motion behavior in the canonical block here, then apply the same block to staging's existing fallback.css through the supported theme editor/deployment process. Retain this client block when updating staging theme files; no automatic deployment/synchronization exists. This exception is explicitly outside Elementor's visual state controls; it does not prevent standard text/layout/override editing. Do not copy it into the shared starter without separate authorization.

## Actual verification

| CSS viewport | Layout | Circle / number | Result |
| --- | --- | --- | --- |
| 1440×900 | Four equal horizontal columns | 64px / Montserrat24 white | Aligned circles and headings, connected line, no overflow |
| 1200×800 | Four equal horizontal columns | 64px / Montserrat24 white | Same; text remains within columns |
| 900×900 | Vertical; copy right | 56px / Montserrat24 white | Continuous vertical segments, readable grouping, no overflow |
| 390×844 | Vertical; copy right | 56px / Montserrat22 white | All four steps in normal scrolling; no clipping/overflow |

Measured connector center offsets were zero; endpoint errors below0.001px (browser subpixel rounding). Actual CSS innerWidth was measured rather than assuming browser outer viewport equals CSS width. Desktop screenshots use a full-width CSS viewport capture; mobile screenshot uses mobile emulation. This is browser responsive QA, not a physical-device touch or screen-reader test.

Native actual instance edit test: Step2 Number02→22 changed only the second canvas circle; restored02 and saved. All12 original override values persisted on independent saved read. Shared class dimensions were visible in normal Size controls. All24 component nodes have empty local style arrays; rendered timeline has zero inline style attributes. Reading order is01→04; section H2 and four H3s preserved. Informational steps have no links/buttons/tabindex, and do not need click/keyboard actions. No performance benchmark is claimed.

Real pointer test over the first description: parent:hover=true while circle:hover=false; circle background became#142862 and outline orange. Circle remains64×64 with transform:none/cursor:auto, no geometry transition. Normal duration0.2s; emulated prefers-reduced-motion produces0s. At390px with touch emulation, hover=false and pointer:fine=false; default full content remains present and hover rule does not apply. No essential information depends on hover. Final four-width layout checks were repeated after the exception. Evidence: [saved checks](../evidence/2026-10-16-process-timeline.json), [responsive geometry](../evidence/2026-10-16-process-timeline/responsive-qa.json), [desktop](../evidence/2026-10-16-process-timeline/desktop-1440.jpg), [whole-step hover](../evidence/2026-10-16-process-timeline/desktop-hover.jpg), [mobile](../evidence/2026-10-16-process-timeline/mobile-390.jpg).

Full saved trees compare equal for the other eight Homepage sections, Feature65, Header113 and Footer114. Affected section/component contain no links; no URLs or link configuration changed. Existing unrelated placeholders and unpublished destinations remain recorded by E10/E12/E14; no new placeholder was introduced. Blog/Portfolio findings and canonical CSV unchanged.

## Outstanding items and recovery

- Visual approval pending. No service-page instances were created to test cross-page reuse; the reusable component/12 content controls are verified on Homepage.
- Private local scoped before snapshots include Homepage, Feature65, Header/Footer and design resources. Restore only the old four process instances/parent classes from that snapshot through supported Elementor controls if rollback is authorized; preserve later unrelated edits. Remove new component/classes only after checking consumers. Full database/files restore was not tested. Documentation Git revert alone does not restore WordPress.
- Hover-only rollback: remove the marked E15 block from staging fallback.css and clear native circle transition if desired. Preserve unrelated fallback rules; source block is version-controlled here, not automatically deployed. Do not remove the reusable timeline to disable its cosmetic hover.
