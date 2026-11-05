# GCPRO agent instructions

Standing instructions for AI agents working on the GCPRO Restoration website. Sections 1–2 govern every task. Later sections apply only when the task touches their subject. Owner decisions are consolidated here; their dated history lives in [CHANGELOG.md](CHANGELOG.md). This file has no hidden precedence: when two rules seem to conflict, the order in section 2.2 decides.

Elementor objects are written as Name (ID), e.g. Section Heading (71). Other project docs use the compact form `Section Heading71`; both refer to the same object.

## 1. Security and authorization boundaries

These apply to every task and override everything below.

- **Production:** never modify production. The only implementation environment is GCPRO staging: `https://vitaliiv1.sg-host.com`. Verify that the connection actually targets this host before any staging write.
- **Authorization scope:** only the owner's explicit request authorizes a change. Read-only, documentation, audit and planning requests authorize no WordPress write, theme change, plugin installation, deployment or production action. Redirects, URL changes, deletions, removals and publication always need separate explicit authorization.
- **Repositories:** project work belongs in https://github.com/vvvetalll/gcpro-website (GCPRO content, page IDs, design values, implementation records). The [ROBYLO repository](https://github.com/vvvetalll/robylo-website-starter) is a separate product: read it as a dependency; do not change it or copy client-specific documentation into it without a separate authorized task.
- **Secrets and private data:** never put passwords, application passwords, encoded Authorization values, tokens, raw session/admin responses, customer data, database dumps or private backup archives in the repository, logs, screenshots or progress messages. Record only reviewed, sanitized evidence. Public shortcode/plugin instance identifiers are locators, not secrets.
- **Git:** preserve unrelated changes. Never force-push, reset others' work or bypass branch protections.
- **Usage and billing:** never purchase extra credits, change automatic recharge or activate a usage reset without explicit owner authorization. If a usage limit stops work, report the completed state and the blocker instead of looping.
- **BEAF Pro (third-party integration):** excluded from architecture cleanup. Preserve its plugin files, shortcodes, CSS overrides, popup behavior, selectors and Elementor integration. Its page/body/grid/slider numeric scoping is an intentional third-party isolation exception, not architectural debt. Authorization to clean up custom Atomic components does not cover BEAF; a BEAF task needs its own explicit owner scope.

## 2. Executing tasks

### 2.1 Classify the task first

| Type | What it covers | What to do |
|---|---|---|
| **Execution** | An explicitly requested, bounded change to existing elements: text, icon, color, spacing, an approved variant swap, an approved Override value, a single link correction. | Implement the requested change. Do only the preparation and verification it needs. Do not expand scope. Stop after delivery. |
| **Read-only analysis** | Audits, reviews, investigations, proposals, documentation reviews. | Inspect and report. Modify nothing unless the owner explicitly authorizes a specific change. |
| **Complex implementation** | New sections or pages, shared-definition or structural changes, new code or Custom Code, structural or multi-page linking/navigation changes, publication changes, multi-step builds, migrations. | Follow the relevant architecture, security, backup, testing and documentation procedures in sections 5–11, within the authorized scope. |

If a task's type is unclear, treat it as the lighter type that still fully covers the actual risk. A task becomes complex only when the change itself does (for example, a "small" edit that turns out to require a shared-definition change). Say so before proceeding. The task description alone does not make it complex.

### 2.2 Priority order

1. Security, authorization and environment boundaries (section 1).
2. The owner's current, explicitly authorized task.
3. Preservation of approved architecture and decisions.
4. Minimum necessary implementation.
5. Proportional verification.
6. Proportional documentation and GitHub synchronization.
7. Stop after successful delivery.

Speed never justifies sacrificing correctness, security, accessibility or the staging boundary.

### 2.3 Execution rules

