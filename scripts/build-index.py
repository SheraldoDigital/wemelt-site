#!/usr/bin/env python3
"""
Generate wemelt-landing/index.html.

The page has 39 images, each needing an AVIF + JPEG <picture> across three
widths. Writing that by hand is where mistakes live, so the repeating blocks
(products, territories, landscape frames) are emitted from the data below.

Run after scripts/optimize-images.py, or any time the content changes:
    python3 scripts/build-index.py
"""
import os

ICON_V = "2"   # bump when the favicon set changes

OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "wemelt-landing", "index.html")

WIDTHS = {
    "hero": [900, 1500, 2100],
    "landscape": [900, 1500, 2100],
    "editorial": [900, 1500, 2100],
    "territory": [640, 1040, 1440],
    "product": [440, 760, 1120],
}
SIZES = {
    "hero": "(max-width: 679px) 100vw, 50vw",
    "landscape": "(max-width: 679px) 100vw, 50vw",
    "editorial": "(max-width: 679px) 100vw, 50vw",
    "territory": "(min-width: 1080px) 25vw, (min-width: 620px) 50vw, 100vw",
    "product": "(min-width: 620px) 25vw, 50vw",
    "band": "100vw",
}


def pic(stem, role, alt, cls, *, eager=False, sizes_key=None, extra=""):
    """One responsive <picture>: AVIF first, JPEG fallback."""
    ws = WIDTHS[role]
    sizes = SIZES[sizes_key or role]
    avif = ", ".join(f"img/{stem}-{w}.avif {w}w" for w in ws)
    jpg = ", ".join(f"img/{stem}-{w}.jpg {w}w" for w in ws)
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    return (
        f'<picture>\n'
        f'          <source type="image/avif" srcset="{avif}" sizes="{sizes}">\n'
        f'          <img src="img/{stem}-{ws[1]}.jpg" srcset="{jpg}" sizes="{sizes}"\n'
        f'               alt="{alt}" class="{cls}" {load} decoding="async"{extra}>\n'
        f'        </picture>'
    )


TERRITORIES = [
    ("01", "Objects", "Table, Desk and Bathroom Rituals — the pieces we make in series.",
     "See objects", "#objects", "territory-objects"),
    ("02", "Landscapes", "Frosted Lava, Stormy Ocean, etc — the material library.",
     "Explore landscapes", "#landscapes-section", "territory-landscapes"),
    ("03", "Projects", "Custom Editions for brands, events and spaces.",
     "Explore projects", "#projects", "territory-projects"),
    ("04", "Community", "Plastic Guardians, workshops and collection points across the city.",
     "Discover community", "#guardians", "territory-community"),
]

PRODUCTS = [
    ("Coaster Set", "154g", "product-coaster-set", "product-coaster-set-hover"),
    ("Tray 02", "110g", "product-tray-02", "product-tray-02-hover"),
    ("Post-it Case", "126g", "product-post-it", "product-post-it-hover"),
    ("Incense Holder", "139g", "product-incense", "product-incense-hover-v2"),
    ("Incense Pack", "278g", "product-05", "product-05-hover"),
    ("Napkins Holder", "433g", "product-06", "product-06-hover"),
    ("Soap Dish", "74g", "product-07-v2", "product-07-hover"),
    ("Tray Set", "363g", "product-08", "product-08-hover"),
]

