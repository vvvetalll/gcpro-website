# GCPRO Service Coverage

Staging adaptation, version1.2.1. See [configuration and verified results](../../docs/components/service-availability-popup.md#staging-coverage-bridge-and-owner-approved-cities--2026-10-29).

Package this directory as `gcpro-service-coverage/` in a ZIP; install/update using native WordPress plugin upload. No credentials or environment-specific secrets are required. Fresh activation seeds unapproved records only; updates preserve the existing option. Runtime edits belong in the native management screen, not the seed or repository snapshot.

`engine.php`: pure matcher. `gcpro-service-coverage.php`: guarded admin/import/export, registry, REST and narrowly scoped Elementor render integration. `self-test.php`: synthetic in-memory fixtures. `popup.js`: one endpoint client. `popup.css`: dynamic slots only. `admin.css`: management screen only. No entered-location persistence or third-party request.

Public POST `/wp-json/gcpro-coverage/v1/lookup` takes a string `location`. Protected register, single-record save and synthetic self-test routes require manage_options; native admin POSTs also require nonces. No bulk approval endpoint. CSV cannot import approval; admin saves require explicit individual approval/reference and revision. Unknown is never automatically not_served.

Recovery: disable bridge/deactivate to restore saved native call-only fallback without deleting the registry. Preserve private native settings/template backups outside Git. There is deliberately no destructive uninstall routine. Source seed is a historical proposal; never use it to overwrite approved runtime data.
