# GCPRO workflows

These are required procedures for future authorized work, not claims that a backup, test or deployment has already happened. Follow [AGENTS](../AGENTS.md) and [current context](../PROJECT_CONTEXT.md).

## Begin a task

1. Read AGENTS, PROJECT_CONTEXT, CHANGELOG, DECISIONS and the references for the affected area.
2. Inspect Git branch, remote and status; preserve unrelated work. Confirm the repository is `vvvetalll/gcpro-website`. Use the task's authorized branch; initialization explicitly targets main. Never force-push.
3. Establish scope and owner: Codex for repository work; ChatGPT Work for authorized staging Elementor work.
4. Before any site operation verify the connection/returned URLs target `vitaliiv1.sg-host.com`. Never modify production. An earlier chat instruction does not authorize new implementation.
5. Read current documents, global resources, component schemas, consumers and Theme Builder conditions. Record versions and gaps; do not infer a feature from a tool name.

## Back up before authorized implementation

1. Confirm a recoverable staging backup of database and files, including uploads, themes, plugins and configuration. Record timestamp with timezone, scope, secure storage reference, backup mechanism and restore owner without exposing secrets.
2. Capture affected document/configuration snapshots and component override schemas, plus baseline screenshots and relevant checks. These complement a full backup.
3. For global changes include active kit variables, tag defaults, Global Classes and ordering; for Components include definitions and affected consumers; for site parts include publish states and display conditions.
4. Verify that a restore is possible using an isolated target or a documented validated restore procedure. If recovery is unverified, state the blocker before risky writes; do not label a successful export a tested backup.
5. Keep private archives, database dumps and credentials outside Git. Only commit reviewed, sanitized evidence when appropriate.

No backup or restore procedure was executed during documentation initialization.

## Edit through Elementor

1. Reuse native controls and existing global values/classes. Use a Component for a reusable structure and supported overrides for individual content. Discover actual permissions and schemas first.
2. Make the smallest scoped change. Record affected page/component/element IDs and whether a change affects all instances.
3. Use fresh saved structure; do not send stale trees after composition or another writer's changes. Keep writes sequential for a document and read back after each meaningful save.
4. Inspect warnings and saved results. Confirm draft/publish/autosave state explicitly; saving and publishing can differ. Publish staging documents only when the task authorizes it.
5. Check the actual editor: change text, image/SVG, link, spacing, color and responsive controls as relevant; confirm supported overrides without detaching. Revert temporary test edits.
6. Check the frontend, responsive layout, keyboard/focus, links and shared consumers. Test instance independence where overrides change. Record actual viewport sizes/results and untested cases.
7. Record any existing/custom code touched, exact location, native capability gap and recovery. Prefer a simpler native design if the effect otherwise requires fragile code.

## Native-first addition gate

Before creating any Global Class, Global Variable, Atomic Component, code file, plugin or external dependency:

1. Inspect the existing system and the supported native Elementor Atomic V4 controls/Overrides for the actual requirement.
2. Reuse an appropriate existing resource when it reasonably satisfies that requirement.
3. If an addition is necessary, record the specific present gap, purpose, reuse scope and editor/source location. Do not add a speculative abstraction or reusable class merely for possible future use.
4. Keep significant design settings discoverable and visually editable in Elementor. Do not hide behavior or styling in undocumented code. Custom code remains subject to the existing capability-gap, scope and documentation rules in AGENTS.

## Pre-completion complexity audit

Every meaningful implementation, including a minor fix, requires this review before completion:

- Duplicate or redundant Global Classes and Variables.
- Unnecessary Components or abstractions.
- Excessive DOM nesting.
- Hidden styling or hard-to-find design controls.
- Unnecessary custom CSS, JavaScript or PHP.
- Additional plugins or external dependencies.

Inspect actual saved configuration and affected consumers, not only intended tool inputs. Remove unjustified complexity introduced by the task within authorized scope, preserve unrelated/shared resources, and recheck affected rendering and functionality after simplification. If an existing shared issue cannot be safely removed in scope, report it under Outstanding Items. State what was simplified, or give the concrete reason retained additions are necessary. "Reusable someday" is not a justification.

## Milestone documentation — mandatory for ChatGPT Work

After **every meaningful implementation milestone**, update the relevant documentation, commit it, push it and verify the remote branch before marking completion. This is the user's standing GCPRO workflow instruction, confirmed on 2026-10-16. A meaningful milestone includes delivered page sections, reusable component changes, global styling, navigation/templates, integrations or material fixes. The current authorized agent can complete this directly with verified access; a Codex handoff is needed only when access is unavailable.

| Change | Required documentation |
| --- | --- |
| Any meaningful implementation | PROJECT_CONTEXT current status/next work and CHANGELOG actual delivered change, evidence and checks |
| Page/component/template ID, name, overrides, conditions or status | ELEMENTOR_MAP |
| Variables, tag defaults, classes, ordering, responsive conventions | DESIGN_SYSTEM |
| Layer ownership, integration, runtime or portability | ARCHITECTURE |
| Significant tradeoff, exception, replacement or reversal | DECISIONS |
| Editing/backup/handoff procedure changes | WORKFLOWS; AGENTS only for permanent rules |

