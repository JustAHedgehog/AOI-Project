import numpy as np
import matplotlib.pyplot as py

#定義一個sec函數
def sec(x):
    y=1/np.cos(x*np.pi/180)

    return y

n_i=1   #入射光介質折射率
n_r=1.5 #折射光介質折射率
theta_i = np.linspace(0,90,100)
theta_r = np.arcsin((1/1.5)*np.sin(theta_i*np.pi/180)) #計算反射角
d = 5*sec(theta_r)*np.sin(theta_i-theta_r) #計算經過折射後的出射光與原入射光延伸線的距離
py.plot(theta_i,d,color="r")
py.xlabel("incidence angle",color="b")
py.ylabel("distance",color="b")
py.grid()
py.show()

