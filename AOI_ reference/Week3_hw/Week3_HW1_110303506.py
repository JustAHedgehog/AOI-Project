# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:41:06 2024

@author: user
"""

import numpy as np
import matplotlib.pyplot as plt
import math as m
#import sympy as sy



a_=np.array([-1,0])

uni_normal_vector_1=np.array([(5/m.sqrt(26)),(-1/m.sqrt(26))])
uni_normal_vector_2=np.array([(10/m.sqrt(101)),(-1/m.sqrt(101))])
uni_normal_vector_3=np.array([(50/m.sqrt(2501)),(-1/m.sqrt(2501))])


b_1=np.dot(a_,uni_normal_vector_1)*uni_normal_vector_1
b_2=np.dot(a_,uni_normal_vector_2)*uni_normal_vector_2
b_3=np.dot(a_,uni_normal_vector_3)*uni_normal_vector_3

c_1=a_-2*b_1
c_2=a_-2*b_2
c_3=a_-2*b_3

x=np.linspace(0,2,100)
x_1=np.linspace(0.01,2,100)
x_2=np.linspace(0.0025,2,100)
x_3=np.linspace(0.0001,2,100)
plt.xlim(0, 0.3)
plt.ylim(-0.1, 0.3)
y=x**2


s_1=(c_1[1]/c_1[0])
s_2=(c_2[1]/c_2[0])
s_3=(c_3[1]/c_3[0])
y_1=s_1*(x_1-0.01)+0.1
y_2=s_2*(x_2-0.0025)+0.05
y_3=s_3*(x_3-0.0001)+0.01
#print(b_)
#print(a_-2*b_)

plt.plot(y,x)
plt.plot(x_1,y_1)
plt.plot(x_2,y_2)
plt.plot(x_3,y_3)
plt.grid()

