// Per-frame face boxes for Dan's original (Apple Vision). usage: swift faces.swift in.mp4 > faces.csv
import AVFoundation
import Vision
let url = URL(fileURLWithPath: CommandLine.arguments[1])
let asset = AVAsset(url: url)
let track = asset.tracks(withMediaType: .video)[0]
let reader = try! AVAssetReader(asset: asset)
let out = AVAssetReaderTrackOutput(track: track, outputSettings: [kCVPixelBufferPixelFormatTypeKey as String: kCVPixelFormatType_32BGRA])
reader.add(out); reader.startReading()
print("t,x,y,w,h,n")
while let sb = out.copyNextSampleBuffer() {
  guard let pb = CMSampleBufferGetImageBuffer(sb) else { continue }
  let t = CMSampleBufferGetPresentationTimeStamp(sb).seconds
  let req = VNDetectFaceRectanglesRequest()
  try? VNImageRequestHandler(cvPixelBuffer: pb, options: [:]).perform([req])
  let fs = (req.results ?? []).sorted { $0.boundingBox.width > $1.boundingBox.width }
  if let f = fs.first { let b = f.boundingBox
    print(String(format: "%.3f,%.4f,%.4f,%.4f,%.4f,%d", t, b.midX, 1 - b.midY, b.width, b.height, fs.count))
  } else { print(String(format: "%.3f,,,,,0", t)) }
}
