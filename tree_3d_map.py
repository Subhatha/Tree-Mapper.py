import os
import glob
import numpy as np
import matplotlib.pyplot as plt

# Path 
labels_dir = r"runs/detect/predict2/labels"

tree_points = []

frame_index = 0

txt_files = sorted(glob.glob(os.path.join(labels_dir, "*.txt")))

for txt_file in txt_files:
    with open(txt_file, "r") as f:
        lines = f.readlines()

    for line in lines:
        parts = line.strip().split()
        if len(parts) < 5:
            continue

        
        # class x_center y_center width height [confidence]
        cls_id = int(float(parts[0]))
        x_center = float(parts[1])
        y_center = float(parts[2])
        width = float(parts[3])
        height = float(parts[4])

        # 3D 
        # x = horizontal image position
        # y = frame progression (walk direction)
        # z = tree "height/strength" estimated from bbox height
        x = (x_center - 0.5) * 20
        y = frame_index * 1.5
        z = height * 30

        # Simple rule:
        # smaller trees -> cut (green)
        # larger trees -> keep (red)
        decision = "cut" if height < 0.25 else "keep"
        color = "green" if decision == "cut" else "red"

        tree_points.append((x, y, z, color, decision, height))

    frame_index += 1

if not tree_points:
    print("No detections found. Check your labels folder path.")
    exit()

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

for i, (x, y, z, color, decision, h) in enumerate(tree_points, start=1):
    ax.scatter(x, y, z, c=color, s=60)
    ax.text(x, y, z, str(i), fontsize=8)

ax.set_title("3D Tree Decision Map")
ax.set_xlabel("Left / Right")
ax.set_ylabel("Path Direction")
ax.set_zlabel("Estimated Tree Size")

plt.tight_layout()
plt.savefig("tree_3d_map.png", dpi=300)
plt.show()

print("3D map saved as tree_3d_map.png")