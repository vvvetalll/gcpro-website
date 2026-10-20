# Orange Call Now and24/7 — E63

2026-10-20, staging only. Owner requested orange bottom Call Now, then the existing24/7 mark to the right of Emergency help. [Browser/class observations](2026-10-20-mobile-cta-orange-247-results.json).

## Exact native locations

Existing global Header113 → separate root Div feba833 → instance18849090 → Atomic Component895, GCPRO / Mobile Emergency CTA.895 ID/UID and label/call_text/call_link override keys are preserved. Native component update was staged as Draft and published; its element IDs regenerate normally:

|895 child|Current locator|Configuration|
|---|---|---|
|Root aside|175d43eb|gcpro-mobile-cta g-6771860|
|Emergency label|111fcda3|gcpro-mobile-cta__label g-4d22e61; existing label override|
|Availability mark|1acf10db →286|Existing Emergency Service Mark; caption override empty, original white numbers/orange slash|
|Emergency call|2077bfde →53|Existing Primary CTA; existing exposed call_text/call_link; Header renders Call Now/tel:+18476563322|

Previous895 had root4f446aa2/label142139fa/button2c82656e→103. No other consumers of53/103/286 were restyled; those definitions were not edited. Native895 schema readback retains all three existing outer keys; rendered Call Now confirms the Header's independent text override survives the rebuild.

## Class ownership and minimal exception

Design System → Classes → gcpro-mobile-cta g-6771860: native padding now space-xs8px on all sides. Existing navy/white/orange-border colors, radius8, border1, display:none fallback, row/gap8/space-between/center remain. Fresh class-resource reload confirms109 identities and unchanged property owners apart from the authorized padding. Custom CSS is exactly the four rules recorded in [smart-navigation](../components/smart-navigation.md#atomic-ownership-and-additions): nested Primary sizing/no-wrap, mark no-shrink, empty caption hiding, editor-only visibility. No superseded Outline selector or duplicate rules remain.

Primary53 exposes text/link, not size; the panel therefore owns a scoped14px/8px-padding/min-height44px compact variant. It inherits shared primary colors/radius/hover/focus rather than copying brand styling or creating a new component.286 is nested rather than duplicating its spans/artwork; only its empty caption is hidden within this panel. No new Global Class/Variable/Component/plugin/library/JS/PHP/theme file or Custom Code entry.903 behavior and repository runtime sources are unchanged. Native control/selector IDs above are editing references, not new runtime dependencies.

## Verification and limits

Published895 native readback: four nodes, nested53/286, three stable override keys. Existing class read after editor reload has one clean desktop variant. Staging Purge SG Cache invoked, authenticated Chrome frontend reloaded.

- 360/393/430: orange rgb(240,90,41), white text, correct phone, button44px high, label → mark → call button ordered without intersecting rectangles, overflow0 even with the admin chat footprint reserved.
- 768/1440: panel hidden. At393 Hero hides it, footer retains it; native open menu suppresses it and close restores it.
- Keyboard focus reaches Call Now, :focus-visible=true and solid outline. Existing Primary hover computes rgb(20,40,98). No call was placed. Shared page phone links and unresolved # destinations were not edited.

Chrome emulation only; no physical Android/iOS, anonymous/cache-HIT, screen-reader or formal accessibility/performance certification. The standalone895 visual editor shell stayed loading in this session, so no full visual-editor interaction claim; saved Atomic configuration, schemas, class resources and rendered behavior were verified. Edit through Header113 → Global Mobile Emergency CTA → Edit Component if the direct editor route stalls. Do not detach the component.

## Rollback

Private scoped pre-E63 tree/schema/class snapshots retained outside Git. Restore895 to its prior three-node composition using nested103, keep label/call_text/call_link keys, publish; restore the panel class's horizontal space-sm padding and original Outline no-wrap/editor rules. Preserve895 ID/UID so Header references remain valid. Do not delete shared53/286 or alter903. Purge staging and retest. Git documentation alone does not deploy WordPress; no full-site restore test performed.
