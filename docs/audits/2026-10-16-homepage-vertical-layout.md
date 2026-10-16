# Homepage V2 vertical layout and scroll audit — E9

Observed 2026-10-16, America/Chicago, on staging https://vitaliiv1.sg-host.com/, Homepage **154**. This audit phase was read-only: no layout, content, styles, templates or production changes. The owner subsequently authorized a separate [CTA hierarchy implementation](../milestones/2026-10-16-homepage-cta-strategy.md). The screenshots below show the **pre-CTA-change baseline**; subsequent CTA-only QA reproduced the same section/document dimensions at all four sizes.

## Finding

The desktop composition has a reasonable sequence and useful breathing room. It does not need a rebuild or fewer sections. Mobile feels longer than its present information value justifies: six serial service cards, three serial project examples and a large trust section dominate the scroll, while much of the proof is still explicitly placeholder content. The first priority is useful destinations and approved proof, followed by selective spacing changes. A page-height target alone would not solve those problems.

Measured document length is **6,167px / 6.85 viewport heights at 1440×900**, and **10,413px / 12.34 viewport heights at 390×844**. Neither a 4–6-screen target nor page length is treated as an SEO ranking rule. No visitor analytics or conversion experiment was conducted.

## Method and limits

- Actual IAB frontend DOM, bounding rectangles and computed styles; exact CSS viewport sizes verified against browser layout metrics at zoom 1. All Y positions are document coordinates, not screenshot pixels or scroll-relative positions. Fractional dimensions are rounded to one decimal in tables.
- Fresh normal reload plus a browser-cache-disabled reload. At 900px, cache-disabled dimensions matched the first read exactly. Saved MCP structure matched the visible latest audience cards, six services and native inactive ZIP panel; saved Homepage modification time before CTA edits was `2026-10-16 15:42:20` as returned by WordPress. No server-cache purge was performed.
- Authenticated WordPress session: the 32px desktop/tablet and 46px mobile admin toolbar contributes to document height and Y offsets. This is **not a measured anonymous-session layout**. Screenshots exclude the toolbar strip where possible. Native screenshot rendering can include the logged-in SiteGround assistant overlay; it is not part of the homepage design.
- Header 113 and Footer 114 measured once per viewport in their normal collapsed-menu state. No production action, external lookup, form submission or telephone call was made.
- Native editor Navigator and Service Card override controls were inspected without changing values during the audit. Full edit/save testing was outside the read-only audit; the subsequent CTA milestone separately tests native override editing.

## A. Measurements

Each cell below is **start Y / section height**, in CSS px. Component 80's saved Homepage instance is `37feb023`; its generated rendered section ID changes on reload, so it is identified by its position and heading rather than a generated ID.

| Section / stable saved ID | 1440×900 | 1200×800 | 900×900 | 390×844 |
| --- | ---: | ---: | ---: | ---: |
| Hero `a62cdd3` | 174.9 / 562.9 | 174.9 / 562.9 | 174.9 / 663.4 | 164.9 / 742.3 |
| Residential / Commercial `7b416658` | 737.9 / 752.5 | 737.9 / 752.5 | 838.4 / 715.1 | 907.3 / 995.7 |
| Core Services `38ed6da4` | 1490.4 / 843.7 | 1490.4 / 843.7 | 1553.5 / 1055.1 | 1902.9 / 1855.5 |
| Emergency CTA `6cde656f` | 2334.1 / 150.4 | 2334.1 / 150.4 | 2608.6 / 230.3 | 3758.4 / 353.8 |
| How We Work `4681b8f5` | 2484.4 / 472.6 | 2484.4 / 472.6 | 2839.0 / 657.1 | 4112.3 / 944.6 |
| Projects / Before & After `4221ba60` | 2957.1 / 860.4 | 2957.1 / 860.4 | 3496.1 / 1353.4 | 5056.8 / 1702.5 |
| Why GCPRO + Testimonials `5b2c6d3c` | 3817.4 / 993.1 | 3817.4 / 993.1 | 4849.5 / 1031.9 | 6759.3 / 1623.8 |
| Service Areas + ZIP `7d8c17ad` | 4810.6 / 474.9 | 4810.6 / 474.9 | 5881.4 / 547.9 | 8383.2 / 843.8 |
| Final CTA `37feb023` | 5285.5 / 458.9 | 5285.5 / 458.9 | 6429.3 / 454.3 | 9227.0 / 427.4 |

