import cv2
import os

# 讀取圖片
image = cv2.imread(r"final\prob_1\init_image.png")
height, width, _ = image.shape

# 切割參數
rows = 3
cols = 4
tile_height = height // rows
tile_width = width // cols

# 輸出資料夾
output_dir = "final/prob_1/train_set"
os.makedirs(output_dir, exist_ok=True)

# 切割與儲存
for row in range(rows):
    for col in range(cols):
        y1 = row * tile_height
        y2 = (row + 1) * tile_height
        x1 = col * tile_width
        x2 = (col + 1) * tile_width
        tile = image[y1:y2, x1:x2]
        filename = f"{row+1}-{col+1}.png"
        cv2.imwrite(os.path.join(output_dir, filename), tile)