import numpy as np
import matplotlib.pyplot as plt

# 題目參數
f_1 = 100 # 透鏡L1焦距
l =300 # 兩透鏡距離
f_x = 100 # 像散透鏡x軸焦距
f_y = 120 # 像散透鏡y軸焦距

class M_Len():
    def __init__(self, f, D=0):
        self.D = D  # 光在同介質中的位移
        self.MR_i = np.array([[1, 0], [-1 / f, 1]])  # 透鏡矩陣（焦距公式）
        self.MR_o = np.identity(2)  # 外側矩陣為單位矩陣，因為已由 f 計算

        self.MT = np.array([[1, self.D], [0, 1]])
        self.M_Len = self.MR_o.dot(self.MT.dot(self.MR_i))

x_ = np.array([1, 0])
y_ = np.array([-1, 0])

d = np.linspace(0,1000,1000) # 像散透鏡與偵測器距離
for d  in d:
    M_x = M_Len(f_x, d)
    M_y = M_Len(f_y, d)

    x_1 = M_x.M_Len.dot(x_)[0]
    y_1 = M_y.M_Len.dot(y_)[0]

    if abs(x_1 - y_1) < 0.001: # 計算當兩點接近重和時d的數值
        print(f"d = {d}")
        print(x_1,y_1)
        d = d

delta = np.linspace(0,100,1000) # 像散透鏡與偵測器距離

for delta in delta:
    M_L1 = M_Len(f_1,f_1-delta)
    x_1 = M_L1.M_Len.dot(x_)
    y_1 = M_L1.M_Len.dot(y_)
    x_b = M_L1.M_Len.dot(x_1)# L1反射光
    y_b = M_L1.M_Len.dot(x_1)# L1反射光

    MT = np.array([[1, l], [0, 1]])
    x_b1 = MT.dot(x_b)
    y_b1 = MT.dot(y_b)

    M_x = M_Len(f_x, d)
    M_y = M_Len(f_y, d)
    a = M_x.M_Len.dot(x_b1)[0]
    b = M_y.M_Len.dot(y_b1)[0]

    mesh = 500 # 定義網格數量
    range = 20
    x = np.linspace(-range,range,mesh)  #定義x,y範圍
    y = np.linspace(-range,range,mesh)
    dA = (2*range/mesh)**2 #指定單位面積大小
    FES =[] #建立空的串列
    A = 0; B = 0; C = 0; D = 0
    for X in x:
        for Y in y:
            if X**2/a**2+Y**2/b**2<=1 and X-Y<0 and X+Y>0: #橢圓上半部
                A=A+dA
            if X**2/a**2+Y**2/b**2<=1 and X-Y>0 and X+Y>0: #橢圓右半部
                B=B+dA
            if X**2/a**2+Y**2/b**2<=1 and X-Y>0 and X+Y<0: #橢圓下半部
                C=C+dA
            if X**2/a**2+Y**2/b**2<=1 and X-Y<0 and X+Y<0: #橢圓左半部
                D=D+dA
    fes=((A+C)-(B+D))/(A+B+C+D) #計算FES
    FES.append(fes)
plt.plot(delta,FES) #畫出delta,FES的關係圖
plt.show()
