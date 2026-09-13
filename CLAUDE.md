# WeMelt — Website

Site: `wemelt.studio`. E-commerce on **Shopify** with an editorial front-end.

Brand system source of truth: the five PDFs in `wemelt_brand_system_docs/`. This file
is the working summary — when it and a PDF disagree, **the PDF wins**; update this file.

> Extracting text from those PDFs: `swift scripts/pdftext.swift <file.pdf>`
> (poppler/pdftoppm is NOT installed on this machine, and there is no Homebrew.)

---

## 1. What WeMelt is

**A design lab specialized in elevating plastics beyond waste.**

Descriptor: `Design Lab`. Purpose: transform plastic waste into high-quality design
products with strong aesthetic value.

**Core positioning — the most important single rule:**
WeMelt does not sell recycling. WeMelt sells **design that starts from recycling**.
Recycling is the process; design is the value proposition. Never present the material
only as an environmental solution — present it as matter, texture, colour, possibility,
function, culture, experience.

Primary claim: **Elevating plastics beyond waste.**

### Four brand territories
| Territory | Role |
|---|---|
| **Objects** | Functional/decorative objects. Main B2C e-commerce environment. |
| **Landscapes** | The material/finish universe — recycled-plastic textures and colour compositions. |
| **Projects** | Collaborations & Custom Editions (brands, events, hospitality, spaces, gifting). |
| **Community** | Protect Plastic — Workshops, Community Actions, Plastic Guardians. |

Voice: **Warm · Bold · Sharp.** Personality: Friend / Magician / Rebel.

---

## 2. Colour

Web Profile A — **Formal**. Confirmed by the client (2026-09-10) as the active
profile; Profile B (Distinctive) is not in use and its PDF is not needed. The two
differ in exactly one value: Molten Coral, `#FE492A` in A vs `#F05A3C` in B.

The site is *not* a Navy interface. It is **a neutral interface identified by Navy**.

| Token | Hex | Role |
|---|---|---|
| Deep Navy | `#16336F` | Digital brand signature. **Identifies.** |
| Molten Coral | `#FE492A` | Expressive brand ink — hovers, markers, arrows. **Activates.** |
| Gram Coral | `#F05A3C` | **Gram System metrics only** — Profile B's coral, kept deliberately |
| Molten Coral UI Ink | `#C13720` | Accessible derivative — small functional text only |
| Light Grey | `#E9E9E8` | Primary canvas. **Unifies.** |
| Cool Grey | `#C2CDD6` | Secondary field — deliberate pauses only |
| Charcoal Black | `#222321` | Functional interface ink. **Operates.** |
| Medium Grey | `#6D7481` | Metadata, captions, secondary info |
| Acid Lime | `#C5F95E` | Experimental / lab / data accent |

### The rule that governs everything
**Navy identifies. Charcoal operates.**

Deep Navy is for: header wordmark, hero wordmark, selected page headings, structural
brand statements, Cool Grey editorial fields, Projects/B2B moments.
Deep Navy is **not** for: body text, product names, prices, controls, navigation,
universal interface ink. Its identity value depends on staying distinct from Charcoal.

**Never** use Navy, Coral or Acid Lime just to make routine e-commerce controls feel
branded. Molten Coral must not become the universal CTA colour. Acid Lime must not be
a standard CTA or navigation colour.

Do not alternate Light Grey and Cool Grey mechanically section by section — the canvas
should read as one continuous digital surface.

### Defaults
- **Header:** Light Grey bg / Deep Navy wordmark / Charcoal navigation + utility.
  Do not recolour the whole navigation Navy.
- **Hero:** Light Grey bg / Deep Navy wordmark / Charcoal or Navy claim / Charcoal copy.
  Calm, editorial, confident, product-oriented — not colour-led.
- **Commerce:** Light Grey bg; product name, price, body, gram data, controls all Charcoal.
  Buttons = neutral high-contrast. Product imagery stays dominant.
- **Sold out:** `SOLD OUT` in Molten Coral UI Ink + strikethrough + disabled state +
  accessible semantics. **Must be understandable without colour.**

### Hover
Do not recolour product names or prices just to create interaction — Charcoal→Navy is
too subtle to be meaningful feedback. Prefer secondary image reveal, subtle image scale,
restrained line movement. *Colour responds to meaning, not to cursor presence.*

---

## 3. Typography

Four families, four jobs. They are **not interchangeable styles**.

| Family | Role | Principle |
|---|---|---|
| **Martian Grotesk** Expanded Black | Signature / impact / metrics | the metric **amplifies** |
| **Plantin MT Pro** | Story / editorial / brand voice | — |
| **Clash Grotesk** | Structure / interface — **primary typeface** | — |
| **Source Code** | Process / lab / information | Source Code **informs** |

