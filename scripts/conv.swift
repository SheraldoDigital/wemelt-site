import Foundation
import ImageIO
import CoreGraphics
import UniformTypeIdentifiers

// conv <in> <out> <maxEdge> <quality 0-1> <uti>
let a = CommandLine.arguments
guard a.count >= 6, let src = CGImageSourceCreateWithURL(URL(fileURLWithPath: a[1]) as CFURL, nil) else { exit(1) }
let maxEdge = Int(a[3])!, q = Double(a[4])!, uti = a[5]
let opts: [CFString: Any] = [
    kCGImageSourceCreateThumbnailFromImageAlways: true,
    kCGImageSourceCreateThumbnailWithTransform: true,
    kCGImageSourceThumbnailMaxPixelSize: maxEdge
]
guard let img = CGImageSourceCreateThumbnailAtIndex(src, 0, opts as CFDictionary) else { exit(1) }
let out = URL(fileURLWithPath: a[2])
guard let dest = CGImageDestinationCreateWithURL(out as CFURL, uti as CFString, 1, nil) else { exit(1) }
CGImageDestinationAddImage(dest, img, [kCGImageDestinationLossyCompressionQuality: q] as CFDictionary)
if !CGImageDestinationFinalize(dest) { exit(1) }
print("\(img.width)x\(img.height)")
