# WeMelt — Landing Page

Production build of the approved Claude Design landing page (`Landing Page.dc.html`).
Static HTML, CSS and vanilla JS. **No build step, no dependencies, no Node.**

Serve the folder and it runs:

```bash
python3 -m http.server 8900
```

Deploy by uploading the folder as-is to Netlify, Vercel, Cloudflare Pages, S3 or
any static host. All paths are relative, so it works from a subdirectory too.

---

## Structure

```
index.html                 generated — see scripts/build-index.py
favicon.ico                root copy — browsers request /favicon.ico directly
og-image.png               1200×630 share card — scripts/make-og-image.swift
site.webmanifest           PWA icons + theme colour
icons/                     favicon set — scripts/make-favicons.swift
css/
  tokens.css               design-system tokens + @font-face
  base.css                 reset, focus, shared primitives (.btn .eyebrow .mark .media …)
  components/
    header.css  hero.css  about.css  territories.css
    objects.css  split-panel.css  landscapes.css  gram.css  footer.css
js/
  main.js                  entry
  landscapes.js            the carousel — the only behaviour needing JS
fonts/                     all WOFF2 — Clash ×3, Martian, Plantin, Source Code
img/                       AVIF + JPEG, 3 widths each
logos/                     wordmark / brandmark / lettermark, used as CSS masks
```

`split-panel.css` is shared by Material Landscapes, Custom Editions and Plastic
Guardians — all three are the same two-up layout with different modifiers.

## Regenerating

`index.html` is emitted from `scripts/build-index.py`, which holds the product,
territory and landscape data. Hand-writing 36 responsive `<picture>` blocks is
where mistakes live, so edit the data and re-run:

```bash
python3 scripts/build-index.py
```

To re-process imagery from the original handoff:

```bash
python3 scripts/optimize-images.py <handoff-root> wemelt-landing
```

## Interactions

Everything except the carousel is CSS `:hover` — each effect lives inside its own
hover target, exactly as the design file's state handlers did.

| Interaction | Implementation |
|---|---|
| Header hover → both marks Navy → Coral | `.header:hover .mark` |
| Hero claim warms on panel hover | `.hero__panel:hover .hero__claim-accent` |
| Hero image crossfade | `.media:hover .media__img--hover` |
| Product card image crossfade | `.product:hover .product__img--base { opacity: 0 }` |
| Product name → gram data | opposing opacity transitions |
| Objects band copy reveal | `.objects__band:hover .objects__band-overlay` |
| Landscape name + composition | `.landscapes__stage:hover .landscapes__overlay` |
| Custom Editions / Guardians image hover | shared `.media` |
| Guardians heading warms | `.split__text--navy:hover .split__title` |
| Carousel prev/next | `js/landscapes.js` |

Without JavaScript the page is complete; the carousel simply rests on the first
Landscape. Arrow keys step it when focus is inside the section.

## Metric typography