- **Mandatory opening for every delegated Work prompt.** Start each implementation prompt with: "Keep execution proportional to the task. For a small copy or visual change, inspect and edit only the affected element and its actual shared dependencies. Perform a short targeted check. Do not crawl, audit or regression-test the entire website unless explicitly requested or the change demonstrably affects it. Check shared-resource consumers only to establish the real impact; do not automatically open every page. Avoid repeated checks, unrelated cleanup and unnecessary documentation. Report verification limits briefly." This is a standing scope rule, not a reason to skip necessary checks or an explicitly requested audit.

- **Do exactly what was requested.** Do not invent tasks, add polish, run audits or modify unrelated components. If a project rule seems to require work outside the task, report it as a finding; do not do it.
- **Do not reopen approved decisions.** Implement approved icons, designs, styles, components and copy without researching alternatives again. Reopen a decision only when implementation is technically impossible or clearly broken, and say so before changing course.
- **Execute authorized simple edits directly.** No lengthy plan, design review or repeated confirmation.
- **Deviations need approval first.** A redesign, experiment, replacement of an established component, content deletion, new code or plugin, alternative implementation or scope expansion needs explicit owner approval *before* implementation. Describe the exact deviation and affected scope, then request approval through the client's approval prompt; if none is available, ask in chat and wait. Silence and progress messages are not approval. While waiting, continue only independent authorized work.
- **Ask only when the answer changes the result**, for example when two button variants are equally suitable or a structural change carries significant regression risk. Otherwise continue routine authorized work without approval requests.
- **Context:** reuse verified session knowledge and established decisions. Read only the documentation the task needs; do not reread the repository or repeat completed investigations. Documentation is a dated handoff, not a live mirror.
- **Tools:** prefer supported Elementor MCP operations over visual-editor or browser navigation. Use the shortest reliable workflow, batch independent operations and avoid redundant reads, navigation and screenshots. Do not use tool-driven execution for discussion, drafting or planning that needs no tools. When selectable, choose a cost-conscious model or reasoning effort that does not compromise correctness.
- **Blockers:** do not repeat a failed method. Try at most one reasonable alternative, announced in chat, then report the exact failed action, the error and the current saved state. If manual Elementor editing is faster, give the owner exact steps immediately. Never spend 20–30 minutes silently on a minor task or retry indefinitely.
- **Progress:** for short tasks, report only meaningful progress, completion or blockers; no step-by-step activity reports. For genuinely long-running operations (uploads, multi-step builds, long tool calls), post a short status update at least every 60 seconds; never leave the owner watching a spinner without explanation. Report actions, evidence and results, not internal reasoning or invented activity.
- **Stop:** when the owner says stop, stop all tool activity immediately, including checks, documentation and Git operations. Report the actual saved, published and committed state without further tool calls. Do not claim unperformed verification. An instruction to *finish* the task permits its normal completion steps.

### 2.4 Definition of DONE

A task is done when **all** of the following are true:

1. The explicitly requested result has been implemented (or, for read-only analysis, reported) within the authorized scope.
2. It passed the checks its task type requires (section 10), with no open defect in the changed scope.
3. Documentation and a verified remote commit exist only where the task scope justifies them or the owner requested them (section 11). A minor Elementor edit needs no documentation entry.
4. The final report states what changed, what was verified, what remains unfinished or problematic, and a commit link when applicable. It explicitly notes any deviation from the request or these rules and never claims an unperformed save, test, approval, publication or commit.

Then stop. Further refinement, audits or polishing require a new request.

**If execution is blocked:** report the exact blocker, the actual saved state and the remaining work, then stop. Do not continue unnecessary retries.

## 3. Elementor MCP connection (staging)

