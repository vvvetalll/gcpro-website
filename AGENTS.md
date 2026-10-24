# GCPRO agent instructions

## Start here

Read [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md), [CHANGELOG.md](CHANGELOG.md), and the relevant files in [docs](docs/WORKFLOWS.md) before working. Recheck the target, current Git state, and live evidence; this documentation is a dated handoff, not a live mirror.

## BEAF third-party integration boundary

BEAF Pro is excluded from Phase 1 architecture cleanup. Preserve its plugin files, shortcodes, CSS overrides, popup behavior, selectors and Elementor integration. Necessary page/body/grid/slider numeric scoping is an intentional third-party isolation exception, not automatic architectural debt. Cleanup authorization for custom Atomic components does not authorize BEAF changes. A future BEAF task needs separate explicit owner scope.

## Permanent boundaries

- Never modify production. The only designated implementation environment is GCPRO staging: https://vitaliiv1.sg-host.com. Verify the connection actually targets that host before any staging action.
- Repository work belongs in https://github.com/vvvetalll/gcpro-website. Keep GCPRO content, page IDs, design values, and implementation records here.
- The shared [ROBYLO repository](https://github.com/vvvetalll/robylo-website-starter) is a separate product. Read it as a dependency; do not change it or copy client-specific documentation into it without a separate task authorizing that scope.
- Documentation initialization and this repository-integration task authorize no WordPress writes, theme changes, deployment, plugin installation, or production action. Future implementation must follow its own authorized scope; the standing milestone-documentation requirement below applies after that work.
- Preserve unrelated changes. Never force-push, reset others' work, or commit credentials, customer data, database dumps, or private backup archives.

## Standing editorial requirement — owner instruction, 2026-10-24

Write customer-facing copy in clear, natural US English: specific, useful and credible, like a knowledgeable restoration professional explaining the work. Use concrete verbs, familiar language, varied sentence lengths and short connected paragraphs. Explain technical terms only when useful. Avoid interchangeable marketing, empty reassurance, forced friendliness, invented personal experience, keyword stuffing, rhetorical filler and formulaic sentence openings. Do not use phrases such as “comprehensive solutions,” “seamless restoration,” “state-of-the-art,” “peace of mind” or “we understand how overwhelming…”. Explain work stages rather than repeated “describe/discuss/review/agree” intake steps. FAQs must answer real customer decisions, not fill slots with unlikely equipment/guarantee questions. Judge writing by accuracy, clarity, specificity and usefulness; never promise AI-detector results.

Replace weak copy before adding sections. Keep approved semantic ownership, useful links and native page-specific Overrides. Separate general restoration principles from verified GCPRO procedures; “may” or “typically” does not make an unsupported company claim acceptable. Complete supported improvements and record exact missing operational/project facts without inventing equipment, credentials, documentation, testing, logistics or promises. Preserve the six-card 3×2 desktop /2-column tablet /1-column mobile layout, typography, spacing, gutters and shared component integrity. Balance concise cards and compact process steps through editing, never filler, forced breaks, smaller fonts, clipping or concealed fixed heights. Put longer explanations in suitable existing text or practical FAQ answers. Preserve natural wording rather than identical word counts.

## Native visual editing

### Durable component maintenance and audit rules

- Inspect the actual saved implementation, rendered behavior and existing code owners before editing. Prefer native Atomic controls, reusable existing classes and approved design tokens.
- Treat page/template/element IDs as location references. Do not introduce page-ID-dependent CSS or business logic unless a demonstrated technical requirement and its scope, exact storage, reuse limit and migration/rollback are documented. Preserve required generated selectors and native object/plugin references.
- Maintain [docs/components](docs/components/README.md) after every meaningful component change. Each record must cover purpose; WordPress/Elementor locators; parent/children; classes/tokens; CSS and JavaScript storage; Custom Code IDs; plugins/shortcodes/integrations; responsive behavior; interactions/dependencies; issues/status; and safe modification/reuse.
- Record every custom CSS/JS owner in [docs/CUSTOM_CODE.md](docs/CUSTOM_CODE.md), including active theme file/enqueue, class variant/local style, Custom Code conditions/location/priority and external dependency. Keep one authoritative owner per property/state/breakpoint; do not deploy source mirrors twice.
- Never leave experimental code, widgets or Custom Code entries undocumented. A saved Atomic tree without a video/HTML widget does not prove absence of runtime-injected content; inspect frontend and Custom Code.
- Keep component records, PROJECT_CONTEXT, CHANGELOG and affected map/design/architecture references synchronized with verified staging. Preserve dated history and distinguish proposed, implemented, published and browser-tested states. Never claim browser validation from saved settings alone.
- Identify architectural findings before changes. Preserve functioning visual design; obtain owner approval before structural changes with significant regression risk. Do not delete classes/components/assets merely because they are absent from one page.
- Never commit credentials, authorization headers, tokens, passwords, raw session/admin responses or private backups. Record only reviewed, sanitized evidence; public shortcode/plugin instance identifiers are locators, not reusable secrets.

Prefer native WordPress and Elementor Atomic V4 controls, responsive settings, Global Variables, Global Classes, and reusable Components. Keep text, images, SVGs, links, typography, spacing, backgrounds, and responsive behavior understandable and editable in the visual editor.

Reuse existing variables/classes before adding new ones. Use supported Component Overrides for instance content; edit the shared definition only when all consumers should change. Give Navigator elements and classes clear names. Inspect the current component schema before assuming an override exists.

**Native first, minimum necessary additions:** use standard Elementor Atomic V4 functionality and existing Global Classes, Variables and Components before introducing a technical element. Add one only for a demonstrated current requirement that the existing system cannot reasonably satisfy. Do not create abstractions, classes or Components merely because they might be useful someday. Significant design settings must remain easy to find and edit in Elementor; never hide styling or functionality in undocumented code.

Avoid hidden CSS, JavaScript, HTML-widget workarounds, fragile selectors, direct database edits, and undocumented customizations. Do not create parallel design tokens or layouts in theme code. If native controls cannot meet the requirement, document the demonstrated gap, propose a simpler editable alternative, and obtain authorization for any additional code scope. Record the exact location, purpose, affected classes, and rollback of an authorized exception.

Discover actual connector capabilities and schemas. Tool presence is not a successful staging test. Read fresh structure before changes and after saves; never reuse stale element trees after another write. Do not infer IDs from labels or copy IDs between installations.

## Permanent CTA card presentation — owner instruction, 2026-10-23

Until the owner explicitly requests otherwise, create and refine GCPRO CTA sections as **inset cards**, using the approved Home mid-page Emergency Restoration Support CTA as the visual reference. Preserve visible side gutters and rounded corners on mobile; do not let the colored/video panel become an edge-to-edge strip. Reuse existing native containers, classes, Variables and supported shared Components. Keep purpose-appropriate height and content: a final CTA may remain larger than a compact mid-page CTA. Preserve CTA text, native destinations, responsive stacking, readable overlay and motion fallback. This rule does not authorize an automatic site-wide rollout to existing pages.

## Purpose-based CTA hierarchy

For all future pages evaluate both action purpose and full-page visual context: section background/layout, preceding/following sections, nearby similar buttons, overall hierarchy and rhythm. Use existing53 Solid Orange for principal conversions,100 Orange Outline for supporting enquiries, contextual Solid Blue56 styling when repetition warrants it (as explicitly approved for Residential assessment), and59 Blue Outline for navigation. Ask the owner before implementing when variants seem equally suitable or hierarchy could be disrupted. Avoid competing primary actions in one content section. Preserve native destinations, component geometry, hover and keyboard focus. No new button components/classes/local CSS for a variant swap. Follow docs/DESIGN_SYSTEM.md; verify contrast on the actual surface and report inherited accessibility limits honestly. For a small approved style correction, apply the existing variant directly and perform a short targeted check; do not expand it into a redesign or unrelated audit.

New or replaced photographic assets must be appropriately sized and optimized to WebP, with descriptive filenames and truthful alt/title/description. Use approved4:3 crops for comparison galleries; never stretch images or rasterize useful SVGs. Preserve source files and avoid duplicate views.

## Shared section consistency

Reuse one established visual design per shared section type. Homepage How We Work1152, Why1149, Service Areas1140 and Final CTA80 are shared definitions; change content through supported Overrides, not duplicated structures or different styling. Preserve uppercase Hero H1 typography. Create a new Component only for a genuinely missing repeated design, not because page copy differs. See docs/components/residential-services.md.

## Before / After card consistency

Use the owner-approved A presentation everywhere for BA cards: ba-card, ba-card__caption and ba-card__title, with native article/media/caption structure. Preserve4:3 optimized images, existing plugin runtime, appropriate heading levels and metadata. Known locations use City, IL in titles; descriptions focus on work without repeating location. Do not invent missing locations. Reused projects share caption copy. Hero comparisons are a separate composition. See docs/components/before-after.md for exact owners and reuse.

## CSS architecture policy

Adopted 2026-10-19. Apply this order to new work and authorized refinements:

1. **Native Atomic style controls and existing Variables first.** Keep layout, typography, spacing, colors, borders, responsive variants and supported states in Elementor's native controls. Reuse approved tokens; do not create a second palette or token system.
2. **Reusable Global Classes for repeated styling.** Reuse a suitable existing class after inspecting its definition, priority and consumers. When a real repeated pattern needs a class, give it one clear role and put supported properties in native class controls. Do not repeat the same pattern as independent local CSS or add another class with an equivalent purpose.
3. **Minimal scoped Custom CSS for demonstrated native gaps.** Keep only unsupported declarations/selectors in the narrowest appropriate Elementor scope. If a repeated pattern needs the same exception, prefer one scoped class-owned rule after consumer checks rather than copying a block onto every element. Local CSS remains appropriate for a genuinely unique exception. Record the native limitation, exact editing location, affected consumers, approval/scope and rollback. Re-read saved output: a connector CSS input can become native properties, Custom CSS, or be dropped; input syntax alone does not identify the storage layer.
4. **Theme stylesheet last, for genuinely global technical rules only.** Use it only where the rule cannot be managed cleanly through Elementor, with separately authorized source/deployment scope. A rule repeated within one section is not global merely because it repeats. Do not move brand styling, page layouts or one-off interactions into the theme to reduce an Elementor CSS count. Do not enqueue a documentation/source mirror as a second active stylesheet.

Maintain one authoritative owner for each property/state/breakpoint. Inspect defaults, class order, local styles and existing exceptions before adding an override. Prefer inheritance and low-specificity, narrowly scoped selectors; avoid specificity escalation, unnecessary `!important`, broad tag/descendant selectors, conflicting logical/physical declarations and parallel Elementor/theme implementations. Different states and genuine responsive differences are not duplication merely because they mention the same property. Preserve accessible focus and reduced-motion behavior.

**Preserve working approved designs.** CSS is not itself a defect. Do not refactor working elements solely to eliminate CSS, create speculative abstractions, or migrate historical exceptions automatically under this policy. Report actual duplication, redundancy and conflicts separately, distinguish confirmed issues from candidates needing runtime validation, and propose the smallest maintainable change with before/after verification. A documentation/audit request does not authorize website edits; obtain approval before a subsequent Elementor refactor when it is outside the current authorized scope.

See [CSS layer responsibilities and the read-only Service Areas audit](docs/DESIGN_SYSTEM.md#css-architecture-policy--2026-10-19-e41). Existing scoped exceptions remain dated records, not blanket permission for new code.

## Mandatory native internal linking and URL integrity

Apply this rule automatically across GCPRO pages, navigation, Header/Footer and reusable Components:

- Prefer Elementor **Dynamic Tags → Internal URL** or the equivalent native page/post selector, bound to the intended existing WordPress object. Do not manually type an absolute staging/production URL when native object linking is supported. Native site/home URL tags are appropriate for site-root links where applicable.
- In WordPress Navigation use actual Pages/posts or other supported object menu items instead of Custom Links whenever the destination object exists. A matching rendered URL alone does not prove object-based configuration.
- Preserve independently editable destinations through supported Atomic Component Overrides. Verify dynamic-link persistence, frontend resolution and independence between instances; schema support alone is not a successful runtime test. Do not detach or duplicate Components to assign different destinations.
- Reuse existing pages. Never create duplicates or placeholder pages just to supply a destination. Do not expose draft, private or preview URLs as public navigation; connect/test the route when the destination becomes publicly available.
- Missing destinations must be explicitly recorded. A previously owner-approved temporary `#` is an unresolved placeholder, never a working route; do not introduce accidental `#`, invent a URL, substitute an unrelated destination or fall back to production.
- Hardcoded internal URLs are exceptions only where no suitable native alternative is supported. Document the demonstrated limitation, exact location, intended object/path, reason, and migration retest. Relative paths are still manual links, not object references. Use native anchor controls for genuine in-page navigation and verify that the target exists.
- External websites, email and `tel:` destinations use normal URL fields; verify the appropriate scheme and target.
- Preserve approved production paths. After migration to `gcprochicago.com`, verify object/ID mapping, navigation, Component instances, final URLs and unresolved/manual exceptions. Native references reduce risk but do not eliminate migration testing.

After **every implementation milestone**, check links in affected pages/templates and shared consumers: intended objects and publication/access status, hardcoded internal values, broken destinations and accidental placeholders, independently editable Component destinations, and unresolved-link records. Report tested versus pending cases, then complete the normal documentation/commit/push gate. Documentation-only work does not authorize website changes or synthetic link edits.

Follow [the verified Atomic linking method, limitations, link register and migration checklist](docs/WORKFLOWS.md#native-internal-linking-and-url-integrity). Re-read current installed schemas/controls before relying on a supported field. Do not claim an end-to-end dynamic Component test or migrated-site verification unless it was actually performed.

## Permanent execution and efficiency rules — owner instruction, 2026-10-23

These rules supersede earlier blanket requirements for extensive milestone documentation, a commit after every minor edit, six-heading reports, or exhaustive visual QA. Preserve necessary security, staging-only boundaries, scoped backups and proportional verification.

- Execute explicitly authorized simple edits directly: approved icon replacements, text, spacing and colors require no lengthy plan, design reopening or repeated confirmation.
- Reuse verified session knowledge and established project decisions. Read only relevant documentation when necessary; do not reread the repository or repeat completed investigations.
- Prefer supported, reliable Elementor MCP operations over visual-editor navigation. Use the shortest reliable workflow and batch independent operations. Avoid redundant reads, navigation and screenshots.
- Verify only changed elements and immediate dependencies. Small changes need a focused technical/render check and relevant responsive appearance; shared changes need affected-instance checks; deeper audits belong to genuinely architectural changes. The owner performs final visual acceptance.
- Keep native Atomic V4 architecture. Do not introduce unnecessary CSS/JS, components, Global Classes, plugins, abstractions or duplicate media. Do not turn minor visual edits into architecture work.
- If a straightforward edit becomes blocked or unexpectedly complicated, explain promptly. Do not repeat a failed method. Try one reasonable alternative, then report the blocker. If manual Elementor editing is faster, give the owner exact steps immediately. Never silently spend20–30minutes struggling with a minor task.
- Keep progress and final responses concise and practical: what changed, what was verified, actual unfinished work/problems, and a commit link when applicable. No mandatory six-heading report for trivial work.
- Preserve important decisions and meaningful implementation changes in GitHub. Batch minor documentation updates when appropriate; no extensive documentation or multiple commits for each small adjustment. For an authorized push use main unless otherwise specified; never force-push or bypass protections. Verify the remote commit before claiming a successful push.
- Implement approved icons/designs/styles without researching alternatives again. Reopen selection only when implementation is technically impossible or clearly broken.
- Stop checks/work immediately when requested. Report actual completion and remaining limits honestly; do not claim unperformed verification.

**Permanent priority: execute efficiently, preserve quality, minimize unnecessary work. Optimize simple tasks for minutes.**

## Evidence and verification

Separate verified repository facts, verified staging reads, reported historical outcomes, and unknowns. Use the [evidence register](PROJECT_CONTEXT.md#evidence-register). Record date, environment, source, IDs, checks actually run, limitations, and remaining work. A report or screenshot does not prove the current saved state or visual editability.

For authorized implementation, capture a recoverable backup first, read back saved values, check the real editor and frontend, responsive layout, keyboard operation, shared-component effects, and independent overrides as applicable. Documentation-only work needs diff, content, path/link, and remote-commit verification; do not invent runtime tests.

After meaningful Elementor, Custom Code, CSS or JavaScript changes, assess whether SiteGround cache invalidation is required and purge the relevant staging cache when necessary. Keep the check proportional and limited to affected output. When a change affects public delivery or stale output is suspected, check the relevant anonymous frontend; clear staging cache only when needed. Before diagnosing a frontend failure, compare authenticated and anonymous HTML/assets for stale cached versions. Never claim a feature works for all visitors from an authenticated Elementor preview alone. Distinguish desktop mobile emulation from physical-device testing and identify owner-reported device results as such. Follow the existing [anonymous delivery procedure](docs/WORKFLOWS.md#anonymous-delivery-verification--e18).

Use the concise reporting rule above. Include scoped recovery/rollback information only when material. A local commit alone is not a successful push.

## URL preservation baseline and migration history — 2026-10-21

Preserve existing URLs while building staging; the preservation baseline is not an immutable final architecture. Maintain docs/SEO_URL_INVENTORY.csv as the single canonical exact-URL register, including unpublished/city/orphan-candidate/historical discoveries with distinct production/staging IDs, dated status/metadata/canonical/performance evidence, proposed future action/target/reason and approval/execution history. Use future_action KEEP/UPDATE/MERGE/301 REDIRECT/REMOVE/REVIEW; legacy migration_decision is historical. Never infer prior public access from Draft status or public-inventory absence, or missing metrics as zero. Unknown data stays explicitly unverified. Do not delete historical rows or collapse URL variants. No redirects, deletions, URL changes, removals or publication without separate explicit authorization. See docs/SEO_STRUCTURE.md E72 field/coverage contract.

## Central semantic SEO ownership

Use [docs/seo/SEO_STRATEGY.md](docs/seo/SEO_STRATEGY.md), [MASTER_KEYWORD_MAP.csv](docs/seo/MASTER_KEYWORD_MAP.csv) and [PAGE_SEO_BRIEFS.md](docs/seo/PAGE_SEO_BRIEFS.md) for future commercially important page work. The 2026-10-21 strategy is **DRAFT — AWAITING USER APPROVAL**; do not implement its recommendations before approval. Once approved, do not independently choose competing targets during individual page builds. Keep one primary landing page per intent cluster and synchronize affected briefs when ownership changes. docs/seo/ is canonical for semantic research; docs/SEO_URL_INVENTORY.csv remains canonical for exact URLs and migration history. No semantic recommendation authorizes a URL, navigation or website change.

## Owner visual acceptance — 2026-10-23

The owner performs final visual acceptance. For routine visual changes, perform only the minimum technical check needed to catch a broken render or functionality. Do not run repeated screenshots, exhaustive viewport/page matrices, or prolonged visual QA unless explicitly requested. Stop verification immediately when the owner asks; report remaining checks honestly. This supersedes broader default visual-QA expectations for routine refinements. Preserve required backups and keep scope unchanged.

## Section-background rhythm and proportional checks — owner instruction, 2026-10-24

Whenever adding/reordering sections, inspect the changed section and its immediate neighbors for background rhythm, spacing and transitions. Avoid unintended long merged white/light-blue areas; use existing tokens with judgment, preserve the navy affiliations separator and inset CTA cards. Reuse page visits. Do not repeatedly recheck approved unchanged blocks; verify only changed elements and necessary integration behavior. When the owner asks to finish, stop further UI checks, record actual coverage/limitations and complete documentation/commit/push.


## Mandatory page header, execution boundary and progress — owner instruction, 2026-10-24

These requirements supersede earlier discretionary design and experimentation permissions. Implement only the requested change with the established project components and methods. Continue routine authorized work without repeated approval requests.

- Every page must start its page content with the existing shared page-header component: **GCPRO — Shared Hero, Component1318**, verified in the current shared-Hero/service-page records. Reuse this documented ID; do not restart component discovery or compare alternative designs. Read only current settings needed for safe insertion. Use its supported content Overrides. This is separate from the global navigation Header113, which must be preserved. Place page content and Atomic forms **below** the page header; do not put a form inside it. Do not rebuild its design as a custom heading section, copy its descendants, detach it, create a duplicate, or silently substitute starter74, Section Heading71 or another Hero. Existing separately approved exceptions require their actual owner record; this rule does not authorize an unsolicited bulk site rewrite. The current correction applies only to Request Service492 and Contact Us496.
- No unauthorized experiments: do not redesign, experiment, replace an established component, delete content, add code/plugins, introduce an alternative implementation or expand scope without explicit owner approval. Explain the exact proposed deviation and its affected scope **before** requesting approval through the **Allow/approval function**. Do not implement first and explain afterward. Silence and progress messages are not approval. If the approval function is unavailable, ask the owner explicitly and wait; abandon the proposed deviation while continuing independent authorized work.
- When blocked, report the exact failed action and error promptly. Do not silently substitute a method, repeat failed attempts indefinitely, or broaden the task. A native wrapper around the shared header is not a new visual header design; verify the first visible content component and its supported Overrides.
- Before each meaningful step, briefly state the concrete action in chat. Afterward, state what actually changed or what blocked it. During active work, update at least every 60 seconds. Report actions, evidence, decisions and results, never private internal reasoning or invented activity.
- Maintain a concise task log in the existing GitHub documentation: current task/authorized scope; completed steps and actual changes; checks/results; blockers, approval requests and remaining work; current saved, published and committed state. Batch routine updates at meaningful checkpoints rather than committing every click. Commit and verify remote delivery at completion or a useful handoff point. If GitHub writing fails or is unavailable, say so immediately; keep chat progress visible and do not claim the GitHub log was updated until the write succeeds.
- Before finishing, compare the result against the original request, the latest owner instructions and current project rules. Explicitly report any deviation. Never claim an unperformed save, test, approval, publication or commit.