# The two "Frosted Lava" entries are INTENTIONAL — do not collapse them.
#   Slide 1  artistic interpretation of the Landscape. Title only: no composition
#            and no "Recycled HDPE" (the meta block hides when composition is "").
#   Slide 2  the original Frosted Lava material, carrying its real composition.
# Frosted Lake was deliberately removed from the carousel and is not coming back.
LANDSCAPES = [
    ("Frosted Lava", "", "material-landscapes"),
    ("Frosted Lava", "Light Blue 60% · White 30% · Brown 6% · Orange 4%", "ls-01"),
    ("Marble Snow", "Black 40% · White 60%", "ls-02"),
    ("Stormy Ocean", "Navy Blue 80% · Blue 15% · White 5%", "ls-03"),
    ("Wild Sunset", "White 65% · Orange 20% · Red 10% · Purple 5%", "ls-04"),
    ("Low-Tide Reef", "Light Blue 85% · White 5% · Black 5% · Brown 5%", "ls-07"),
    ("Deep Forest", "Dark Green 65% · Green 25% · White 10%", "ls-08"),
    ("Solar Storm", "Semi-Transparent 70% · Purple 20% · Yellow 10%", "ls-09"),
    ("Glassy Lake", "Semi-Transparent 85% · White 10% · Light Blue 3% · Beige 2%", "ls-10"),
]


def territory_cards():
    out = []
    for idx, title, copy, cta, href, img in TERRITORIES:
        out.append(f'''      <article class="territory">
        {pic(img, "territory", "", "territory__img")}
        <span class="territory__veil" aria-hidden="true"></span>
        <span class="territory__index">{idx}</span>
        <div class="territory__body">
          <h3 class="territory__title">{title}</h3>
          <p class="territory__copy">{copy}</p>
          <a class="arrow-link" href="{href}">{cta} <span aria-hidden="true">&rarr;</span></a>
        </div>
      </article>''')
    return "\n".join(out)


def product_cards():
    out = []
    for entry in PRODUCTS:
        name, gram, base, hover = entry[:4]
        mod = f" product--{entry[4]}" if len(entry) > 4 else ""
        out.append(f'''      <a class="product{mod}" href="#objects">
        <span class="product__media">
          {pic(hover, "product", "", "product__img")}
          {pic(base, "product", f"{name} in recycled plastic", "product__img product__img--base")}
        </span>
        <span class="product__info">
          <span class="product__name">{name}</span>
          <span class="product__gram">
            <span class="product__gram-label">Recycled plastic</span>
            <span class="product__gram-value">{gram}</span>
          </span>
        </span>
      </a>''')
    return "\n".join(out)


def landscape_slides():
    out = []
    for i, (name, comp, img) in enumerate(LANDSCAPES):
        active = " data-active" if i == 0 else ""
        eager = i == 0
        p = pic(img, "landscape", "", "landscapes__slide", eager=eager,
                extra=f' data-landscape-slide data-name="{name}" data-composition="{comp}"{active}')
        out.append("          " + p)
    return "\n".join(out)


HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>WeMelt — Design Lab</title>
<meta name="description" content="WeMelt is a Barcelona design lab elevating plastics beyond waste: objects for everyday rituals, material landscapes and custom editions in recycled plastic.">

<!-- Open Graph. og:image and og:url MUST be absolute — most scrapers reject
     relative paths. SITE_ORIGIN below is the only thing to change if this
     deploys anywhere other than the production domain. -->
<meta property="og:type" content="website">
<meta property="og:site_name" content="WeMelt">
<meta property="og:url" content="https://wemelt.studio/">
<meta property="og:title" content="WeMelt — Design Lab">
<meta property="og:description" content="The design lab specialized in elevating plastics beyond waste. Made in Barcelona.">
<meta property="og:image" content="https://wemelt.studio/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="WeMelt — elevating plastics beyond waste.">
<meta name="twitter:card" content="summary_large_image">

<!-- Favicons — the W from the approved Lettermark: scripts/make-favicons.swift
     ICON_V busts the browser favicon cache, which is a separate store from the
     HTTP cache and survives hard reloads. Bump it whenever the icons change or
     the old icon will keep appearing. -->
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png?v={ICON_V}">
<link rel="icon" type="image/png" sizes="16x16" href="icons/favicon-16.png?v={ICON_V}">
<link rel="icon" type="image/png" sizes="48x48" href="icons/favicon-48.png?v={ICON_V}">
<link rel="icon" href="favicon.ico?v={ICON_V}" sizes="any">
<link rel="apple-touch-icon" sizes="180x180" href="icons/apple-touch-icon.png?v={ICON_V}">
<link rel="manifest" href="site.webmanifest?v={ICON_V}">
<meta name="theme-color" content="#16336F">

