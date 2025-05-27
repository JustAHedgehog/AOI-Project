# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:59:06 2024

@author: user
"""

import numpy as np 
import matplotlib.pyplot as plt
import math as m

x_0=-1
y_0=2
xm_1=-2
ym_1=0
xm_2=0
ym_2=1

#入射光向量

a_1=np.array([(xm_1-x_0),(ym_1-y_0)])
a_2=np.array([(xm_2-x_0),(ym_2-y_0)])

#法線

uni_normal_vector=np.array([1/(m.sqrt(5)),-2/(m.sqrt(5))])
b_=(np.dot(a_1, uni_normal_vector)*uni_normal_vector)
#b_2=(np.dot(a_2, uni_normal_vector)*uni_normal_vector)
#print(b_)

#反射光

c_1=a_1-(2*b_)
c_2=a_2-(2*b_)
#print(c_1)
#print(c_2)


#直線方程式

s_1=c_1[1]/c_1[0]
s_2=c_2[1]/c_2[0]

x=np.linspace(-4,4,10 )
y_1=s_1*(x-xm_1)+ym_1
y_2=s_2*(x-xm_2)+ym_2
y=0.5*x+1
plt.ylim(-5,5)
#plt.plot(x,y_1,x,y_2,x,y)
plt.plot(x,y_1,color="b")
plt.plot(x,y_2,color="g")
plt.plot(x,y,color="r")
plt.plot((x_0,xm_1),(y_0,ym_1),'o-')
plt.plot((x_0,xm_2),(y_0,ym_2),'o-')
plt.grid()
plt.show()
#交點
#p=np.array([-2,0])-c_1
p=np.array([0,1])-c_2
plt.scatter(p[0], p[1])
print("交點:",p)