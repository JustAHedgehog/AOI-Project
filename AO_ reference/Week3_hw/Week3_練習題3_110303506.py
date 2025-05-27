# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:22:16 2024

@author: user
"""

import numpy as np

matrix_1=np.array([[5,3],[3,5]])
matrix_2=np.array([[10,3],[5,5]])
matrix_3=np.array([[5,10],[3,5]])
delta=np.linalg.det(matrix_1)
delta_x=np.linalg.det(matrix_2)
delta_y=np.linalg.det(matrix_3)

x=delta_x/delta
y=delta_y/delta

print('x=',x)
print('y=',y)
