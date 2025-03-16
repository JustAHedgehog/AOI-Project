import numpy as np

def AngleTrans(thi):
    deg = thi*180/np.pi
    return deg

A = 50*np.pi/180 #頂角(rad)
n_a = 1  # 入射光介質折射率
n_g = 1.5  # 折射光介質折射率

# 發生全反射
thi_2p = 90*np.pi/180
thi_2 = np.arcsin((n_a/n_g)*np.sin(thi_2p))
thi_1p = A - thi_2
thi_1 = np.arcsin((n_g/n_a)*np.sin(thi_1p))

print("發生全反射，入射角 =", AngleTrans(thi_1), "deg.")
print("發生全反射，第一折射角 =", AngleTrans(thi_1p), "deg.")
print("發生全反射，臨界角 =", AngleTrans(thi_2), "deg.")