import cv2
import os

video_path = "inputtrees.mp4"
output_folder = "frames"


os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)

frame_count = 0
fps = 5 

video_fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(video_fps / fps)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % frame_interval == 0:
        filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(filename, frame)

    frame_count += 1

cap.release()
print("Done extracting frames!")