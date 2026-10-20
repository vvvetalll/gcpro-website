# Responsive global footer — E67

2026-10-20. Implemented and published only on https://vitaliiv1.sg-host.com. Global Footer114 remains active with include/general. Desktop appearance approved by owner; no BEAF, Header113, Code903, Core Services, preceding CTA, production or shared ROBYLO repository edits.

## Exact saved owners

Footer114 → Footer Shell1687d698 → Container119ffe98 → Columns73b78d01. Existing 36 saved nodes retained; no new widget/Component.

| Owner / local style | Saved change |
| --- | --- |
| Columns73b78d01 child order | Move existing Contacte424c2c before Services39be2867. Order now Identity → Contact → Services; mobile visual and DOM priorities agree. |
| Identity7ac91d92 / e-fdb3237-8a23 | Native grid column1/row1 desktop and tablet; mobile auto/auto. Existing24px gap preserved. |
| Contacte424c2c / e-7b5b31ec-eb16 | Native desktop column3/row1 preserves approved position; tablet column2/row1 instead of full-width second row; mobile auto/auto. Existing8px gap, icons, values, phone/mail/Maps and Component103 preserved. |
| Services39be2867 / e-6077e757-234e | Desktop column2/row1; desktop gap0/space-between preserved. Tablet native two-column grid across full second row,8px space-xs gap. Mobile native flex column, gap0/justify-start. |
| Services Heading7ffa59b5 / e-2f1bfe77-c32f | Tablet grid column1/-1; existing heading and16px bottom margin retained. |
| Existing class gcpro-footer-item / g-aca1669 | Native min-height44px tablet/mobile, across exactly six service paragraphs and three contact Flexbox rows. Existing divider/padding/alignment unchanged; desktop min-height untouched. Edit Design System → Classes → selected breakpoint → Size. |
| Cities5fe71200 / e-6d369c26-c6cb | Existing paragraph retains all12 cities in12 rich-text outer spans with11 nested dot spans. Native tablet grid4 equal minmax columns,8px gap; mobile2 columns. Desktop remains inline dot-separated. |
| Bottom1d11b99e / e-3a3f1a6d-bc52 | Mobile native nowrap flex row,8px gap; desktop/tablet untouched. |
| Copyright Group578307c4 / e-1e6afb39-6123 | Mobile nowrap/flex1; inherited base4px gap/baseline retained without duplicate responsive declarations. |
| Year890602e / e-b20365b-db91 | Mobile native13px/1.5 line height/no shrink; existing native current-date-time Y tag retained. No frozen2026 text. |
| Identity23d35135 / e-63994f17-a62c | Mobile native13px/1.5; full rights text retained; local balanced wrapping below. |
| Top5a520a4e / e-3d1cd11b-276c | Mobile native13px,44px minimum height, flex0/0/auto, flex/center. Existing arrow and full accessible text/link retained; nowrap below. Desktop unchanged. |

IDs above are editor/storage locators, not new authored runtime selectors. Existing shared footer-link/footer-column/layout-reset/text-meta classes, color-border#CBD5E1, color-accent#F05A29 and spacing tokens reused. Shared Components103/286 and their definitions/overrides unchanged.

## Minimal Custom CSS retained by this milestone

All other listed layout/typography/size changes convert to native Atomic controls. Three small local exceptions; no new Custom Code entry or runtime script:

1. Cities5fe71200 → Style local e-6d369c26-c6cb → **Tablet → Custom CSS**: `& > span > span { display:none; }`. Native grid controls cannot address the paragraph's nested decorative separators. Rule inherits to mobile; desktop dots remain. Reuses one paragraph instead of creating12 new widgets/classes. Native rich-text editor sanitizes aria-hidden on spans; no retained ARIA attribute is claimed.
2. Top5a520a4e → local e-3d1cd11b-276c → **Mobile → Custom CSS**: `white-space: nowrap;`. Verified actual editor field; unsupported by native converter. Keeps arrow/label together, with native no-shrink/44px height.
3. Copyright Identity23d35135 → local e-63994f17-a62c → **Mobile → Custom CSS**: `text-wrap: balance;`. Avoids isolated trailing word on narrow screens without changing full content, adding nodes, hiding words or changing desktop. Progressive CSS enhancement; older browsers fall back to normal wrapping.

Editor shows element.style wrapper automatically; edit only its body. Existing footer-root orange hover/focus and divider exceptions remain unchanged. White link text with orange underline/outline avoids low-contrast orange body text on navy. No theme CSS/enqueue, JS, PHP, asset, plugin, dependency, new Global Class/Variable/Atomic Component. Class inventory remains112.

