import numpy as np
import matplotlib.pyplot as plt
import math as m

a_ = np.array([-1, 0])

normal_unit_vector_1 = np.array([(5/m.sqrt(26)), (-1/m.sqrt(26))])
normal_unit_vector_2 = np.array([(10/m.sqrt(101)), (-1/m.sqrt(101))])
normal_unit_vector_3 = np.array([(50/m.sqrt(2501)), (-1/m.sqrt(2501))])


b_1 = np.dot(a_, normal_unit_vector_1)*normal_unit_vector_1
b_2 = np.dot(a_, normal_unit_vector_2)*normal_unit_vector_2
b_3 = np.dot(a_, normal_unit_vector_3)*normal_unit_vector_3

c_1 = a_-2*b_1
c_2 = a_-2*b_2
c_3 = a_-2*b_3

x = np.linspace(0, 2, 100)
x_1 = np.linspace(0.01, 2, 100)
x_2 = np.linspace(0.0025, 2, 100)
x_3 = np.linspace(0.0001, 2, 100)
plt.xlim(0, 0.3)
plt.ylim(-0.1, 0.3)

# parabola
y = x**2

s_1 = (c_1[1]/c_1[0])
s_2 = (c_2[1]/c_2[0])
s_3 = (c_3[1]/c_3[0])
y_1 = s_1*(x_1-0.01)+0.1
y_2 = s_2*(x_2-0.0025)+0.05
y_3 = s_3*(x_3-0.0001)+0.01


plt.plot(y, x, color="r")
plt.plot(x_1, y_1, color="g")
plt.plot(x_2, y_2, color="orange")
plt.plot(x_3, y_3)
plt.grid()
plt.legend(["y=x^2", "y=0.1x+0.1", "y=0.05x+0.05", "y=0.01x+0.01"])
plt.show()
