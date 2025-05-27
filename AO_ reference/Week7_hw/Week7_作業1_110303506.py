import matplotlib.pyplot as plt
import numpy as np

def main():
    s = np.linspace(0,100,100)   #定義題目s的範圍
    x = np.linspace(-20,20,500)  #定義x,y範圍
    y = np.linspace(-20,20,500)
    dA = (2*20/500)**2 #指定單位面積大小
    FES =[] #建立空的串列

    #計算面積以及fes的值，並將其放到FES串列中
    for S in s:
        a = 10+10*S/100
        b = 20-10*S/100
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
    plt.plot(s,FES) #畫出s,FES的關係圖
    plt.show()

if __name__ == '__main__':
    main()




