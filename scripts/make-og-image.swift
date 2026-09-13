// Generate the WeMelt Open Graph image — 1200×630.
//
// Deliberately minimal, using only approved assets and brand values:
//   Deep Navy field · Light Grey Wordmark · the claim in Plantin MT Pro Roman
//   · a Source Code descriptor line, matching the hero's own meta treatment.
// No new visual direction: this is the hero's colour and type relationship,
// cropped to a share card.
//
//   swift scripts/make-og-image.swift <wordmark.png> <plantin.ttf-or-otf> <sourcecode> <out.png>

import Foundation
import CoreGraphics
import CoreText
import ImageIO
import UniformTypeIdentifiers

let args = CommandLine.arguments
guard args.count >= 5 else {
    print("usage: make-og-image <wordmark.png> <plantin> <sourcecode> <out.png>"); exit(1)
}

let W = 1200, H = 630

let navy      = CGColor(red: 0x16/255.0, green: 0x33/255.0, blue: 0x6F/255.0, alpha: 1)
let lightGrey = CGColor(red: 0xE9/255.0, green: 0xE9/255.0, blue: 0xE8/255.0, alpha: 1)
let coolGrey  = CGColor(red: 0xC2/255.0, green: 0xCD/255.0, blue: 0xD6/255.0, alpha: 1)

func loadFont(_ path: String, _ size: CGFloat) -> CTFont? {
    guard let ds = CTFontManagerCreateFontDescriptorsFromURL(URL(fileURLWithPath: path) as CFURL) as? [CTFontDescriptor],
          let d = ds.first else { return nil }
    return CTFontCreateWithFontDescriptor(d, size, nil)
}

guard let wmSrc = CGImageSourceCreateWithURL(URL(fileURLWithPath: args[1]) as CFURL, nil),
      let wordmark = CGImageSourceCreateImageAtIndex(wmSrc, 0, nil) else {
    print("could not read wordmark"); exit(1)
}
guard let plantin = loadFont(args[2], 76), let mono = loadFont(args[3], 21) else {
    print("could not load fonts"); exit(1)
}

let cs = CGColorSpaceCreateDeviceRGB()
guard let ctx = CGContext(data: nil, width: W, height: H, bitsPerComponent: 8,
                          bytesPerRow: 0, space: cs,
                          bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) else { exit(1) }
ctx.interpolationQuality = .high

// field
ctx.setFillColor(navy)
ctx.fill(CGRect(x: 0, y: 0, width: W, height: H))

let padX: CGFloat = 84

// wordmark, recoloured Light Grey from its own alpha
let wmW: CGFloat = 300
let wmH = wmW * CGFloat(wordmark.height) / CGFloat(wordmark.width)
if let a = CGContext(data: nil, width: Int(wmW), height: Int(wmH), bitsPerComponent: 8,
                     bytesPerRow: 0, space: cs, bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) {
    a.interpolationQuality = .high
    a.draw(wordmark, in: CGRect(x: 0, y: 0, width: wmW, height: wmH))
    a.setBlendMode(.sourceIn)
    a.setFillColor(lightGrey)
    a.fill(CGRect(x: 0, y: 0, width: wmW, height: wmH))
    if let tinted = a.makeImage() {
        ctx.draw(tinted, in: CGRect(x: padX, y: CGFloat(H) - 74 - wmH, width: wmW, height: wmH))
    }
}

/// Draw one line of text, return its height.
func draw(_ text: String, font: CTFont, color: CGColor, x: CGFloat, y: CGFloat,
          tracking: CGFloat = 0) {
    var attrs: [CFString: Any] = [
        kCTFontAttributeName: font, kCTForegroundColorAttributeName: color
    ]
    if tracking != 0 { attrs[kCTKernAttributeName] = tracking }
    let s = CFAttributedStringCreate(nil, text as CFString, attrs as CFDictionary)!
    let line = CTLineCreateWithAttributedString(s)
    ctx.textPosition = CGPoint(x: x, y: y)
    CTLineDraw(line, ctx)
}

// NOTE: CoreGraphics origin is bottom-left, so larger y is higher up the card.
// Layout, top to bottom: wordmark · claim · hairline · descriptor.

// the claim, in Plantin — two lines, echoing the hero's own line break
draw("Elevating plastics", font: plantin, color: coolGrey, x: padX, y: 322)
draw("beyond waste.",      font: plantin, color: coolGrey, x: padX, y: 322 - 88)

// hairline rule — the same structural line the site uses between modules
ctx.setStrokeColor(coolGrey.copy(alpha: 0.32)!)
ctx.setLineWidth(1)
ctx.move(to: CGPoint(x: padX, y: 152))
ctx.addLine(to: CGPoint(x: CGFloat(W) - padX, y: 152))
ctx.strokePath()

// descriptor line, Source Code — the hero's meta treatment, beneath the rule
draw("WEMELT — DESIGN LAB", font: mono, color: coolGrey, x: padX, y: 104, tracking: 2.4)

guard let img = ctx.makeImage() else { exit(1) }
let out = URL(fileURLWithPath: args[4])
guard let dest = CGImageDestinationCreateWithURL(out as CFURL, UTType.png.identifier as CFString, 1, nil) else { exit(1) }
CGImageDestinationAddImage(dest, img, nil)
if CGImageDestinationFinalize(dest) {
    let bytes = (try? FileManager.default.attributesOfItem(atPath: out.path)[.size] as? Int) ?? 0
    print("wrote \(out.lastPathComponent)  \(img.width)×\(img.height)  \(String(format: "%.1f", Double(bytes ?? 0)/1024)) KB")
}
