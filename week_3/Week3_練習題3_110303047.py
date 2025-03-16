"""
Subject: find the intersection point of two lines
"""
import numpy as np

# a_1*x+b_1*y=c_1
a_1 = 5
b_1 = 3
c_1 = 10

# a_2*x+b_2*y=c_2
a_2 = 3
b_2 = 5
c_2 = 5

# delta=|a_1 b_1|
#       |a_2 b_2|
matrix_1 = np.array([[a_1, b_1], [a_2, b_2]])
delta = np.linalg.det(matrix_1)

# delta_x=|c_1 b_1|
#         |c_2 b_2|
matrix_2 = np.array([[c_1, b_1], [c_2, b_2]])
delta_x = np.linalg.det(matrix_2)

# delta_y=|a_1 c_1|
#         |a_2 c_2|
matrix_3 = np.array([[a_1, c_1], [a_2, c_2]])
delta_y = np.linalg.det(matrix_3)

x = delta_x/delta
y = delta_y/delta

print('x=', x)
print('y=', y)
