import Foundation
import CoreGraphics
import CoreText
import ImageIO
let args=CommandLine.arguments
let root=URL(fileURLWithPath:args[1]);let out=URL(fileURLWithPath:args[2])
let data=try Data(contentsOf:root.appendingPathComponent("docs/pdf-layout.json"))
let pages=try JSONSerialization.jsonObject(with:data) as! [[String:Any]]
for file in ["Jost.ttf","IBMPlexMono.ttf"] {CTFontManagerRegisterFontsForURL(root.appendingPathComponent("book/vendor/"+file) as CFURL,.process,nil)}
let width:CGFloat=1008,height:CGFloat=720,margin:CGFloat=36,content:CGFloat=936
let bone=CGColor(red:0.953,green:0.945,blue:0.925,alpha:1),gold=CGColor(red:0.804,green:0.725,blue:0.416,alpha:1),muted=CGColor(red:0.66,green:0.70,blue:0.66,alpha:1),black=CGColor(red:0.04,green:0.05,blue:0.04,alpha:1),line=CGColor(red:0.23,green:0.27,blue:0.24,alpha:1)
var media=CGRect(x:0,y:0,width:width,height:height)
let info=[kCGPDFContextTitle as String:"Andrew Rose / Alita 22NFT / Sunset Noir",kCGPDFContextAuthor as String:"Andrew Rose",kCGPDFContextCreator as String:"Native CoreText / source-grounded scripted 3D build study"] as CFDictionary
let consumer=CGDataConsumer(url:out as CFURL)!
let ctx=CGContext(consumer:consumer,mediaBox:&media,info)!
var clipped=0
func attr(_ text:String,_ size:CGFloat,_ color:CGColor=bone,_ mono:Bool=false)->NSAttributedString {
 let font=CTFontCreateWithName((mono ? "IBMPlexMono-Regular":"Jost-Regular") as CFString,size,nil)
 return NSAttributedString(string:text,attributes:[NSAttributedString.Key(kCTFontAttributeName as String):font,NSAttributedString.Key(kCTForegroundColorAttributeName as String):color])
}
func measure(_ text:String,_ w:CGFloat,_ size:CGFloat,_ mono:Bool=false)->CGFloat {
 let fs=CTFramesetterCreateWithAttributedString(attr(text,size,bone,mono) as CFAttributedString)
 return ceil(CTFramesetterSuggestFrameSizeWithConstraints(fs,CFRange(location:0,length:0),nil,CGSize(width:w,height:10000),nil).height)+3
}
@discardableResult func draw(_ text:String,_ x:CGFloat,_ top:CGFloat,_ w:CGFloat,_ h:CGFloat,_ size:CGFloat,_ color:CGColor=bone,_ mono:Bool=false)->CGFloat {
 let a=attr(text,size,color,mono);let fs=CTFramesetterCreateWithAttributedString(a as CFAttributedString);let path=CGPath(rect:CGRect(x:x,y:height-top-h,width:w,height:h),transform:nil)
 let frame=CTFramesetterCreateFrame(fs,CFRange(location:0,length:0),path,nil);ctx.textMatrix = .identity;CTFrameDraw(frame,ctx)
 if CTFrameGetVisibleStringRange(frame).length<a.length {clipped+=1;print("TEXT_CLIP",text.prefix(50),"size",size,"height",h)}
 return measure(text,w,size,mono)
}
func stroke(_ x1:CGFloat,_ y1:CGFloat,_ x2:CGFloat,_ y2:CGFloat,_ color:CGColor=line){ctx.setStrokeColor(color);ctx.setLineWidth(0.5);ctx.move(to:CGPoint(x:x1,y:height-y1));ctx.addLine(to:CGPoint(x:x2,y:height-y2));ctx.strokePath()}
func image(_ file:String,_ x:CGFloat,_ top:CGFloat,_ w:CGFloat,_ h:CGFloat){
 guard let provider=CGDataProvider(url:URL(fileURLWithPath:file) as CFURL),let im=CGImage(jpegDataProviderSource:provider,decode:nil,shouldInterpolate:true,intent:.defaultIntent) else{print("MISSING_IMAGE",file);return}
 let ratio=min(w/CGFloat(im.width),h/CGFloat(im.height));let iw=CGFloat(im.width)*ratio,ih=CGFloat(im.height)*ratio
 ctx.draw(im,in:CGRect(x:x+(w-iw)/2,y:height-top-h+(h-ih)/2,width:iw,height:ih))
}
func blockHeight(_ blocks:[[String:Any]],_ w:CGFloat,_ size:CGFloat)->CGFloat{blocks.reduce(0){r,b in let k=b["kind"] as? String ?? "body";return r+measure(b["text"] as! String,w,k=="heading" ? size+7:size)+10}}
func drawBlocks(_ blocks:[[String:Any]],_ x:CGFloat,_ top:CGFloat,_ w:CGFloat,_ available:CGFloat,_ initial:CGFloat=13){
 var size=initial;while blockHeight(blocks,w,size)>available && size>8.5 {size-=0.5}
 var y=top
 for b in blocks {let k=b["kind"] as? String ?? "body",t=b["text"] as! String;let fs=k=="heading" ? size+7:size;let h=measure(t,w,fs)
  if k=="note" {ctx.setFillColor(CGColor(red:0.09,green:0.12,blue:0.09,alpha:1));ctx.fill(CGRect(x:x-6,y:height-y-h-8,width:w+12,height:h+12));stroke(x-6,y-4,x-6,y+h+8,gold)}
  draw(t,x,y,w,h+2,fs,k=="heading" ? gold:bone);y+=h+10
 }
}
for page in pages {
 ctx.beginPDFPage(nil);ctx.setFillColor(black);ctx.fill(media)
 let num=page["number"] as! Int,title=page["title"] as! String,type=page["type"] as! String
 draw((page["kicker"] as! String).uppercased(),margin,24,content,18,8,gold,true)
 if type=="cover" {
  draw("ALITA 22NFT\nSunset Noir.",margin,82,355,170,54,bone)
  draw(page["lede"] as! String,margin,293,355,145,17,bone)
  image(page["image"] as! String,421,105,551,345)
  let metrics=[("1,650 W","SIX PARALLEL / ROOF"),("10.24 kWh","TWO B4810 / NOMINAL"),("18K BTU","DUCTED HEAT PUMP"),("A / B","LAUNDRY LOCATION OPEN")]
  for (i,m) in metrics.enumerated(){let x=margin+CGFloat(i)*240;stroke(x,492,x+215,492,gold);draw(m.0,x,506,215,52,34);draw(m.1,x,563,215,34,8,gold,true)}
  draw("A researched design visualization. Published component envelopes; estimated coach geometry, placement, routes and clearances. Verify the production unit before purchasing or installing.",margin,625,content,45,12,muted)
 } else {
  draw(title,margin,49,content,47,29,bone)
  if type=="image" {
   image(page["image"] as! String,margin,99,content,527)
   draw(page["caption"] as! String,margin,641,content,45,10.5,bone)
  } else if type=="columns" {
   var top:CGFloat=111
   if let summary=page["summary"] as? String,!summary.isEmpty{draw(summary,margin,top,content,42,12,gold);top+=54}
   let cols=page["columns"] as! [[[String:Any]]];let gap:CGFloat=30;let cw=(content-gap)/2
   for (i,col) in cols.enumerated(){drawBlocks(col,margin+CGFloat(i)*(cw+gap),top,cw,675-top,13)}
  } else if type=="table" {
   let rows=page["rows"] as! [[[String:Any]]];let n=rows[0].count
   var widths:[CGFloat]
   if n==3{widths=[190,353,393]}else if n==4{widths=[152,266,88,430]}else if n==5{widths=title.contains("Gross") ? [228,90,100,100,418]:[280,126,180,175,175]}else{widths=Array(repeating:content/CGFloat(n),count:n)}
   let after=page["blocks"] as! [[String:Any]];var size:CGFloat=11
   func rowWidths(_ row:[[String:Any]])->[CGFloat]{var index=0;return row.map{cell in let span=cell["span"] as? Int ?? 1;let end=min(widths.count,index+span);let w=widths[index..<end].reduce(0,+);index=end;return w}}
   func rowH(_ row:[[String:Any]],_ idx:Int)->CGFloat{let rw=rowWidths(row);return row.enumerated().map{measure($0.element["text"] as! String,rw[$0.offset]-16,idx==0 ? 8.5:size,idx==0)+16}.max() ?? 28}
   while rows.enumerated().reduce(0,{$0+rowH($1.element,$1.offset)})+blockHeight(after,content,12)>556 && size>8 {size-=0.5}
   var y:CGFloat=108
   for (ri,row) in rows.enumerated(){let h=rowH(row,ri);if ri>0 && ri%2==0{ctx.setFillColor(CGColor(red:0.07,green:0.095,blue:0.073,alpha:1));ctx.fill(CGRect(x:margin,y:height-y-h,width:content,height:h))};var x=margin
    let rw=rowWidths(row)
    for (ci,cell) in row.enumerated(){let text=cell["text"] as! String;draw(ri==0 ? text.uppercased():text,x+8,y+8,rw[ci]-16,h-14,ri==0 ? 8.5:size,ri==0 ? gold:bone,ri==0)
     if let u=cell["url"] as? String,let url=URL(string:u){ctx.setURL(url as CFURL,for:CGRect(x:x+8,y:height-y-26,width:rw[ci]-16,height:20))}
     x+=rw[ci]
    }
    stroke(margin,y+h,margin+content,y+h);y+=h
   }
   drawBlocks(after,margin,y+16,content,675-y-16,12)
  } else {drawBlocks(page["blocks"] as! [[String:Any]],margin,111,content,562,14)}
 }
 stroke(margin,697,margin+content,697)
 draw(String(format:"ANDREW ROSE  /  ALITA 22NFT  /  07 OCT 2026                                                  %02d",num),margin,705,content,12,7,muted,true)
 ctx.endPDFPage()
}
ctx.closePDF();print("PDF_COMPLETE",pages.count,"pages","clipped",clipped)
