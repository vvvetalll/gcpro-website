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

## Milestone documentation — mandatory for ChatGPT Work

After **every meaningful implementation milestone**, ChatGPT Work must update documentation before marking completion. A meaningful milestone includes delivered page sections, reusable component changes, global styling, navigation/templates, integrations or material fixes.

| Change | Required documentation |
| --- | --- |
| Any meaningful implementation | PROJECT_CONTEXT current status/next work and CHANGELOG actual delivered change, evidence and checks |
| Page/component/template ID, name, overrides, conditions or status | ELEMENTOR_MAP |
| Variables, tag defaults, classes, ordering, responsive conventions | DESIGN_SYSTEM |
| Layer ownership, integration, runtime or portability | ARCHITECTURE |
| Significant tradeoff, exception, replacement or reversal | DECISIONS |
| Editing/backup/handoff procedure changes | WORKFLOWS; AGENTS only for permanent rules |

If repository tools are unavailable to Work, Work must supply exact replacement text or a patch and supporting evidence to Codex. The handoff remains **documentation synchronization pending** until the repository update is committed and verified remotely. Chat-only notes are insufficient.

Keep facts and reported outcomes separate. Record date/timezone, source, environment, versions, actual IDs, checks and their limits. Reconcile superseded claims rather than silently preserving contradictions.

## Documentation verification and Git delivery

1. Read all changed/new files. Check consistency, spelling of IDs/names, relative Markdown targets and evidence labels. Confirm no secrets, private data or invented implementation claims.
2. Inspect Git status, full diff (including new files), changed paths and `git diff --check`. Documentation-only changes require no WordPress mutations or synthetic application tests.
3. Stage only intended paths. Commit with a concrete documentation message.
4. Recheck remote main before an authorized direct push; if it moved, fetch and review/reconcile the changes. Never overwrite remote work. Use a normal fast-forward push.
5. Confirm the target remote branch SHA equals the delivered commit and inspect its tree/diff. Report the canonical commit URL and push result. Keep local/push/remote verification outcomes distinct.

## Handoff receipt

Provide this at milestone completion:

- Date/timezone, authorized scope and staging host; implementation owner.
- Actual changed pages/components/templates/classes/variables and repository files.
- Before/after behavior, instance/shared effects and saved/published state.
- Evidence references, versions, checks run with outcomes, and checks not run.
- Backup reference, restore readiness and rollback scope.
- Any custom code: exact source, purpose and reason native controls were insufficient; or explicitly no new code for that milestone.
- Documentation commit URL, target branch and verified push status.
- Remaining placeholders, dependencies, approvals and the next authorized action.

Do not call the work complete while its required documentation is pending. Do not deploy or alter production.

## Recovery

For a failed staging change, stop further writes, preserve evidence and restore the affected configuration from the verified backup using the authorized staging recovery process. Include dependent Components/classes/templates and media as needed. Recheck frontend, editor, consumers and conditions. Document what was restored and remaining issues. A Git revert of documentation cannot restore WordPress; a theme rollback alone cannot restore Elementor state.
