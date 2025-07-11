import numpy as np
import matplotlib.pyplot as plt 

def xNalpha( x_0 , a_0 , d_1 , f , d_2): #定義一個光追跡副函式
    
    X0 = np.array([[x_0],[a_0]])
    T01 = np.array([[1,d_1],[0,1]])
    T12 = np.array([[1,d_2],[0,1]])
    L1 = np.array([[1,0],[(-1/f),1]])
    xa = T12.dot(L1).dot(T01).dot(X0)
    return xa

H = []
f = 100 #透鏡焦距
d_1 = 300 #水珠到透鏡的距離
d_2 = 150 #透鏡到成像的距離
x_0 = np.linspace(-5,5,100) #光源的範圍

for j in x_0:
    if abs(j)<2: #水珠的位置
        a = np.deg2rad(np.linspace(-5,5,1000)) #光源角度
    else:
        a = np.deg2rad(np.linspace(-0.0005,0.0005,1000))
    for i in a:
        if xNalpha(j , i , d_1 , f , 100)[0]<=-0.001: #遮光板位置
            continue
        X = xNalpha(j , i , d_1 , f , d_2)
        H.append(X[0])

H = np.array(H)
plt.figure()
bin = np.linspace(-10,10,50)
plt.hist(H,bin)
plt.show()
