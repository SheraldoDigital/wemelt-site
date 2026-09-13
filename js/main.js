/* ==========================================================================
   Entry point. Everything here is progressive enhancement — the page is
   complete and readable with JavaScript disabled.
   ========================================================================== */

import { initLandscapes } from './landscapes.js';

const start = () => initLandscapes(document);

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', start, { once: true });
} else {
  start();
}