- Connection name: `gcpro-restoration-elementor`.
- Endpoint: `https://vitaliiv1.sg-host.com/wp-json/elementor/mcp/` — HTTP MCP, WordPress application-password Basic authentication.
- Reuse the existing connection. Check the available tools once per session. Tool presence is not a successful staging test: verify actual access and the staging hostname before the first edit. Do not claim a working connection merely because configuration was saved.
- The owner authorizes reusing the saved credentials and re-establishing this staging connection for authorized project tasks without repeated connection approval. This does not authorize broader website changes or bypass client permissions.
- If the tools are not exposed and the task needs them, inspect the existing secure local client configuration before asking the owner for connection details again. Owner-designated location: `~/mcp-config.json` on Linux/macOS, `%USERPROFILE%\mcp-config.json` on Windows, on the computer running the AI client (not an unrelated remote environment). The file's existence does not register a server; verify that the client supports it. If supported, merge the named server into the existing `mcpServers` object without overwriting other entries, using `type: "http"`, the endpoint above and an `Authorization` header taken from the protected local credential store.
- If native bindings remain unavailable and a direct MCP protocol client is supported, reuse the stored credentials, initialize the session, retain the returned session header, then run `tools/list` and one read-only page check. Report direct protocol access separately from registered client tools.
- Do not restart or terminate the client during active work; report the exact client action needed. If this environment cannot reach the client machine or stored credentials, state that limitation and ask only for the missing setup step. AGENTS.md cannot install a connector or transfer secrets between machines or sessions.

## 4. Reading and writing Elementor data

- Before a write, read the current saved structure of the elements you will change. Read it again after each save before the next write. Never reuse a stale element tree.
- Inspect a component's current schema before assuming an Override exists. Check connector capabilities once per session, not before every operation.
- Do not infer IDs from labels or copy IDs between installations.

## 5. Architecture: native Atomic V4 first

Applies to complex implementation, and to execution tasks only where the requested change touches these rules.

- Use native WordPress and Elementor Atomic V4 controls, responsive settings, Global Variables, Global Classes and reusable Components. Keep text, images, SVGs, links, typography, spacing, backgrounds and responsive behavior understandable and editable in the visual editor.
- **Reuse before creating.** Use existing component instances, supported Overrides/variants, approved page patterns, button components and design tokens. Use Overrides for instance content; edit a shared definition only when all consumers should change. Give Navigator elements and classes clear names.
- **Minimum necessary additions.** Add an element, class, Component or abstraction only for a demonstrated current requirement the existing system cannot reasonably meet. Never add one because it might be useful someday or because page copy differs.
- Avoid hidden CSS/JS, HTML-widget workarounds, fragile selectors, direct database edits and undocumented customizations. Do not create parallel design tokens or layouts in theme code. If native controls cannot meet a requirement, document the gap, propose a simpler editable alternative and obtain authorization for any additional code scope. Record the exact location, purpose, affected classes and rollback of an authorized exception.
- Treat page/template/element IDs as location references. Do not introduce page-ID-dependent CSS or business logic unless the technical requirement, scope, exact storage, reuse limit and migration/rollback are documented. Preserve required generated selectors and native object/plugin references.
- **Preserve working approved designs.** Do not delete classes, components or assets merely because one page does not use them. Structural changes with significant regression risk need owner approval. Minor visual edits are not architecture work: report architectural issues you notice, and do not act on them within an unrelated task.
- Never leave experimental code, widgets or Custom Code entries undocumented. A saved Atomic tree without a video/HTML widget does not prove that no content is injected at runtime. When that matters, check the frontend and Custom Code.

### CSS architecture policy (adopted 2026-10-19)

Apply this order to new work and authorized refinements:

1. **Native Atomic style controls and existing Variables first.** Keep layout, typography, spacing, colors, borders, responsive variants and supported states in Elementor's native controls. Reuse approved tokens; do not create a second palette or token system.
2. **Reusable Global Classes for repeated styling.** Reuse a suitable existing class after inspecting its definition, priority and consumers. When a real repeated pattern needs a class, give it one clear role and put supported properties in native class controls. Do not repeat the same pattern as independent local CSS or add another class with an equivalent purpose.
3. **Minimal scoped Custom CSS for demonstrated native gaps.** Keep only unsupported declarations/selectors, in the narrowest appropriate Elementor scope. If a repeated pattern needs the same exception, prefer one scoped class-owned rule (after consumer checks) over copying a block onto every element. Local CSS remains appropriate for a genuinely unique exception. Record the native limitation, exact editing location, affected consumers, approval/scope and rollback. Re-read the saved output: a connector CSS input can become native properties or Custom CSS, or it can be dropped, so input syntax alone does not identify the storage layer.
4. **Theme stylesheet last, for genuinely global technical rules only.** Use it only where a rule cannot be managed cleanly in Elementor, with separately authorized source/deployment scope. A rule repeated within one section is not global. Do not move brand styling, page layouts or one-off interactions into the theme to reduce an Elementor CSS count. Do not enqueue a documentation/source mirror as a second active stylesheet.

