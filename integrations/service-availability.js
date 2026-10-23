/* Runs only inside native Elementor Popup1801. No network, storage or analytics. */
(() => {
  'use strict';
  if (location.hostname !== 'vitaliiv1.sg-host.com') return;
  if (window.gcproAvailabilityReady) return;
  window.gcproAvailabilityReady = true;
  let pagePosition = { x: window.scrollX, y: window.scrollY };
  let trigger = [...document.querySelectorAll('a')].find(a => a.textContent.trim().toLowerCase() === 'check service availability');
  document.addEventListener('click', event => {
    const a = event.target.closest('a');
    if (a && a.textContent.trim().toLowerCase() === 'check service availability') { trigger = a; pagePosition = { x: window.scrollX, y: window.scrollY }; }
  }, true);
  const rootNow = () => document.querySelector('.elementor-popup-modal [data-elementor-id="1801"]');
  const normalize = value => value.trim().replace(/\s+/g, ' ').toLowerCase();
  function lookup(value, data) {
    const key = normalize(value);
    if (!data.approved) return { status: 'uncertain' };
    const records = data.locations;
    // Exact approved operational exclusions take precedence over city coverage.
    if (records.some(x => x.status === 'excluded' && x.verified && normalize(x.location) === key)) return { status: 'excluded' };
    const kind = /^\d{5}$/.test(key) ? 'zip' : 'city';
    const match = records.find(x => x.kind === kind && x.verified && [x.location, ...(x.aliases || [])].some(v => normalize(v) === key));
    if (!match || match.ambiguous || ['proposed', 'requires_call'].includes(match.status)) return { status: 'uncertain' };
    if (match.status === 'partial') {
      const resolvable = records.some(z => z.kind === 'zip' && z.verified && !z.ambiguous && normalize(z.city || '') === normalize(match.location));
      return { status: resolvable ? 'partial' : 'uncertain', location: match.location };
    }
    if (kind === 'city' && records.some(x => x.verified && x.status === 'excluded' && normalize(x.city || '') === normalize(match.location))) return { status: 'uncertain' };
    return { status: match.status === 'confirmed' ? 'covered' : 'uncertain', location: match.location };
  }
  function reset() {
    const root = rootNow(); if (!root) return;
    const form = root.querySelector('form'), input = root.querySelector('input');
    const error = root.querySelector('[data-error]'), result = root.querySelector('[data-result]'), call = root.querySelector('a[href="tel:+18476563322"]');
    form.noValidate = true; input.maxLength = 80; input.setAttribute('aria-describedby', 'gcpro-coverage-error');
    form.reset(); error.textContent = ''; result.textContent = ''; call.hidden = true;
    input.removeAttribute('aria-invalid');
    const modal = root.closest('.elementor-popup-modal');
    if (modal) {
      modal.setAttribute('role', 'dialog');
      modal.setAttribute('aria-label', 'Check Service Availability');
      modal.focus({ preventScroll: true });
      const close = modal.querySelector('.dialog-close-button');
      if (close) close.setAttribute('aria-label', 'Close service availability');
    }
  }
  document.addEventListener('submit', event => {
    const root = event.target.closest('.elementor-popup-modal')?.querySelector('[data-elementor-id="1801"]'); if (!root) return;
    const input = root.querySelector('input'), error = root.querySelector('[data-error]');
    const result = root.querySelector('[data-result]'), call = root.querySelector('a[href="tel:+18476563322"]');
    const config = JSON.parse(root.querySelector('[type="application/json"]').textContent);
    event.preventDefault(); event.stopImmediatePropagation();
    const value = input.value.trim().replace(/\s+/g, ' ');
    const valid = value.length <= 80 && (/^\d{5}$/.test(value) || /^[A-Za-z]+(?:[ .’'\-][A-Za-z]+)*$/.test(value));
    error.textContent = ''; result.textContent = ''; call.hidden = true;
    if (!valid) {
      error.textContent = 'Enter a city name or a five-digit US ZIP code.';
      input.setAttribute('aria-invalid', 'true'); input.focus({ preventScroll: true }); return;
    }
    input.removeAttribute('aria-invalid');
    const match = lookup(value, config);
    const messages = {
      covered: `Yes, GCPRO serves ${match.location}. Call us to discuss your restoration needs.`,
      excluded: 'This location is outside our current service area.',
      partial: `We serve selected areas of ${match.location}. Please enter your ZIP code to check your location.`,
      uncertain: config.provisionalMessage || 'We couldn\u2019t confirm coverage for this location. Call us to check your area.'
    };
    result.textContent = messages[match.status] || messages.uncertain;
    call.hidden = !['covered', 'uncertain'].includes(match.status);
  }, true);
  // Elementor owns the modal, Escape, overlay and focus restoration. Supplement Tab containment.
  document.addEventListener('keydown', event => {
    if (event.key !== 'Tab') return;
    const modal = event.target.closest('.elementor-popup-modal');
    if (!modal || !modal.querySelector('[data-elementor-id="1801"]')) return;
    const focusable = [...modal.querySelectorAll('a[href],button,input,[tabindex="0"]')].filter(x => !x.hidden && !x.disabled && x.getClientRects().length);
    const first = focusable[0], last = focusable[focusable.length - 1];
    if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
    else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
  });
  if (window.jQuery) window.jQuery(document).on('elementor/popup/show.gcproAvailability', (event, id) => { if (+id === 1801) reset(); });
  if (window.jQuery) window.jQuery(document).on('elementor/popup/hide.gcproAvailability', (event, id) => {
    if (+id === 1801) {
      const restore = () => {
        if (trigger?.isConnected) trigger.focus({ preventScroll: true });
        window.scrollTo({ left: pagePosition.x, top: pagePosition.y, behavior: 'instant' });
      };
      requestAnimationFrame(restore);
      // Elementor finishes its native fade-out/focus work after 300ms.
      setTimeout(restore, 340);
    }
  });
  reset();
})();