**Default: if no other role is specifically required, use Clash Grotesk.**

Limits: simple component → max 2 families. Complex editorial composition → max 3.
All four in one composition should be exceptional.

### Pairings
- **Plantin + Clash** = Story + Structure → hero, brand storytelling, campaigns, editorial
- **Clash + Source Code** = Structure + Information → **the primary Product Page relationship**
- **Metric + Source Code** = Impact + Documentation → Gram Visualization with annotation
- **Metric + Brand Mark** = Metric + Signature → Gram Seal

### Never use
- **the metric face** for: navigation, buttons, body, product names, routine gram data, long headings. *Its value comes from scarcity.*
- **Plantin** for: navigation, CTA, product metadata, prices, specs, long technical text.
- **Source Code** for: long narrative, About storytelling, navigation, large headlines.

### Case
- Clash **uppercase** for short structural elements: `TABLE RITUAL`, `SHOP NOW`, `ADD TO CART`
- Clash **sentence case** for body, descriptions, longer headings, forms
- Plantin **sentence case** — literary, not institutional. Avoid systematic uppercase.
- Source Code **uppercase** for labels/specs/classifications: `RECYCLED HDPE`

### Scale — display
| | Desktop | Mobile | Line-height |
|---|---|---|---|
| Metric (Martian Grotesk) | `clamp(72px, 11vw, 190px)` | `clamp(56px, 18vw, 110px)` | 0.80–0.92 |
| Plantin / brand | `clamp(52px, 7vw, 120px)` | `clamp(36px, 11vw, 64px)` | 0.95–1.08 |
| Clash / structural | `clamp(48px, 6vw, 96px)` | `clamp(32px, 9vw, 56px)` | 0.90–1.05 |

### Scale — general content
H1 Clash Semibold 40–64 / 32–44 · H2 Clash Medium–Semibold 28–44 / 24–34 ·
H3 Clash Medium 18–26 / 18–22 · Body Clash Regular 16–18, line-height 1.4–1.55

### Scale — product / commerce (compact, product-first)
| | Desktop | Mobile |
|---|---|---|
| Product name (Clash Med/Semi) | 18–20px | 17–19px |
| Price (Clash Medium) | 15–16px | 14–16px |
| Interface labels (Clash Medium) | 12–13px | 12–13px |
| Nav / CTA (Clash Medium) | 12–13px | 12–13px |
| Source Code / product info | 14–16px | 14–16px |
| Source Code / technical data | 11–13px | 11–13px |

**Critical:** do not apply display typography just because an element is semantically an
`H1`. Semantic HTML hierarchy and visual scale are separate decisions. Product pages
never inherit editorial display sizes.

---

## 4. The Gram System

Same verified value, three functions:

| Level | Typeface | Use | Principle |
|---|---|---|---|
| **Gram Data** | Source Code | Product pages, specs — factual | informs |
| **Gram Visualization** | Martian Grotesk | Posters, campaigns, community metrics | amplifies |
| **Gram Seal** | Martian Grotesk + Brand Mark | Labels, packaging, provenance | signs |

- Notation is always lowercase `g`: `22g`, never `22G`.
- Thousands separator is a **full stop**: `490.839g`, never `490,839g` — client-confirmed
  2026-09-10. The V1 PDFs show commas (`12,840g`) and have not been reissued.
- Standard Product Page expression: `RECYCLED PLASTIC / {value}g` → e.g. `RECYCLED PLASTIC / 139g`
- **Do not** use `139g PROTECTED` as the default Product Page expression. `PROTECTED` is
  contextual, only where the Protect Plastic narrative is relevant.
- Colour: product-specific grams → **neutral by default** (Charcoal). Editorial/collective
  gram visualization → colour permitted.
- Gram Seal default: Gram Visualization + Brand Mark as **one colour unit** (Medium Grey on
  Light Grey/white). Don't colour metric and mark separately.

---

## 5. Product architecture

```
OBJECTS → RITUALS → PRODUCTS → LANDSCAPE VARIANTS
```

V1 Rituals: **Table Ritual** (encounter, balance, domesticity, shared ritual),
**Desk Ritual** (focus, clarity, structure, daily rhythm),
**Bathroom Ritual** (care, calm, intimacy, sensory ritual).
Creative Ritual is out of V1 scope.

Each Ritual = one Shopify Collection. Collections give commercial structure; the
front-end gives the editorial experience.

**There is no separate "Shop".** Shopping is integrated into Objects.

