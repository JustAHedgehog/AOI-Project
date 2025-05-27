import numpy as np 
import matplotlib.pyplot as plt 

x = np.ones(100)
alpha = np.deg2rad(np.linspace(-5,5,100))
x_0 = np.array([x , alpha])
m_1 = np.array([[1 , 0] , [(-1/100) , 1]]) #f= 100 的透鏡矩陣
m_2 = np.array([[1 , 0] , [(-1/80) , 1]])  #f= 80 的透鏡矩陣

#轉移矩陣
t_1 = np.array([[1 , 120] , [0 , 1]])
t_2 = np.array([[1 , 220] , [0 , 1]])
t_3 = np.array([[1 , 150] , [0 , 1]])

m_l = t_3.dot(m_2).dot(t_2).dot(m_1).dot(t_1).dot(x_0) #光追跡
print(m_l)
plt.plot(np.rad2deg(alpha) , m_l[0])
plt.grid()
plt.show()
