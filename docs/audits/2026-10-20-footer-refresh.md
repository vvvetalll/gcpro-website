# Global footer, local relevance and mobile end clearance — E64

Verified 2026-10-20 on https://vitaliiv1.sg-host.com only. Scope includes the owner-requested footer rebuild/refinement, separated items, Get Directions, white-tail correction and exposed working-title correction. Broader content changes are [opportunities only](2026-10-20-local-content-opportunities.md). Production and BEAF were not modified.

## Result and verified causes

- Existing global Footer114 stays Published/active/include/general. Replaced its V3 nested dropdown menu1faf8090 with readable service information; original WordPress menu and Header113 consumer are intact.
- Four clear areas: quiet contact CTA; brand/services/contact columns; service coverage; copyright/Home.48px desktop section spacing,32px mobile, thin white16% separators and aligned content. The footer CTA is a20px bold plain telephone link rather than a second filled orange button. The preceding Homepage CTA remains the primary action and was not edited.
- Services and contact rows now have8px vertical padding and individual dividers. No accordion/menu JavaScript or new markup per row.
- Reproduced blue link hover/focus from general link styles; footer-only states retain white text and use orange underline/border/outline accents. Orange text at normal16px on navy would have only3.45:1 contrast; white text has11.69:1, while orange non-text indicators exceed3:1. Existing shared button/link definitions outside the footer are untouched.
- The mobile fixed panel itself was fixed correctly; Code903 applied85px body padding, leaving a white tail after the navy footer. Moved the reserve into .site-footer. Bottom copyright/Home remains above the panel, with no external white tail.
- Owner reported the working title; reproduced .robylo-entry-heading > h1 outside Atomic content and native Hide Title unchecked. Saved Homepage154 → Page Settings → Hide Title=yes. Reloaded UI confirms checked; rendered page has only Hero H1. No CSS/title/theme workaround. Existing Full Width template and190-node main remain unchanged.

## Exact global structure and locations

Existing Theme Builder114 → root1687d698 → container119ffe98. All IDs below are editor/storage locators, never runtime selectors. [Reviewed saved settings and local style inventory](2026-10-20-footer-refresh-settings.json) records all34 final nodes, native object references and exact CSS returned after publication.

| Area | Saved elements / component references |
| --- | --- |
| CTA |671c4f66 → copy233d6afa → title3ca0b443 / description4884b146; quiet native button29c8d2e0 |
| Main columns |73b78d01; native grid1fr 1fr 1.2fr desktop, two columns tablet, one mobile |
| Brand |7ac91d92; logo4eac9eb/asset232/200px; intro1432e75b; instance bdfaa44 → existing Emergency Mark286 |
| Services |39be2867; heading7ffa59b5; rows1a57ae23,7e3dc0fd,2a175611,15d483d9,147c396c,308c7b8f |
| Contact |e424c2c; existing native ID robylo-contact retained; heading779deb5e; phone641a5869; email25e52737; address2a44b1ed |
| Directions |37cec545 → existing Outline White103 with text/link supported Overrides |
| Coverage |5245645d; heading43e8f919; cities5fe71200 |
| Copyright |1d11b99e; group578307c4 contains native dynamic year890602e and identity23d35135; Home5a520a4e |

The initial interim Primary53 footer instance55e1d02 was removed during the approved refinement and replaced with the native quiet link29c8d2e0, preserving its telephone destination and wording. Shared53 itself was never edited. New copyright group578307c4 keeps year and identity together; it is not a new Component. No duplicate footer template.

## Content and destination integrity

Final local wording:
- CTA description: “Call our team for help in Chicago and the surrounding area.”
- Heading: “Chicago Restoration Services.”
- Services: Water Damage Restoration; Fire & Smoke Restoration; Mold Remediation; Reconstruction; Storm Damage Restoration; Personal Property Restoration.
- Contact heading: “Contact Our Lombard Office.”
- Coverage heading: “Serving Chicago and Surrounding Areas.”

