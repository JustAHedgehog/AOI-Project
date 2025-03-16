import numpy as np
import matplotlib.pyplot as plt

A = 30*np.pi/180 #頂角(rad)
n_a = 1
n_g = 1.5 #稜鏡折射率

q_1 = np.linspace(0,90,30)*np.pi /180
q_1p = np.arcsin((n_a/n_g)*np.sin(q_1))
q_2 = A - q_1p
q_2p = np.arcsin(n_g/n_a*np.sin(q_2))
D = q_1 + q_2p - A

plt.plot(q_1 , D,"o-")
plt.grid()
#plt.show()

for i in range(len(q_1)-1):
    if D[i] <= D[i+1]:
        print(f"最小偏向角{D[i]} rad\n入射角{q_1[i]} rad")
        break
