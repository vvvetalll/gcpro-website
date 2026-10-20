/* One global controller. No page/template/element ID selectors. */
(() => {
  if (location.hostname !== 'vitaliiv1.sg-host.com' || window.gcproScrollNavigation) return;
  if (document.body.classList.contains('elementor-editor-active') || new URLSearchParams(location.search).has('elementor-preview')) return;
  const header = document.querySelector('.gcpro-smart-header');
  const host = header?.closest('header');
  const bar = document.querySelector('.gcpro-mobile-cta');
  if (!header || !host || !bar) return;
  window.gcproScrollNavigation = true;
  const root = document.documentElement;
  const origin = document.querySelector('.gcpro-cta-origin');
  const intros = [...document.querySelectorAll('.gcpro-sticky-intro')];
  const introTops = new Map();
  const chat = document.querySelector('.sg-ai-floating-chat');
  const phone = bar.querySelector('a[href^="tel:"]')?.getAttribute('href');
  const calls = [...document.querySelectorAll('a[href^="tel:"]')].filter(a => !bar.contains(a) && a.getAttribute('href') === phone);
  let tasks = [...document.querySelectorAll('main form, main .gcpro-cta-suppress')];
  const overlaySelector = 'dialog[open], [aria-modal="true"], .bafg_popup_preview, .gcpro-cta-overlay';
  let overlays = [];
  let lastY = Math.max(0, scrollY), distance = 0, direction = 0, hidden = false, pending = false;
  let headerHeight = 0, utilityHeight = 0, barHeight = 0;
  const set = (el, key, value) => { if (el.style.getPropertyValue(key) !== value) el.style.setProperty(key, value); };
  const visible = el => {
    const r = el.getBoundingClientRect(), s = getComputedStyle(el);
    return r.width > 0 && r.height > 0 && s.display !== 'none' && s.visibility !== 'hidden' && Number(s.opacity) !== 0;
  };
  function measure() {
    intros.forEach(el => { el.style.removeProperty('top'); introTops.set(el, parseFloat(getComputedStyle(el).top) || 0); });
    headerHeight = header.offsetHeight;
    utilityHeight = header.querySelector('.info-bar')?.offsetHeight || 0;
    // Measure the hidden panel without flashing it or changing its native design.
    bar.classList.add('is-visible');
    barHeight = bar.offsetHeight;
    bar.classList.remove('is-visible');
    set(host, 'min-height', `${headerHeight}px`);
    set(root, '--gcpro-utility-height', `${utilityHeight}px`);
    set(root, '--gcpro-bottom-reserve', `${barHeight + 24}px`);
    schedule();
  }
  function update() {
    pending = false;
    const y = Math.max(0, Math.min(scrollY, root.scrollHeight - innerHeight));
    const delta = y - lastY;
    const nextDirection = Math.sign(delta);
    if (nextDirection && nextDirection !== direction) { distance = 0; direction = nextDirection; }
    distance += delta;
    lastY = y;
    const focusedHeader = header.contains(document.activeElement);
    const menuOpen = !!header.querySelector('[aria-expanded="true"]');
    const floating = host.getBoundingClientRect().bottom <= 0;
    if (!floating || focusedHeader || menuOpen) hidden = false;
    else if (distance > 40) hidden = true;
    else if (distance < -24) hidden = false;
    const admin = document.querySelector('#wpadminbar');
    const adminTop = admin ? Math.max(0, admin.getBoundingClientRect().bottom) : 0;
    set(root, '--gcpro-admin-top', `${adminTop}px`);
    header.classList.toggle('is-floating', floating);
    header.classList.toggle('is-hidden', floating && hidden);
    const clearance = floating && !hidden ? headerHeight - (focusedHeader ? 0 : utilityHeight) + adminTop : adminTop;
    set(root, '--gcpro-header-clearance', `${clearance + 8}px`);
    intros.forEach(el => {
      if (floating && !hidden && getComputedStyle(el).position === 'sticky') set(el, 'top', `${Math.max(introTops.get(el), clearance)}px`);
      else if (el.style.top) el.style.removeProperty('top');
    });
    const viewport = window.visualViewport;
    const height = viewport?.height || innerHeight;
    const editing = document.activeElement?.matches('input, textarea, select, [contenteditable="true"]');
    const chatPanel = chat?.shadowRoot?.querySelector('.wp-ai-studio-chat');
    const chatVisible = chatPanel && visible(chatPanel);
    const chatOpen = chatVisible && !chatPanel.classList.contains('wp-ai-studio-chat__minimized');
    set(root, '--gcpro-cta-right', chatVisible && !chatOpen ? `${innerWidth - chatPanel.getBoundingClientRect().left + 8}px` : '8px');
    const blocked = menuOpen || chatOpen || overlays.some(visible) || editing || height < 480 || (viewport && (viewport.scale > 1.05 || innerHeight - height > 150));
    const passed = origin ? origin.getBoundingClientRect().bottom < clearance - 8 : floating;
    const competing = calls.some(a => {
      if (!visible(a)) return false;
      const r = a.getBoundingClientRect();
      return r.top >= clearance && r.bottom <= height - barHeight - 24;
    });
    const taskVisible = tasks.some(el => {
      if (!visible(el)) return false;
      const r = el.getBoundingClientRect();
      return r.top < height - 24 && r.bottom > clearance;
    });
    let show = innerWidth < 768 && passed && !blocked && !competing && !taskVisible && !document.querySelector('.gcpro-cta-off');
    if (bar.contains(document.activeElement) && !menuOpen && !chatOpen && !overlays.some(visible)) show = true;
    bar.classList.toggle('is-visible', show);
    bar.inert = !show;
    bar.setAttribute('aria-hidden', String(!show));
    set(root, '--gcpro-bottom-clearance', show ? `${barHeight + 24}px` : '0px');
  }
  function schedule() { if (!pending) { pending = true; requestAnimationFrame(update); } }
  root.classList.add('gcpro-nav-ready');
  const resize = new ResizeObserver(measure);
  resize.observe(header);
  // Popup/menu state can change without a scroll. Ignore our own runtime writes.
  const mutations = new MutationObserver(records => {
    if (!records.some(r => ![root, header, bar, host].includes(r.target))) return;
    if (records.some(r => r.type === 'childList')) tasks = [...document.querySelectorAll('main form, main .gcpro-cta-suppress')];
    overlays = [...document.querySelectorAll(overlaySelector)];
    schedule();
  });
  const mutationOptions = {subtree: true, childList: true, attributes: true, attributeFilter: ['class', 'style', 'open', 'aria-expanded', 'aria-hidden']};
  mutations.observe(document.body, mutationOptions);
  chat?.addEventListener('click', schedule);
  overlays = [...document.querySelectorAll(overlaySelector)];
  window.addEventListener('scroll', schedule, {passive: true});
  window.addEventListener('resize', measure, {passive: true});
  window.addEventListener('pageshow', schedule);
  document.addEventListener('focusin', schedule);
  document.addEventListener('focusout', schedule);
  window.visualViewport?.addEventListener('resize', schedule, {passive: true});
  measure();
})();
