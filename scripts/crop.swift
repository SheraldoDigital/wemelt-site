// Crop a region out of a PNG, preserving pixels exactly. No resampling, no redraw.
import Foundation
import CoreGraphics
import ImageIO
import UniformTypeIdentifiers

let a = CommandLine.arguments
guard a.count >= 7,
      let s = CGImageSourceCreateWithURL(URL(fileURLWithPath: a[1]) as CFURL, nil),
      let img = CGImageSourceCreateImageAtIndex(s, 0, nil) else {
    print("usage: crop <in.png> <out.png> <x> <y> <w> <h>"); exit(1)
}
let x = Int(a[3])!, y = Int(a[4])!, w = Int(a[5])!, h = Int(a[6])!
guard let cut = img.cropping(to: CGRect(x: x, y: y, width: w, height: h)) else {
    print("crop failed"); exit(1)
}
guard let d = CGImageDestinationCreateWithURL(URL(fileURLWithPath: a[2]) as CFURL,
                                              UTType.png.identifier as CFString, 1, nil) else { exit(1) }
CGImageDestinationAddImage(d, cut, nil)
if CGImageDestinationFinalize(d) {
    print("wrote \(a[2])  \(cut.width)x\(cut.height)")
}