| Overall measurement | 1440×900 | 1200×800 | 900×900 | 390×844 |
| --- | ---: | ---: | ---: | ---: |
| Document height | 6167 | 6167 | 7307 | 10413 |
| Admin toolbar height | 32 | 32 | 32 | 46 |
| Header Y / height | 32 / 142.9 | 32 / 142.9 | 32 / 142.9 | 46 / 118.9 |
| Footer Y / height | 5744.4 / 423.1 | 5744.4 / 423.1 | 6883.6 / 423.1 | 9654.4 / 758.9 |
| Full document / viewport height | 6.85 | 7.71 | 8.12 | 12.34 |
| Footer start Y / viewport height | 6.38 | 7.18 | 7.65 | 11.44 |
| Scroll offset when Footer first enters bottom edge | 4844.4 | 4944.4 | 5983.6 | 8810.4 |
| Horizontal overflow (`scrollWidth > innerWidth`) | No | No | No | No |

The document fits the same 1200px outer container / 1136px inner content at 1440 and 1200, explaining identical desktop heights. At 900px the service grid has two columns, process two, and projects two plus a second-row third card. Mobile uses one column throughout these grids.

### Measured spacing

| Section | Top / bottom padding at 1440, 1200, 900 | Top / bottom at 390 | Important internal gaps / geometry |
| --- | --- | --- | --- |
| Hero | 96 / 96 | 56 / 56 | Hero grid 48px desktop, 32px tablet/mobile; copy stack 24px desktop/tablet, 16px mobile; media 16:9 |
| Residential / Commercial | 96 / 96 | 56 / 56 | Section stack/grid gap 24px, mobile 16px; image 16:9; body padding 32px, mobile 24px; two 450.1px cards at desktop |
| Core Services | 96 / 96 | 56 / 56 | Grid gap 0 desktop/tablet, 16px mobile; each service card padding 24px, internal gap 16px; links retain 44px minimum height |
| Emergency CTA | 32 / 32 | 56 / 56 | Split layout gap 32px; action gap 16px desktop/tablet, 8px mobile; mobile section padding overrides strip's compact intent |
| How We Work | 96 / 96 | 56 / 56 | Process grid gap 24px at all four sizes; feature gap 16px and bottom padding 24px; numbers 24px desktop/tablet, 22px mobile |
| Projects | 96 / 96 | 56 / 56 | Grid 24px desktop/tablet, 16px mobile; comparison 4:3 with 1px divider; summary padding 24px/gap 16px |
| Why + Testimonials | 96 / 96 | 56 / 56 | Two-column grid 24px, mobile stacked 16px; lists 24px, mobile 16px; feature/testimonial internal gap 16px |
| Service Areas + ZIP | 96 / 96 | 56 / 56 | Main grid 24px, mobile 16px; city gap 8px; ZIP panel gap 16px, padding 32px/mobile 24px; input/button 52px |
| Final CTA | 96 / 96 | 56 / 56 | Inset navy panel padding 48px/mobile 24px, gap 32px; action gap 16px/mobile 8px |

The nine sections together contain 1600px of outer vertical padding on desktop/tablet and 1008px on mobile. This is measured padding, **not automatically wasted space**. Between the last audience card and Core Services heading, two adjoining white sections produce a 192px desktop/tablet separation and 112px mobile separation.

## B. Scroll and visitor flow

| Important content, document Y | 1440×900 | 1200×800 | 900×900 | 390×844 |
| --- | ---: | ---: | ---: | ---: |
| First Header Request Service CTA, baseline `#` | 96.9 | 96.9 | Hidden | Hidden |
| Hero first CTA, baseline Request Service `#` | 589.3 | 589.3 | 621.3 | 509.3 |
| Hero actionable telephone CTA, baseline secondary | 589.3 | 589.3 | 689.9 | 569.9 |
| Core Services heading top | 1586.4 | 1586.4 | 1649.5 | 1958.9 |
| Scroll offset when Core heading first enters bottom edge | 686.4 | 786.4 | 749.5 | 1114.9 |
| First Core Services card top | 1696.8 | 1696.8 | 1755.3 | 2097.3 |

