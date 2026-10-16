# E19 — Core Restoration Services cards

2026-10-16. Staging Homepage154, section38ed6da4, grid5a3d7f5d. No production, Header, Footer, timeline590/theme or URL changes.

## Implementation

Recomposed the section visually as six separated service cards, retaining all existing services, descriptions, SVG assets, CTA labels/destinations and component instances. Removed only `grid--flush` from the grid, reusing `grid-3`: three columns desktop, two at tablet1024px, one at mobile767px. Gaps24px desktop/tablet and16px mobile. Existing section/container/heading typography remain.

Updated existing **ROBYLO / Service Card62**, UID unchanged. Still five nodes: article → SVG, H3, paragraph, CTA. No wrappers, new component or detachment. Shared refinement also appears in the two existing Style Guide50 examples. Existing five Override keys remain `icon`, `title`, `description`, `cta_text`, `cta_link`.

The article uses existing `service-card`: surface token,1px border token,16px corners,32px desktop/tablet padding and24px mobile padding, column layout/gap16px and100% available row height. Auto top margin on CTA aligns actions at the bottom; no fixed card height. Whole-card hover changes surface to white and border to navy without movement/layout shift. Chose the compact outline CTA rather than adding arrows/extra SVG nodes. CTA is Montserrat600/14px, minimum44px height,8px corners; navy hover/focus with white text and existing native link focus outline. No orange conversions compete with service discovery.

## Native resources and editing

| Resource | Change/purpose | Why needed; where edited |
| --- | --- | --- |
| `service-card` g-f569734 | Existing class updated, no duplicate | Native Class styles on component article. Removed old bottom-only divider/custom declaration in favor of native full border. |
| `service-card__icon` g-b759e84 | **New reusable Global Class**:56px badge,12px padding,14px corners, light-blue token | Existing `icon-svg` supplies SVG color/behavior but has no badge. Apply together on existing SVG4a4396ac; badge modifier precedes base in class priority. Native Elementor Style tab/Classes. |
| `service-card__action` g-d0416c8 | **New reusable Global Class**: compact outline action, bottom alignment, normal/hover/focus | Existing text-link is underlined; global CTA button variants are larger/louder. Do not alter shared conversion styles. Applied to existing CTA210ecf0d instead of text-link. Native Elementor Style tab/Classes. |

Reuse: `grid-3`, section/container/stack, `icon-svg`, existing Montserrat/Inter HTML Defaults and color/spacing/font Variables. New class count87→89; Variables36 unchanged. No new Atomic Components, executable files, custom CSS/JS/PHP, plugins or dependencies. Submitted class declarations were converted to native Atomic style properties; final three changed classes have `custom_css:null` in every variant. A converter fallback was removed before delivery by using native focus instead of focus-visible style overrides and omitting unnecessary text-align. Existing global icon-svg custom rules/native SVG inline sizing predate this task and were preserved, not introduced as a workaround.

Open [Homepage editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=154&action=elementor), select any service instance to edit its five independent fields; click Edit ROBYLO / Service Card to change shared structure/classes. [Component editor62](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=62&action=elementor). Saved edits were staged by manage-elements and promoted using native publish-document, not left as autosaves. No shared ROBYLO source changes.

## Verification and complexity audit

- Authenticated and actual logged-out Chrome at1440/1200/900/390:3/3/2/1 columns, six cards, equal heights within each row,56px badges, no horizontal overflow. Final guest read verifies CTA Montserrat600.
- Actual whole-card description hover gives white surface/navy border and stationary geometry. Keyboard Tab reaches a service CTA, native focus-visible outline plus navy/white colors; action remains visually secondary. No animation or motion dependency introduced.
- Homepage editor opened and existing Water instance selected: SVG picker, title, description, link label/destination exposed; component stays attached, Publish disabled. Independent values and all Override keys persist. No new temporary edit-independence experiment was necessary for class-only changes.
- Style Guide50 desktop1440/mobile390: two independently retained water/flame SVG examples and their distinct titles/anchor destinations render with new shared treatment, no overflow. No Style Guide content was edited.
- Fresh saved Homepage tree equals baseline except removal of grid--flush. Component62 tree equals baseline except the two class assignments. All five component nodes retain empty local styles; all six Homepage instance content/link values unchanged. Header/Footer/unrelated sections were not written.
- Native SiteGround staging cache purge performed. Plain anonymous root MISS then HIT carries six badge/action classes. Logged-out browser shows current treatment; captured guest console has no warnings/errors. No optimization/security settings changed.

[QA measurements](../evidence/2026-10-16-service-cards/qa.json), [native class data](../evidence/2026-10-16-service-cards/native-classes.json), [HTTP evidence](../evidence/2026-10-16-service-cards/http.json), [desktop](../evidence/2026-10-16-service-cards/anonymous-1440.jpg), [mobile](../evidence/2026-10-16-service-cards/anonymous-390.jpg).

No new DOM nodes or duplicate components/classes. Base service class reused; only the two specific reusable style roles were missing. No shadow framework, animation library or code deployment. Existing service CTA text and destinations are preserved; hover does not turn the whole article into a clickable link.

## Link register and outstanding checks

Homepage instances28d9f7c (Water),7ce1a666 (Fire),4ac87e43 (Mold),95336d4 (Reconstruction),318ea723 (Storm),22d372d7 (Personal Property) all retain approved unresolved `cta_link.destination:#`. Intended service pages remain Draft in the canonical SEO inventory; no Draft/preview routes were exposed, no production URLs or unrelated targets substituted. Connect through native object linking when authorized destinations become publicly available. Style Guide links remain genuine existing `#robylo-content` anchors. No hardcoded internal domain URLs were added.

Visual approval pending. Responsive testing used desktop browser emulation, not a physical phone. An actual logged-out normal Chrome profile was tested; a controlled incognito session was not available through the connected surfaces, so the permanent incognito acceptance check remains pending. No claim of an incognito or physical-device test. No screen-reader/performance benchmark run.

## Recovery

Scoped pre-change Homepage/component/class snapshots are stored outside Git in local outputs/recovery/service-cards-before.json and service-card-classes-before.txt. These are configuration recovery snapshots, not a tested full-site backup. Reapply original class assignments, grid--flush and original service-card rules through native controls to reverse. Remove the two new classes only after detaching them and checking consumers. Git does not automatically deploy or reverse Elementor settings.
