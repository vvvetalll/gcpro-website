# Shared GCPRO Hero — blocked native media migration

Status: **NOT IMPLEMENTED; original pages restored**. Date:2026-10-22, staging only. No SEO research, service copy, production change or bulk service population.

## Authorized scope and existing designs

Only Homepage (154), Residential Restoration Services in Chicago (484), Commercial Restoration Services in Chicago (499), and the existing residential Water Damage page (514) were mutation targets. Other service pages remain untouched. The published page titles/parents were read from WordPress; numeric IDs below are implementation locators, not manually entered link destinations.

Approved Home uses a1:1.15 grid,48px gap,64px desktop/48px mobile section padding, no media caption and a suppressed fullscreen button. Residential/Commercial use the same equal-column design with24px grid gap,96px desktop/56px mobile section padding and page-specific captions. Native widget schemas expose content properties, not responsive style variants. Maintaining these exact existing differences would require two actual design variants rather than a silent redesign; future genuinely different designs should also be attached variants, never detached page copies. This does not establish that separate designs are mandatory forever.

## Confirmed blocker

1. Direct MCP authenticated from `/root/mcp-config.json`; initialization and native component create/update/place/publish operations succeeded. No credential was retrieved from conversation history. Credentials and raw private responses are not committed.
2. `elementor-manage-component` rejected an attempted native property on the existing V3 Shortcode widget: `[media_shortcode] Invalid element: Element type widget with widget type shortcode is not an atomic element/widget.` This is an observed limitation of the currently exposed Atomic/MCP property path, not proof that every future Elementor version or every editor extension lacks slots.
3. A native Atomic Paragraph with Dynamic Tags → Shortcode accepted per-instance BEAF shortcodes, but frontend sanitization stripped the comparison's image/div/script/style markup and exposed residual stylesheet text. The captured DOM had zero Hero images and zero initialized slider handles. A schema accepting a dynamic tag did not establish a safe arbitrary-HTML media slot.
4. Therefore the tested native path does **not** safely preserve independent Before/After content in a shared Atomic Hero. No custom HTML/CSS/JS renderer, plugin, security bypass or duplicated fixed-media component per page was introduced as a solution. No successful global-structure propagation or page-content isolation test is claimed.

The blocker affects Home's existing Tinley Park comparison723, Residential's Glenview742 and Commercial's entrance1209. Water has no existing approved Hero description/media; its brief test used only its existing title, empty description/media and telephone/native Service Request reference, then was withdrawn. Its body/template/builder/page settings were restored. No default service copy or another page's project image was left on Water.

## Final saved state and recovery verification

The three original Hero subtrees are restored at Home/a62cdd3, Residential/5357c5f3 and Commercial/971dcf76. Published page bodies compare equal to their captured pre-task JSON. Native saving had normalized two ampersands in Residential service-card labels; those serialization differences were also restored. The Home Request Service placeholder remains its original known pending issue; this failed architecture attempt must not be reported as fixing all Hero destinations.

Water's original empty Elementor body, editor-mode metadata, page settings and WordPress template were restored through registered WordPress REST fields. No other service page was written. The unrelated74 starter Hero and existing53/103/286 components were not changed. BEAF records, Kit6, plugin code and approved other sections were not edited. Private recoverable page/component snapshots remain outside Git; no full database restore test is claimed.

Restoring registered Elementor data alone initially left cached rendered HTML from the test. Native Elementor Tools → Clear Files & Data and SiteGround toolbar cache purge were required. Final authenticated browser observations:

| Page | Width | Original Hero height px | Restored height px | Images / initialized handles | Horizontal overflow |
|---|---:|---:|---:|---|---|
| Home |1440|564.4375|564.4375|2 /1|none|
| Residential |1440|647.390625|647.390625|2 /1|none|
| Commercial |1440|647.390625|647.390625|2 /1|none|
| Home |393|730.265625|730.265625|2 /1|none|
| Residential |393|791.046875|791.046875|2 /1|none|
| Commercial |393|839.046875|839.046875|2 /1|none|

These are desktop-browser viewport checks, not physical-device tests or independent anonymous certification. Slider initialization was observed; no new claim of exhaustive drag/keyboard/fullscreen testing is made. Final layouts and assets match the baseline; the shared architecture completion criteria remain unmet.

## Unused prototypes — do not use

Two test Atomic definitions remain unreferenced after rollback:1318 `GCPRO / Service Split Hero` and1321 `GCPRO / Home Split Hero`. Both preserve native existing classes/variables and nested existing buttons/emergency mark, with content/link/media properties; their dynamic-shortcode media rendering is unsuitable. The Home prototype retained the original fullscreen-suppression declaration during the test; it is not active on a migrated page. There are no active new Hero classes, variables, custom scripts, plugins, dependencies or media assets. These prototypes are **not** a delivered reusable system.

- [Unused Service prototype editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1318&action=elementor)
- [Unused Home prototype editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=1321&action=elementor)

Automatic approval review rejected archiving the two newly created definitions as a separate destructive cleanup action. No alternate deletion/archiving route was attempted; they are left unused and documented. Cleanup remains pending explicit authorization under that review boundary.

## Continuation boundary

A viable native implementation must first demonstrate a supported unsanitized media/slot property that can retain the existing BEAF widget and vary its content independently. That capability was not demonstrated here. Do not claim shared Global Classes or these unused prototypes complete the task. Do not copy the failed Paragraph/Shortcode path into service pages. Do not resume rollout, redesign or Water content work from this record without a new authorized implementation step.