## Service navigation and preserved destinations

Fresh staging WordPress searches found only Draft matching service pages:

| Footer text | Matching page IDs | Result |
| --- | --- | --- |
| Water Damage Restoration | 514,515 | Draft; leave informational |
| Fire & Smoke Restoration | 517,520 | Draft; leave informational |
| Mold Remediation (Mold Removal pages) | 516,519 | Draft; leave informational |
| Reconstruction | 518,524 | Draft; leave informational |
| Storm Damage Restoration | 523 | Draft; leave informational |
| Personal Property Restoration | 521,525 | Draft; leave informational |

No placeholder/draft/preview/production URL introduced; no page published to satisfy navigation. When approved destinations become public, use native Internal URL object references after confirming which existing page is canonical. This is the outstanding link dependency, not a broken-link workaround.

All existing eight footer destinations unchanged: four verified social URLs, tel:+18476563322, mailto:restore@gcprochicago.com, existing Google Maps directions to220 Eisenhower Lane North,Lombard IL60148, and#top. Native browser reserved top fragment was activated with Enter and returned scrollY0 even though there is no literal id=top element. No telephone/email external app launched or social destination content newly audited.

## Browser and saved-state verification

[Saved36-node configuration](2026-10-20-footer-responsive-settings.json); [sanitized six-width measurements](2026-10-20-footer-responsive-qa.json). SiteGround staging cache purged after final publish, then normal Chrome frontend reloaded; body has no logged-in class/adminbar. Separate authenticated native Elementor114 editor opened: Paragraph rich text, tablet local separator CSS, Button text/#top and mobile local nowrap field inspected. No editor value edits published during verification.

| Width | Verified result |
| --- | --- |
| 360,393,430 | Identity then emergency contacts then services; service rows44px/gap0; city2-column grid; copyright and top link share one row with full text; no horizontal/visible-text overflow. Footer1459.25px. About15.5px clearance above fixed Call Now at page end. |
| 768,1024 | Identity/contact balanced side-by-side; services2 columns below; city4-column grid; footer851.17px, about56.36px shorter than907.53px baseline. No horizontal/visible-text overflow. |
| 1440 | Existing node x/y/width/height/font/color/gap compared with baseline at0.5px tolerance: **no differences**. Footer558.375px before/after; original three-column composition and inline city list preserved. |

Mobile service section302.40px versus387.96px before (~85.56px shorter), without reducing row height below44px. Tablet contact width328.33px/456.33px replaces oversized full-row688.67px/944.67px. Desktop informational service rows remain original42.26px; they are not interactive links. Active footer actions preserve44px targets.

Actual keyboard Tab moved Directions → Back to top with visible brand-orange outline; Enter returned top. Mouse hover on top link kept white text/orange decoration. Footer phone/email/Maps destinations preserved, no accidental new# placeholders. Reduced-motion emulation checked: layout/overflow unchanged and no animation added. Social screen-reader-only1px labels excluded from visible clipping checks; no actual clipping found.

These are desktop Chrome responsive simulations, not physical Android/iOS/tablet tests. Independent incognito/cache-HIT and actual notched-device safe-area/keyboard/browser-chrome tests not certified. Existing903 safe-area/end reserve untouched and measured footer clearance passes. No full site accessibility/performance audit or full database/files restore test claimed.

## Complexity and recovery

Reused existing36-node template and9-consumer row class; no duplicate mobile footer, no extra wrappers/widgets/classes/scripts. Explicit native desktop grid placement is required to preserve desktop after source-order change; mobile auto positions allow source order. Two small local text-flow declarations and one nested separator rule cover native gaps; all are documented above. Redundant mobile gap/alignment on Copyright Group removed before final verification. Inherited grid-column settings on heading/grid-template on mobile services are inert once parent display switches to flex; no conflicting active layout.

Scoped recovery: retain current snapshot, then restore only affected local styles/settings from the [reviewed before/after delta](2026-10-20-footer-responsive-delta.json), using replace mode to remove introduced breakpoint declarations; move Contact after Services as recorded by the Columns child list. Revert only g-aca1669 tablet/mobile min-height44px, leaving base/E65 declarations intact. Restore original flat city paragraph and remove its new responsive grid/separator rule. Restore original bottom responsive typography/wrap and remove the two text-flow declarations. Publish114, purge staging cache, repeat all six widths and keyboard/end-clearance tests. Git revert restores documentation only; it does not roll back Elementor. Do not restore BEAF/Kit6/903/Header or unrelated resources. Full-site backup restoration remains uncertified.
