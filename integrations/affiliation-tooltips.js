/* GCPRO staging: one centralized behavior owner; native Elementor owns content and visual styling. */
(() => {
  'use strict';
  if (location.hostname !== 'vitaliiv1.sg-host.com' || window.gcproAffiliationTooltips) return;
  const start = () => {
    const organizations = [
      ['iicrc', 'IICRC-white.svg', 'Institute of Inspection, Cleaning and Restoration Certification'],
      ['iaqa', 'IAQA-white.svg', 'Indoor Air Quality Association'],
      ['bbb', 'BBB-white.svg', 'Better Business Bureau'],
      ['ria', 'RIA.svg', 'Restoration Industry Association'],
      ['ra', 'gcpro-ra-white.png', 'Restoration Affiliates']
    ];
    const boxes = [...document.querySelectorAll('.gcpro-affiliation-tooltip')];
    const triggers = [...document.querySelectorAll('.gcpro-affiliation-trigger')];
    if (!boxes.length || !triggers.length) return;
    window.gcproAffiliationTooltips = true;
    let active = null, timer = 0, ignoreFocus = false, frame = 0;
    const focusable = box => box.querySelector('a[href], button, [tabindex="0"]');
    const place = () => {
      if (!active) return;
      const {trigger, box} = active, r = trigger.getBoundingClientRect();
      const b = box.getBoundingClientRect(), edge = 12, gap = 8, viewportWidth = document.documentElement.clientWidth;
      const x = Math.max(edge, Math.min(r.left + (r.width - b.width) / 2, viewportWidth - b.width - edge));
      const below = r.bottom + gap, above = r.top - b.height - gap;
      const y = below + b.height <= innerHeight - edge ? below : Math.max(edge, above);
      Object.assign(box.style, {left: `${Math.round(x)}px`, top: `${Math.round(y)}px`, maxHeight: `${innerHeight - edge * 2}px`, overflowY: 'auto'});
    };
    const close = (restore = false) => {
      clearTimeout(timer);
      if (!active) return;
      const {trigger, box} = active;
      trigger.setAttribute('aria-expanded', 'false');
      box.style.display = 'none'; box.setAttribute('aria-hidden', 'true');
      active = null;
      if (restore) { ignoreFocus = true; trigger.focus({preventScroll: true}); }
    };
    const open = (trigger, box, mode) => {
      clearTimeout(timer);
      if (active?.trigger !== trigger) close();
      active = {trigger, box, mode};
      box.style.display = 'block'; box.style.visibility = 'hidden';
      box.setAttribute('aria-hidden', 'false'); trigger.setAttribute('aria-expanded', 'true');
      place(); box.style.visibility = 'visible';
    };
    const later = () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        if (!active || active.mode === 'pinned') return;
        const {trigger, box} = active, focused = document.activeElement;
        if (!trigger.matches(':hover') && !box.matches(':hover') && focused !== trigger && !box.contains(focused)) close();
      }, 160);
    };
    organizations.forEach(([key, file, name]) => {
      const box = boxes.find(b => b.querySelector('h3')?.textContent.trim() === name);
      if (!box) return;
      box.id = `gcpro-affiliation-info-${key}`;
      box.setAttribute('role', 'dialog'); box.setAttribute('aria-modal', 'false');
      box.setAttribute('aria-label', name); box.setAttribute('aria-hidden', 'true');
      // Keep native Elementor styles scoped to the Footer document.
      box.addEventListener('pointerenter', () => clearTimeout(timer));
      box.addEventListener('pointerleave', later);
      box.addEventListener('focusout', () => setTimeout(() => {
        if (active?.box === box && !box.contains(document.activeElement) && document.activeElement !== active.trigger && !box.matches(':hover') && !active.trigger.matches(':hover')) close();
      }, 0));
      box.addEventListener('keydown', event => {
        if (event.key === 'Tab' && event.shiftKey && document.activeElement === focusable(box) && active) { event.preventDefault(); active.trigger.focus(); }
      });
      triggers.filter(t => t.querySelector('img')?.src.split('/').pop()?.split('?')[0] === file).forEach(trigger => {
        trigger.setAttribute('role', 'button'); trigger.tabIndex = 0;
        trigger.setAttribute('aria-label', `About ${name}`);
        trigger.setAttribute('aria-haspopup', 'dialog'); trigger.setAttribute('aria-expanded', 'false');
        trigger.setAttribute('aria-controls', box.id);
        let pointerFocusUntil = 0;
        trigger.addEventListener('pointerdown', () => { pointerFocusUntil = performance.now() + 500; });
        trigger.addEventListener('pointerenter', event => { if (event.pointerType === 'mouse' && active?.mode !== 'pinned') open(trigger, box, 'hover'); });
        trigger.addEventListener('pointerleave', later);
        trigger.addEventListener('focus', () => {
          if (ignoreFocus) { ignoreFocus = false; return; }
          if (performance.now() >= pointerFocusUntil) open(trigger, box, 'focus');
        });
        trigger.addEventListener('focusout', later);
        const toggle = () => active?.trigger === trigger && active.mode === 'pinned' ? close() : open(trigger, box, 'pinned');
        trigger.addEventListener('click', event => { event.preventDefault(); toggle(); });
        trigger.addEventListener('keydown', event => {
          if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); toggle(); }
          if (event.key === 'Tab' && !event.shiftKey && active?.trigger === trigger) {
            const link = focusable(box);
            if (link) { event.preventDefault(); link.focus(); }
          }
        });
      });
    });
    document.addEventListener('pointerdown', event => {
      if (active && !active.trigger.contains(event.target) && !active.box.contains(event.target)) close();
    }, true);
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && active) { event.preventDefault(); close(true); }
    });
    const reposition = () => {
      if (!active || frame) return;
      frame = requestAnimationFrame(() => { frame = 0; place(); });
    };
    addEventListener('resize', reposition, {passive: true});
    addEventListener('scroll', reposition, {passive: true, capture: true});
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, {once: true});
  else start();
})();
