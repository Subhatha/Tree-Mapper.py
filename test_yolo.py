from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model("frames/frame_0000.jpg")

results[0].plot() 