# Partner Programs — Draft structure and prepared navigation

**Current E75 (includes pending E74 sync), 2026-10-21:** Staging structural publication:92 Pages,87 Published/5 Draft;84 newly published approved targets including Resources1007,51 city Pages and Partner982–986. Native shared Single Page1008 supplies79 structural placeholders. Final service-first Header113:five main sections (Residential/Commercial/Service Areas/Projects/About), utility Partner Programs with four children/Careers/Contact Us; Blog and Our Team await real staging destinations. Standard1200px grid/logo sizes retained, native toggle below1200, one complete mobile menu. No production/BEAF/Footer/Homepage-content/903 edits.321 canonical migration rows preserve prior source mappings/decisions. [Exact storage, tests, limitations and rollback](../audits/2026-10-21-staging-structure-and-navigation.md) · [Actual hierarchy](../SITEMAP.md).

E73,2026-10-21. Staging only. Parent and four child Pages created with native WordPress title/slug/parent/status controls after an all-status conflict scan. No existing Page renamed, moved, deleted or published. All five remain **Draft** and contain minimal headings only; content/design are unfinished.

## Actual Pages, native controls and preview links

| Page | ID / admin | Intended route under staging | Authenticated preview |
| --- | --- | --- | --- |
| Partner Programs | [982](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=982&action=edit) | `/partner-programs/` | [Preview982](https://vitaliiv1.sg-host.com/?page_id=982&preview_id=982&preview=true) |
| Plumber Support Program | [983](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=983&action=edit) | `/partner-programs/plumber-support-program/` | [Preview983](https://vitaliiv1.sg-host.com/?page_id=983&preview_id=983&preview=true) |
| Insurance Agent Program | [984](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=984&action=edit) | `/partner-programs/insurance-agent-program/` | [Preview984](https://vitaliiv1.sg-host.com/?page_id=984&preview_id=984&preview=true) |
| Condominium / HOA Program | [985](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=985&action=edit) | `/partner-programs/condominium-hoa-program/` | [Preview985](https://vitaliiv1.sg-host.com/?page_id=985&preview_id=985&preview=true) |
| Commercial Partnership Programs | [986](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=986&action=edit) | `/partner-programs/commercial-partnership-programs/` | [Preview986](https://vitaliiv1.sg-host.com/?page_id=986&preview_id=986&preview=true) |

982 has parent0;983–986 have native parent982. Native GET after creation and final editor initialization confirmed statuses/slugs/parents. No slug suffix/collision. Intended pretty paths are not public routes while Draft. [Full hierarchy](../SITEMAP.md), [canonical URL register](../SEO_URL_INVENTORY.csv).

Every Page reuses existing `section` and `container` classes and the existing H1/default typography tokens. Exactly3 Atomic nodes per Page: section → container → H1. Native Full Width page layout (`elementor_header_footer`) and Hide Title=yes prevent a second theme title while preserving existing Header/Footer. Opened each actual native Elementor editor to initialize the builder: a REST-created blank Page initially emitted fallback unstyled markup until native editor initialization. This was corrected and final previews render the Atomic root with Montserrat H1. No plugin/runtime workaround or duplicate content was added.

| Page | Section → Container → H1 |
| --- | --- |
|982|2caf1a1f →1ee9ecbf →364b538d|
|983|1ae186d0 →30670ad0 →48638b57|
|984|4d98dba8 →7dd78c7f →5539dc73|
|985|4e177a13 →30c0bf06 →900adb8|
|986|46ee9215 →3e16e507 →75e6c1c|

[Exact saved native structures](../evidence/2026-10-21-partner-atomic-settings.json). No local CSS, JS/PHP, Custom Code ID, new Global Class/Variable, library Atomic Component, media, plugin or external dependency. Existing15 native nodes are sufficient; no experimental template or duplicated homepage created. Existing Header113/Footer114 render by their existing conditions; definitions and assignments were not modified. BEAF/Homepage/Core/Code903 untouched.

## Program-name verification

Read existing GCPRO materials without modifying them: marketing package `GCPRO-Marketing-Project-2026-10-20`, `01_Brand_System/AI_CONTEXT.md` and README confirm **PSP — Plumber Support Program** and **ASP — Agency Support Program**, the latter for insurance agents. Thus984's owner-requested Insurance Agent Program is the website section label for ASP, not a newly claimed branded program.

`02_Document_Sources/Condo-Coverage/copy.json` confirms condominium/unit-owner/association material. `CSP-Trifold/original-copy.json` and `ERP-Comparison/copy.json` identify **Emergency Response Program**; `PGP-Cover/copy.json` identifies **Property Guardian Program**. These support partner-topic organization, but do not independently establish that “Condominium / HOA Program” and “Commercial Partnership Programs” are formal marketed brand names. Those two headings use the owner's explicit section labels; formal naming and detailed program terms remain for content approval. No benefits, discounts, payment/referral promises, insurance coverage advice or eligibility details were invented or copied into the skeleton.

## Prepared native navigation — not active Header navigation

Native WordPress menu **13**, **GCPRO Partner Programs — Prepared Draft Navigation**: [open its visible hierarchy](https://vitaliiv1.sg-host.com/wp-admin/nav-menus.php?action=edit&menu=13).

| Native menu item | Object reference | Parent item |
| --- | --- | --- |
|987 Partner Programs|Page982|0|
|988 Plumber Support Program|Page983|987|
|989 Insurance Agent Program|Page984|987|
|990 Condominium / HOA Program|Page985|987|
|991 Commercial Partnership Programs|Page986|987|

All links are native `post_type`/`page` object references, not manually typed staging URLs, preview URLs or `#`. WordPress's normal saved menu-item records use publish status; **their target Pages remain Draft** and the native menu UI labels them Draft. This saved navigation metadata does not publish the Pages. The first transient draft-status menu-item records were invisible in the menu editor; normal native saved menu-item status corrected that while keeping target Pages Draft.

Verified actual Menus UI: Pages picker offers only Published Pages; unfinished Partner Pages are unavailable there. Menu13 is therefore prepared and **unassigned**, with Header/Footer locations unchecked and auto-add off. Existing Primary menu5 retains Header/menu-1, existing Header113/menu7983af36 stays unchanged. No broken or unfinished Partner link is exposed to visitors, no sixth visible desktop navigation item or duplicated mobile script introduced. This is a prepared top-level navigation entry, not a claim that Partner Programs is live in the current Header.

After separate content/publication approval: approve public destinations and program labels, publish the completed Pages, then merge the object-based987–991 hierarchy into existing Primary menu5 (do not replace it with this five-item preparation menu). Validate desktop width/dropdown and mobile menu keyboard/touch behavior before assigning/activating; retain other menu items/current functionality. Do not publish empty Pages just to satisfy the picker.

## Verification and recovery

[Browser QA](../evidence/2026-10-21-partner-preview-qa.json): landing360/393/430/768/1024/1440, each child393/1440; one Montserrat H1, native Atomic rendering and horizontal overflow0. Actual editor headings/native tree confirmed. All91 staging Pages reread:88 Draft/3 Published; all86 prior Page fields unchanged. Saved Homepage154/Header113/Footer114 trees exactly equal before/after. Primary menu5 location unchanged. Authenticated Draft previews, not physical-device/incognito/public route certification; no form/call/BEAF/animation regression suite replay claimed because those structures/controllers were not edited.

Menu screenshot: outputs/gcpro-partner-programs-navigation.png. No staging cache purge was necessary for non-public new Drafts and an unassigned menu; no current visitor-rendered layout changed.

Rollback: first check dependencies/content since this record. Keep or move only982–986 to recoverable Trash if explicitly authorized, children before parent; never remove existing Pages. Menu13 is unassigned and can be retained as a preparation record or removed through the normal menu UI only with authorization. No Header/Footer/code rollback is needed. Git revert changes documentation, not WordPress; no full-site restore drill performed.
