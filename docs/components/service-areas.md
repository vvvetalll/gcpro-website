# Service Areas

**E77 current:** Shared Component1140 now owns the unchanged Homepage design, with Homepage10feca9e and Residential5ced3ca1 consumers.12 city links and both actions are native real Page references. Former inactive availability action becomes Outline Orange100→492. Source7d8c17ad is historical. [Current exact locations and checks](residential-services.md).

Twelve community links and a directory action, followed by the separate [unfinished ZIP prototype](zip-search.md).

## Location and structure

Homepage154/main46c3aad4 → section **7d8c17ad** → container585624a1 → intro **3dc285eb**. Eyebrow1e3e2129; heading instance2554ebe8 →71; city grid **d6dbbe2**. Directory wrapper62862a3a contains link instance **2b5f493 →59** and prototype button5350691e.

All12 displayed-city/row/text locators and current destinations are maintained once in the [link register](../audits/2026-10-19-elementor-state-sync.md#current-service-areas-link-register). Several Navigator titles are stale; use displayed text plus actual IDs.

## Style/code ownership

Atomic native/local grid is3/2/1 columns; native **city-link g-9a26448** owns repeated layout/color, and **city-link__text g-efb17e3** owns typography. Standard section/container/stack, section-heading--accent and section-eyebrow apply. Tokens: font-heading/body, color-primary/accent/text, space-xs/sm and existing container/gutter values.

City-link's one class-owned Custom CSS block owns pseudo-arrow, focus outline, per-side border/transition limitations and reduced-motion rules. [Exact owner/exception](../CUSTOM_CODE.md); no page IDs or per-city copies are needed. Some border values remain literal approved visual values, not newly introduced tokens.

No Service Areas JavaScript, Custom Code, shortcode, HTML widget or external lookup API. Component71 supplies heading/description;59 supplies the directory button.

## Behavior, limitations and reuse

Hover/focus turns text/arrow orange and moves the pseudo-arrow0.2rem; reduced motion removes movement. Actual rendered width checks pass360/393/430/768/1440. All12 destinations and All Service Areas remain literal#; they are explicitly unresolved routes, not verified working navigation.

Edit content in Homepage native controls; repeated styles in the two existing classes. Bind intended existing published destination objects through supported Internal URL/page selectors when routes are approved. Preserve independent destinations, avoid duplicate location pages and retest native bindings after migration. Do not connect this layout to an invented ZIP backend. No visual refactor was performed.
