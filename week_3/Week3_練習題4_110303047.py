"""
Subject: draw the reflection of two lights and find the intersection point
"""
import numpy as np
import matplotlib.pyplot as plt
import math as m

# subject position (x_0,y_0) = (-1,2)
x_0 = -1
y_0 = 2

# first reflection lights pass the point (xm_1,ym_1) = (-2,0)
xm_1 = -2
ym_1 = 0

# second reflection lights pass the point (xm_2,ym_2) = (0,1)
xm_2 = 0
ym_2 = 1

# incident light vector
a_1 = np.array([(xm_1-x_0), (ym_1-y_0)])
a_2 = np.array([(xm_2-x_0), (ym_2-y_0)])

# normal vector of x-2y=-2
normal_unit_vector = np.array([1/(m.sqrt(5)), -2/(m.sqrt(5))])
b_vector = (np.dot(a_1, normal_unit_vector)*normal_unit_vector)

# reflection light
c_1 = a_1-(2*b_vector)
c_2 = a_2-(2*b_vector)

# line equation
s_1 = c_1[1]/c_1[0]
s_2 = c_2[1]/c_2[0]

x = np.linspace(-4, 4, 10)
y_1 = s_1*(x-xm_1)+ym_1
y_2 = s_2*(x-xm_2)+ym_2
# print("y_1 = ",s_1,"(x-",xm_1,")+",ym_1)
# print("y_2 = ",s_2,"(x-",xm_2,")+",ym_2)
y = 0.5*x+1
plt.ylim(-5, 5)
plt.plot(x, y_1, color="b")
plt.plot(x, y_2, color="g")
plt.plot(x, y, color="r")
plt.plot((x_0, xm_1), (y_0, ym_1), 'o-')
plt.plot((x_0, xm_2), (y_0, ym_2), 'o-')
plt.grid()
plt.show()

# intersection
p = np.array([0, 1])-c_2
plt.scatter(p[0], p[1])
print("交點:", p)