Maintain one authoritative owner for each property/state/breakpoint. Inspect defaults, class order, local styles and existing exceptions before adding an override. Prefer inheritance and low-specificity, narrowly scoped selectors. Avoid specificity escalation, unnecessary `!important`, broad tag/descendant selectors, conflicting logical/physical declarations and parallel Elementor/theme implementations. Different states and genuine responsive differences are not duplication. Preserve accessible focus and reduced-motion behavior.

CSS is not itself a defect. Do not refactor working elements solely to eliminate CSS, create speculative abstractions or migrate historical exceptions automatically. In audits, separate confirmed issues from candidates that need runtime validation, and propose the smallest maintainable change with before/after verification. Existing scoped exceptions are dated records, not blanket permission for new code. See [CSS layer responsibilities](docs/DESIGN_SYSTEM.md#css-architecture-policy--2026-10-19-e41).

## 6. GCPRO design standards

- **Page header.** Every page starts its content with the shared page header **GCPRO — Shared Hero (1318)**, using its supported content Overrides. It is separate from the global navigation **Header (113)**, which must be preserved. Place page content and Atomic forms below the page header, never inside it. Do not rebuild its design as a custom heading section, copy its descendants, detach it, duplicate it, or substitute starter (74), Section Heading (71) or another Hero. A native wrapper around it is not a new header design. Use the documented ID; do not restart component discovery or compare alternative designs. Existing approved exceptions require their owner record. This rule does not authorize an unsolicited bulk site rewrite.
- **Section headings.** Use the actual **Section Heading (71)** instance with the existing `section-heading--accent` wrapper (orange line) and its supported subtitle/description where appropriate. Do not imitate it with a standalone heading, line and paragraph. Preserve semantic heading levels.
- **Shared sections.** Reuse one established design per shared section type. How We Work (1152), Why (1149), Service Areas (1140) and Final CTA (80) are shared definitions: change content through supported Overrides, not duplicated structures or different styling. Preserve uppercase Hero H1 typography. See [docs/components/residential-services.md](docs/components/residential-services.md).
- **Service Damage Types card grid.** The approved card layout on the service pages is owned by the shared component **GCPRO — Service Damage Types (1345)**. Its *documented* configuration ([docs/components/service-damage-types.md](docs/components/service-damage-types.md)) is six cards in 3 desktop / 2 tablet / 1 mobile columns; this is a documentation record, not live-verified Elementor state. Before relying on the card count or column settings, read the live component. Preserve the existing approved responsive layout, typography, spacing, gutters and shared-component integrity; change per-page content through its Overrides. Balance card lengths through editing, never with filler, forced breaks, smaller fonts, clipping or hidden fixed heights. This rule applies only to component 1345; do not enforce its card count on other grids.
- **CTA sections** (until the owner says otherwise). Build and refine CTA sections as **inset cards**, using the approved Home mid-page Emergency Restoration Support CTA as the reference. Keep visible side gutters and rounded corners on mobile; the colored/video panel must not become an edge-to-edge strip. Reuse existing native containers, classes, Variables and shared Components. A final CTA may stay larger than a compact mid-page CTA. Preserve CTA text, native destinations, responsive stacking, readable overlay and motion fallback. This rule does not authorize a site-wide rollout to existing pages.
- **Button hierarchy.** On new pages, choose variants by action purpose and page context (section background, neighboring sections, nearby buttons, overall rhythm): Solid Orange (53) for principal conversions, Orange Outline (100) for supporting inquiries, Solid Blue (56) where repetition warrants it (as approved for the Residential assessment), Blue Outline (59) for navigation. Avoid competing primary actions in one section. Ask the owner when variants are equally suitable or hierarchy could be disrupted. Preserve native destinations, component geometry, hover and keyboard focus. A variant swap needs no new button components, classes or local CSS. Follow [docs/DESIGN_SYSTEM.md](docs/DESIGN_SYSTEM.md); verify contrast on the actual surface and report inherited accessibility limits honestly. A small approved style correction is an execution task: apply the existing variant directly with a short targeted check.
- **Before/After cards.** Use the approved "A" presentation everywhere: `ba-card`, `ba-card__caption`, `ba-card__title`, with native article/media/caption structure, 4:3 optimized images, the existing plugin runtime, appropriate heading levels and metadata. Known locations use "City, IL" in titles; descriptions focus on the work without repeating the location. Do not invent missing locations. Reused projects share caption copy. Hero comparisons are a separate composition. See [docs/components/before-after.md](docs/components/before-after.md).
- **Images.** New or replaced photos must be appropriately sized and optimized to WebP, with descriptive filenames and truthful alt/title/description. Use approved 4:3 crops for comparison galleries. Never stretch images or rasterize useful SVGs. Preserve source files and avoid duplicate media.
- **Section rhythm.** When adding or reordering sections, check the changed section and its immediate neighbors for background rhythm, spacing and transitions. Avoid unintended long merged white/light-blue areas; use existing tokens; preserve the navy affiliations separator and inset CTA cards.

## 7. Internal linking and URL integrity

Applies to GCPRO pages, navigation, Header/Footer and reusable Components:

- Prefer Elementor **Dynamic Tags → Internal URL** or the equivalent native page/post selector, bound to the intended existing WordPress object. Do not type absolute staging/production URLs when native object linking is supported. Native site/home URL tags are appropriate for site-root links.
- In WordPress Navigation, use Page/post (or other supported object) menu items instead of Custom Links whenever the destination object exists. A matching rendered URL does not prove object-based configuration.
- Keep destinations independently editable through supported Atomic Component Overrides. Do not detach or duplicate Components to assign different destinations. Schema support alone is not a successful runtime test.
- Reuse existing pages. Never create duplicate or placeholder pages to supply a destination. Do not expose draft, private or preview URLs in public navigation.
- Record missing destinations explicitly. An owner-approved temporary `#` is an unresolved placeholder, not a working route. Do not introduce accidental `#`, invent a URL, substitute an unrelated destination or fall back to production.
- Hardcoded internal URLs are exceptions, allowed only where no native alternative is supported; document the limitation, exact location, intended object/path, reason and migration retest. Relative paths are still manual links. Use native anchor controls for in-page navigation and verify that the target exists.
- External websites, email and `tel:` links use normal URL fields with the correct scheme.
- After migration to `gcprochicago.com`, verify object/ID mapping, navigation, Component instances, final URLs and recorded manual exceptions. Preserve approved production paths.

**Link checks:** when a task adds or changes links, navigation, page publication status or shared Components, check the affected pages/templates and shared consumers. Cover intended objects and access status, hardcoded values, broken destinations, accidental placeholders, independent Component destinations and unresolved-link records, and report tested versus pending cases. Edits that do not touch links need no link check. Follow [the verified Atomic linking method](docs/WORKFLOWS.md#native-internal-linking-and-url-integrity). Do not claim an end-to-end dynamic Component test or migrated-site verification unless it was performed.

## 8. Customer-facing copy

Applies whenever a task writes or edits website copy.

Write in clear, natural US English: specific, useful and credible, like a knowledgeable restoration professional explaining the work. Use concrete verbs, familiar language, varied sentence lengths and short connected paragraphs. Explain technical terms only when useful. Avoid interchangeable marketing, empty reassurance, forced friendliness, invented personal experience, keyword stuffing, rhetorical filler and formulaic sentence openings. Do not use phrases such as "comprehensive solutions," "seamless restoration," "state-of-the-art," "peace of mind" or "we understand how overwhelming…". Explain work stages rather than repeated "describe/discuss/review/agree" intake steps. FAQs must answer real customer decisions, not fill slots with unlikely equipment or guarantee questions. Judge writing by accuracy, clarity, specificity and usefulness; never promise AI-detector results.

Within the requested copy scope, improve weak existing copy before adding new sections. Keep approved semantic ownership, useful links and native page-specific Overrides. Separate general restoration principles from verified GCPRO procedures: "may" or "typically" does not make an unsupported company claim acceptable. Never invent equipment, credentials, documentation, testing, logistics or promises; record the exact missing facts instead. Put longer explanations in suitable existing text or practical FAQ answers. Preserve natural wording rather than identical word counts.

## 9. SEO and URL ownership

- **URL baseline (2026-10-21).** Preserve existing URLs while building staging; the baseline is not an immutable final architecture. [docs/SEO_URL_INVENTORY.csv](docs/SEO_URL_INVENTORY.csv) is the single canonical exact-URL register. It includes unpublished, city, orphan-candidate and historical URLs with distinct production/staging IDs, dated status/metadata/canonical/performance evidence, proposed action/target/reason and approval/execution history. Use `future_action` values KEEP / UPDATE / MERGE / 301 REDIRECT / REMOVE / REVIEW; `migration_decision` is historical. Never infer prior public access from Draft status or absence from a public inventory, and never treat missing metrics as zero; unknown data stays marked unverified. Do not delete historical rows or collapse URL variants. See the E72 field/coverage contract in [docs/SEO_STRUCTURE.md](docs/SEO_STRUCTURE.md).
- **Semantic SEO.** For commercially important page work, use [docs/seo/SEO_STRATEGY.md](docs/seo/SEO_STRATEGY.md), [MASTER_KEYWORD_MAP.csv](docs/seo/MASTER_KEYWORD_MAP.csv) and [PAGE_SEO_BRIEFS.md](docs/seo/PAGE_SEO_BRIEFS.md). The 2026-10-21 strategy is **DRAFT — AWAITING OWNER APPROVAL**; do not implement its recommendations before approval. Once approved, do not choose competing targets during individual page builds; keep one primary landing page per intent cluster and update affected briefs when ownership changes. `docs/seo/` is canonical for semantic research; the URL inventory is canonical for exact URLs and migration history. No semantic recommendation authorizes a URL, navigation or website change.

## 10. Verification and rollback protection

Verify only what changed and its immediate dependencies, in one relevant pass. Repeat a check only after a new edit, a failure or an unresolved issue. The owner performs final visual acceptance. Do not run repeated screenshots, viewport/page matrices or prolonged visual QA unless asked. If a concrete defect needs more checking, explain why before extending the scope. Never reduce checks where the change carries real risk.

| Task type | Rollback protection | Required checks |
|---|---|---|
| **Execution** (small reversible Atomic edit) | Preserve the previous values or an equivalent reliable recovery reference (e.g. the pre-edit read or Elementor revision). | Read back the saved value and run one focused check of the changed block (aim for 30–60 seconds). Check the relevant responsive state only if layout is affected. No link audits, screenshot series, unchanged shared-component checks or repository scans. |
| **Complex implementation** | A proper recoverable backup of the affected page, template or shared definition before structural or higher-risk changes. | Read back saved values. Check the editor and frontend, relevant responsive layout and keyboard operation for interactive elements. For shared definitions, check affected instances and independent Overrides. Run link checks per section 7. |
| **Read-only analysis** | — | Verify the relevant evidence and report findings. Make no edits or commits; do not retest the website unless needed for the requested analysis. |
| **Documentation-only changes** | — | Check the edited content, diff and relevant file paths/links. Verify the remote commit only if a commit was made. No website retesting or invented runtime tests. |

**Cache and anonymous delivery.** After meaningful Elementor, Custom Code, CSS or JavaScript changes, decide whether SiteGround cache invalidation is needed and purge only the relevant staging cache. When a change affects public delivery or stale output is suspected, check the relevant anonymous frontend. Before diagnosing a frontend failure, compare authenticated and anonymous HTML/assets. Never claim a feature works for all visitors from an authenticated Elementor preview. See the [anonymous delivery procedure](docs/WORKFLOWS.md#anonymous-delivery-verification--e18).

**Evidence.** Separate verified repository facts, verified staging reads, reported historical outcomes and unknowns. Distinguish proposed, implemented, published and browser-tested states. Saved settings, reports or screenshots do not prove current rendering or visual editability. Distinguish desktop mobile emulation from physical-device testing, and label owner-reported device results as such.

## 11. Documentation and GitHub

Keep documentation proportional. Do not create separate evidence files or duplicate the same update across several documents. Update AGENTS.md only for permanent instructions or decisions.

**Execution tasks**
- Documentation is optional: add it only when it has future value or the owner asks. Then keep it to at most a 1–3 sentence note in one relevant existing record, batched with other minor notes.
- No GitHub commit is required for a minor Elementor edit. Commit batched notes at the next meaningful commit, or when the owner asks.
- Never update AGENTS, PROJECT_CONTEXT, CHANGELOG, component records and code registers together for a minor edit.

**Complex implementation**
- Update the component's record in [docs/components](docs/components/README.md): purpose; WordPress/Elementor locators; parent/children; classes/tokens; CSS and JavaScript storage; Custom Code IDs; plugins/shortcodes/integrations; responsive behavior; interactions/dependencies; issues/status; safe modification/reuse. Update PROJECT_CONTEXT, CHANGELOG and map/design/architecture references only where they are actually affected.
- Record every custom CSS/JS owner in [docs/CUSTOM_CODE.md](docs/CUSTOM_CODE.md): theme file/enqueue, class variant/local style, Custom Code conditions/location/priority and external dependencies. Do not deploy source mirrors twice.
- Record staging evidence meant for future sessions in the [evidence register](PROJECT_CONTEXT.md#evidence-register): date, environment, source, IDs, checks actually run, limitations and remaining work.
- For multi-step work, keep a concise task log in the existing GitHub documentation: scope, completed changes, checks and results, blockers/approval requests/remaining work, and current saved/published/committed state. Update it at meaningful checkpoints, not after every step.

**Commits**
- Commit meaningful implementation changes, tracked code changes and explicitly requested updates, at task completion or at a useful handoff point.
- Push to `main` unless told otherwise. Verify the remote commit before claiming a push; a local commit is not a push.
- Git work must not delay reporting that a website change is already saved and published. If a GitHub write fails or stalls, say so immediately and do not claim the record was updated.

**Permanent priority: execute efficiently, preserve quality, minimize unnecessary work. Optimize simple tasks for minutes.**

## Service-page benefits — owner instruction, 2026-11-02

Every service page must include the existing shared Why Choose GCPRO Component1149. Preserve existing instances; add a native instance where absent, using supported page-specific Overrides. Do not duplicate certificate rows; retain the existing separate Credentials1886 convention. Certificate updates are a separate deferred task. For routine copy/SEO edits, confirm the save and report briefly; do not prolong work with repeated visual evaluations.

## Marketing documents — owner instruction, 2026-11-05

For GCPRO marketing layouts, printed materials, fillable PDFs, logos and source work, start at [marketing/README.md](marketing/README.md) and follow [marketing/AGENTS.md](marketing/AGENTS.md). This is the owner-designated knowledge/source folder, based on the supplied October 20 kit. Reuse its exact established layouts; a text/photo correction does not authorize redesign. Website tokens/components remain governed by the website records. Current unapproved ERP/PM revisions, presentations and Thank You flyers are not part of this baseline kit.
