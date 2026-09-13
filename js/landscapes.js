/* ==========================================================================
   MATERIAL LANDSCAPES — crossfade carousel
   The only behaviour on the page that needs JavaScript. Every other
   interaction (header marks, hero claim, product cards, image hovers) is a
   descendant of its own hover target, so CSS :hover handles it.

   Slides are already in the DOM; this only moves the active flag and updates
   the caption. Without JS the first Landscape stays visible and readable.
   ========================================================================== */

export function initLandscapes(root) {
  const stage = root.querySelector('[data-landscape-stage]');
  if (!stage) return;

  const slides = Array.from(stage.querySelectorAll('[data-landscape-slide]'));
  const nameEl = root.querySelector('[data-landscape-name]');
  const metaEl = root.querySelector('[data-landscape-meta]');
  const compEl = root.querySelector('[data-landscape-comp]');
  const live = root.querySelector('[data-landscape-live]');
  const prev = root.querySelector('[data-landscape-prev]');
  const next = root.querySelector('[data-landscape-next]');
  if (!slides.length) return;

  let index = slides.findIndex((s) => s.hasAttribute('data-active'));
  if (index < 0) index = 0;

  function show(i) {
    const n = slides.length;
    index = ((i % n) + n) % n; // wrap in both directions

    slides.forEach((slide, k) => {
      const on = k === index;
      slide.toggleAttribute('data-active', on);
      // the frame coming into view must not stay lazy
      if (on && slide.loading === 'lazy') slide.loading = 'eager';
    });

    const active = slides[index];
    const name = active.dataset.name || '';
    const comp = active.dataset.composition || '';

    if (nameEl) nameEl.textContent = name;
    if (compEl) compEl.textContent = comp;
    if (metaEl) metaEl.hidden = !comp;
    // announce the change for screen readers without moving focus
    if (live) live.textContent = comp ? `${name}. ${comp}.` : name;

    preload(index + 1);
  }

  // fetch the neighbouring frame so stepping does not flash the placeholder
  function preload(i) {
    const slide = slides[((i % slides.length) + slides.length) % slides.length];
    if (slide && slide.loading === 'lazy') slide.loading = 'eager';
  }

  prev && prev.addEventListener('click', () => show(index - 1));
  next && next.addEventListener('click', () => show(index + 1));

  // arrow keys step the carousel when focus is inside it
  stage.closest('section').addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') { show(index - 1); }
    else if (e.key === 'ArrowRight') { show(index + 1); }
    else return;
    e.preventDefault();
  });

  show(index);
}
