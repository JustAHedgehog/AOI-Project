import numpy as np
import matplotlib.pyplot as py

n_i = eval(input("請輸入入射介質折射率:"))
n_r = eval(input("請輸入折射介質折射率:"))
q_i = eval(input("請輸入入射角:"))*np.pi/180

q_r = np.arcsin((n_i/n_r)*np.sin(q_i*np.pi/180)) #計算折射角

if n_i > n_r:  #判斷發生全反射條件
    theta_c = np.arcsin(n_r/n_i)
    print(theta_c*180/np.pi)
    if q_i > theta_c:
        print("發生全反射，反射角 = " , q_i, "rad")
    elif q_i < theta_c:
        print("未發生全反射，折射角 = " , q_r, "rad") 
    else:
        print("入射角等於臨界角")
else:
    print("未發生全反射，折射角 = " , q_r, "rad") 