Footer start Y divided by viewport height is a location metric, not a number of mouse-wheel gestures. On mobile the Footer begins within the twelfth screenful; its top first appears after about 10.44 viewport heights of scrolling because the visible viewport itself covers the preceding screenful. Core's heading begins at 2.32 viewport heights and first enters after 1.32 viewport heights of scrolling.

- **First screen:** the heading establishes property restoration and Chicago. Residential/commercial scope is explicit. Both Hero actions are visible at every tested size. Calling already has a real telephone destination, while Request Service does not. Making Call primary is a conversion improvement rather than a page-length fix; it was implemented in the later authorized milestone.
- **Early scroll:** the two audience cards provide an understandable choice and match the owner's approved reference. Their combined height is driven by useful 16:9 media and mobile stacking, not empty minimum-height containers. The large white-to-white boundary delays services unnecessarily. All category/service destinations are still placeholders, so discoverability currently stops at the click.
- **Middle:** emergency strip, process, projects and proof have distinct jobs. Repeated calls at Hero, emergency support and the page end are useful checkpoints; removing them just to reduce button counts is not warranted. Process is understandable, with no extra checkmarks on numbered steps. Projects and trust have substantial visual weight but cannot yet establish real credibility because evidence is pending.
- **Bottom:** eight city choices, directory action and clearly inactive ZIP panel are legible and neatly stacked. Their position is late primarily because of preceding sections. Final CTA and Footer retain telephone access. No fake ZIP coverage results were displayed.

## C. Section assessment

| Section | Assessment / action |
| --- | --- |
| Hero | Height justified by three-line H1, short lead, two actions and responsive media. Keep heading, image ratio and layout. CTA hierarchy was the meaningful issue, not excess Hero height. |
| Residential / Commercial | Balanced owner-approved cards. Do not discard imagery or replace with dense text rows. Selectively reduce the trailing boundary to Core Services; preserve card geometry. |
| Core Services | Six services justify the section, but repeating 24px card padding plus 16px internal gaps is expensive across six mobile rows. Keep all six services, text links and readable type. |
| Emergency CTA | Excellent compact desktop contrast/reset at 150.4px. At 900px stacking is natural. A real alignment defect exists: split-row zero padding overrides container gutters at desktop/tablet. Heading X is 120 instead of 152 at 1440, and 0 instead of 32 at 1200/900. Mobile X=20 is correct. Mobile 56px top/bottom also loses the intended compact-strip treatment. |
| How We Work | 472.6px desktop and 944.6px mobile are largely real four-step content. The grid's serial mobile layout is justified. Do not use smaller body type or hide steps to reach an arbitrary target. Await approved process descriptions before more compression. |
| Projects | Desktop three-card row is proportionate. Tablet's 2+1 grid adds a genuine second row, leaving an empty column beside the third card. Mobile has three 262.5px media blocks (787.5px total). These are intentional geometry for eventual proof, not six independent oversized backgrounds. Do not force three narrow tablet columns or remove a project solely for height. |
| Why + Testimonials | Largest desktop section (993.1px), nearly two mobile screens (1623.8px). Three generic benefits, three credential/source notices, two placeholder reviews and an approval note currently repeat administrative/pending content. It is mostly a content-value problem, not a huge blank container. Keep the roles but resolve proof before final spacing decisions. |
| Service Areas + ZIP | Already appropriately compact: 474.9px desktop including 192px section padding. The native panel is 272.1px desktop. Mobile's 843.8px is explained by eight 44px city targets, directory link and stacked panel. Preserve input font, 52px controls, disabled button and future-feature notice. |
| Final CTA | Useful closing action but outer white padding plus inset panel padding creates an avoidable double frame. Keep both actions and panel; reduce only the outer frame if approved. |

## D. Prioritized optimization plan — proposals, not implemented

Current heights are measured at **1440 / 900 / 390px**; 1200 matches 1440. Savings below are **estimates**, not measured post-change results. Shared-class changes require consumer checks before implementation. Rows overlap; do not add every estimate into a promised total.

