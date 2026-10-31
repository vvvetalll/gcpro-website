# Partner Programs — Draft structure and prepared navigation

**Current2026-10-24:**982–986 have completed native Hero1318/Heading71 bodies, documented program context, page-specific SEO and native service/contact links. Already Published before this task; all five republished and desktop/mobile checked. Earlier Draft/structural records below are historical. [Current record](page-completion-2026-10-24.md).

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


## Customer insurance support — owner confirmation, 2026-10-31

Distinct from Agent Program984: Vitalii explicitly confirmed damage documentation/photos, written restoration estimates and adjuster communication for residential and commercial customers. Existing Insurance Component3796 now published on Home154 as4ebf7d5d after Services; source69325bdd/gridfdb5ecf uses shared Heading71+accent, global orange-dot eyebrow, native Button59 bound to Contact Us496 and three editable native heading/paragraph groups. Desktop two columns, mobile stacked; local Atomic spacing/grid and sentence-case point text, existing brand tokens/classes, no JS/plugin/shared-definition edits. CTA navigation and desktop/native-mobile rendering checked; no free-estimate, billing, insurer-acceptance or coverage/approval promise. Exact approved copy and recovery/verification scope: docs/content/HOMEPAGE_COPY_PROPOSAL.md, latest insurance checkpoint. Earlier factual hold is superseded only for those three confirmed support services.

Owner visual refinement in the same task: Insurance3796 root69325bdd uses existing color-surface-alternate (#EFF6FF) to separate it from the adjacent white Services and Before/After sections; typography, native layout and CTA unchanged.


## Insurance visual refinement — 2026-10-31

Published existing Insurance3796 on Home154 in its unchanged position/light-blue surface: left Heading71/introduction/Button59→Contact Us496 preserved byte-for-byte; right69a4a2ba now holds three compact white native cards2c9b21c2/35d2c961/44952f64, reusing card styling with16px padding,8px corners,1px color-border, no shadows, navy600/16px Montserrat headings at all breakpoints and dark16px descriptions (approved copy unchanged).
Individual Flaticon Uicons Regular Rounded SVGs: [File image10469600](https://www.flaticon.com/free-icon-font/file-image_10469600)→3863, [Calculator3914400](https://www.flaticon.com/free-icon-font/calculator_3914400)→3864, [Comments5070422](https://www.flaticon.com/free-icon-font/comments_5070422)→3865; native e-svg controls24×24px/color-accent, no icon backgrounds, no library/plugin/custom controller or component detachment, with native card-grid/text/icon styles stored only in3796.
Staging desktop and Elementor Mobile Portrait checked: white cards/no shadows,16px headings,24px orange icons, mobile cards303px client/scroll widths without overflow and natural stacking; Contact Us destination retained, Elementor generated files refreshed after stale CSS, no physical-device/anonymous-cache certification claimed; restore3796's prior right-hand children for rollback, preserving its left side, Home instance and all other components.


## Insurance composition correction — 2026-10-31

Published native layout-only edits in existing Insurance3796: fdb5ecf is a single-column24px-gap stack, introduction59b439ca is left-aligned/max720px with its existing CTA beneath, and69a4a2ba is an equal three-column16px-gap card grid that becomes one column on mobile; existing cards now stack icon→heading→description, without shadows or fixed heights.
Latest owner correction uses color-text graphite headings and color-primary navy24px icons; approved wording, Heading71/Button59→native Contact Us496, light-blue background,16px typography,8px corners,16px card padding, existing component/element IDs and page position retained, with no Home/Services/other component writes.
Desktop confirmed three368px cards with equal154.8px natural height and720px introduction; native Elementor Mobile Portrait confirmed305px single-column grid/cards303px client=scroll widths, and CTA's frontend destination remains /contact-us/; restore only the six layout styles and six heading/icon color values for scoped rollback, with no detach/new section/class/plugin/code owner.


## Approved open-column Insurance layout — 2026-10-31

Applied the approved separate visual proposal to existing Insurance3796 only: native introduction59b439ca now has Heading71/copy left (max690px) and existing Button59→Contact Us496 right; below,69a4a2ba has three equal open columns, preserving original copy, SVG assets3863–3865,16px typography, light-blue background and homepage position.
Removed only the three points' card class/local surface/border/radius/padding, retained natural icon→heading→description order, and matched the accepted mockup's orange24px icons/navy bold headings; native32px desktop grid gaps and24px mobile gaps, no new elements/component/class/plugin/JS or homepage/Services writes.
Saved readback confirms all element IDs/copy/icon bindings unchanged; actual Elementor desktop showed three357.3px columns, transparent/no-border/no-shadow points and right-aligned CTA, Mobile Portrait showed one305px column with all point scrollWidth=clientWidth and CTA after introduction, existing contact destination retained; physical-device/anonymous-cache acceptance not claimed, scoped recovery restores only3796's prior local styles and three card-class assignments.


## Separate Insurance photo-composition review draft — 2026-10-31

Created unpublished Canvas Page3872, root7ad9fd/grid6b617040, solely for owner's two-column Insurance review: neutral native placeholder5b54bb78 occupies40% beside text326e12e6 at60%, using existing Heading71/accent and Button59→Contact Us496 with the approved introduction and three simple16px text rows; no icons, cards, photos, generated/stock media or new shared component.
Native grid/order/aspect-ratio and existing container/tokens keep the placeholder approximately4:5 on desktop and4:3 on mobile, where text/CTA precede the placeholder; actual desktop frontend shows orange-dot/line and435px/653px columns, native Elementor Mobile Portrait shows text first and305px client=scroll width.
Review only: [draft preview](https://vitaliiv1.sg-host.com/?page_id=3872&preview_id=3872&preview=true) and [native editor](https://vitaliiv1.sg-host.com/wp-admin/post.php?post=3872&action=elementor); never published/placed on homepage, Home154 and Insurance3796 untouched, and no physical-device or public-route acceptance claimed.


## Homepage Insurance photo/text layout published — 2026-10-31

Updated existing Insurance3796/root69325bdd and its unchanged Home154 instance in place, using native40/60 gridfdb5ecf: existing shared Heading71/approved introduction, three retained text rows and Button59→Contact Us496 are grouped in59b439ca; support gaps reduced24→16px, three SVG elements removed, no cards/shadows/numbers.
New neutral photo-area container59652a97 (Navigator “GCPRO team photo placeholder — replace using Background image”) uses existing color-border and native Background image controls for the future real owner-supplied photograph; no image sourced/generated/uploaded, no desktop height/min-height/aspect ratio, stretching only to469px text height, while mobile text/CTA precede its4:3 placeholder.
Published staging only: saved copy/CTA bindings match prior values, actual desktop435.2/652.8px columns/equal content height and native Elementor Mobile Portrait305px client=scroll width/text-first order checked; retained light-blue background/orange heading accent/section position, with no Home tree/neighbour/shared-heading/button/draft3872 edits; rollback restores pre-change3796 tree and removes only the new placeholder, and physical-device/anonymous-cache verification is not claimed.


2026-10-31 owner alignment correction: preserved the existing stacked point headings/descriptions, approved copy, supplied native image77f7c37 and all other styles; only Insurance3796 text container59b439ca now distributes its three content groups with native justify-content:space-between (mobile:flex-start), matching the photo's natural height, with desktop539px text/photo heights and top/button-bottom differences0px verified; the temporary text-row typography/layout trial was fully reverted.
