# wemelt-site

Website to present WeMelt projects — a Barcelona design lab elevating plastics
beyond waste.

Static HTML, CSS and vanilla JavaScript. **No build step, no dependencies, no Node.**
The repository root *is* the deployable site.

```bash
./serve.sh          # http://localhost:8900 + your LAN address, for phone/tablet review
```

---

## Structure

```
index.html                  the page — generated, see scripts/build-index.py
site.webmanifest            PWA icons + theme colour
favicon.ico                 root copy; browsers request /favicon.ico directly
og-image.png                1200×630 share card

css/
  tokens.css                design tokens + @font-face
  base.css                  reset, focus, shared primitives (.btn .eyebrow .mark .media)
  components/
    header.css              sticky header, identity-mark hover
    hero.css                Deep Navy panel + product photograph
    about.css               tonal lettermark, Plantin statement, process line
    territories.css         the four brand territories
    objects.css             editorial band + product card grid
    split-panel.css         shared two-up layout (landscapes / editions / guardians)
    landscapes.css          material carousel
    gram.css                Gram System + community metrics
    footer.css

js/
  main.js                   entry point
  landscapes.js             the carousel — the only behaviour that needs JS

fonts/                      Clash Grotesk, Plantin MT Pro, Source Code Pro, Martian Grotesk
logos/                      approved identity marks, used as CSS mask-image
icons/                      favicon set
img/                        AVIF + JPEG, three widths each

scripts/                    build + asset tooling (see below)
DESIGN-NOTES.md             full implementation notes, decisions and rationale
CLAUDE.md                   brand system reference
```

## Components

Every section is its own stylesheet, and `split-panel.css` is shared by Material
Landscapes, Custom Editions and Plastic Guardians — all three are the same two-up
layout with different modifiers. Shared primitives (`.btn`, `.eyebrow`,
`.arrow-link`, `.mark`, `.media`) live in `base.css` so components stay thin.

Only the carousel needs JavaScript. Every other interaction — header marks, hero
claim, product crossfades, gram data, image hovers, territory darkening — is a
descendant of its own hover target, so plain CSS `:hover` drives it. **The page is
complete and readable with JavaScript disabled.**

## Responsive

Verified from 340 px to 1920 px: no horizontal overflow, no broken assets, no
console errors. Grids step 4 → 2 → 1 for territories and 4 → 2 for products.
Under `@media (hover: none)` everything hover-dependent is shown outright, so
touch users never lose content.

## Tooling

Nothing here runs at build or deploy time — these regenerate committed artefacts.

| Script | Purpose |
|---|---|
| `build-index.py` | Emits `index.html`; holds product, territory and landscape data |
| `optimize-images.py` | Camera originals → AVIF + JPEG at three widths |
| `make-favicons.swift` | Favicon set from approved artwork |
| `make-og-image.swift` | 1200×630 share card |
| `crop.swift` | Pixel-exact crop (used to cut the W from the Lettermark) |
| `conv.swift` | Single-image resize/convert helper |
| `dev-server.py` | Local review server with `Cache-Control: no-store` |
| `pdftext.swift` | Extract text from the brand-system PDFs |

Regenerate the page after editing its data:

```bash
python3 scripts/build-index.py
```

## Fonts

| Family | Role | Licence |
|---|---|---|
| Clash Grotesk 300/400/500 | Structure / interface — the primary typeface | ITF Free Font License |
| Plantin MT Pro Roman | Story / editorial | **Licensed Monotype webfont** |
| Source Code Pro 2.042 | Process / lab / information | SIL OFL 1.1 |
| Martian Grotesk (variable) | Signature / impact metrics | SIL OFL 1.1 |

All self-hosted as WOFF2, 324 KB total. **Plantin is licensed, not open** — it must
not be redistributed outside this project. This repository is private; keep it that
way, or remove the Plantin files before making it public.

## Before deploying

- `og:image` and `og:url` are absolute against `https://wemelt.studio/`. Change
  them in `scripts/build-index.py` if the site lands on another domain first, or
  the share card will 404 for scrapers.
- `scripts/dev-server.py` sends `Cache-Control: no-store`. That is correct for
  local review and **wrong for production** — hosting should serve long `max-age`
  for hashed assets.
- Bump `ICON_V` in `scripts/build-index.py` whenever the favicons change. The
  browser favicon cache ignores `Cache-Control` and survives hard reloads.

## Known open item

Anchor navigation uses a fixed `scroll-padding-top: 52px`, but the sticky header
grows to 69 px at 390 px wide and 99 px at 340 px, so a jumped-to section sits
17–47 px under the header on small screens. Fix pending.

See `DESIGN-NOTES.md` for the full record of decisions, measurements and known items.
