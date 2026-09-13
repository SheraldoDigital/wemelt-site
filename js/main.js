/* ==========================================================================
   Entry point. Everything here is progressive enhancement — the page is
   complete and readable with JavaScript disabled.
   ========================================================================== */

import { initLandscapes } from './landscapes.js';
import { initHeaderOffset } from './header-offset.js';

const start = () => {
  initHeaderOffset(document);
  initLandscapes(document);
};

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', start, { once: true });
} else {
  start();
}
