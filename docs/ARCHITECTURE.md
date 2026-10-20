# GCPRO architecture

## Verified current ownership — E56, 2026-10-20

Active staging theme is **standalone ROBYLO Starter0.2.0**, not Hello Elementor + a child theme. One installed theme;20 active PHP/CSS files read through native Theme File Editor, with no save. Older child-theme observations below describe a historical shared-source revision. functions.php enqueues fallback.css once with content-MD5 versioning and uses public Elementor location/document APIs.

Atomic owns the saved visual tree, classes/tokens and reusable Components. Legacy BEAF/Trustindex shortcodes delegate vendor behavior. The theme contains the documented client timeline block. **Two active Elementor Custom Code entries exist:**590 timeline(body-end10,Page154) and847 CTA video experiment(body-end1,Page154).847 injects content missing from the Atomic tree and retains staging-specific selector/host/media coupling; preserve it as a documented experiment until an approved replacement.

Start from [component maintenance index](components/README.md), [exact code/dependency register](CUSTOM_CODE.md), and [current audit/proposals](audits/2026-10-20-architecture-and-mobile.md). These define ownership without duplicating the historical milestone narratives. Repository mirrors are not separately enqueued, no automatic deployment exists, and required WordPress/plugin/object IDs remain distinct from avoidable authored CSS/JS coupling.

E56 implements only Core B native mobile padding and documentation improvements. Shared class cleanup, semantic scoping/native video replacement and accessibility/product changes remain explicit proposals; no theme/JS/PHP/plugin/global-class refactor was deployed.

E20: Code590 remains Homepage154-only and now includes the color-only `gcpro-process-number` keyframe in existing integrations/process-timeline-mobile.css. Reuses current hover/played triggers and stagger; no JS, theme, global typography or Atomic structure changes. [Source, timing, accessibility and QA](milestones/2026-10-16-timeline-number-color.md).

E18 anonymous-delivery correction: Code590 remains unchanged and Homepage154-only. Stale SiteGround guest HTML was purged; plain-root cache HIT and logged-out browser execution verified. [Incident/limits](milestones/2026-10-16-anonymous-timeline-cache.md).

## Client-only viewport integration — E17

Existing Elementor Pro Custom Code provides a centralized client-owned deployment location without editing ROBYLO: **590**, body-end/priority10, native Page154 display condition. Canonical [CSS](../integrations/process-timeline-mobile.css)/[JS](../integrations/process-timeline-mobile.js) are pasted together into that one documented native code entry; no HTML widget, widget Custom CSS, inline style attribute, PHP hook, extra plugin or forced jQuery. Native scrollIn cannot trigger the existing pseudo-elements, so the explicitly permitted minimal IntersectionObserver sets one runtime data attribute and unobserves after entry. Content/Atomic configuration remains native; this decorative exception is intentionally edited in Code590/source rather than hidden in visual controls.

Desktop theme CSS/keyframes remain byte-identical to E16. Mobile uses the same keyframe and accent token under mutually exclusive touch/reduced-motion media gates. No new framework, theme override or automatic deployment is introduced. [Exact scope/editing/recovery](milestones/2026-10-16-mobile-sequence.md).

E16 refinement,2026-10-16: the same owner-authorized client CSS exception now supplies two one-shot ripple pseudo-elements, rather than a static outline. No DOM/PHP/enqueue/shared-source changes. [E16 scope, editing and rollback](milestones/2026-10-16-process-ripple.md) supersedes only E15's hover treatment below.

## Verified staging theme and scoped exception — E15, 2026-10-16

Native staging Theme File Editor identifies active **ROBYLO Starter0.2.0**, theme directory `robylo-starter`. Read-only functions.php shows existing `robylo-fallback` enqueue for `assets/css/fallback.css`, content-MD5 asset versioning. This is newer verified installed evidence than the historical child-theme source observations below; no PHP was changed.