Existing brand introduction still describes residential/commercial restoration in Chicagoland. Existing12 city names retained, no new unconfirmed cities or service claims. Chicago/surrounding area was explicitly confirmed by the owner. Geographic context is placed in headings/description rather than repeating Chicago on every service row.

Phone **847-656-3322 / tel:+18476563322**, email **restore@gcprochicago.com**, and address **220 Eisenhower Lane North, Lombard, IL60148** unchanged.

Get Directions uses an ordinary new-tab URL in103 link Override:
https://www.google.com/maps/dir/?api=1&destination=220%20Eisenhower%20Lane%20North%2C%20Lombard%2C%20IL%2060148
Google Maps rendered the correct destination. No origin supplied, permission granted, directions sent, phone call placed or email sent.

Home uses native internal-url/type=post/post_id={id:154}; renders the staging root. This is an essential WordPress object reference, not a runtime page-ID dependency. Service/city destinations remain Draft in the canonical URL inventory; lists are deliberately informational, with no new fake# links, guessed URLs, production fallback or unauthorized publication. Other Homepage/Header unresolved routes were not altered.

## Native classes, CSS owners and complexity review

Reused: section, section--dark, site-footer, container, stack/stack--compact, footer-column/footer-meta, heading-label, layout-reset, text-meta/text-measure--short; existing103 and286 and design tokens.36 Variables unchanged. Two necessary reusable Global Classes added,109→111, editable in Elementor Design System → Classes:

1. **gcpro-footer-link / g-373d928** — quiet/plain white telephone/email/Home links. Native44px minimum target, inline-flex, body font/token size, weight400/1.6, no filled background/border/padding, underline hover. No class Custom CSS. Existing text-link is an accent/action pattern and navigation-links targets the vendor menu; neither supplies this plain footer pattern.
2. **gcpro-footer-item / g-aca1669** — eight repeated service/contact rows,8px vertical padding and1px white16% bottom divider. Native padding/border widths; converter retains only border-bottom-style/color as class Custom CSS. It precedes g-373d928 so the row modifier overrides the link's zero padding/border. Avoids eight copied local row definitions; two temporary duplicated contact styles were removed.

No new Variables, Components, plugins, libraries, shortcode, PHP, theme file, JS observer/listener or Custom Code entry. Existing Google Maps is an ordinary outbound action, not an embedded dependency.

Footer114 local owners are fully enumerated in the settings JSON. Important visual controls:
-1687d698/e-65a7ec46-9cb8: native48px top/32px bottom,2px accent top border; mobile32px top/56px baseline bottom, overridden only by measured903 clearance.
-119ffe98/e-2a649526-9b99: gap0 so four areas own consistent spacing.
-671c4f66/e-4e9c981d-4e97 and5245645d/e-37aa61e2-bb74: spacing and white16% dividers; native widths, local converter CSS style/color.
-73b78d01/e-576e780c-5019: grid/gaps/padding; contact spans both tablet columns.
-3ca0b443/e-338b3ebe-b1f2:20px/1.35/normal case; description4884b14614px; quiet call29c8d2e0/e-310ab1e8-bff020px700/no shrink.
-39be2867/e-6077e757-234e gap0; heading7ffa59b5/e-2f1bfe77-c32f margin-bottom space-sm; e424c2c/e-7b5b31ec-eb16 gap space-xs.
-1d11b99e/e-3a3f1a6d-bc52: subtle divider, aligned/wrapping; mobile column/start. Group578307c4/e-1e6afb39-6123 uses4px gap; year/identity14px; Home5a520a4e14px/auto inline margin, mobile0.
-Root1687d698 Custom CSS owns exactly four scoped state rules: white/orange underline for .gcpro-footer-link hover/focus; orange keyboard outline; white/transparent/orange border for .button-outline-white hover/focus; orange outline for that button. This overrides verified general blue states and shared103's white-fill/blue-text state only in the global footer. Combined descendant state rules and text-decoration/outline are retained in Custom CSS because the connector cannot express these as root native controls; changing shared103 would affect unrelated consumers. No IDs or !important.

