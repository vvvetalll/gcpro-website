# E18 — Anonymous timeline cache diagnosis

2026-10-16, staging only. User reported Samsung S25 Ultra failure, then clarified the same failure for logged-out desktop visitors. Physical Android access was unavailable.

## Root cause and evidence

The ordinary public homepage returned **X-Proxy-Cache: HIT**, HTTP200, 134923 decoded characters, with the timeline markup but **zero** `gcpro-process-mobile-style` and `gcpro-process-mobile-sequence` markers. Cookie-free Windows desktop and Samsung/Android Chrome User-Agent requests returned the same missing integration. Authenticated frontend had both blocks. Code590 was Published, body-end, priority10, native Page154 condition, and its saved source matched the canonical CSS/JS exactly.

A diagnostic query request returned **MISS**, 137625 characters, and both blocks. This isolated a stale SiteGround anonymous HTML cache, rather than an Android, selector, publication, timing or pointer defect. The underlying reason the earlier publish did not invalidate that cached entry was not established.

## Smallest correction

Used the existing WordPress **Purge SG Cache** toolbar action on staging. No changes to590, its display conditions, CSS/JS, theme, optimization/security settings, stored pages, Components, classes, links or production. Native purge clears the staging site's cache; it was not a production purge. No cache system was disabled.

After purge, ordinary cookie-free root requests returned MISS then **HIT**, both containing exactly one current CSS and JS block. Script occurs at offset136596 after timeline markup at67223: required DOM already exists when the body-end script executes. No delayed/rewritten script type is present for this block. Canonical source stays Homepage-only; no sitewide scope expansion.

## Actual browser verification

A separate connected Chrome profile was genuinely logged out (`logged-in` false, no admin bar); this was a normal logged-out session, not an incognito window. The internal browser was authenticated, so it was used for admin comparison/purge, not mislabeled as guest verification. No cookies/login state were changed.

- **390×844 and430×932 touch emulation:** initial page top, timeline below viewport, marker waiting. Scroll into section changes marker to played; time-sampled pseudo-element opacity shows01→02→03→04, both staggered rings, eventual transparency. Circles keep transform:none; no horizontal overflow. Guest style/script contents exactly match tracked sources.
- **390 re-entry:** played remains; completed rings do not restart after leaving/re-entering.
- **430 reduced motion:** integration delivered, no observer marker or ring animation on entry, intentionally respecting preference.
- **1440 desktop:** no mobile marker; hovering description/whole step still triggers existing first-circle desktop ripple with160ms second-ring delay; stationary circles/no overflow.
- Authenticated/guest step classes and titles match. Actual animation proves keyframes are available; public fallback asset separately returns200 with the existing keyframe. Captured guest console contains no warnings/errors. No missing animation asset was identified.
- No Elementor document writes or integration source edits, so native editing and12 content overrides remain untouched. No unrelated destination/link conversion was attempted.

[HTTP before](../evidence/2026-10-16-android-diagnosis/http.json), [HTTP after](../evidence/2026-10-16-android-diagnosis/after-http.json), [browser samples](../evidence/2026-10-16-android-diagnosis/browser-qa.json), [390 ripple sample](../evidence/2026-10-16-android-diagnosis/anonymous-390-ripple.jpg), [430 finished state](../evidence/2026-10-16-android-diagnosis/anonymous-430.jpg). Static screenshots do not prove temporal behavior; opacity samples do.

## Complexity audit and remaining limits

**No new classes, components or custom code.** No Variables, wrappers, plugins, dependencies, fallback handlers, new files of executable code, or speculative media/observer rewrites. Existing centralized integration remains unchanged. The corrective operation is cache invalidation, with no source rollback required; no stale cache restoration is recommended.

Anonymous browser operation is now verified. Physical S25 Ultra is **not tested**: owner should reload the ordinary homepage while logged out and scroll to How We Work once. Android OS reduced-motion preference and real-device pointer behavior remain unverified. The once-per-page-load sequence starts at10% timeline visibility; lower steps may complete below the viewport if the user pauses at the section's edge. That existing timing design was preserved, not confused with the proven missing-code failure. E17 verified only authenticated emulation and did not establish anonymous delivery; this record closes that verification gap.
