# Why GCPRO — reusable Trust Logos media (2026-10-22)

Existing shared Atomic Component1149 remains the only definition. Consumers: Residential484 instance225936ef, Commercial499 instance94c4cddb and Home154 instance60cdf058. Only484/499 media Overrides changed; all other page body data and page settings compare equal after excluding these media fields. Home body is exactly unchanged. Production, Header/Footer and BEAF were not edited.

## Editing and media modes

Edit Component1149 → Why introduction column → Trust logos media. Edit per-page media using existing Image and five new native image Overrides: trust_iicrc, trust_iaqa, trust_bbb, trust_ria, trust_ra. Image mode: fill Image, clear five logos. Trust mode: clear Image, fill five logos. None: clear all six. This approved field convention is not a dropdown. Existing text and four benefit Overrides retain their keys. Empty-logo hiding removes the entire group, including its label.

One native p element inside the group reads INDUSTRY CERTIFICATIONS & AFFILIATIONS. Native local typography: existing font-body and color-surface-alternate tokens,11px,500 weight,1px tracking,uppercase,70% opacity,no decoration. It is not an SEO heading. The label is a full-width flex item; no duplicate mobile label/group.

## Owners and layout

Three new reusable Global Classes, edited in Elementor Global Classes:

- trust-logos g-c8bf649: media layout, left aligned desktop3+2, mobile five logos in one row. Gap12px desktop;6px mobile with12px between label and row. Empty group Custom CSS: `&:not(:has(img[src]:not([src=""]))) { display:none; }`.
- trust-logo g-da9c4af: transparent frames,white12% border,8px radius,108px height desktop/64px mobile. Native opacity68%,180ms opacity/transform transition; native hover100% and translateY(-2px),no shadow. Scoped Custom CSS owns box-sizing:border-box and reduced-motion disabling of transition/transform. Touch-hover suppression was removed at owner request. Do not add it back.
- trust-logo__image g-a5e0eea: contain original proportions;86px height desktop/50px mobile. No artwork changes.

On mobile only, existing introduction wrapper uses native display:contents, editorial container flex column/gap24px, benefits order1 with8px top margin, trust group order2 with8px top margin. This preserves the single component and DOM group while placing logos visually after all four benefits. Desktop/tablet retain the existing columns/order. Informational logos add no keyboard tab stops. DOM reading order retains introduction/media before benefits; none are interactive.

No new Component,Variable,JS,PHP,theme stylesheet,Custom Code entry,plugin or dependency.11 media nodes plus one p were added inside existing1149. All CSS exceptions have the above single class owners; native layout/text remain editable. No page-ID selectors.

## Assets

Media1294 IICRC-white.svg,1295 IAQA-white.svg,1296 BBB-white.svg,1297 RIA.svg: supplied static vectors,transparent,original paths/viewBoxes retained,checked for scripts/remote references and rendered for QA. Media1303 gcpro-ra-white.png: transparent400×290,7512bytes,exact raster conversion from supplied WebP without tracing; owner will supply true vector. Descriptive Media Library titles/alt/descriptions saved. Failed SVG-wrapper trial1298 is private,unplaced and explicitly marked unused; sanitizer removed its embedded raster. Do not reuse it or claim it is a vector logo. Owner-provided marks do not independently establish current accreditation.

## Verification and limits

Before final label/mobile-order refinements,both pages passed360,393,430,768,1024,1440px DOM row/overflow checks with all five images loaded. Final Commercial DOM checks at360,392,768,1440 CSSpx: p label11px,left aligned,no overflow,mobile one logo row after benefit04,tablet/desktop3+2 before benefits. Nominal393 rendered392 due browser zoom; do not label this an exact393 retest. Hover browser computed style was68%/none →100%/translateY(-2px),using forced pseudo-state. Native reduced-motion guard saved. Final screenshots failed with blank IAB capture after Chrome disconnected; earlier screenshots predate these refinements. Image/None switching remains unverified end to end; preserved native image configuration and hidden-group condition are saved-state evidence only. No physical-device test or new SEO claim.

Source representation and sanitized class/QA evidence: [source](../evidence/2026-10-22-why-trust-source.json),[evidence](../evidence/2026-10-22-why-trust.json). Source is a reviewed implementation record,not an automatically deployed duplicate.

## Rollback

Restore Component1149 revision before Trust Logos and restore484/499 Image Overrides from private task backups,then explicitly publish1149,clear Elementor Files & Data and purge staging cache. For only hover rollback,remove native hover/transition on trust-logo; do not delete shared classes/media. For future RA vector,replace only trust_ra image on both instances. No credentials/backups are committed.


## 2026-10-22 — Homepage Trust Logos activation

Owner requested the same logos on Homepage154. Existing Why Component1149 instance60cdf058 now has only six media Overrides: empty Image and existing attachments1294/1295/1296/1297/1303. Shared definition,classes,hover,label and SEO metadata unchanged. No new classes,Variables,Components,code,assets,plugins or dependencies. Cache cleared; frontend confirms five image URLs/alt labels and supporting p label. Browser DOM checks:360px one row after benefit04;1440px3+2 in original left column;no horizontal overflow. Rollback:clear the six instance media Overrides to restore previous default None.


2026-10-22 — Owner-approved Trust Logos separator: existing trust-logos g-c8bf649 now has a1px solid white16% top border and14px top padding. It spans only the media column; browser1440px confirms40px separation from right benefits,360px retains one logo row/no overflow. Existing native block-start border width/padding controls and class-owned border-top style/color exception; no new class,element,Component,Variable,JS,plugin or dependency. Hover unchanged. Applies to Home154,Residential484,Commercial499 through existing1149. Owner accepted; do not redesign further. Rollback:remove only the added top border and14px padding.
