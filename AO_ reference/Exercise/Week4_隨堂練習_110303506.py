import numpy as np

n_a=1    #refractive index (Air)
n_g=1.5  #refractive index (prism)
A = 50*np.pi/180 #angle of prism(rad)
theta_c = np.arcsin(n_a/n_g)  #critical angle
q_1p= A-theta_c
q_1=np.arcsin((n_g/n_a)*np.sin(q_1p))
a=q_1*180/np.pi
print(f"Incident angle = {a:.2f}")





