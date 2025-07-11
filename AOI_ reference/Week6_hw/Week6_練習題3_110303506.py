import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(-10,10,50)
T = np.linspace(-10,10,50)
Y_1 = np.zeros(len(T))
Y_2 = np.zeros(len(T))
dx = (10-(-10))/100

plt.ion()
plt.figure(1)
for i in range(0,len(T)):
    t = T[i]
    y_0 = np.exp(-(t-x)**2) #生成方波
    y_0[np.where(y_0>0.01)]=1
    y_0[np.where(y_0<=0.01)]=0
    y_1 = np.exp(-(x+2)**2)
    y_2 = np.exp(-(x-2)**2)
    Y_1[i] = np.sum(y_1*y_0)*dx #捲積
    Y_2[i] = np.sum(y_2*y_0)*dx
    plt.subplot(2,1,1)
    plt.cla()
    plt.plot(x,y_0,color="b") #畫出函數
    plt.plot(x,y_1,color="orange")
    plt.plot(x,y_2,color="orange")
    plt.axis([-10,10,0,3])
    plt.draw()
    plt.subplot(2,1,2)
    plt.plot(x[i],max(Y_1[i],Y_2[i]),"o") #畫出函數與方波捲積的結果
    plt.axis([-10,10,0,3])
    plt.draw()
    plt.pause(0.1)
plt.ioff() 

plt.figure(2)
plt.plot(x,y_1/max(y_1),x,y_2/max(y_2),x,Y_1/max(Y_1),x,Y_2/max(Y_2))
plt.show()
