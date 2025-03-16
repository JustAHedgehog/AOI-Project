import numpy as np
import matplotlib.pyplot as plt

n_i = 1  # 入射光介質折射率
n_r = 1.5  # 折射光介質折射率
t = 1
thi_i = np.linspace(0, 90, 180)*np.pi/180
thi_r = np.arcsin((n_i/n_r)*np.sin(thi_i))  # 計算折射角
light_path = t/np.cos(thi_r)  # 光在n_r介質中走的路徑長
d = light_path * np.sin(thi_i-thi_r)  # 計算經過折射後的出射光與原入射光延伸線的距離

plt.plot(thi_i, d, color="r")
plt.xlabel("incidence angle")
plt.ylabel("distance")
plt.grid()
plt.show()
