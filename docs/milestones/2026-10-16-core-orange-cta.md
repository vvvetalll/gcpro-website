# E21 — Core Services Orange Outline CTA correction

2026-10-16. Staging Homepage154 section38ed6da4; Service Card62 CTA210ecf0d. Button styling only; no production, Header/Footer, card design, timeline, theme or URL changes.

## Implementation Summary

Reused existing button-outline-orange g-563da68 from Orange Outline Component100 on the existing CTA, beside service-card__action g-d0416c8. The compact class retained navy hover/focus colors that overrode the orange variant. Removed its base color/background/border-color and hover/focus variants. Final normal state: transparent/orange text and border. Hover: #F05A29 fill/border, #FFFFFF text.

## Technical Changes

Kept compact service-card__action ahead of Orange Outline in Global Class priority to preserve sizing, typography and bottom alignment. It now owns geometry and a native200ms transition for background-color/color/border-color; custom_css:null. Existing Orange Outline is byte-for-byte unchanged, including its pre-existing focus-visible outline rules. No new classes, components or custom code. No new Variables, plugins or dependencies;89 Classes/36 Variables remain. Same five-node Component, empty local styles and five independent Overrides. Shared Style Guide50 examples inherit this treatment; no consumer content was edited.

Edit in Elementor Component62 → Service Link210ecf0d → Style/Classes. Colors belong to existing Orange Outline normal/hover; compact dimensions and transition belong to service-card__action. Instance cta_text/cta_link remain supported Overrides; SVG/title/description fields are preserved. No detachment or structure changes.

## Complexity Audit

Removed redundant color-state ownership rather than stacking another override. No wrappers, duplicate button resources, hidden styling, executable files, theme edits or new dependencies. No Homepage content write. Existing Orange Outline/icon custom declarations predate this task; none added or changed.

## Verification

- Anonymous normal Chrome after final native staging Purge SG Cache: all six transparent/orange defaults and individual pointer hover tests confirm orange fill/white text; computed native200ms transitions. Authenticated first-button hover independently confirms orange/white.
- Keyboard Tab reaches CTA with focus-visible true, navy outline and white separation. Existing focus indicator preserved.
- Desktop1440/mobile390: all six labels/# destinations intact, Montserrat600/14px,44px height and unchanged measured widths. Before/after card backgrounds/borders/radius/padding/heights, heading font and CTA offsets match; no overflow. All six stack normally on mobile. Browser emulation, not physical phone.
- Native editor class resource confirms removed competing state variants, native transition and null custom_css on compact class; Orange Outline unchanged. Saved Component62 readback confirms attached Overrides/empty local styles and only CTA class attachment changed structurally. No fresh content-edit experiment needed for class-only correction.
- Cache purge followed by actual logged-out frontend test. HTTP evidence also records anonymous200/HIT and six Orange Outline CTA classes; no optimization/security changes.

[QA](../evidence/2026-10-16-core-orange-cta/qa.json), [native classes](../evidence/2026-10-16-core-orange-cta/native-classes.json), [authenticated hover](../evidence/2026-10-16-core-orange-cta/authenticated.json), [HTTP](../evidence/2026-10-16-core-orange-cta/http.json), [desktop normal](../evidence/2026-10-16-core-orange-cta/1440.jpg), [mobile](../evidence/2026-10-16-core-orange-cta/390.jpg). Full-section screenshots show normal state; QA records settled hover colors per button.

## Outstanding Items

All six approved # placeholders remain unresolved intentionally; no Draft/production destinations substituted. White/orange contrast3.39:1 and orange/light-card approximately3.24:1 are below4.5:1 for preserved14px text. Owner explicitly requested these brand colors and unchanged dimensions; no silent substitution. Actual logged-out normal-profile verification complete; controlled incognito and physical-device tests unavailable/not performed. Visual approval pending.

Scoped pre-change recovery: local outputs/recovery/orange-outline-before.json outside Git. Restore compact class colors/states/priority and remove Orange Outline from CTA62 through native controls to reverse. Git docs do not deploy or restore Elementor configuration; full-site recovery not tested.