| Priority / section | Current height D / T / M | Specific proposed change | Estimated reduction D / T / M | Impact / native path |
| --- | --- | --- | --- | --- |
| Essential: conversion destinations, Hero/Final/Header | Hero 562.9 / 663.4 / 742.3; Final 458.9 / 454.3 / 427.4 | Use verified telephone target; document absent Request Service instead of inventing a route. Later authorized CTA milestone changes the two Homepage pairs only. | 0 / 0 / 0px | Better action clarity at every size. Existing Component 53/103 and Component 80 overrides; no layout change. |
| Essential: Emergency alignment | 150.4 / 230.3 / 353.8 | Restore container horizontal gutters where split-row padding resets them. Retain current mobile 20px gutter. | About 0 / 0 / 0px | Prevents flush-edge copy/buttons at 1200/900; restore native class responsibility/priority, no new selector or component. Recheck wrapping after correction. |
| Essential before launch: trust/proof and service destinations | Trust 993.1 / 1031.9 / 1623.8; services 843.7 / 1055.1 / 1855.5 | Obtain approved capability evidence, attributable reviews, credentials and real destinations; resolve repeated approval notices editorially after approval. | Not reliably estimable until approved material exists | Makes scrolling valuable. No invented copy/credentials; retain nine-section sequence. |
| Recommended: audience-to-Core boundary | Audience 752.5 / 715.1 / 995.7; Core 843.7 / 1055.1 / 1855.5 | Reduce only audience bottom and Core top from 96 to 64px desktop/tablet, 56 to 48px mobile. Resulting shared white boundary 128/96px instead of 192/112px. | 64 / 64 / 16px combined | Earlier service discovery without shrinking approved cards. Reuse existing section modifiers/native responsive padding; inspect the existing section--compact definition and consumers before applying. Do not change global section spacing indiscriminately. |
| Recommended: Core card rhythm | 843.7 / 1055.1 / 1855.5 | Trial existing service-card vertical padding 24→16px, internal gaps 16→8px; keep horizontal padding, font sizes and 44px links. | About 80 / 120 / 240px | Most useful mobile reduction; 2/3/6 service rows. Existing class only; verify all Component 62 consumers and visual breathing room. Revert if rhythm becomes dense. |
| Recommended: Final CTA outer frame | 458.9 / 454.3 / 427.4 | Trial outer section padding 96→64px desktop/tablet and 56→40px mobile; retain inset panel padding and controls. | About 64 / 64 / 32px | Removes a double frame rather than useful copy spacing. Existing section modifier/native tokens; shared Component 80 consumer review required. |
| Optional: Emergency mobile strip | 150.4 / 230.3 / 353.8 | Preserve compact variant at mobile with 32px top/bottom rather than inherited 56px. | 0 / 0 / about 48px | Keeps call checkpoint compact while retaining both 52.5px actions. Existing section--strip responsive controls, after gutter correction. |
| Optional: Projects media crop | 860.4 / 1353.4 / 1702.5 | Only if approved photographs work at 16:9, trial comparison-media 4:3→16:9. Keep all three examples and both static Before/After panels. | About 68 / 152 / 197px | Two tablet rows and three mobile rows benefit. Existing native aspect-ratio control; preserve 4:3 if evidence/cropping suffers. Not the first change. |
| Optional after content approval: trust list rhythm | 993.1 / 1031.9 / 1623.8 | Trial existing stack--compact on benefits/review list wrappers (24→16px desktop/tablet); mobile already has 16px list gaps. | About 16 / 16 / 0px | Minor desktop gain only; not worth a new abstraction. Do not shrink text or remove approved reviews. |
| Unchanged: Hero, audience cards, process, ZIP geometry | See measurement table | Preserve layouts, content hierarchy, typography, image ratios and form control targets. | 0px proposed | These structures already have a clear role. No accordion, slider, new component or dependency is justified. |

A first restrained pass on the boundary, Core cards and Final outer frame would estimate roughly **208px desktop, 248px tablet and 288px mobile** saved, excluding optional/overlapping changes and future text reflow. This is a proposal to test, not an achieved result or required page-length target. The savings are deliberately modest: much of the mobile length represents real stacked content. Approved proof may matter more than further compression.

## E. Architecture and simplicity

