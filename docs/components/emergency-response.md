# Emergency response strip

**Purpose:** repeated access to telephone/request actions between services and process.

| Field | Current implementation |
| --- | --- |
| Location/parent | Homepage154/main46c3aad4 → section6cde656f → container2bf35876 |
| Children | Heading2631f818 →71; actions53d683de; call300e78c6 →53; request91ce6f0 →103 |
| Classes/tokens | section--strip,section,section--dark,container,split-row,cluster; existing navy/white/accent,fonts and spacing |
| CSS owner | Native Global Classes and local action layout; inherited documented section--dark/button exceptions, no strip-specific Custom CSS |
| JavaScript / Custom Code | None |
| Plugins / shortcodes | Elementor Pro shared Components; no shortcode/HTML widget/extra dependency |
| Responsive behavior | Desktop split copy/actions; wraps/stacks on narrow widths; remains in normal flow, no sticky rule |
| Interactions | Existing native button hover/focus; telephone href tel:+18476563322, request# |
| Known limits | Request destination unresolved; phone call not initiated by tests |
| Safe editing/reuse | Use71 heading/title/description and53/103 text/link instance overrides; edit repeated appearance through existing classes, check shared consumers before changing definitions |

Current responsive page checks found no overflow or overlap; this audit changed only the separate Core B intro.
