import Foundation
import CoreGraphics
import ImageIO
let a=CommandLine.arguments
let src=URL(fileURLWithPath:a[1]); let dest=URL(fileURLWithPath:a[2])
try FileManager.default.createDirectory(at:dest,withIntermediateDirectories:true)
guard let pdf=CGPDFDocument(src as CFURL) else {fatalError("PDF open failed")}
for i in 1...pdf.numberOfPages {
 let p=pdf.page(at:i)!; let box=p.getBoxRect(.mediaBox);let scale:CGFloat=1.2
 let w=Int(box.width*scale),h=Int(box.height*scale)
 let c=CGContext(data:nil,width:w,height:h,bitsPerComponent:8,bytesPerRow:0,space:CGColorSpaceCreateDeviceRGB(),bitmapInfo:CGImageAlphaInfo.premultipliedLast.rawValue)!
 c.setFillColor(CGColor(gray:1,alpha:1));c.fill(CGRect(x:0,y:0,width:w,height:h));c.scaleBy(x:scale,y:scale);c.drawPDFPage(p)
 let target=dest.appendingPathComponent(String(format:"page-%02d.png",i))
 let out=CGImageDestinationCreateWithURL(target as CFURL,"public.png" as CFString,1,nil)!
 CGImageDestinationAddImage(out,c.makeImage()!,nil)
 guard CGImageDestinationFinalize(out) else{fatalError("Page write failed")}
}
print("PDF_RASTERIZED",pdf.numberOfPages,"pages")
