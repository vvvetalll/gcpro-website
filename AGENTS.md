# GCPRO agent instructions

## Start here

Read [PROJECT_CONTEXT.md](PROJECT_CONTEXT.md), [CHANGELOG.md](CHANGELOG.md), and the relevant files in [docs](docs/WORKFLOWS.md) before working. Recheck the target, current Git state, and live evidence; this documentation is a dated handoff, not a live mirror.

## Permanent boundaries

- Never modify production. The only designated implementation environment is GCPRO staging: https://vitaliiv1.sg-host.com. Verify the connection actually targets that host before any staging action.
- Repository work belongs in https://github.com/vvvetalll/gcpro-website. Keep GCPRO content, page IDs, design values, and implementation records here.
- The shared [ROBYLO repository](https://github.com/vvvetalll/robylo-website-starter) is a separate product. Read it as a dependency; do not change it or copy client-specific documentation into it without a separate task authorizing that scope.
- This initialization task authorizes documentation, commit, and push to GCPRO main only. It authorizes no WordPress writes, theme changes, deployment, plugin installation, or production action. Future agents must use the scope of their own task.
- Preserve unrelated changes. Never force-push, reset others' work, or commit credentials, customer data, database dumps, or private backup archives.

## Native visual editing

Prefer native WordPress and Elementor Atomic V4 controls, responsive settings, Global Variables, Global Classes, and reusable Components. Keep text, images, SVGs, links, typography, spacing, backgrounds, and responsive behavior understandable and editable in the visual editor.

Reuse existing variables/classes before adding new ones. Use supported Component Overrides for instance content; edit the shared definition only when all consumers should change. Give Navigator elements and classes clear names. Inspect the current component schema before assuming an override exists.

Avoid hidden CSS, JavaScript, HTML-widget workarounds, fragile selectors, direct database edits, and undocumented customizations. Do not create parallel design tokens or layouts in theme code. If native controls cannot meet the requirement, document the demonstrated gap, propose a simpler editable alternative, and obtain authorization for any additional code scope. Record the exact location, purpose, affected classes, and rollback of an authorized exception.

Discover actual connector capabilities and schemas. Tool presence is not a successful staging test. Read fresh structure before changes and after saves; never reuse stale element trees after another write. Do not infer IDs from labels or copy IDs between installations.

## Responsibilities and milestone completion

Codex owns repository documentation, Git, verification, and any separately authorized integration code. ChatGPT Work owns authorized staging Elementor configuration. These roles do not grant access or authorize changes.

**ChatGPT Work MUST update this repository's documentation after every meaningful implementation milestone, before calling the milestone complete.** This includes page/component changes, global style changes, navigation, templates, integrations, or significant fixes. Update PROJECT_CONTEXT and CHANGELOG plus every affected reference document; follow the [milestone matrix and handoff](docs/WORKFLOWS.md). If Work cannot write the repository, provide an exact documentation patch/handoff to Codex and keep documentation synchronization explicitly pending until the commit is verified.

## Evidence and verification

Separate verified repository facts, verified staging reads, reported historical outcomes, and unknowns. Use the [evidence register](PROJECT_CONTEXT.md#evidence-register). Record date, environment, source, IDs, checks actually run, limitations, and remaining work. A report or screenshot does not prove the current saved state or visual editability.

For authorized implementation, capture a recoverable backup first, read back saved values, check the real editor and frontend, responsive layout, keyboard operation, shared-component effects, and independent overrides as applicable. Documentation-only work needs diff, content, path/link, and remote-commit verification; do not invent runtime tests.

Finish with changed files/IDs, checks and results, custom-code exceptions, documentation commit URL and push status, and outstanding verification. A local commit alone is not a successful push.
