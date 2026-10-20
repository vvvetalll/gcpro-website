# Testimonials

Actual Trustindex integration, separate from Why GCPRO.

| Field | Current implementation |
| --- | --- |
| Location/parent | Homepage154/main46c3aad4 → section10a34543 → inner7d037e04 |
| Children | Heading wrapper629e394d: eyebrow31825a3f,H2 3d727826,divider41bcab5a; Shortcode **02441ff** |
| Saved shortcode | [trustindex data-widget-id=b15b7138395d9632254618dee92] (public widget identifier, freshly read in native editor) |
| Classes/tokens | section,container,stack,layout-reset,section-eyebrow; native H2 uses font-heading/color-text; light surface-alternate #EFF6FF |
| CSS owner | Native section/heading controls; Trustindex plugin/CDN owns review presentation and Poppins font |
| JavaScript / Custom Code | Vendor Trustindex runtime; no GCPRO-developed Testimonials JS or Custom Code entry |
| Dependency | Widgets for Google Reviews14.2; external cdn.trustindex.io assets/data |
| Responsive behavior | Review carousel manages responsive cards inside its own clipped track; offscreen slides are not by themselves page overflow |
| Interactions | Vendor next/previous/read-more and review source links; no custom carousel reimplementation |
| Limits | Plugin Poppins is a design-system exception; review/source approval and structured-data consistency need owner review |
| Safe editing/reuse | Change widget/layout/data in Trustindex configuration, shortcode in02441ff, native heading/surface in Homepage; do not copy review HTML or edit vendor files |

The current closed-page width scan passes360/393/430/768/1440 despite offscreen carousel slides. Runtime JSON-LD's aggregate review count differs from the visible widget's count; treat this as a source/configuration consistency question, not proof of false reviews. No review content, schema settings or typography was changed by this audit.
