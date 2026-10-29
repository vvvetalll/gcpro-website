# Analytics configuration and QA — 2026-10-29

Status: staging QA installed; production activation and complete analytics acceptance are pending. This is an actual checkpoint, not a claim that every requested event has been tested.

## Resources and configuration owners

- Existing GTM account6212444930/container174858096, GTM-K544QFXV reused. Original seven-tag workspace exported privately before changes. Seven legacy tags paused in versions42–44; **production Live41 remains unchanged**.
- Custom environment **GCPRO Staging QA**, env-45, version44. Version43 exercised for the form/network checks;44 additionally uses native form names and fixes shared Hero/final CTA classification.
- Existing GA4 account190928786/property422500318 retained. Production stream6529843165/G-EFZT426LQ8 unchanged. New isolated QA stream16231944569/**G-Q32NMQPFMP**, enhanced measurement disabled.
- Active Developer Traffic exclusion **GCPRO QA debug traffic** added to keep debug tests out of standard reports; existing Internal Traffic exclusion preserved. Do not remove historical data. A historical statistics report export has **not** been completed. Private original GTM export preserves configuration, not historical GA4 metrics.
- **Elementor Custom Code3127**, GCPRO / Analytics QA — staging only: head, priority1, Entire site. Sole loader, hard-gated to staging hostname. Explicit `?gcpro_analytics_qa=1` enables this browser session; `?gcpro_analytics_qa=0` disables it. This is a documented QA switch, **not a public consent interface or production launch**. Analytics consent is granted only within that intentional QA session; Ads consent stays denied. Ordinary visitor sessions do not load GTM. Environment authorization remains outside Git; repository template contains a placeholder.
- GTM **Central event bridge34** owns `integrations/analytics-events.js`. GA4 event tag44 and Google tag31 use native GTM data-layer variables. Hostname conditions and analytics consent required. One explicit page_view; automatic send_page_view=false. No per-page analytics widgets, tracking plugin, new components or global classes.
- Atomic4.3.5 form handler inspection found no exposed successful-submit CustomEvent. The smallest shared observer watches native `form-state-success` transitions; no form values or request payloads are read. Form purpose is selected by native accessible name: GCPRO | Request Service / GCPRO | Contact Us. Apply/unknown forms excluded.

## Event map

| Event | Trigger / meaning | Key-event role |
|---|---|---|
| page_view | One bridge initialization per navigation | ordinary event |
| generate_lead | Request Service native confirmed-success transition | intended primary; GA4 key-event marking still pending |
| contact_submit | Contact native confirmed-success transition | separate general enquiry, not service lead |
| click_to_call | tel link click with CTA placement | intent, not a verified conversation |
| request_service_click | Native service-request destination click | secondary funnel intent |
| email_click / directions_click | mailto / verified Google directions link | supporting |
| coverage_search | Completed result data-status, not input | supporting |
| coverage_area_click | Result link to local page | supporting |
| portfolio_filter / portfolio_reset / portfolio_load_more | Native WPGB controls | supporting; Load More counts interaction, not asserted append success |
| project_open | Native loop-card case link | supporting |

Allowlisted parameters: cta_location, form_type, result_status, filter_dimension/value, project_id, city/service when available, sanitized page_location/referrer/title. Query/fragment removed; legacy detail paths normalized to /portfolio/project/ because old slugs can contain customer identifiers. Referrer origin only. No entered names, phone, email, message, address or raw ZIP/city input. The service parameter is prepared but not populated from unverified input.

## Actual checks and remaining work

- Guest browser: QA loader resolves env-45 and G-Q32NMQPFMP. One page_view per tested navigation; QA query absent from analytics page_location.
- Empty Request submission:3 invalid controls, **zero generate_lead**. One clearly labeled TEST submission saved successfully: **one generate_lead**, form_type=request_service, debug_mode=true. Test contacts/message absent from inspected GA4 request. Mailbox delivery not confirmed.
- DebugView visibly received page_view, first_visit, session_start and user_engagement; generate_lead was verified in outgoing network but not yet confirmed in DebugView. Full Tag Assistant Preview acceptance remains undone.
- Final44 shared-name/CTA-context change was published only to QA; full end-to-end retest of44 was not completed before owner requested checkpoint.
- Contact success, failed server delivery, Apply exclusion, popup reopen, portfolio interaction analytics, mobile analytics, Ads linkage/actions/dedup and GA4 primary key-event marking remain unverified/unfinished. Earlier functional site audit is not evidence for these analytics events.
- Public production integration remains off. Before launch: agree public consent handling; complete listed QA; mark service lead only as primary; inspect existing Ads linkage/conversion actions to avoid GA4/direct Ads double count; remove QA-only gates/debug settings deliberately; approve production deployment separately.

## Other owner corrections in this checkpoint

Coverage1.2.3 now exposes result data-status, clears it on reset/error, and gives served results a light green background. Existing coverage list/approval unchanged. Guest60026 served green verified.

Card2233 heading is now ordinary Inter16px/400 on every breakpoint, owner-confirmed direction; frontend16px verified. Native global H2 default28/26/24px replaces32/28/24, H1 unchanged. Apply486 added as native menu item3123 under About243/menu5. No custom typography/navigation code added.

Request492 confirmation is **Thank you. Your service request has been sent.** Contact496 is **Thank you. Your message has been sent.** Corresponding errors use **could not be sent** with retry/phone. Apply486 already correctly says application submitted and retains its messages. Saved messages checked on all3; guest Request/Apply HTML checked; Contact anonymous HTTP check returned an error and was not claimed passed. Browser-native validation preserved. These messages confirm form submission, not verified mailbox receipt.

[Sanitized checks](evidence/2026-10-29-analytics-qa.json). Private scoped snapshots and original GTM export retained outside public Git. Restore Custom Code3127/QA environment separately from source rollback; do not publish Live41 changes during rollback.
