import numpy as np
import matplotlib.pyplot as plt

def intersection(cenX, cenY, R, theta):
    # 計算光線與球面的交點
    slope = np.tan(theta)
    A = 1 + slope**2
    B = -2 * (cenX + slope * cenY)
    C = cenX**2 + cenY**2 - R**2

    # 解二次方程 Ax^2 + Bx + C = 0
    discriminant = B**2 - 4*A*C
    x_hit1 = (-B - np.sqrt(discriminant)) / (2*A)  # 取較小的 x
    y_hit1 = slope * x_hit1  # 計算對應的 y
    return x_hit1, y_hit1

# (x-18)^2 + y^2 = radius^2
def focus_point(x, y, theta, R, CenY,n_a, n_g):
    thi = np.arcsin((y-CenY)/R)
    # print("thi=", np.degrees(thi))
    theta_i = thi + theta
    theta_r = np.arcsin((n_a/n_g)*np.sin(theta_i))
    L = x + y*np.tan(np.radians(90)-thi+theta_r)
    return L

CenX = 18 # 單位 mm
CenY = 0 # 單位 mm
radius = 5 # 單位 mm
n_a = 1  # 空氣折射率
n_g = 1.5  # 玻璃折射率

bevel =np.sqrt(CenX**2- radius**2)
# 可照射之臨界角(rad)
theta_c = np.arccos(bevel/CenX)

# 入射角(rad)
theta = np.linspace(0,theta_c,100)
x, y = intersection(CenX, CenY, radius, theta)

# 計算焦點
for i in range(len(x)):
    L = focus_point(x[i], y[i], theta, radius, CenY, n_a, n_g)

# 繪圖
plt.figure(figsize=(8, 5))
plt.plot(np.degrees(theta), L, label="L vs θ")
plt.xlabel(" incident angle θ ")
plt.ylabel("focus L (mm)")
plt.title("Relation of θ & L")
plt.legend()
plt.grid()
plt.show()