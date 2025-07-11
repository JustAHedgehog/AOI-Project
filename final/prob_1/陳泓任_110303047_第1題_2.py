import os
import sys
from ultralytics import YOLO
import cv2
import torch

# === 設定路徑 ===
model_path = r"final\prob_1\yolo\best.pt"
video_path = r"final\prob_1\puzzle.mp4"
output_path = r"final\prob_1\puzzle_output.mp4"
save_frames_dir = "final/prob_1/yolo/frames"

# === 檢查檔案存在 ===
if not os.path.exists(model_path):
    print(f"❌ 找不到模型檔案：{model_path}")
    sys.exit(1)

if not os.path.exists(video_path):
    print(f"❌ 找不到影片檔案：{video_path}")
    sys.exit(1)

# === 建立儲存 frame 圖片的資料夾 ===
os.makedirs(save_frames_dir, exist_ok=True)

# === 載入模型 ===
print(f"📦 載入模型：{model_path}")
model = YOLO(model_path)

# === 開啟影片 ===
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("❌ 無法打開影片")
    sys.exit(1)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = int(cap.get(cv2.CAP_PROP_FPS))  # 每秒幾張影格
print(f"🎥 FPS = {fps}")
w, h = int(cap.get(3)), int(cap.get(4))
out = cv2.VideoWriter(output_path, fourcc, fps, (w, h))

frame_count = 0
save_interval = fps * 2  # 每 2 秒儲存一次

saved_count = 0  # 記錄儲存張數

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    with torch.no_grad():
        results = model.predict(source=frame, conf=0.2, verbose=False)[0]

    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
        cls = int(box.cls[0])
        conf = float(box.conf[0])
        label = f"{model.names[cls]} {conf:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 1) # 調薄一點

    # 每 2 秒儲存一次
    if frame_count % save_interval == 0:
        saved_count += 1
        filename = os.path.join(save_frames_dir, f"frame_{saved_count:04d}.jpg")
        cv2.imwrite(filename, frame)
        print(f"📸 已儲存第 {saved_count} 張 frame：{filename}")

    out.write(frame)
    cv2.imshow("YOLOv8 Detection", frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("✅ 推論與間隔儲存完成！")
