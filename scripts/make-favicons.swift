// Generate the WeMelt favicon set from approved identity artwork.
//
// The source PNG is approved artwork as black-on-transparent (the same files the
// site uses as CSS masks). Nothing is redrawn: the artwork's own alpha channel is
// recoloured and scaled. Proportions are always preserved — the mark is fitted to
// the square canvas by its longer edge and centred.
//
//   swift scripts/make-favicons.swift <source.png> <out-dir> <#RRGGBB> <bg|none> [margin] [root-ico]
//
//   margin:   fraction of the canvas kept clear on the constraining axis (default 0.04)
//   root-ico: optional second path for favicon.ico. Browsers request /favicon.ico at
//             the origin root on their own, regardless of <link> tags, so the site
//             root needs a copy or that request 404s and the browser falls back to
//             whatever it cached for the origin.

import Foundation
import CoreGraphics
import ImageIO
import UniformTypeIdentifiers

let args = CommandLine.arguments
guard args.count >= 5 else {
    print("usage: make-favicons <source.png> <out-dir> <#RRGGBB> <bg-hex|none> [margin]")
    exit(1)
}
let srcURL = URL(fileURLWithPath: args[1])
let outDir = URL(fileURLWithPath: args[2])
let margin = args.count > 5 ? (Double(args[5]) ?? 0.04) : 0.04

func colour(_ hex: String) -> CGColor? {
    if hex.lowercased() == "none" { return nil }
    var h = hex.hasPrefix("#") ? String(hex.dropFirst()) : hex
    guard h.count == 6, let v = UInt32(h, radix: 16) else { return nil }
    return CGColor(red: Double((v >> 16) & 0xff)/255, green: Double((v >> 8) & 0xff)/255,
                   blue: Double(v & 0xff)/255, alpha: 1)
}
guard let ink = colour(args[3]) else { print("bad ink colour"); exit(1) }
let bg = colour(args[4])   // nil == transparent

guard let s = CGImageSourceCreateWithURL(srcURL as CFURL, nil),
      let mark = CGImageSourceCreateImageAtIndex(s, 0, nil) else {
    print("could not read \(srcURL.path)"); exit(1)
}
let aspect = Double(mark.width) / Double(mark.height)

func render(size: Int) -> CGImage? {
    let cs = CGColorSpaceCreateDeviceRGB()
    let bmp = CGImageAlphaInfo.premultipliedLast.rawValue
    let S = Double(size)

    // fit by the longer edge, preserving proportions, leaving `margin` clear
    let avail = S * (1 - margin * 2)
    var dw = avail, dh = avail / aspect
    if dh > avail { dh = avail; dw = avail * aspect }
    let box = CGRect(x: (S - dw)/2, y: (S - dh)/2, width: dw, height: dh)

    // pass 1 — recolour the artwork's alpha
    guard let a = CGContext(data: nil, width: size, height: size, bitsPerComponent: 8,
                            bytesPerRow: 0, space: cs, bitmapInfo: bmp) else { return nil }
    a.interpolationQuality = .high
    a.draw(mark, in: box)
    a.setBlendMode(.sourceIn)
    a.setFillColor(ink)
    a.fill(CGRect(x: 0, y: 0, width: S, height: S))
    guard let coloured = a.makeImage() else { return nil }

    guard let bg = bg else { return coloured }   // transparent

    guard let b = CGContext(data: nil, width: size, height: size, bitsPerComponent: 8,
                            bytesPerRow: 0, space: cs, bitmapInfo: bmp) else { return nil }
    b.interpolationQuality = .high
    b.setFillColor(bg)
    b.fill(CGRect(x: 0, y: 0, width: S, height: S))
    b.draw(coloured, in: CGRect(x: 0, y: 0, width: S, height: S))
    return b.makeImage()
}

func write(_ img: CGImage, _ name: String) {
    let url = outDir.appendingPathComponent(name)
    guard let d = CGImageDestinationCreateWithURL(url as CFURL, UTType.png.identifier as CFString, 1, nil)
    else { print("  FAIL \(name)"); return }
    CGImageDestinationAddImage(d, img, nil)
    if CGImageDestinationFinalize(d) {
        let n = (try? FileManager.default.attributesOfItem(atPath: url.path)[.size]) as? Int ?? 0
        print("  \(name.padding(toLength: 26, withPad: " ", startingAt: 0)) \(img.width)x\(img.height)  \(n/1024) KB")
    }
}

print("favicons from \(srcURL.lastPathComponent)  aspect \(String(format: "%.3f", aspect)):1  margin \(Int(margin*100))%")
for (size, name) in [(16, "favicon-16.png"), (32, "favicon-32.png"), (48, "favicon-48.png"),
                     (180, "apple-touch-icon.png"), (192, "icon-192.png"), (512, "icon-512.png")] {
    if let i = render(size: size) { write(i, name) }
}

var icoTargets = [outDir.appendingPathComponent("favicon.ico")]
if args.count > 6 { icoTargets.append(URL(fileURLWithPath: args[6])) }
for ico in icoTargets {
    guard let d = CGImageDestinationCreateWithURL(ico as CFURL, "com.microsoft.ico" as CFString, 3, nil)
    else { continue }
    for size in [16, 32, 48] { if let i = render(size: size) { CGImageDestinationAddImage(d, i, nil) } }
    if CGImageDestinationFinalize(d) {
        let n = (try? FileManager.default.attributesOfItem(atPath: ico.path)[.size]) as? Int ?? 0
        print("  \(ico.path.replacingOccurrences(of: FileManager.default.currentDirectoryPath + "/", with: "").padding(toLength: 40, withPad: " ", startingAt: 0)) 16/32/48  \(n/1024) KB")
    }
}
