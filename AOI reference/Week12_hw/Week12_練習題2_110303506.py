import numpy as np
import matplotlib.pyplot as plt

def main():
    x = [0,1,2,3,4,5,5]
    y = [0,1,2,3,4,5,20]
    q = np.linspace(-np.pi,np.pi,500)
    plt.subplot(1,2,1)
    plt.title('x,y plane')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x,y,'o')
    plt.subplot(1,2,2)
    plt.title('Hough transform')
    plt.xlabel('theta')
    plt.ylabel('r')
    for i in range(len(x)):
        r = x[i]*np.cos(q)+y[i]*np.sin(q)
        plt.plot(q,r)
    plt.show()
if __name__=='__main__':
    main()