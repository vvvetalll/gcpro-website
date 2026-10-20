# Shared restrained BEAF presentation — E66

2026-10-20, staging only. Owner explicitly expanded scope after E65: fix unreadable Before/After labels and style expand icons globally, then requested a subtler treatment. This is separate from Phase1 cleanup; its third-party exclusion remains. No plugin files/records/shortcodes/images/layout/handle behavior/JS or production writes.

## Verified source and owner

Frontend generated vendor rules for slider723/742/767 set both label foreground and background white; default labels only appear on hover. Before this change, Homepage154 Page Settings Custom CSS and Kit6 Site Settings Custom CSS were empty in native editor; the historical E56/E57 override was no longer emitted. Its disappearance was not diagnosed to a specific write in this task. Do not treat old documentation as live state.

One authoritative shared owner: **existing Elementor Kit6 → Site Settings → Custom CSS**. Native editor active-document=6, saved using Save Changes. Source mirror [integrations/beaf-presentation.css](../../integrations/beaf-presentation.css) is documentation/recovery only; do not enqueue it again. No new Custom Code post. Existing plugin classes scope every current/future BEAF comparison, including body-mounted fullscreen content. No page/template/generated/grid/slider IDs or added Global Class. Atomic controls cannot style vendor-generated label pseudo-elements or body-mounted popup internals.

Labels use10px existing font-body/white tokens,16px line,2px5px padding,2px radius, black60% translucent background and top10px; readable without white boxes. White contrast is at least5.74:1 against the brightest white photo through that background. Opacity1 in ordinary state; vendor active-drag hiding remains. Popup AFTER has right56px to clear vendor close control.

Expand buttons use36px desktop/44px mobile or coarse pointer,16px existing white SVG, dark52% translucent background,4px radius and subtle white40% border. Orange accent only hover/focus border and visible focus outline. One necessary !important overrides vendor `.popup_button:focus{outline:0!important}`. No added animation/listener/library or image asset. Removed an unnecessary image-fallback rule after verifying all current buttons use inline SVG.

## Verification and limits

After an independent editor reload, native Custom CSS was selected/copied and matched the1490-character source mirror exactly. [Final supplemental readbacks](2026-10-20-footer-final-supplement.json) include settled hidden-panel states for723/742/767. Immediate/300ms samples were not stable-state assertions; no exact overlay timing guarantee is claimed.
[Six-width inline settings](2026-10-20-beaf-presentation-results.json):360/393/430/768/1024/1440, three instances/six readable labels, appropriate36/44px targets and16px glyph, no horizontal overflow. [Continuous actual pointer drag](2026-10-20-beaf-drag-results.json) changed clipping in all3 at1440 and393. Initial single-move samples did not trigger a continuous gesture and are retained as intermediate evidence. [Fullscreen](2026-10-20-beaf-popup-results.json): all3 opened/closed at1440/393, shared popup labels/56px AFTER clearance and no horizontal overflow. Immediate overlay samples can precede the controller update; settled-state checks recorded separately. Existing903 overlay adapter is unchanged. Native Full screen button keyboard focus shows orange outline.

Vendor handle remains a non-keyboard DIV and vendor close control lacks button semantics; this CSS task does not claim full keyboard-modal/slider accessibility or fit-to-window remediation. No screen-reader/physical Android/iOS/independent incognito/cache-HIT/full-restore certification. Existing plugin motion/layout remains; no new animation introduced.

## Recovery

Save current Kit6 field first, then remove only the bounded GCPRO BEAF block or restore the prior empty Custom CSS field if no later edits exist. Do not restore obsolete page-ID CSS alongside it. Purge staging cache and retest inline/popup controls on all3 and mobile panel suppression. Plugin content/data/configuration are unaffected; historical vendor-record numeric IDs remain essential references. Scoped before-state was an empty native field, not a full site backup.
