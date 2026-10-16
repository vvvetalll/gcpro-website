# Desktop Hero background — E32

2026-10-16, staging Homepage154, visual approval pending. Owner's latest direction retains the photograph, removes the top gradient and fits the photograph to the Hero height. Do not reinstate the rejected vertical fade/contain trial.

## Implementation Summary

Existing Hero section a62cdd3 now uses a full-section background, with its1200px content container, existing grid/copy/H1/eyebrow/CTA order unchanged. Existing placeholder17c26181 is hidden above the mobile breakpoint and preserved on mobile. No nodes deleted or added; full145-node saved Homepage comparison shows only these two class assignments changed. Unrelated Homepage sections, Header, Footer, production and shared ROBYLO untouched.

## Technical Changes

Original supplied PNG1983×793,2,252,689 bytes preserved as WordPress Media632 and in owner's Downloads. Optimized WebP633, same dimensions,198,202 bytes, quality84/method6, no resize/upscale/AI/crop/retouch. Native media alt: GCPRO branded SUV and service van with the Chicago skyline at sunset. Repository source assets/images/homepage/gcpro-chicago-hero-desktop.webp.

Two necessary reusable native Global Classes:

- **hero--panorama g-708f717**, applied only to a62cdd3: native Background image Media633, Full; custom size width auto/height100%, center-right, no-repeat. One native horizontal navy-to-transparent gradient protects copy, stops0/24/38/63%,90deg. No vertical/top fade. On mobile a solid navy native gradient replaces the image layers, retaining the prior appearance. An empty native background layer list did not reliably clear inherited desktop layers, so the opaque same-color native layer is intentional.
- **hero-media--mobile g-02b63b3**, applied only to existing placeholder17c26181: native display none desktop/tablet, flex mobile≤767px. Ordered before existing media-placeholder classes to make visibility deterministic.

Existing generic section/section--dark/container/stack/hero-layout and CTA Components53/103 reused unchanged. Existing classes cannot supply scoped Hero photography or hide only this placeholder without affecting other consumers. Both additions are reusable, individually editable through selected Hero/placeholder → Style → named Global Class. Background → image layer exposes native Media selection, Full, Position and Size; gradient layer exposes stops/angle. Responsive mobile state is in the same class. All variants custom_css:null. No local styles, new Components/Variables, custom CSS/JS/PHP/files, dependencies or plugins. No theme changes.

## Complexity Audit

No wrappers or duplicate Hero, no animation or preload code. Native image object reference633 replaces the temporary URL used during setup; verify native-classes.json, not just rendered URL. No broad H1/site styles changed. Both new classes have separate current responsibilities; no speculative abstractions. Source asset and evidence are documentation, not a second deployed style system.

## Verification

Native editor background layers, image selector, custom height100%, position and responsive controls inspected. Staging published, native SiteGround cache purged, ordinary anonymous Chrome frontend checked at1440/1200/1024 and390. Screenshots and computed checks in [E32 evidence](../evidence/E32/verification.json): [1440](../evidence/E32/1440.jpg), [1200](../evidence/E32/1200.jpg), [1024](../evidence/E32/1024.jpg), [390](../evidence/E32/390-after.jpg), [native classes](../evidence/E32/native-classes.json).

Image fills Hero height with natural aspect ratio; no forced section height, distortion or top mask. Narrower desktop widths crop horizontally, as expected for height-fit; SUV/van and branding remain represented, with composition subject to owner review. No horizontal overflow. Copy and CTA definitions/destinations unchanged: Call tel:+18476563322, Request Service intentional unresolved #. No new manual internal navigation URLs.

Native CSS background is discovered with the stylesheet, not an img with lazy-loading; no custom preload introduced. No formal LCP/network/CLS benchmark, physical-device or incognito test. Ordinary logged-out browser verification is distinct from an incognito test. Native Media optimization setting shows Compression Level None for the already optimized WebP; no optimization settings/plugins changed.

## GitHub

Asset, evidence, PROJECT_CONTEXT, CHANGELOG, DESIGN_SYSTEM, ELEMENTOR_MAP and asset register updated on main. Final user report records pushed commit and matching remote SHA. Git does not deploy Elementor.

## Outstanding Items / Recovery

Visual approval; mobile photography remains deferred. Existing Request Service destination pending. Prechange full Homepage and class snapshots are outside Git in project outputs/recovery/homepage154-before-hero-background.json and classes-before-hero-background.json. To reverse, remove only the two new class assignments, publish staging, purge cache and verify. Retain Media632/633 for future use; configuration snapshots are not a full site backup or a tested restore.
