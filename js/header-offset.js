/* ==========================================================================
   Anchor offset — keeps jumped-to sections clear of the sticky header.

   `scroll-padding-top` reads `--header-h`. css/tokens.css sets per-breakpoint
   fallbacks, but the header's real height is not predictable from width alone:
   it changes as the nav wraps, and those wrap points move with the width of the
   nav text. So here we measure the actual element and publish the result.

   Progressive enhancement — with JS off, the CSS fallbacks still clear the
   header; this only makes the offset exact.
   ========================================================================== */

export function initHeaderOffset(root = document) {
  const header = root.querySelector('.header');
  if (!header) return;

  const docEl = root.documentElement;
  let last = -1;

  const apply = () => {
    // round up so a fractional height never leaves a sliver of the section hidden
    const h = Math.ceil(header.getBoundingClientRect().height);
    if (h && h !== last) {
      last = h;
      docEl.style.setProperty('--header-h', h + 'px');
    }
  };

  apply();

  if ('ResizeObserver' in window) {
    // fires on wrap changes too, not just viewport resizes
    new ResizeObserver(apply).observe(header);
  } else {
    window.addEventListener('resize', apply, { passive: true });
  }

  // late-loading webfonts can change the nav's wrap point, and therefore the height
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(apply);
  }
}
