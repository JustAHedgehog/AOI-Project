import numpy as np
import matplotlib.pyplot as plt


# 光線傳遞矩陣定義
def MT(D):
    """自由傳播距離 D 的轉移矩陣"""
    return np.array([[1, D], [0, 1]])


def ML(f):
    """焦距 f 的薄透鏡矩陣"""
    return np.array([[1, 0], [-1 / f, 1]])


# --- 第 (1) 題：計算像散透鏡與偵測器距離 D0 ---
fx = 100.0  # x 方向焦距 (mm)
fy = 120.0  # y 方向焦距 (mm)

# 以調和平均求出 D0，理論上即是二次透鏡對平行光的成像距離
D0 = 109.09

# --- 第 (2) 題：離焦距離 Δ 與 FES 的關係 ---
# 系統移動量 Δ (mm)
S = np.linspace(-50, 50, 501)

# 取樣範圍（依光斑預期大小 ±0.2 mm，共 1001 點）
X = np.linspace(-150, 150, 501)
Y = X.copy()

# 建立二維網格、並算出每格面積 dA
Xg, Yg = np.meshgrid(X, Y, indexing="xy")
dA = (X[1] - X[0]) * (Y[1] - Y[0])

# 初始化 FES 陣列
FES = np.zeros_like(S)

# 向量化計算各 Δ 的 FES
for idx, s in enumerate(S):
    # 透鏡傳遞矩陣計算出橢圓半軸比例 a, b
    Mx = (
        MT(D0)
        .dot(ML(fx))
        .dot(MT(300))
        .dot(ML(100))
        .dot(MT(100 - 2 * s))
        .dot(np.array([[0], [1]]))
    )
    My = (
        MT(D0)
        .dot(ML(fy))
        .dot(MT(300))
        .dot(ML(100))
        .dot(MT(100 - 2 * s))
        .dot(np.array([[0], [1]]))
    )
    a = abs(Mx[0, 0])
    b = abs(My[0, 0])

    # 橢圓內部遮罩
    mask = (Xg**2 / a**2 + Yg**2 / b**2) <= 1

    # 四個象限條件
    condA = (Xg - Yg < 0) & (Xg + Yg > 0)
    condB = (Xg - Yg > 0) & (Xg + Yg > 0)
    condC = (Xg - Yg > 0) & (Xg + Yg < 0)
    condD = (Xg - Yg < 0) & (Xg + Yg < 0)

    # 面積累加並計算 FES
    A = np.sum(mask & condA) * dA
    B = np.sum(mask & condB) * dA
    C = np.sum(mask & condC) * dA
    D = np.sum(mask & condD) * dA

    FES[idx] = ((A + C) - (B + D)) / (A + B + C + D)

# 繪圖
plt.figure(figsize=(8, 6))
plt.plot(S, FES, marker="o", markersize=4)
plt.xlabel("鏡面位移 S (mm)", fontsize=12)
plt.ylabel("Focus Error Signal (FES)", fontsize=12)
plt.title("FES vs S", fontsize=14)
plt.grid(True)
plt.show()
