import numpy as np 
import matplotlib.pyplot as plt 

n_ = 1
n_l = 1.5
r_ = 15
p_ = (n_l-n_)/r_

M_ = np.array([[1 , 0],[-p_/n_l , n_/n_l]])
x_ = np.array([1 , np.deg2rad(1)])

print(np.rad2deg(M_.dot(x_)[1]))