If repository tools are unavailable to Work, Work must supply exact replacement text or a patch and supporting evidence to Codex, naming the exact access restriction. The handoff remains **documentation synchronization pending** until the repository update is committed, pushed and verified remotely. Chat-only notes are insufficient. Documentation synchronization does not authorize extra website work or changes to the shared ROBYLO repository.

Keep facts and reported outcomes separate. Record date/timezone, source, environment, versions, actual IDs, checks and their limits. Reconcile superseded claims rather than silently preserving contradictions.

## Documentation verification and Git delivery

1. Read all changed/new files. Check consistency, spelling of IDs/names, relative Markdown targets and evidence labels. Confirm no secrets, private data or invented implementation claims.
2. Inspect Git status, full diff (including new files), changed paths and `git diff --check`. Documentation-only changes require no WordPress mutations or synthetic application tests.
3. Stage only intended paths. Commit with a concrete documentation message.
4. Recheck remote main before an authorized direct push; if it moved, fetch and review/reconcile the changes. Never overwrite remote work. Use a normal fast-forward push.
5. Confirm the target remote branch SHA equals the delivered commit and inspect its tree/diff. Report the canonical commit URL and push result. Keep local/push/remote verification outcomes distinct.

## Mandatory final implementation report

Permanent standard for every GCPRO AI agent, effective 2026-10-16. End every meaningful implementation task/milestone with the following exact six headings, in order. Keep them concise; minor changes can use one sentence per heading. Never omit a new technical element or custom code to shorten the report. Apply automatically without a reminder.

### Implementation Summary

State what changed and where: page/section/Component names, actual WordPress/Elementor IDs, and resulting functionality or design. Identify staging, authorized scope, saved/published state and shared-consumer effects where relevant. Include date/timezone and evidence/recovery reference when material.

### Technical Changes

Describe native Elementor controls used; existing Global Classes, Variables, Atomic Components and supported Overrides reused; and any Component structure change. Explicitly identify custom CSS, JavaScript or PHP introduced or changed, including modifications to an existing code file.

List **every** newly created Global Class, Global Variable, Atomic Component, custom code file, plugin and external dependency individually in the user-facing report. Do not replace the inventory with a count or documentation link alone. Use this compact row format when useful:

| Addition (type, name/ID or exact file path) | Purpose | Why existing functionality was insufficient | Reusable? / actual consumers | Edit location |
| --- | --- | --- | --- | --- |
| One row for each actual addition | Current requirement solved | Specific native/existing resource gap | Yes/no and current scope | Exact Elementor control/class/Component or source file |

Do not include an example row as an actual delivered addition. For custom code, also state why native controls could not reasonably satisfy the requirement. Identify plugin/dependency versions when verified and distinguish an installed dependency from one merely proposed.

When applicable, explicitly state **"No new classes, components or custom code"**. Separately list any new Variables, plugins or external dependencies, or state none; the required phrase does not substitute for those categories. Links may supply deeper evidence or editing instructions, but must not hide the inventory.

### Complexity Audit

Report the pre-completion review of duplicate/redundant classes, unnecessary Components, excessive DOM nesting, hidden styling, unnecessary code and added dependencies. State what was removed/simplified and reverified, or why the retained additions are needed. Do not introduce speculative abstractions or treat an unreviewed implementation as audited.

### Verification

Report actual desktop and mobile checks, viewport sizes and results, functional behavior tested, Elementor visual editability and responsive issues. Include relevant keyboard/accessibility and performance concerns, evidence references, and material backup/restore limitations. Clearly label verified facts, assumptions, tests not run and unresolved issues. Do not invent a performance benchmark, touch test or successful interaction.

For documentation-only tasks, website/editor/runtime verification is not applicable: verify document content, requirement coverage, links, diff/whitespace, intended file set and Git delivery instead. Do not modify WordPress or perform unrelated runtime tests just to fill this section.

### GitHub

List documentation files updated, the canonical commit URL, target branch, push result and verified remote branch/commit. A local commit is insufficient. If blocked, identify the exact access/protection/failure and leave synchronization explicitly pending.

### Outstanding Items

List anything incomplete, unverified, dependent on external materials, or requiring owner approval, including known technical limitations and remaining documentation issues. State none when there are no outstanding items. This section does not authorize additional work.

Do not call the milestone complete while required documentation delivery is pending. Preserve the native-first and production boundaries; the report itself does not authorize deployment or website changes.

## Recovery

For a failed staging change, stop further writes, preserve evidence and restore the affected configuration from the verified backup using the authorized staging recovery process. Include dependent Components/classes/templates and media as needed. Recheck frontend, editor, consumers and conditions. Document what was restored and remaining issues. A Git revert of documentation cannot restore WordPress; a theme rollback alone cannot restore Elementor state.
