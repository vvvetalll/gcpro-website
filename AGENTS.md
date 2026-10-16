# GCPRO agent instructions

## Start here

Read [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md), [CHANGELOG.md](CHANGELOG.md), and the relevant files in [docs](docs/WORKFLOWS.md) before working. Recheck the target, current Git state, and live evidence; this documentation is a dated handoff, not a live mirror.

## Permanent boundaries

- Never modify production. The only designated implementation environment is GCPRO staging: https://vitaliiv1.sg-host.com. Verify the connection actually targets that host before any staging action.
- Repository work belongs in https://github.com/vvvetalll/gcpro-website. Keep GCPRO content, page IDs, design values, and implementation records here.
- The shared [ROBYLO repository](https://github.com/vvvetalll/robylo-website-starter) is a separate product. Read it as a dependency; do not change it or copy client-specific documentation into it without a separate task authorizing that scope.
- Documentation initialization and this repository-integration task authorize no WordPress writes, theme changes, deployment, plugin installation, or production action. Future implementation must follow its own authorized scope; the standing milestone-documentation requirement below applies after that work.
- Preserve unrelated changes. Never force-push, reset others' work, or commit credentials, customer data, database dumps, or private backup archives.

## Native visual editing

Prefer native WordPress and Elementor Atomic V4 controls, responsive settings, Global Variables, Global Classes, and reusable Components. Keep text, images, SVGs, links, typography, spacing, backgrounds, and responsive behavior understandable and editable in the visual editor.

Reuse existing variables/classes before adding new ones. Use supported Component Overrides for instance content; edit the shared definition only when all consumers should change. Give Navigator elements and classes clear names. Inspect the current component schema before assuming an override exists.

**Native first, minimum necessary additions:** use standard Elementor Atomic V4 functionality and existing Global Classes, Variables and Components before introducing a technical element. Add one only for a demonstrated current requirement that the existing system cannot reasonably satisfy. Do not create abstractions, classes or Components merely because they might be useful someday. Significant design settings must remain easy to find and edit in Elementor; never hide styling or functionality in undocumented code.

Avoid hidden CSS, JavaScript, HTML-widget workarounds, fragile selectors, direct database edits, and undocumented customizations. Do not create parallel design tokens or layouts in theme code. If native controls cannot meet the requirement, document the demonstrated gap, propose a simpler editable alternative, and obtain authorization for any additional code scope. Record the exact location, purpose, affected classes, and rollback of an authorized exception.

Discover actual connector capabilities and schemas. Tool presence is not a successful staging test. Read fresh structure before changes and after saves; never reuse stale element trees after another write. Do not infer IDs from labels or copy IDs between installations.

## Responsibilities and milestone completion

Codex owns repository documentation, Git, verification, and any separately authorized integration code. ChatGPT Work owns authorized staging Elementor configuration. These roles do not grant access or authorize changes.

**Every completed GCPRO website development milestone MUST include updating the relevant documentation in this repository, committing it, pushing it, and verifying the remote branch before calling the milestone complete.** This includes page/component changes, global style changes, navigation, templates, integrations, or significant fixes. Update PROJECT_CONTEXT and CHANGELOG plus every affected reference document; follow the [milestone matrix and handoff](docs/WORKFLOWS.md).

The user's standing instruction authorizes this documentation synchronization for subsequent GCPRO development milestones. Use main unless the task names another branch or repository protections require a pull request. Never bypass protections or force-push. These responsibilities do not prevent the current authorized agent from doing Git/docs directly when access is verified. If repository write access is unavailable, provide the exact limitation and a documentation patch/handoff; keep synchronization pending until the commit and remote update are verified. Tool availability, reported permissions, a local commit, or chat-only notes do not satisfy this requirement.

## Mandatory implementation reporting standard

This is a permanent requirement for every AI agent working on GCPRO, effective 2026-10-16. Apply it automatically after every meaningful implementation task/milestone, including minor fixes. The final user-facing report MUST use these six headings, in this order:

1. **Implementation Summary** — what changed: pages, sections, Components, WordPress/Elementor IDs, and resulting design or functional behavior.
2. **Technical Changes** — native controls, existing Global Classes/Variables, Atomic Components and supported Overrides reused; Component structure changes; every custom CSS, JavaScript or PHP change. List every new Global Class, Global Variable, Atomic Component, custom code file, plugin and external dependency individually. For each addition give its name/ID or exact path, purpose, why existing functionality was insufficient, whether it is reusable, and where it can be edited. A link may provide detailed controls/evidence, but must not replace this inventory in the report. When applicable, explicitly state **"No new classes, components or custom code"**; separately identify new Variables/dependencies or state none.
3. **Complexity Audit** — before completion, check for duplicate/redundant Global Classes, unnecessary Components, excessive DOM nesting, hidden styling, unnecessary custom code and added dependencies. Remove unjustified complexity introduced by this task within its authorized scope, reverify affected behavior, and report what was simplified or why retained additions are necessary. Do not silently clean up unrelated shared resources.
4. **Verification** — actual desktop/mobile widths and results, functional tests, Elementor visual editability, responsive issues and relevant accessibility/performance findings. Clearly distinguish verified results, assumptions and untested cases; never imply checks were run because tools exist.
5. **GitHub** — documentation files updated, canonical commit URL, target branch, push confirmation and remote commit verification. Report failures and synchronization still pending accurately.
6. **Outstanding Items** — incomplete/unverified work, limitations, remaining issues, dependencies or approvals; explicitly say none when applicable.

Keep all six headings even for a minor change; one concise sentence per heading can suffice. Scale detail to the task, but never omit newly added technical elements or custom code. For documentation-only tasks, state that website/editor/runtime checks are not applicable and report document/Git verification instead; this standard never authorizes a WordPress change or unnecessary test.

Follow the [implementation report template and completion gate](docs/WORKFLOWS.md#mandatory-final-implementation-report). A milestone is not complete until its complexity review, evidence-backed report, relevant documentation, commit, push and remote verification are handled (or the exact blocker is explicitly reported).

## Evidence and verification

Separate verified repository facts, verified staging reads, reported historical outcomes, and unknowns. Use the [evidence register](PROJECT_CONTEXT.md#evidence-register). Record date, environment, source, IDs, checks actually run, limitations, and remaining work. A report or screenshot does not prove the current saved state or visual editability.

For authorized implementation, capture a recoverable backup first, read back saved values, check the real editor and frontend, responsive layout, keyboard operation, shared-component effects, and independent overrides as applicable. Documentation-only work needs diff, content, path/link, and remote-commit verification; do not invent runtime tests.

Finish using the mandatory six-section report above. Include scoped recovery/rollback information when material. A local commit alone is not a successful push.