<link rel="preload" href="fonts/ClashGrotesk-Light.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/ClashGrotesk-Medium.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/PlantinMTPro-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/SourceCodePro-Regular.woff2" as="font" type="font/woff2" crossorigin>

<link rel="stylesheet" href="css/tokens.css">
<link rel="stylesheet" href="css/base.css">
<link rel="stylesheet" href="css/components/header.css">
<link rel="stylesheet" href="css/components/hero.css">
<link rel="stylesheet" href="css/components/about.css">
<link rel="stylesheet" href="css/components/territories.css">
<link rel="stylesheet" href="css/components/objects.css">
<link rel="stylesheet" href="css/components/split-panel.css">
<link rel="stylesheet" href="css/components/landscapes.css">
<link rel="stylesheet" href="css/components/gram.css">
<link rel="stylesheet" href="css/components/footer.css">

<script type="module" src="js/main.js"></script>
</head>
<body>

<a class="skip-link" href="#main">Skip to content</a>

<!-- ===================================================================== -->
<!-- HEADER                                                                -->
<!-- ===================================================================== -->
<header class="header">
  <a class="header__wordmark mark mark--wordmark" href="#top" aria-label="WeMelt — home"></a>
  <nav class="header__nav" aria-label="Primary">
    <a class="header__link" href="#objects">Objects</a>
    <a class="header__link" href="#landscapes-section">Landscapes</a>
    <a class="header__link" href="#projects">Projects</a>
    <a class="header__link" href="#guardians">Community</a>
    <a class="header__brandmark mark mark--brandmark" href="#about" aria-label="About WeMelt"></a>
  </nav>
</header>

