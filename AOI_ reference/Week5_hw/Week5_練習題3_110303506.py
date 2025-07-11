import numpy as np 
import matplotlib.pyplot as plt 

n_ = 1
n_l = 1.5
r_1 = 10
r_2 = -10
p_1 = (n_l-n_)/r_1
p_2 = (n_-n_l)/r_2

A_1 = np.array([[1 , 0],[-p_1/n_l , n_/n_l]])
A_2 = np.array([[1 , 0],[-p_2/n_ , n_l/n_]])

M_L = A_2.dot(A_1)
print(M_L)