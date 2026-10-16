# GCPRO decisions

Decisions below are adopted on 2026-10-16 for this documentation system, based on the user's initialization requirements and the inspected shared source. They do not establish historical implementation dates. Append a superseding decision when a material choice changes.

| ID | Status | Decision and reason | Consequence / review trigger |
| --- | --- | --- | --- |
| D001 | Accepted | Keep GCPRO-specific records in gcpro-website and generic theme work in ROBYLO. Client state and installation IDs should not leak into a shared starter. | Link pinned shared source; separately authorize any shared-theme change. |
| D002 | Accepted | Native Elementor owns visual configuration: variables, tag defaults, Global Classes, layouts, Components and overrides. Preserve independent visual editing. | Reuse before adding; no parallel theme design system. Review demonstrated native capability gaps before any code exception. |
| D003 | Accepted | WordPress staging is the current source for saved Elementor state; this repository records evidence and decisions. | Git docs and theme ZIPs are not full backups or portable site packages. Validate export/import and restore separately. |
| D004 | Accepted | Production must never be modified by project agents. Implementation is staging-only and task-scoped. | Verify target before operations; no launch/migration/deployment is implied by a Git push. |
| D005 | Accepted | Codex owns Git/docs; ChatGPT Work owns authorized staging configuration and must update docs after every meaningful milestone. | If Work lacks repository access, completion stays pending until its exact docs handoff is committed and remotely verified. |
| D006 | Accepted | Distinguish verified source, verified staging reads, historical reports and unknowns. | Preserve source/date/scope; never elevate a reported QA claim to a current test or guess missing IDs. |
| D007 | Accepted | Prefer reusable Components and supported instance overrides over duplication/detachment. | Read current schemas and test independence; shared definition changes require consumer checks. |
| D008 | Accepted | Keep customization transparent and minimal. Hidden CSS/JS and undocumented patches conflict with maintainability. | A necessary authorized exception needs a documented capability gap, exact location, effects and rollback; audit existing legacy rules separately. |
| D009 | Accepted | Initialize documentation directly on main as explicitly requested. | This does not establish blanket permission for future direct pushes or WordPress writes; use each future task's scope. |

## Pending decisions

- Accessible CTA treatment for the reported white/orange contrast issue; inspect real states and native options before choosing.
- Approved final photography, reviews, credentials, copy and missing destinations.
- Verified environment/version baseline and supported configuration-transfer/backup workflow.
- Inventory and disposition of existing legacy navigation styling.

No choice has been made for these pending items. Record an accepted follow-up with date, evidence, considered options, consequence and affected documents after it is resolved.