<main id="main">

  <!-- =================================================================== -->
  <!-- HERO                                                                -->
  <!-- =================================================================== -->
  <section class="hero" id="top">
    <div class="hero__panel">
      <div class="hero__meta">
        <span>WeMelt — Design Lab</span>
        <span>Barcelona / Recycled plastic</span>
      </div>
      <div class="hero__body">
        <h1 class="hero__claim">The design lab specialized in <span class="hero__claim-accent">elevating plastics beyond&nbsp;waste.</span></h1>
        <p class="hero__lede">Objects for everyday rituals, material landscapes and custom editions. <br>Made in Barcelona.</p>
        <div class="hero__actions">
          <a class="btn btn--on-navy" href="#objects">Explore objects</a>
        </div>
      </div>
    </div>
    <div class="hero__media media">
      {pic("hero-main-opt", "hero", "Sunglasses with dark round lenses resting on a mound of discarded blue face masks", "media__img", eager=True)}
      {pic("hero-hover-opt", "hero", "", "media__img media__img--hover")}
    </div>
  </section>

  <!-- =================================================================== -->
  <!-- ABOUT / PROCESS                                                     -->
  <!-- =================================================================== -->
  <section class="about" id="about">
    <h2 class="visually-hidden">About WeMelt</h2>
    <span class="about__watermark mark mark--lettermark" aria-hidden="true"></span>
    <div class="about__aside">
      <span class="eyebrow">About</span>
      <span class="about__kicker">A circular design lab, <br>not a recycler</span>
      <span class="about__brandmark mark mark--brandmark" aria-hidden="true"></span>
    </div>
    <div class="about__main">
      <p class="about__statement">We transform locally recovered plastic into high-quality design objects.</p>
      <div class="about__detail">
        <p class="about__copy">Waste is sorted, washed, shredded, and pressed in our lab. The material is shaped through temperature, pressure, and color composition to create new design applications.</p>
        <span class="about__process">Sort<span class="about__process-arrow" aria-hidden="true"> &rarr; </span>Wash<span class="about__process-arrow" aria-hidden="true"> &rarr; </span>Shred<span class="about__process-arrow" aria-hidden="true"> &rarr; </span>Press<span class="about__process-arrow" aria-hidden="true"> &rarr; </span>Shape</span>
        <div class="about__spec">
          <span>Materials / HDPE 02 · PP 05</span>
          <span>Source / Post-consumer goods</span>
        </div>
      </div>
    </div>
  </section>

  <!-- =================================================================== -->
  <!-- FOUR TERRITORIES                                                    -->
  <!-- =================================================================== -->
  <section class="territories" id="landscapes">
    <div class="territories__bar">
      <h2 class="label">Four territories</h2>
      <span class="eyebrow">Objects · Landscapes · Projects · Community</span>
    </div>
    <div class="territories__grid">
{territory_cards()}
    </div>
  </section>

  <!-- =================================================================== -->
  <!-- SELECTED OBJECTS                                                    -->
  <!-- =================================================================== -->
  <section class="objects" id="objects">
    <div class="objects__bar">
      <h2 class="label"><span class="eyebrow__marker" aria-hidden="true"></span>01 / Selected objects</h2>
    </div>
    <div class="objects__band">
      {pic("objects-band", "editorial", "Four recycled-plastic trays marbled in blue and orange, holding sunglasses, keys and earrings on a dark grey surface", "objects__band-img", sizes_key="band")}
      <div class="objects__band-overlay">
        <p class="objects__band-copy">Home goods designed around everyday rituals. From the table to the desk and bathroom, each collection explores new ways of living with recycled plastic.</p>
      </div>
    </div>
    <div class="objects__grid">
{product_cards()}
    </div>
  </section>

  <!-- =================================================================== -->
  <!-- MATERIAL LANDSCAPES                                                 -->
  <!-- =================================================================== -->
  <section class="split split--text-first" id="landscapes-section">
    <div class="split__text">
      <span class="eyebrow"><span class="eyebrow__marker" aria-hidden="true"></span>02 / Material landscapes</span>
      <h2 class="section-title split__title">material <br>landscapes</h2>
      <p class="copy">A material library where colour, texture and process become landscapes — translating nature into our creative material language.</p>
      <div class="split__actions">
        <span class="landscapes__explore">Explore landscapes</span>
        <div class="landscapes__nav">
          <button class="landscapes__step" type="button" data-landscape-prev aria-label="Previous landscape">&larr;</button>
          <button class="landscapes__step" type="button" data-landscape-next aria-label="Next landscape">&rarr;</button>
        </div>
      </div>
      <p class="visually-hidden" role="status" aria-live="polite" data-landscape-live></p>
    </div>
    <div class="split__media landscapes__stage" data-landscape-stage>
{landscape_slides()}
      <div class="landscapes__overlay">
        <div class="landscapes__name-wrap">
          <span class="landscapes__name" data-landscape-name>Frosted Lava</span>
        </div>
        <div class="landscapes__meta" data-landscape-meta hidden>
          <span data-landscape-comp></span>
          <span>Recycled HDPE</span>
        </div>
      </div>
    </div>
  </section>

  <!-- =================================================================== -->
  <!-- CUSTOM EDITIONS                                                     -->
  <!-- =================================================================== -->
  <section class="split split--media-first" id="projects">
    <div class="split__media media">
      {pic("custom-edition-v3", "editorial", "Flower-shaped recycled-plastic coasters mottled in blue, red and white, each embossed with a brand name", "media__img")}
      {pic("custom-editions-hover", "editorial", "", "media__img media__img--hover")}
    </div>
    <div class="split__text">
      <span class="eyebrow"><span class="eyebrow__marker" aria-hidden="true"></span>03 / Projects</span>
      <h2 class="section-title split__title">custom <br>editions</h2>
      <p class="copy">For brands, events and spaces looking to explore new materials through design. <br>We develop custom objects and editions in recycled plastic, creating pieces with their own material identity.</p>
      <div class="split__cta-group">
        <span class="split__cta-lead">Have something in mind?</span>
        <a class="btn btn--lg" href="mailto:wemelt.studio@gmail.com?subject=Custom%20Edition%20enquiry">Let’s talk about it <span aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
  </section>

  <!-- =================================================================== -->
  <!-- PLASTIC GUARDIANS                                                   -->
  <!-- =================================================================== -->
  <section class="split split--text-first" id="guardians">
    <div class="split__text split__text--navy">
      <span class="eyebrow eyebrow--on-dark"><span class="eyebrow__marker" aria-hidden="true"></span>04 / Community</span>
      <h2 class="section-title split__title">Plastic Guardians</h2>
      <p class="copy copy--on-dark">Workshops and community actions that bring people closer to recycled plastic through design, material experimentation and hands-on making.</p>
      <div class="split__actions">
        <a class="arrow-link" href="mailto:wemelt.studio@gmail.com?subject=Workshop%20enquiry">Book a workshop <span aria-hidden="true">&rarr;</span></a>
      </div>
    </div>
    <div class="split__media media">
      {pic("plastic-guardians-v2", "editorial", "Two people passing a glass jar of blue and white shredded plastic flakes between them", "media__img")}
      {pic("plastic-guardians-hover", "editorial", "", "media__img media__img--hover")}
    </div>
  </section>

  <!-- =================================================================== -->
  <!-- GRAM SYSTEM                                                         -->
  <!-- =================================================================== -->
  <section class="gram" id="gram-system">
    <h2 class="visually-hidden">Gram system</h2>
    <div class="gram__grid">
      <div class="gram__seal">
        <span class="gram__mark mark mark--brandmark" aria-hidden="true"></span>
        <span class="gram__value">490.839g</span>
        <span class="gram__caption">Plastic protected to date.</span>
      </div>
      <dl class="gram__stats">
        <div class="gram__stat"><dt>Objects produced</dt><dd>43</dd></div>
        <div class="gram__stat"><dt>Collection points</dt><dd>02</dd></div>
        <div class="gram__stat"><dt>Community actions</dt><dd>03</dd></div>
      </dl>
    </div>
  </section>

  <!-- =================================================================== -->
  <!-- BRAND CLOSING                                                       -->
  <!-- =================================================================== -->
  <section class="community" id="community">
    <p class="community__statement">Protect plastic. Create landscapes.</p>
  </section>

