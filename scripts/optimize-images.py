#!/usr/bin/env python3
"""
Optimise the Landing Page media set into responsive AVIF + JPEG.

macOS has no WebP encoder available to ImageIO, but it does encode AVIF, which
compresses better anyway. Every photographic asset becomes:
    <name>-<width>.avif   (primary)
    <name>-<width>.jpg    (fallback for older Safari/Edge)

Logos stay PNG — they are used as CSS mask-image sources and need clean alpha.

Usage:  python3 scripts/optimize-images.py <src-root> <out-root>
Requires scripts/conv.swift alongside this file.
"""
import os, subprocess, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
CONV = os.path.join(HERE, "conv.swift")

# width sets chosen from how large each image is actually painted in the layout
ROLE_WIDTHS = {
    "hero":       [900, 1500, 2100],
    "landscape":  [900, 1500, 2100],
    "editorial":  [900, 1500, 2100],   # custom editions, guardians, objects band
    "territory":  [640, 1040, 1440],
    "product":    [440, 760, 1120],
}

ROLES = {
    "hero": ["hero-main-opt.jpg", "hero-hover-opt.jpg"],
    "landscape": ["material-landscapes.png", "ls-01.png", "ls-02.jpg", "ls-03.jpg",
                  "ls-04.jpg", "ls-07.jpg", "ls-08.png", "ls-09.png", "ls-10.png"],
    "editorial": ["custom-edition-v3.png", "custom-editions-hover.png",
                  "plastic-guardians-v2.jpg", "plastic-guardians-hover.png",
                  "objects-band.jpg"],
    "territory": ["territory-objects.jpg", "territory-landscapes.jpg",
                  "territory-projects.jpg", "territory-community.jpg"],
    "product": ["product-coaster-set.jpg", "product-coaster-set-hover.jpg",
                "product-tray-02.jpg", "product-tray-02-hover.jpg",
                "product-post-it.jpg", "product-post-it-hover.jpg",
                "product-incense.jpg", "product-incense-hover-v2.jpg",
                "product-05.jpg", "product-05-hover.jpg",
                "product-06.jpg", "product-06-hover.jpg",
                "product-07-v2.png", "product-07-hover.jpg",
                "product-08.jpg", "product-08-hover.jpg"],
}

# masks: keep PNG + alpha, just cut the absurd source resolutions down
LOGOS = {
    "wemelt-wordmark-black.png": 400,
    "wemelt-brandmark-black.png": 512,
    "wemelt-lettermark-black.png": 2000,
}

AVIF_Q, JPEG_Q = "0.55", "0.74"


def run(src, dst, width, quality, uti):
    r = subprocess.run(["swift", CONV, src, dst, str(width), quality, uti],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    src_root, out_root = sys.argv[1], sys.argv[2]
    img_out = os.path.join(out_root, "img")
    logo_out = os.path.join(out_root, "logos")
    os.makedirs(img_out, exist_ok=True)
    os.makedirs(logo_out, exist_ok=True)

    before = after = 0
    manifest = {}

    for role, files in ROLES.items():
        for fn in files:
            src = os.path.join(src_root, "assets/imagery", fn)
            if not os.path.exists(src):
                print(f"  MISSING {fn}", flush=True)
                continue
            before += os.path.getsize(src)
            stem = os.path.splitext(fn)[0]
            made = []
            for w in ROLE_WIDTHS[role]:
                a = os.path.join(img_out, f"{stem}-{w}.avif")
                j = os.path.join(img_out, f"{stem}-{w}.jpg")
                if run(src, a, w, AVIF_Q, "public.avif"):
                    after += os.path.getsize(a)
                if run(src, j, w, JPEG_Q, "public.jpeg"):
                    after += os.path.getsize(j)
                made.append(w)
            manifest[stem] = {"role": role, "widths": made}
            print(f"  {role:10} {fn}", flush=True)

    for fn, w in LOGOS.items():
        src = os.path.join(src_root, "assets/logos", fn)
        if not os.path.exists(src):
            print(f"  MISSING {fn}", flush=True)
            continue
        before += os.path.getsize(src)
        dst = os.path.join(logo_out, fn)
        if run(src, dst, w, "1.0", "public.png"):
            after += os.path.getsize(dst)
        print(f"  logo       {fn} -> {w}px", flush=True)

    with open(os.path.join(out_root, "img", "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=1)

    print(f"\nBEFORE {before/1024/1024:8.1f} MB")
    print(f"AFTER  {after/1024/1024:8.1f} MB  ({100*(1-after/before):.1f}% smaller)")


if __name__ == "__main__":
    main()