Owner approved minimal whole-process-step hover CSS because exposed native Atomic states cannot style a child from parent hover. Client source [theme-overrides/process-timeline.css](../theme-overrides/process-timeline.css) is appended to the existing staging fallback stylesheet; it is not separately enqueued and not placed in Elementor Custom CSS. Global Classes still own base design/duration; the exception owns only scoped parent→child hover/outline and reduced-motion override. [E15 editing/recovery](milestones/2026-10-16-process-timeline.md#approved-external-css-exception). Shared ROBYLO repository untouched; this client block must be preserved explicitly in future theme deployments. No deployment automation is established.

Reviewed 2026-10-16. Distinguish the intended ownership model from observed installation state; see [evidence](../PROJECT_CONTEXT.md#evidence-register).

## Ownership and data boundaries

| Layer | Responsibility | Evidence / status |
| --- | --- | --- |
| WordPress staging | Content, media, pages and stored Elementor configuration | E3 confirms page/document inventories on the staging host; versions/configuration not fully audited |
| Elementor Atomic V4 | Visual variables, tag defaults, Global Classes, native layout, reusable Components and instance overrides | Declared stack E1; live resources/component schemas and Homepage structure E3; complete runtime compatibility unverified |
| Elementor Theme Builder | Header/footer and other site parts with display conditions | E3 inventory; assignments in ELEMENTOR_MAP |
| ROBYLO Starter0.2.0 (standalone) | Minimal WordPress fallback/Elementor location integration | E56 native Theme File Editor and20-file read; older Hello+Child source is historical, installed Git revision unverified |
| GCPRO repository | Client-specific handoff, status, design records, IDs, history and decisions | E1 and this documentation milestone |
| Shared ROBYLO repository | Reusable theme source and general integration guidance | E2; separate ownership, not a location for GCPRO content or IDs |

Configuration flow: WordPress stores the content and Elementor configuration; Elementor renders its visual documents using that configuration; the shared theme supplies minimal WordPress integration. GCPRO documentation records evidence and decisions. Git documentation is not a backup of WordPress.

## Shared source facts

At [ROBYLO commit 8e1397a](https://github.com/vvvetalll/robylo-website-starter/tree/8e1397aab99ab5965c10a251cf144ea3ba3a0372), `theme/robylo-child/style.css` declares ROBYLO Child version 0.1.0 with parent `hello-elementor` and contains metadata only.

`functions.php` guards ABSPATH and enqueues the child stylesheet via `robylo_enqueue_styles` at `wp_enqueue_scripts` priority 20. It uses the theme version for cache versioning and adds `hello-elementor-theme-style` as a dependency only if that handle is already enqueued. The inspected tree includes no JavaScript or template override files. These are source observations, not a test of the installed theme or an assertion that staging has no customizations.

Do not copy this implementation into GCPRO or change the shared source for client-specific styling. Refer integration gaps to separately authorized ROBYLO work.

## Visual architecture

Use Global Variables for reusable values, tag defaults for base typography, Global Classes for shared style/layout roles, Components for reusable structures, and supported overrides for instance content. Local exceptions require a clear purpose and documentation. Do not replace these layers with a hidden theme stylesheet or script.

Component IDs, document IDs, element IDs and variable/class IDs have different scopes. They are installation-specific; the map is a locator, not a portable deployment manifest. A ROBYLO-prefixed component name on GCPRO staging does not mean that component is shipped in the ROBYLO Git repository.

Header and Footer are separate Theme Builder documents, not sections owned by Homepage 154. Inspect them separately and account for shared effects before editing.

## Runtime and transfer limits

The initial GCPRO baseline had no application code. E15/E16 added a narrowly authorized theme CSS exception; E17 adds two client integration sources deployed through native Custom Code590. There is still no dependency manifest, local WordPress runtime, CI or automatic deployment configuration. Do not invent build/test commands for it.

A theme ZIP does not include Elementor variables, classes, defaults, Components, templates, content, media, or database state. A supported export/import workflow and a restore test must be verified independently before treating a configuration as portable. No synchronization or deployment automation is established here.

Record installed versions, active child/parent themes, deployed theme revision, license/Atomic settings and connector capabilities before the next implementation milestone. No production editing is allowed.
