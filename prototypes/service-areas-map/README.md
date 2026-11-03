# Service Areas map — isolated prototype

Owner-authorized staging draft **4104**, not a rollout. Canonical implementation and verification record: [Service Areas](../../docs/components/service-areas.md#interactive-map-prototype--2026-11-03).

Files: `build.py` generates `map.svg`, `geography.json` and `prototype-widget.html` from official Census data and the current verified native link export. `map.css` and `map.js` are the editable presentation/behavior sources. The HTML fragment is the only deployed artifact, in draft4104 HTML widget `a4104def`; it includes the SVG/CSS/JS inline. Do not enqueue it globally or copy it across service pages.

Build-time dependencies only: Python, pyshp, shapely, pyproj. Obtain `tl_2026_17_place.zip` from the source recorded in `geography.json`. Export current Component1140 city links into a private JSON array with `name`, `page_id`, `status` (`publish`); URLs are not required by the builder. Run:

```sh
python build.py /path/to/tl_2026_17_place.zip /path/to/verified-native-links.json
```

The generated registry is the single city/GEOID/page-ID mapping. Runtime destinations come exclusively from Component1140's native links. Current prototype matches their visible city names and fails closed if a city cannot be matched. A future approved shared integration should attach stable GEOIDs/page-ID keys to native links, preserving their original href ownership.

No runtime geographic downloads, map service, keys, package dependencies or additional network requests. Raw fragment about166KB; gzip estimate55.5KB (actual transport compression depends on the server). Geography is municipality boundaries, never a coverage promise.

No-JS: the original native list/actions remain in their original layout; the styled static map follows them. Popup1801 retains its existing JavaScript dependency. With JS: intro → list → map → actions in DOM/mobile order, two columns on desktop; polygons select and expose a native-derived destination link. Keyboard Enter/Space selects; Escape clears; touch never redirects on first selection.

Removal: trash draft4104 or remove its two children (1140 instance and local HTML widget) after approval to remove. No shared component/global code recovery is required. Preserve these source files as a reproducible reference. Do not publish this draft or alter1140 without the next explicit approval.
