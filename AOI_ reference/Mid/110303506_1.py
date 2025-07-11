import numpy as np 
import matplotlib.pyplot as plt

def T(d): #傳遞矩陣
    D = np.array([[1,d],[0,1]])
    return D

def M(f): #透鏡矩陣
    m = np.array([[1,0],[-(1/f),1]])
    return m

def main():
    h = np.linspace(-100, 100, 400)
    a = np.zeros(len(h))
    a = 100
    b = 100
    n = 1.5
    A = np.deg2rad(5)
    f_1 = 50
    f_2 = 30
    tmp = []

    for i in h:
        I = T(b).dot(M(f_2)).dot(T(a)).dot(M(f_1)).dot([i,0]) #追跡
        # print(I)
        q_1 = I[1] #取得入射角
        q_1p = np.arcsin((1/n)*np.sin(q_1))
        q_2 = A - q_1p
        q_2p = np.arcsin(n/1*np.sin(q_2))
        D = q_1 + q_2p - A #偏轉角
        tmp.append(D)
        
    plt.plot(tmp,h)
    plt.show()

if __name__=='__main__':
    main()

    