Removed redundant local text color/family/weight/line-height where native paragraph/H2 defaults and existing section--dark supply them. Headline explicitly uses20px at desktop/tablet/mobile: browser testing showed the kit's28px/24px responsive H2 sizes otherwise prevailed. These native responsive overrides preserve the intended quiet CTA hierarchy. No unrelated resources deleted.

## Code903 and mobile clearance

Existing WordPress Elementor → Custom Code903, GCPRO / Scroll Navigation & Emergency CTA: Published/Entire site/Body End/priority5. One existing style/script wrapper; native saved source equality verified after reload. [CSS mirror](../../integrations/scroll-navigation.css) changed; [JS mirror](../../integrations/scroll-navigation.js) unchanged. Git does not separately enqueue/deploy either file.

Mobile .gcpro-nav-ready .site-footer now owns:
```css
padding-bottom: max(var(--section-spacing-mobile), calc(var(--gcpro-bottom-reserve, 0px) + env(safe-area-inset-bottom, 0px)));
```
Removed body padding and its max-safe-area fallback. Existing barHeight+24 reserve remains85px in tested viewports; panel retains fixed positioning/8px/safe-area. No overflow masking, runtime numeric dependencies, Header/Core positioning changes or JS edits. A future alternate shell without site-footer must provide equivalent terminal-content clearance.

## Verification and limits

[Sanitized browser results](2026-10-20-footer-refresh-results.json) distinguish final row/viewport checks, earlier refinement states and functional sweeps.

-360/393/430: one column, no horizontal/text overflow, separate rows, fixed contextual panel, no white tail, final content above its footprint.768/1024: two columns/contact full row, panel hidden.1440: three aligned columns/panel hidden. Quiet call stays44px high, copyright fits one21px line at360.
-Actual mouse hover and Tab focus on all five footer actions: white text, orange accents, visible outline. Maps stays white/transparent with orange border rather than blue text; mobile actual Tab/Shift+Tab scrolls it above the panel. Calculated white/navy11.69:1; orange/navy indicator3.45:1.
-393 Hero→Core active/release→Process→footer: panel hidden at top/visible after Hero; Core top0 then releases negative. Menu opens/panel hides; closes/panel returns; next down scroll hides Header. No Core settings edited.
-Reduced-motion emulation gives Header transition0s; safe-area inset0 in emulation. No claim of physical-device/browser-toolbar tests.
-Published114/native class readback, conditions and native editor Desktop/Mobile render checked; email General panel exposes editable content/link/ID/Attributes.154 Hide Title checked after native reload; same190-node main structure.903 saved wrapper exact and Body End5 retained; staging cache purged after meaningful saves.
-Normal Chrome frontend had no logged-in class/adminbar. Independent incognito/cache-HIT delivery, screen reader, physical Android/iOS and formal performance testing remain unverified.
-A late external review-widget layout load moved the first360 sample away from the actual page end. A separate settled-end sweep was performed; this is not a claim that the intermediate sample reached the bottom.

## Recovery

Private scoped pre-change114/903 and pre-refinement114 snapshots are stored under this task's work directory, excluded from Git. They are configuration snapshots, not a rehearsed full database/files restore.

For903 clearance alone, restore parent-commit CSS to the single existing903 entry, preserving conditions/location/priority; this restores the old tail. For footer rollback use native114 revision/validated scoped recovery or reconstruct the prior brand/nav/contact/bottom tree; keep robylo-primary and include/general. Do not copy generated IDs into newly built nodes. Remove the two new classes only after checking later consumers; preserve shared53/103/286/895 and all BEAF integration. For title rollback154 Hide Title=No would restore the unwanted working title. Purge staging cache and recheck responsive/menu/focus/end-of-page behavior after recovery.