UX reference: Blanked Studios — for restraint, product hierarchy, minimal catalogue
info, progressive disclosure. **Do not reproduce its visual identity.**

> Show less before the click. Show everything when it matters.

### Product card — show ONLY
Image (1:1) · Product name · Price *or* `Sold out`. Whole card clickable.

**Never on a card:** Landscape, material, ritual, dimensions, grams, description,
sustainability claims, features. Those belong to the Product Page.

Pricing: single price → `€24`. Variants at different prices → `FROM €24`.
No purchasable variant → `Sold out` (sold-out products stay visible).

Hover (optional): subtle image scale or secondary image reveal. Hover must never be
required to understand the product — mobile has no hover.

### Objects landing
Three Ritual modules (`TABLE RITUAL` / `DESK RITUAL` / `BATHROOM RITUAL`, each `SHOP NOW`),
then the full catalogue. Grid: **desktop 4 col / tablet 2 / mobile 1**.

### Ritual collection page
Ritual hero (collection image, name, short description, four concepts) → then products
immediately. No long editorial intro before products.

### Individual product page
Desktop **50/50**: media left, purchase right. Purchase panel may be sticky on desktop —
**never sticky on mobile**. Mobile: simple swipeable gallery, no complex thumbnails or
floating controls.

Purchase order:
```
PRODUCT NAME
Price
LANDSCAPE            (selector, e.g. LANDSCAPE  FROSTED LAKE ↓)
QUANTITY
ADD TO CART
Short description
RECYCLED PLASTIC / 139g
FEATURES / MATERIALS / SHIPPING   (accordions)
```
Priorities: **purchase first, material visible, technical info when needed.** The user
must never have to search for price, Landscape, quantity or Add to cart.

---

## 6. Language

Vocabulary (use consistently): Objects · Rituals · Landscapes · Custom Editions ·
Protect Plastic · Plastic Guardians · Community Actions · Workshops · Gram System ·
Recycled HDPE. Landscape examples: Frosted Lava, Stormy Ocean, Tropical Cave.
**Frosted Lava, never Frosted Lake** — client-confirmed 2026-09-10; the V1 PDFs say
"Lake" and have not been reissued.

Naming: **Objects** short and functional (Coaster, Tray, Incense Holder) — the Landscape
carries the expressive layer. **Rituals** always `[Context] + Ritual`. **Landscapes**
evoke place/atmosphere/weather/light — `Frosted Lava`, never `Blue White Mix`.

Headlines communicate one idea: `PROTECT PLASTIC.` / `THEY DUMP. WE MELT.` /
`RECYCLING NEVER LOOKED SO GOOD.` Never headlines that read as explanatory paragraphs.

Body copy: headline → 1 short intro sentence → 1–2 short paragraphs max.
CTA verbs: Shop · Explore · Discover · Protect · Join.

The claim has **two valid typographic expressions** — same words, different function:
- Plantin, large → narrative/emotional/hero: *Elevating plastics beyond waste.*
- Source Code, small → annotation/running header: `ELEVATING PLASTICS BEYOND WASTE`

---

## 7. Asset status — OPEN ISSUES

✅ **ABC Gravity retired (2026-09-10).** The only supplied file was an unlicensed
trial, so it was replaced — at the client's direction — by **Martian Grotesk**, the
open-source variable font (SIL OFL 1.1) from `github.com/evilmartians/grotesk`,
self-hosted in `wemelt-landing/fonts/`. Metric style is **Expanded Black** —
`wght 900`, `wdth 125%`, tracking `-0.03em`, leading `0.9` — the client's preferred
direction, chosen over SemiCondensed Ultra (1000 / 87.5%) after both were built and
measured. Being the wider cut, it depends on a 620–899px size step-down in
`gram.css` to clear the seal panel; keep the two together. It is used **only** for Gram
Visualization / large impact metrics — Clash, Plantin and Source Code are unchanged.
The PDFs still name "ABC Gravity SemiCondensed Ultra" and have not been reissued;
the metric role is now Martian Grotesk Expanded Black by the client's decision.

✅ **Clash Grotesk complete (2026-09-10).** Light 300 / Regular 400 / Medium 500 from
the official Fontshare / Indian Type Foundry webfont delivery (v1.001, ITF Free Font
License, commercial use permitted), self-hosted WOFF2 at 19 KB each. Verified
metrically identical to the OTFs they replace. This is Clash **Grotesk**, never Clash
**Display**. Re-download from fontshare.com, not GitHub mirrors.

