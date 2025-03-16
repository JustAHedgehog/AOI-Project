import numpy as np

def AngleTrans(thi):
    deg = thi*180/np.pi
    return deg

n_i = eval(input("請輸入入射介質折射率n_i = "))  # 入射光介質折射率
n_r = eval(input("請輸入折射介質折射率n_r = "))  # 折射光介質折射率
thi_i = eval(input("請輸入入射角 = ")) # 入射角(deg)

if n_i > n_r: # 判斷發生全反射條件
    thi_c = AngleTrans(np.arcsin(n_r/n_i)) # 臨界角(deg)
    if thi_i == thi_c:
        print("入射角等於臨界角")
    elif thi_i > thi_c:
        print("發生全反射，反射角 =", thi_i, "deg.")
    else:
        thi_r = AngleTrans(np.arcsin((n_i/n_r)*np.sin(thi_i*np.pi/180))) # 折射角(deg)
        print("未發生全反射，折射角 =", thi_r, "deg.")
else:
    thi_r = AngleTrans(np.arcsin((n_i/n_r)*np.sin(thi_i*np.pi/180))) # 折射角(deg)
    print("未發生全反射，折射角 =", thi_r, "deg.")
