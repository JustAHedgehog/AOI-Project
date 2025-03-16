import numpy as np
import matplotlib.pyplot as plt

A = 30*np.pi/180 #頂角(rad)
n_a = 1
n_g = 1.5 #稜鏡折射率

thi_1 = np.linspace(0,90,30)*np.pi /180
thi_1p = np.arcsin((n_a/n_g)*np.sin(thi_1))
thi_2 = A - thi_1p
thi_2p = np.arcsin(n_g/n_a*np.sin(thi_2))
D = thi_1 + thi_2p - A

plt.plot(thi_1*180/np.pi, D*180/np.pi,"o-")
plt.xlabel("Insertion Angle")
plt.ylabel("Refraction Angle")
plt.grid()
plt.show()

for i in range(len(thi_1)-1):
    if D[i] <= D[i+1]:
        print(f"最小偏向角{D[i]*180/np.pi} deg\n入射角{thi_1[i]*180/np.pi} deg")
        break