✅ **Source Code Pro upgraded (2026-09-10)** to the official Adobe release 2.042
(adobe-fonts/source-code-pro, SIL OFL 1.1), self-hosted WOFF2 in the landing page —
75 KB with 1335 codepoints, replacing a 101 KB 2012 build with 659. Regular only;
the page sets no other weight.
⚠️ Docs still specify "Source Code **Variable**". The VF exists
(`WOFF2/VF/SourceCodeVF-Upright.otf.woff2`, wght 200–900) and is the upgrade path
when Product Pages need Medium/Semibold — but its family is `SourceCodeVF` and its
default instance is **200 (ExtraLight)**, so every rule must state a weight.

✅ **Plantin MT Pro Roman licensed (2026-09-10).** The user supplied a Monotype
webfont kit (`wemelt_typography/PlantinProRoman/` → woff2 + woff, `PlantinMTPro-Regular`).
It ships in the landing page at 47 KB, replacing the 126 KB TTF; glyph coverage is
identical (665 codepoints, full Catalan set). Roman/Regular only — Semibold exists in
the brand assets but nothing sets it. Docs also list a **Medium** weight that has never
been supplied.

**All fonts on the landing page are now licensed and self-hosted as WOFF2** in
`wemelt-landing/fonts/` (324 KB total): Clash Grotesk 300/400/500 (Fontshare),
Plantin MT Pro Roman (licensed Monotype kit), Source Code Pro 2.042 (Adobe, OFL) and
Martian Grotesk variable (OFL). `wemelt_typography/` holds the original supplied
files and is no longer the source of truth for the build.

Also not yet supplied: identity artwork (Wordmark, Brand Mark, Lettermark, Geometric
Monogram). These are **approved artwork assets, not typefaces** — never recreate or
typeset them in Martian Grotesk or any other face. `Media/` holds 54 photographic assets and
1 SVG.

## 8. Client decisions — 2026-09-10

These are settled and override the V1 PDFs, which have not been reissued:

- **Colour Profile A (Formal)** is active. Molten Coral `#FE492A` for interaction and
  accent. **Exception:** the Gram System's metric typography keeps Profile B's coral
  `#F05A3C` (token `--wm-gram-coral`) — client decision. Two corals, split by role:
  `#FE492A` activates, `#F05A3C` measures.
- **"Frosted Lava", never "Frosted Lake"** — site-wide.
- **Thousands separator is a full stop**: `490.839g`.
- **Material Landscapes**: 9 slides. The **two "Frosted Lava" entries are intentional**
  — slide 1 is an artistic interpretation (title only, no composition, no
  `RECYCLED HDPE`), slide 2 is the original material with its composition. Never
  collapse them as duplicates. Frosted Lake is deliberately out of the carousel.
- **Community stats** confirmed current: 43 objects / 02 collection points /
  03 community actions.
- **Privacy + Terms removed** until the legal pages exist. No placeholder links.
- **Favicon** is the **W from the Lettermark** in Molten Coral `#F05A3C` on
  transparent, fitted square with a 4% margin. Source is a pixel-exact crop at
  `logos/wemelt-lettermark-w.png` (582x454, 1.28:1) — never a redraw. The full
  Lettermark was tried first but is 2.59:1, only ~6px tall at 16px, and illegible.
  Favicon gotchas: `/favicon.ico` must exist at the **site root** (browsers request it
  directly), and every icon link carries `?v=N` from `ICON_V` in build-index.py —
  the browser favicon cache ignores Cache-Control and survives hard reloads, so
  **bump ICON_V whenever icons change**.
  **OG image** is Wordmark + claim on Deep Navy. Both generated by scripts.
- **Product cards**: title Clash Light 16px on the hover label's baseline (states
  swap in place); hover row is `RECYCLED PLASTIC` in Source Code + gram value in
  Martian Grotesk Expanded Black at 27px, both `#F05A3C`. The metric value needs a
  300px card, so it applies only above a 1200px viewport — narrower cards keep the
  compact Source Code value. Row height stays 44px everywhere.
- **Four Territories**: description copy is Clash **Regular 400** (not Light); on
  hover a charcoal `rgba(34,35,33,0.45)` fades in behind the veil over 220ms —
  opacity only, never zoom/scale/blur. 0.45 is the point where Light Grey text over
  a light photo area clears AA (4.61:1).
- **Plastic Guardians text panel is Deep Navy `#16336F`**, never Charcoal. It is the
  one place besides the hero where the brand colour becomes a full field.

## 9. Not yet decided
Tech stack (Shopify theme/Liquid vs headless/Hydrogen vs other). No code in the repo yet.
`WEMELT_WEB_INTERFACE_SYSTEM_V1.md` is referenced by the other documents but has not
been supplied.
