/* GCPRO: Homepage-only Elementor Custom Code, body end. No theme changes. */
(() => {
  const touch = window.matchMedia('(hover: none) and (pointer: coarse)');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (!touch.matches || reduced.matches || !('IntersectionObserver' in window) ||
      document.body.classList.contains('elementor-editor-active')) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting || entry.intersectionRatio < 0.1 ||
          !touch.matches || reduced.matches) return;
      entry.target.setAttribute('data-gcpro-ripple', 'played');
      observer.unobserve(entry.target);
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.process-timeline:not([data-gcpro-ripple])').forEach((timeline) => {
    timeline.setAttribute('data-gcpro-ripple', 'waiting');
    observer.observe(timeline);
  });
})();