</main>

<!-- ===================================================================== -->
<!-- FOOTER                                                                -->
<!-- ===================================================================== -->
<footer class="footer">
  <div class="footer__grid">
    <div class="footer__col">
      <a class="footer__wordmark mark mark--wordmark" href="#top" aria-label="WeMelt — back to top"></a>
      <span class="footer__place">Design Lab / Barcelona</span>
    </div>
    <div class="footer__col">
      <span class="footer__heading">Info</span>
      <a href="#about">About</a>
      <a href="#projects">Projects</a>
      <a href="#guardians">Community</a>
    </div>
    <div class="footer__col">
      <span class="footer__heading">Contact</span>
      <a href="mailto:wemelt.studio@gmail.com">wemelt.studio@gmail.com</a>
    </div>
    <div class="footer__col">
      <span class="footer__heading">Follow</span>
      <a href="https://www.instagram.com/wemelt.lab/" target="_blank" rel="noopener">Instagram</a>
    </div>
  </div>
  <div class="footer__legal">
    <span>© WeMelt Studio 2026</span>
    <!-- Privacy / Terms intentionally absent until the legal pages exist.
         Re-add here as real links (not "#") when they do. -->
  </div>
</footer>

</body>
</html>
'''

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"wrote {OUT} ({len(HTML)/1024:.1f} KB)")