Gram Visualization and large impact metrics use **Martian Grotesk**, the open-source
variable font from [evilmartians/grotesk](https://github.com/evilmartians/grotesk),
self-hosted as a single 145 KB WOFF2 (`wght` 100–1000, `wdth` 75–200), SIL OFL 1.1.
The licence ships alongside it in `fonts/MartianGrotesk-OFL.txt`.

Approved style — the four values live in `css/tokens.css` so optical tuning never
touches the typographic direction:

```css
--metric-weight:   900;      /* Black    */
--metric-width:    125%;     /* Expanded */
--metric-tracking: -0.03em;
--metric-leading:  0.9;
```

`wdth: 125%` is the Expanded master exactly — measured against
`MartianGroteskExpanded-Black.otf` with font synthesis disabled, 672px vs 673px
for `490.839g` at 100px.

**Expanded Black is the client's preferred direction.** It is the wider of the two
cuts tested (6.484px of width per 1px of size), so it depends on the 620–899px
step-down in `gram.css` to clear the seal panel — keep the two together. Measured
clearance with it in place:

| viewport | size | clearance | with a 10-digit figure |
|---|---|---|---|
| 375 | 41px | 77px | 35px |
| 640 (tightest) | 34px | 61px | 26px |
| 900 | 46px | 98px | 51px |
| 1280 | 65px | 140px | 73px |

SemiCondensed Ultra (`1000` / `87.5%`) is the alternative that was built and
measured alongside it — 18% narrower, holds the base clamp with no step-down, and
matches the cut the typography PDF names. Swap the two token values to switch;
the step-down can stay either way (it is size-only and harmless).

Used **only** on `.gram__value`. Clash Grotesk, Plantin MT Pro and Source Code Pro
are untouched. `font-synthesis: none` keeps a fallback face from faking the weight
or width if the WOFF2 ever fails to load.

This replaced ABC Gravity, whose only supplied file was an unlicensed trial — so
the font blocker on this page is now closed.

## Editorial typography

Plantin MT Pro **Roman** (`PlantinMTPro-Regular`, Monotype) sets the hero claim, the
About statement, the Landscape name on carousel hover, and the closing brand line —
all at weight 400. It is the licensed Monotype webfont kit, woff2 with a woff
fallback, 47 KB (down from a 126 KB TTF). Glyph coverage was checked against the
original TTF: 665 codepoints in both, nothing subset away, full Catalan set intact.

Plantin **Semibold** exists in the brand assets but nothing on this page sets it, so
it does not ship. If a bold Plantin is ever needed, add it as a real 600 face rather
than letting the browser synthesise one from the Roman.

## Structural typography

Clash Grotesk is the primary interface typeface — navigation, CTAs, product
names, territory titles, body copy, labels. **If no other role is specifically
required, this is the face.**

Official Fontshare / Indian Type Foundry webfont delivery, v1.001, ITF Free Font
License (commercial use permitted — see `fonts/ClashGrotesk-LICENSE.txt`). Three
weights, 19 KB each:

| weight | file | used for |
|---|---|---|
| 300 Light | `ClashGrotesk-Light.woff2` | body copy, ledes, product names |
| 400 Regular | `ClashGrotesk-Regular.woff2` | general text |
| 500 Medium | `ClashGrotesk-Medium.woff2` | nav, CTAs, labels, section headings |

Verified against the OTFs it replaces: identical unitsPerEm, weight class,
ascender, descender, 407-codepoint coverage and glyph advances — same typeface,
same version, delivered as WOFF2 instead of OTF. **111 KB → 57 KB.**

This is Clash *Grotesk*, not Clash *Display* — a different typeface with
different metrics. Re-download from Fontshare rather than a GitHub mirror.

## Informational typography

Source Code Pro sets the technical and documentary layer — eyebrows, the
`SORT → WASH → SHRED → PRESS → SHAPE` process line, material and source specs,
the gram statistics table and the footer place line. All at weight 400.

**Official Adobe release 2.042**, self-hosted WOFF2 from
[adobe-fonts/source-code-pro](https://github.com/adobe-fonts/source-code-pro),
SIL OFL 1.1 (licence in `fonts/SourceCodePro-OFL.txt`). 75 KB, replacing a 101 KB
2012-vintage TTF — and **1335 codepoints against the old build's 659**. The only
two dropped are U+0000 and U+000D, which are control characters, not glyphs.

The brand docs specify "Source Code **Variable**". The variable font
(`WOFF2/VF/SourceCodeVF-Upright.otf.woff2`, 87 KB, `wght` 200–900) is the upgrade
path once Product Pages need Medium or Semibold — this page sets only Regular, so
the static is 12 KB lighter and simpler. If you do adopt the VF, note two traps:
its family name is `SourceCodeVF`, not `Source Code Pro`, and its **default
instance is 200 (ExtraLight)** — so every rule must state a weight explicitly,
because the brand system forbids light weights at small sizes.

## Material Landscapes

Nine slides. The **two "Frosted Lava" entries are intentional** — they are two
readings of the same Landscape, and must not be collapsed into one:

| # | slide | image | data shown |
|---|---|---|---|
| 1 | Frosted Lava — artistic interpretation | `material-landscapes` | title only |
| 2 | Frosted Lava — original material | `ls-01` | composition + `RECYCLED HDPE` |
| 3–9 | Marble Snow → Glassy Lake | `ls-02`…`ls-10` | composition + `RECYCLED HDPE` |

Slide 1 shows no composition and no `RECYCLED HDPE` label. That falls out of the
data rather than a special case: the whole meta block is hidden whenever a slide's
composition string is empty, so leaving it `""` is what makes a slide title-only.

**Frosted Lake was deliberately removed from the carousel** and is not returning.

## Footer

Privacy and Terms have been **removed**, not stubbed — there were no legal pages to
point at and the brief is no non-functional links. The markup carries a comment at
the removal point; re-add them there as real hrefs when the pages exist. The legal
bar now reads only `© WeMelt Studio 2026`.

## Brand assets — favicon and share card

Both are generated from approved artwork, not redrawn:

**Favicons** — `scripts/make-favicons.swift` takes approved artwork and recolours
its own alpha channel. Nothing is reconstructed; proportions are always preserved.

Current set: the **W from the Lettermark** in Molten Coral `#F05A3C` on a
transparent background, fitted square with a 4% margin. Outputs a real
multi-resolution `favicon.ico` (16/32/48) plus PNGs at 16, 32, 48, 180
(apple-touch), 192 and 512.

### Two things that make favicon changes appear not to apply

1. **`/favicon.ico` must exist at the site root.** Browsers request that exact path
   on their own, regardless of `<link>` tags; when it 404s they fall back to
   whatever they cached for the origin. The generator writes it to both `icons/`
   and the root — keep both.

2. **The favicon cache is a separate store** from the HTTP cache. It ignores
   `Cache-Control`, survives hard reloads, and on some browsers survives clearing
   site data. The only dependable fix is to change the URL, so every icon link
   carries `?v=N` from `ICON_V` in `scripts/build-index.py`. **Bump `ICON_V`
   whenever the icons change** — including on Vercel — or the old icon persists.

The source is `logos/wemelt-lettermark-w.png` — a pixel-exact crop of the approved
Lettermark, not a redraw. The full mark is two letters with a 26px gap at x 587–612;
the W occupies x 5–586, y 5–458, and the crop is exactly that box, so ink fills
100% of it with no clipping. Regenerate with:

```bash
swift scripts/crop.swift logos/wemelt-lettermark-black.png \
      logos/wemelt-lettermark-w.png 5 5 582 454
```

**Why the W rather than the whole Lettermark.** The full mark is 2.59:1, so in a
square canvas it could only occupy ~38% of the height — 6px of a 16px icon, at
which the counters collapsed into a smear. The W alone is **1.28:1**, so it fills
the canvas properly and stays legible at 16px. Verified by magnifying the actual
generated files, not by assumption.

**OG image** — `scripts/make-og-image.swift`, 1200×630: Deep Navy field, Light Grey
Wordmark, the claim in Plantin MT Pro Roman, a hairline rule, and the
`WEMELT — DESIGN LAB` descriptor in Source Code. It is the hero's own colour and
type relationship cropped to a share card, so no new visual direction is
introduced. Regenerate either script if the source artwork changes.

## Product card typography

All eight cards share one system.

**Default title** — Clash Grotesk Light at **16px** (+2px), sitting on the same
baseline the hover label uses, so the two states cross-fade in place instead of
jumping. The shift is `position: relative` + `top`, which moves the text
visually without touching the flex layout, so the 44px row height is unchanged.

**Hover** — `RECYCLED PLASTIC` left in Source Code Pro, gram value right in
Martian Grotesk Expanded Black (wght 900 / wdth 125%), both in the gram coral
`#F05A3C`.

Value sizing is derived, not guessed: the face's ink for a 4-character value is
0.800em above the baseline and 0.223em below — 1.023em total. The row is 44px
with 6px padding, leaving 32px inside; holding a ~2px safety margin top and
bottom gives 28px of ink, so **28 / 1.023 = 27px**. Measured result: 2.2px above
and below the ink, 2px to the right of the value. Tight on all four sides,
touching none.

### Why the metric treatment has a width floor

**Width, not height, is the binding constraint.** `RECYCLED PLASTIC` at 14px is
139px and the widest value (`433g`) is 94px; with the gap and inset the row needs
**247px**. The 4-column grid only supplies that above a **1200px** viewport
(300px cards).

Below it the label alone nearly fills the row — at 768px the card is 192px and the
inner row 164px — so the value overflowed and the label wrapped to two lines.
Narrower cards therefore keep the established compact treatment: same content,
same order, same alignment, Source Code value at 14px. The +2px title applies at
every width, since the widest title (122px) fits the narrowest row (132px).

If the metric treatment is wanted at all widths, the grid is the lever — dropping
to 2 columns earlier would give the cards the width they need.

## Four Territories cards

Description copy is Clash Grotesk **Regular (400)** — typeface, 16px size, 24px
line-height, position and Light Grey colour all unchanged. Titles and CTAs are
untouched at weight 500.

**Hover darkening.** A solid charcoal fades in behind the two existing gradient
veils at `rgba(34, 35, 33, 0.45)` over 220ms. It rides on `background-color`
rather than a third gradient layer because a background-image list cannot
transition smoothly, whereas a colour can — and painting behind the gradients
composites identically, since all three are semi-transparent charcoal/navy.

Opacity only: no blur, no zoom, no scale, no movement. The image keeps
`transform: none` and its original `saturate(0.82) brightness(0.86)`. Text and CTA
sit above the veil in paint order, so neither is affected.

`0.45` was chosen over `0.40` because it is where the worst case clears WCAG AA.
Text contrast over a light area of the photograph:

| overlay | worst-case contrast | mid-pixel luminance drop |
|---|---|---|
| none (default) | 2.16:1 | — |
| 0.40 | 4.20:1 | −45% |
| **0.45** | **4.61:1 — clears AA** | **−50%** |

## Colour

**Profile A (Formal) is the active profile**, confirmed by the client. The Claude
Design system was authored against Profile B (Distinctive); the two differ in
exactly one value — Molten Coral, `#FE492A` in A against `#F05A3C` in B. Every
other value is identical, and the swap is contrast-neutral (2.79:1 vs 2.77:1 on
Light Grey), so it was a one-line token change with no visual reworking.

Profile B's PDF was never supplied and is not needed.

### Inherited contrast notes

These come from the approved design and were **not** introduced by the build. They
are recorded rather than changed, since the composition is signed off:

| where | ratio | note |
|---|---|---|
| nav / arrow-link hover on Light Grey | 2.79:1 | resting state is Charcoal and passes; only the hover state is low |
| process arrows `→` | 2.79:1 | decorative separators, already `aria-hidden` |
| gram figure on Cool Grey | 2.10:1 | large display type; the brand system sanctions display Coral for exactly this |

`Molten Coral UI Ink` (`#C13720`) is the accessible derivative reserved for small
functional text — it reaches 4.51:1 on Light Grey. It is declared and available if
any of the above ever needs to pass AA.

## Media

**Imagery: 101 MB of camera originals → 1.56 MB** if every image on the page
loads. Each is AVIF with a JPEG fallback at three widths, `srcset`/`sizes` per
role, lazy below the fold, `fetchpriority="high"` on the hero — so a real visit
fetches only what it shows (the hero is ~51 KB).

macOS ImageIO has no WebP encoder, so AVIF is the modern format here. It
compresses better than WebP anyway and is supported by Chrome, Firefox, Edge and
Safari 16.4+; everything older gets the JPEG.

Measured full-page transfer:

| | KB |
|---|---|
| images (all 36) | 1556 |
| fonts | 324 |
| logos (3 masks) | 104 |
| css | 28 |
| js | 3 |
| **total** | **~2.01 MB** |

### Remaining optimisation

Every face on the page is now WOFF2 and properly licensed. Font transfer went
**483 KB → 324 KB (33% less)** across this pass:

| | before | after |
|---|---|---|
| Clash ×3 | 111 KB (otf) | **57 KB** |
| Plantin | 126 KB (ttf) | **47 KB** |
| Source Code | 101 KB (ttf, 2012) | **75 KB** (v2.042, 2× the glyphs) |
| Martian Grotesk | — | 145 KB |

The remaining lever is Martian Grotesk at 145 KB — it is a full two-axis variable
font used for a single line of text. Subsetting it to digits, `g` and the
punctuation the metric needs would cut it to a few KB, but that needs `pyftsubset`
(no Python `fonttools` on this machine).

```bash
pyftsubset fonts/MartianGrotesk-Variable.woff2 --flavor=woff2 \
  --text="0123456789.,g" --output-file=fonts/MartianGrotesk-metric.woff2
```

## Known items for the client

- `#privacy` and `#terms` in the footer have no destinations yet.
- `og:image` and `og:url` are absolute against **https://wemelt.studio/**. If this
  deploys anywhere else first (a Netlify preview, a staging domain), update both in
  `scripts/build-index.py` or the share card will 404 for scrapers.
- Privacy and Terms are deliberately absent — see *Footer* below.

## Corrections made after review

- **Plastic Guardians panel was Deep Navy, not Charcoal.** The approved design
  specifies `background: var(--wm-deep-navy)` on that text panel; the first build
  rendered it Charcoal. Fixed — the modifier is now `.split__text--navy`. All
  text on it still passes AA comfortably (title 9.95:1, copy 7.48:1, CTA 9.95:1).
  Every other section background was re-audited against the design file and
  matches.

## Differences from the design file

Everything visual is preserved. These are the implementation changes, each made
for a stated reason:

1. **`@media` queries replace JS breakpoints.** The design read
   `window.innerWidth` on every resize event to pick column counts. The same
   breakpoints (620 / 820 / 1080) are now CSS, so layout no longer depends on JS.
2. **`<img>` replaces CSS `background-image`.** The design had zero `<img>` tags,
   so images could not carry alt text, `srcset` or lazy-loading. All 36 are now
   real elements with `object-fit: cover` — visually identical.
3. **The gram figure sizes itself.** The design pinned `width:439px; height:48px`
   on text sized `clamp(41px, 5.1vw, 75px)`; above roughly 940px viewport the
   glyphs were clipped by their own box.
4. **Touch fallbacks.** Product gram data, Landscape names and the objects band
   copy were hover-only and unreachable on touch. Under `@media (hover: none)`
   they are shown outright.
5. **Focus states, skip link, landmarks, `prefers-reduced-motion`.** None were in
   the design; all are additive and invisible to mouse users.
6. **Editing artefacts removed** — empty `<span>`s carrying `caret-color` and
   `font-family: -webkit-standard` left over from canvas text editing.
7. **Coral tokenised.** `#F05A3C` appeared as a raw hex 38 times; it is now
   `--wm-molten-coral`.
8. **Two copy typos fixed** — "sapces" → "spaces", and a stray space in
   "Made in Barcelona ."
9. **ABC Gravity replaced by Martian Grotesk** for the metric — see *Metric
   typography* above. Requested by the client; it also closes the trial-licence
   blocker. No other typeface changed.
10. **Metric size eased between 620–899px.** Expanded Black is much wider than
    Gravity SemiCondensed, and just after the gram grid splits into two columns
    the figure cleared its panel by only ~16px — leaving no room for the number
    to grow. Across that band alone it steps to `clamp(34px, 4.4vw, 44px)`,
    handing back to the approved `clamp(41px, 5.1vw, 75px)` at 900px. Weight,
    width, tracking and leading are unchanged, so this is size only and the
    character of the metric is identical.
