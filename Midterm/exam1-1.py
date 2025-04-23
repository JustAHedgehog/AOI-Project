import numpy as np

# 焦距參數
fx = 100.0  # x 方向焦距 (mm)
fy = 120.0  # y 方向焦距 (mm)

# 使用 np.linspace 生成距離範圍
D = np.linspace(100, 120, 10000)  # 0 到 200 mm，共 10001 個點

Mxx = 1 - D / fx
Myy = 1 - D / fy

# 找到 Mxx = -Myy 的近似解
diff = np.abs(Mxx + Myy)

# 找出最小數值的索引值
idx = np.argmin(diff)

D_intersect = D[idx]

print(f"近似交點 D ≈ {D_intersect:.2f} mm")

a = 1 - D_intersect / fy
print(f"{a:.2f}")
