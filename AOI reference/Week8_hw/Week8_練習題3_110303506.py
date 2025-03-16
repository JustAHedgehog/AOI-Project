import numpy as np
import matplotlib.pyplot as plt

def main():
    x = np.linspace(-30, 30, 500)
    X,Y = np.meshgrid(x, x) #網格
    z = 5
    L = 0.5 #波長
    c_1 = (1, 0, z) #光源座標
    c_2 = (0, -1, z) #光源座標
    r_1 = np.sqrt((c_1[0]-X)**2 + (c_1[1]-Y)**2 + (c_1[2]-0)**2) #光源到狹縫的距離
    r_2 = np.sqrt((c_2[0]-X)**2 + (c_2[1]-Y)**2 + (c_2[2]-0)**2)
    k = 2*np.pi/L #波數
    E_1 = np.exp(1j*k*r_1) 
    E_2 = np.exp(1j*k*r_2)
    I = abs(E_1 + E_2)**2 #強度
    plt.imshow(I, cmap = 'Reds')
    plt.show()

if __name__=='__main__':
    main()