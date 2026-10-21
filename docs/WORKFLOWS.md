# GCPRO workflows

**E67 footer link follow-up:** All six corresponding service destinations remain Draft; do not add placeholders or publish pages to supply footer links. Exact candidate object IDs/statuses and native-link activation procedure are in the [responsive footer record](audits/2026-10-20-footer-responsive.md#service-navigation-and-preserved-destinations). Existing footer contact/social/Maps/#top URLs are unchanged.

## Phase 1 maintenance note — E57

Follow [the exact owner/rollback record](audits/2026-10-20-phase1-cleanup.md). BEAF is outside this refactor: preserve its numeric isolation selectors and integration. For class CSS cleanup, edit only the native selected class/breakpoint Custom CSS body (the editor supplies element.style braces), allow the edit to settle, save, and independently reload/read back before declaring success. Never replace complete variants from partial resources. Code847 has a repository-only source mirror; Git does not deploy it. Validation50 must remain Draft; use Save Draft when editing shared class styles from that page.

These are required procedures for future authorized work, not claims that a backup, test or deployment has already happened. Follow [AGENTS](../AGENTS.md) and [current context](../PROJECT_CONTEXT.md).

## Begin a task

Component work additionally starts with [docs/components](components/README.md) and [CUSTOM_CODE](CUSTOM_CODE.md). Update the affected component record and code-owner entry after each meaningful change. IDs locate saved objects; justify any authored ID-dependent selector separately. Follow the durable inventory/evidence rules in [AGENTS](../AGENTS.md#durable-component-maintenance-and-audit-rules).

1. Read AGENTS, PROJECT_CONTEXT, CHANGELOG, DECISIONS and the references for the affected area.
2. Inspect Git branch, remote and status; preserve unrelated work. Confirm the repository is `vvvetalll/gcpro-website`. Use the task's authorized branch; initialization explicitly targets main. Never force-push.
3. Establish scope and owner: Codex for repository work; ChatGPT Work for authorized staging Elementor work.
4. Before any site operation verify the connection/returned URLs target `vitaliiv1.sg-host.com`. Never modify production. An earlier chat instruction does not authorize new implementation.
5. Read current documents, global resources, component schemas, consumers and Theme Builder conditions. Record versions and gaps; do not infer a feature from a tool name.

## Native Draft Page hierarchy — E14

WordPress supports `slug`, `parent` and `status` through its native [Pages REST API](https://developer.wordpress.org/rest-api/reference/pages/). Quick Edit/Gutenberg search restrictions and the limited Elementor create-page schema do not establish that WordPress disallows Draft parents.

For separately authorized Page-skeleton work, E14 verified that the **existing configured same-host Basic authorization** also works with standard staging WordPress REST. Verify the target HTTPS host, a read-only authenticated Draft GET, native OPTIONS schema and required current-user capability first. Keep credentials in their existing secure configuration; never print/commit credentials or copy authentication into evidence, never extract browser runtime/session secrets, and refuse cross-host redirects. An authenticated browser page, public REST schema or installed tool alone is not proof of API write access. Do not create new credentials or change security settings as a workaround.

Before creating anything, read all relevant Page statuses including Drafts/trash, reconcile exact canonical paths/source decisions, verify actual Draft parent IDs and detect collisions. Capture scoped recovery snapshots and an operation record without secrets. Create one approved child with native `POST /wp-json/wp/v2/pages`, exact approved title/slug/parent, `status=draft` and empty content. Independently GET it and verify Draft parent/full path before proceeding in controlled batches. Never blindly retry a timed-out POST; resolve its outcome by re-reading first. Do not invent flat substitutes or publish parents.

Verify saved slugs and full parent chains, plus native `permalink_template` filled using the **saved slug**. Draft `generated_slug` is a title-derived suggestion and can differ from the approved saved slug; never overwrite the approved URL with it. Re-read the complete final Page set, detect duplicates/suffixes, verify unchanged prior objects/settings/layouts and noindex, and update only actual IDs/statuses in the canonical CSV. A verified intended Draft path is not a tested anonymous public route; keep navigation unresolved until authorized publication and actual route testing.

This workflow introduces no website code/plugin and does not authorize internal page design, archive/CPT registration, production writes or copying historical PHP. Preserve E13's Blog/Portfolio findings and unresolved archive-phase questions. Keep a dated sanitized evidence summary and complete the normal documentation/commit/push/remote-verification gate.

## Back up before authorized implementation

1. Confirm a recoverable staging backup of database and files, including uploads, themes, plugins and configuration. Record timestamp with timezone, scope, secure storage reference, backup mechanism and restore owner without exposing secrets.
2. Capture affected document/configuration snapshots and component override schemas, plus baseline screenshots and relevant checks. These complement a full backup.
3. For global changes include active kit variables, tag defaults, Global Classes and ordering; for Components include definitions and affected consumers; for site parts include publish states and display conditions.
4. Verify that a restore is possible using an isolated target or a documented validated restore procedure. If recovery is unverified, state the blocker before risky writes; do not label a successful export a tested backup.
5. Keep private archives, database dumps and credentials outside Git. Only commit reviewed, sanitized evidence when appropriate.

No backup or restore procedure was executed during documentation initialization.

## Edit through Elementor

### Native Atomic SVG imports — E23

Use existing instance → **SVG Icon → Upload SVG → native Media modal → Select Files** for reviewed static SVG assets. E23 verified this imports the approved six navy/orange files even though ordinary WordPress Media → Add Media File rejects the same SVG type. Do not interpret that generic rejection alone as absence of native SVG support. Do not enable unrestricted uploads, add importer PHP/plugins or change security settings. Validate source as safe static vector geometry first, then read back attachment IDs and actual rendered colors; use supported per-instance SVG Overrides and verify independence. Native upload acceptance does not excuse source review or establish separate duotone color-picker support. [Exact observations/IDs/QA](milestones/2026-10-16-icon-b-integration.md).

### Anonymous delivery verification — E18

After meaningful Elementor, Custom Code, CSS or JavaScript changes:

1. Assess whether SiteGround cache invalidation is required. Before diagnosing a frontend feature as broken, compare authenticated and anonymous HTML/assets, source markers and cache HIT/MISS responses for stale guest content.
2. Purge the relevant staging cache when necessary using existing SiteGround controls. Preserve optimization/security settings; do not disable caching as a workaround or purge production.
3. Test the actual frontend at its ordinary public URL as an **anonymous visitor in an incognito browser session after cache clearing**. Confirm current assets and actual behavior, including the subsequent cache HIT where available. A cache-busting query, logged-in page or authenticated Elementor preview alone cannot establish that a feature works for all visitors.
4. Record responsive viewport sizes and distinguish desktop mobile emulation from a physical-device test. State unavailable/unperformed checks explicitly; label owner-reported device confirmation separately from agent testing. For the timeline, verify entry, ordered fade/completion, no replay, reduced motion and preserved desktop hover.

[E18 cache incident](milestones/2026-10-16-anonymous-timeline-cache.md): stale guest HTML omitted Code590; cache purge alone restored it. On 2026-10-16 the owner confirmed the animation works on a physical Samsung Galaxy S25 Ultra, Chrome Android. No CSS/JS changes were required.

### Authorized client Custom Code exception — E17

For the specifically authorized mobile process sequence, use existing native **Elementor → Editor → Custom Elements → Code**, entry590. Keep the client CSS/JS canonical in `integrations/process-timeline-mobile.css` and `.js`; combine them in one `<style id="gcpro-process-mobile-style">` and one `<script id="gcpro-process-mobile-sequence">` block in that existing entry. Location body-end, priority10, native condition Include → Singular → Pages → existing Homepage154; leave Always load jQuery unchecked. Do not create another entry or put code in page widgets/Custom CSS/theme PHP. This is a narrow documented exception, not blanket permission for future snippets. E20 extends this same CSS block with the synchronized desktop/mobile number-color track; keep its1160ms envelope and400ms step offsets aligned to the existing ring pair. No second code entry or observer is needed.

After source edits, update590 through standard controls, reload/read its `code` field and verify exact source plus condition/location. Test actual frontend on coarse-touch390/430 from the page top: waiting below timeline, entry, staggered fade, leave/re-entry, reduced motion and desktop hover; verify unaffected page does not load the entry. Native content/layout controls remain in Component582, while integration timing/threshold/media gates are explicitly in these files. Git does not deploy the entry automatically. Set590 to Draft to disable only the mobile addition; desktop E16 theme CSS remains intact. See [E17](milestones/2026-10-16-mobile-sequence.md) for evidence and limits.

1. Reuse native controls and existing global values/classes. Use a Component for a reusable structure and supported overrides for individual content. Discover actual permissions and schemas first.
2. Make the smallest scoped change. Record affected page/component/element IDs and whether a change affects all instances.
3. Use fresh saved structure; do not send stale trees after composition or another writer's changes. Keep writes sequential for a document and read back after each meaningful save.
4. Inspect warnings and saved results. Confirm draft/publish/autosave state explicitly; saving and publishing can differ. Publish staging documents only when the task authorizes it.
5. Check the actual editor: change text, image/SVG, link, spacing, color and responsive controls as relevant; confirm supported overrides without detaching. Revert temporary test edits.
6. Check the frontend, responsive layout, keyboard/focus, links and shared consumers. Test instance independence where overrides change. Record actual viewport sizes/results and untested cases.
7. Record any existing/custom code touched, exact location, native capability gap and recovery. Prefer a simpler native design if the effect otherwise requires fragile code.

## Native internal linking and URL integrity

Permanent owner rule, effective 2026-10-16. Applies to all GCPRO internal links, including Homepage 154, Header 113, Footer 114, navigation and reusable Component instances. See [AGENTS](../AGENTS.md#mandatory-native-internal-linking-and-url-integrity).

### Choose the destination

1. Find the **existing intended WordPress object** and verify ID, type, title, approved path, publication status and actual accessibility. Do not create a duplicate/placeholder page just to link somewhere. Preserve approved production paths; do not rename a slug to simplify link configuration.
2. In Elementor use **Dynamic Tags → Internal URL**, choose the supported content type and select the actual page/post. An equivalent native object selector is also preferred over typed URLs. Select an object, not merely a URL search suggestion that saves a string. For site-root branding, a supported native Site URL/home binding is appropriate; document which method is used.
3. In WordPress Navigation add the destination from Pages/posts or another supported object source, rather than Custom Links. Inspect its object/type in the menu editor and verify the associated destination; a frontend `href` is insufficient to identify the saved menu-item type.
4. For Components use the existing exposed destination Override. Do not edit the shared definition to assign one instance's page; do not detach or create a duplicate variant. For nested CTA 80 use its Primary Link / Secondary Link overrides rather than changing shared button defaults.
5. A draft/private/preview route is not a public destination merely because an authenticated editor can open it. Record the pending object without presenting its draft URL in public navigation. Activate and test when the destination is published and approved. Never publish a page merely to satisfy this check.
6. Missing destinations remain unresolved. Preserve only explicitly approved temporary placeholders, including existing `#` where permitted; identify them as intentional/pending, not successful links. Do not silently substitute production, an unrelated section or a guessed slug. Treat an accidental `#` as a defect. Use native anchor controls for intentional fragments and verify their target IDs separately.
7. External sites, `mailto:` and `tel:` use ordinary URL fields. They are excluded from object-link conversion but still require correct scheme/destination verification.

### Atomic V4 method verified on this installation — E11

Read-only MCP schema/resource checks on staging `vitaliiv1.sg-host.com`, 2026-10-16. Host was confirmed by the Homepage inventory before reading schemas. Sources: discovered `elementor://dynamic-tags`, `get-widget-schema(e-button)` after widget discovery, and discovered Component schemas for 53/62/80/103. These checks establish the installed **supported data contract**, not an end-to-end dynamic-link save/render/migration test.

| Location | Verified native contract / edit method |
| --- | --- |
| Atomic Button | `link.destination` accepts a string, an object selector with numeric `id` and optional `label`, or a dynamic tag binding. Prefer the object/dynamic choices for internal pages. |
| Internal URL tag | Registered URL tag name `internal-url`; settings include `type` and object selectors `post_id`, `taxonomy_id`, `attachment_id`, `author_id`. Each selector requires numeric `id`; `label` is optional. For a page/post, select the object through the native Internal URL controls (`post_id`). The returned schema does not enumerate `type` values: read the actual controls/current schema; do not invent a literal. |
| Primary CTA 53 / Outline White 103 | Existing `link` Override exposes the same destination union, including `internal-url`. Native instance panel: Button destination → dynamic tag or object selector. |
| Service Card 62 | Existing `cta_link` Override (Link Destination) supports that same link schema. Keep each service instance independently selectable. |
| CTA Section 80 | Existing `cta_link` and `secondary_link` Overrides (Primary Link / Secondary Link) support the same link schema through nested Components. Preserve both exposed fields. |
| Connector editing | Current Component tool metadata documents instance updates via `manage-elements` with `settings.overrides`, deep-merging override keys and clearing a key with null. Read the current Component schema first and send plain values matching it. Native `get-page-structure` output includes typed `$$type` envelopes; do not blindly replay those as plain API inputs. Use the visual editor if a control is not safely exposed by the connector. |

Limitations and evidence boundaries:

- `e-component` is not a widget type returned by widget-schema discovery; a direct widget schema lookup returned unknown type in the preceding milestone. Obtain destination schemas from `list-components(component_ids)` after Component discovery. This is a discovery/API distinction, not proof that native Component links are unsupported.
- Current E10 tests proved independent **static** label/link override editing and saved output in the named Hero/Final instances. Fresh E11 Hero read still shows Call `tel:+18476563322` and Request Service `#`. **Dynamic object-bound Component save/render independence has not yet been exercised.** Do not relabel static-link tests as dynamic-link tests.
- Before relying on dynamic overrides in an authorized implementation, use two existing approved destination objects, save/reopen two instances, verify each stored object and actual frontend destination, then change one instance and confirm the other's saved binding/rendered link is unchanged. Use native controls and restore any temporary test values. Do not create test pages or publish drafts for this purpose. Record exact fields, instance/object IDs, outcomes and any blocker.
- An absolute frontend `href` is normal output from a native binding. Audit saved configuration to distinguish an object reference from a hardcoded URL. Conversely, a relative path or a dynamic field containing a typed URL is not evidence of a WordPress object relationship.
- IDs are installation-specific. Export/import or a different migration process may require remapping/reselection; a supported schema is not a guarantee of portable IDs or working production URLs. Post-migration verification remains mandatory.
- No WordPress/Elementor writes, temporary test binding, page creation or migration occurred during this documentation task. No existing link was converted by merely adopting this rule.

### Milestone link verification gate

After every implementation milestone, inspect affected pages, Header/Footer/navigation where relevant, and consumers of changed shared Components:

- Check stored target object identity/type/status and the resolved frontend URL against the intended approved destination. Verify public accessibility in an anonymous session where appropriate; distinguish an authenticated-only success, 404, redirect loop, unrelated-page redirect and unresolved target.
- Identify manually entered internal URLs, including both staging/production hostnames and relative paths. Inspect Component origins/instance overrides and WordPress menu-item types, not just rendered HTML. Recognize supported native home/site/anchor bindings.
- Detect broken targets and accidental `#`/empty links; distinguish intentionally approved pending placeholders and genuine fragment targets. Record unresolved items instead of claiming an all-links pass.
- Verify Component link controls remain editable without detaching and changing one instance does not affect another. For dynamic bindings, read back the object reference after save/reopen and test the actual rendered destination. State which controls/tests were not available or not run.
- Update the relevant page/milestone link register, PROJECT_CONTEXT and CHANGELOG with exceptions/pending routes and test scope. Keep a single canonical register for each affected scope; do not copy the same unresolved list into multiple new files. Include results/limits in the mandatory final report and commit/push/remote verification gate.

Record each exception/unresolved target with: **source page/template and element or menu item ID; Component/instance and override key if applicable; intended object/type/approved path; actual saved linking method/value; publication/access status; reason native binding is unavailable or destination is pending; test result/date; migration retest and resolution trigger**. No exception is considered approved merely because it appears in a table.

Current pending routes remain recorded in the [E10 CTA milestone](milestones/2026-10-16-homepage-cta-strategy.md#outstanding-items-and-recovery) and [ELEMENTOR_MAP](ELEMENTOR_MAP.md#homepage-cta-instance-values--e10): Request Service and other service/category/project/testimonial/city/utility destinations use existing placeholders. That dated inventory is not a fresh site-wide link pass. Replace a pending entry with a verified object binding when the approved destination exists; do not leave a placeholder when a supported real target is available.

### Manual exceptions and migration checklist

Only use a hardcoded internal URL when the specific Elementor/native control cannot reasonably support the required destination. Record the exact native limitation and affected location, the intended object/path, why the manual value is necessary, who/what approved the exception where required, and the pre/post-migration test. Missing pages or lack of time are not native limitations. Do not add a plugin or custom code just to bypass normal linking controls.

Before migration, inventory all native bindings, menu objects, manual exceptions, drafts and intentional placeholders; preserve the approved path/migration decisions. During an authorized migration verify object and menu-reference remapping, including nested Component overrides. After migration to **gcprochicago.com**:

1. Resolve native links to the intended objects and approved final paths, not merely any HTTP 200 page.
2. Recheck Header/Footer/navigation and independently configured Component instances; confirm public access, keyboard activation and intended same/new-tab behavior.
3. Audit saved configuration **and** rendered URLs for stale staging/production literals, preview/authentication parameters, broken targets, redirects, fragments and `#` placeholders. Review external/tel/email destinations without converting them into page references.
4. Retest every manual exception, record the final result, and explicitly carry unresolved items forward. Native references reduce migration risk but never waive these checks. Do not execute redirects or change URLs outside separately authorized migration scope.

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

## Preservation baseline versus future architecture — E72

Before adding staging structure, reconcile the complete approved mapping with fresh native saved status/slug/parent/full paths; reuse existing objects and do not recreate completed skeletons. Current URL preservation does not approve long-term architecture or source audit redirects/removals. Maintain the single canonical SEO_URL_INVENTORY.csv using the E72 field contract in SEO_STRUCTURE.md. Retain historical fields and exact URL identities, append dated discoveries/decisions/evidence, distinguish intended Draft routing from public history, and record unavailable production unpublished/performance access honestly. Final targets and execution remain a separately authorized migration milestone.
