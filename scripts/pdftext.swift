import Foundation
import PDFKit

let args = CommandLine.arguments
guard args.count > 1 else { print("usage: pdftext <file.pdf>"); exit(1) }
guard let doc = PDFDocument(url: URL(fileURLWithPath: args[1])) else {
    print("ERROR: could not open \(args[1])"); exit(1)
}
for i in 0..<doc.pageCount {
    print("\n===== PAGE \(i+1) =====")
    print(doc.page(at: i)?.string ?? "(no text layer)")
}