- Fresh saved Homepage tree: **148 nodes**, **36 Component instances**, including six Component 62 service cards, seven Component 65 feature/process instances, three Component 68 project summaries, two Component 86 testimonials and one Component 80 CTA. Fifteen reusable definitions exist in the library; no duplicate definition was demonstrated just by their names/variant count. Five button variants serve distinct contexts; no new variant is needed.
- Rendered Homepage subtree: **276 descendant DOM elements**, maximum **10 levels** below its page wrapper. This is an observed count, not a speed score or proof of a performance problem. Single-child wrappers commonly provide container width, aspect ratio, circle geometry or native SVG rendering; do not remove them mechanically.
- Possible low-value wrappers for later review: one-link clusters `7c435ce4` and `62862a3a`, and the three single-paragraph trust placeholder wrappers. They are not causing hundreds of pixels of whitespace. Flatten only when native parent controls retain their layout role and after shared-consumer review. Keep native Form status slots required by Atomic.
- **83 unique Global Class labels**, same **36 variables**. Loaded shared CSS contains redundant declarations within existing classes (e.g. repeated focus-visible definitions on button classes, repeated navigation padding/white-space rules, info-bar underline then no-underline). This is cascade debt, not evidence that an entire Global Class is safely deletable. No complete site-wide usage/declaration comparison of all unused classes was performed; no deletion list is justified.
- Existing hidden/coupled behavior is real: icon-svg uses `:has(+ .card-icon:not(:empty))` to hide graphical icons when a process number exists; navigation--primary hides a specific menu-item ID. These are pre-existing centralized nested rules, not new code from this audit. Preserve the number/icon contract until a separate native visibility review.
- The 148 returned Homepage nodes have no nonempty `styles` arrays. Several generated `e-*` local class identifiers remain attached; this normalized API is not proof that every class/default/site document is free of legacy styling. The currently loaded local-114 stylesheet contains a 200px Footer image width rule. Fifteen SVG elements have Elementor-generated inline width/height/overflow attributes; these are runtime SVG output, not evidence of manually added inline CSS.
- Nine visible media placeholder blocks represent Hero, two audience images and six Before/After halves; plus three text credential/source notices and two explicitly placeholder testimonials. Their amount is substantial for a live credibility story, but their geometry is useful during structural review. Replace with approved material before judging final proof density; do not build sliders or generate stock claims to fill space.
- The authenticated page loads WordPress/Elementor editor/admin assets, SmartMenus, Atomic Form handler, SiteGround AI chat and four Google Font stylesheet requests (Roboto, Roboto Slab, Inter, Montserrat). Visible Homepage heading/body/button families are Montserrat/Inter. Roboto-family requests are a candidate for an **anonymous-session** dependency review, not an instruction to remove global fonts. Login-only assets cannot be labeled public-page overhead from this session. No timing/transfer/CWV benchmark or plugin uninstall recommendation is established.
- All proposed geometry changes can use existing Atomic classes, native spacing/aspect-ratio controls and current variables. No new Global Class, Variable, Component, plugin, custom CSS, PHP or JavaScript is needed for this plan. Read saved definitions/consumers before any later edit.

## F. Visual evidence and verification

[Machine-readable measured values](../evidence/2026-10-16-homepage-vertical-layout.json).

Full-page captures, **pre-CTA baseline**, no image stitching:

- [Desktop 1440×900](../evidence/2026-10-16-homepage-vertical-layout/full-desktop-1440.jpg)
- [Mobile 390×844](../evidence/2026-10-16-homepage-vertical-layout/full-mobile-390.jpg)

Relevant actual section crops:

- [Desktop trust/proof](../evidence/2026-10-16-homepage-vertical-layout/desktop-trust.jpg)
- [Mobile services](../evidence/2026-10-16-homepage-vertical-layout/mobile-core-services.jpg)
- [Mobile projects](../evidence/2026-10-16-homepage-vertical-layout/mobile-projects.jpg)
- [Mobile Service Areas/ZIP](../evidence/2026-10-16-homepage-vertical-layout/mobile-service-areas.jpg)

All four exact viewport sizes were measured and visually reviewed. One H1 and no document horizontal overflow at each size. Natural multiline headings remain readable; no fixed empty full-screen section was found. ZIP button is natively disabled; no lookup/form submission was attempted. White 16px/600 CTA text on fixed orange computes about **3.39:1** contrast; accessible brand-preserving treatment remains unresolved. Header/Footer were inspected, not changed during the audit. Physical-device touch, screen-reader flow, anonymous-session layout/performance and a full backup/restore were not tested.

**Approval checkpoint:** spacing, gutter, media-crop and proof recommendations remain proposals. The later owner-authorized CTA changes do not authorize implementing the other recommendations.
