import os
import cv2
import numpy as np

frames_path = "runs/detect/predict"

tree_positions = []
tree_id = 0

for file in os.listdir(frames_path):
    if file.endswith(".jpg"):
        img_path = os.path.join(frames_path, file)
        img = cv2.imread(img_path)

        h, w, _ = img.shape

        # trees marked in image → detect green boxes (YOLO output)

        # store random sample points

        tree_id += 1
        x = np.random.randint(0, w)
        y = np.random.randint(0, h)

        tree_positions.append((tree_id, x, y))

# Create map
map_img = np.zeros((500, 500, 3), dtype=np.uint8)

for tree in tree_positions:
    _, x, y = tree
    x = int(x / w * 500)
    y = int(y / h * 500)

    cv2.circle(map_img, (x, y), 5, (0, 255, 0), -1)

cv2.imwrite("tree_map.jpg", map_img)

print("Tree map created!")