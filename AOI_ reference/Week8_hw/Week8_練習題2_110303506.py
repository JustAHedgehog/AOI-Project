import numpy as np
import matplotlib.pyplot as plt

def main():
    
    x = np.linspace(-3, 3, 300)
    X,Y = np.meshgrid(x,x) #設定網格
    z_1 = np.sin(4*X**2+2*Y**2) #橢圓
    z_2 = np.sin(2*X**2-4*Y**2) #雙曲線
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.imshow(z_1, cmap = 'Reds')
    plt.subplot(2, 1, 2)
    plt.imshow(z_2, cmap = 'Reds')
    plt.show()

if __name__=='__main__':
    main()