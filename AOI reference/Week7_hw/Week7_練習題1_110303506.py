import numpy as np
import matplotlib.pyplot as plt

def main():
    #讀取txt檔
    d_1=np.loadtxt('Week7_hw/txt/g0t.txt') 
    d_2=np.loadtxt('Week7_hw/txt/g1t.txt')
    d_3=np.loadtxt('Week7_hw/txt/g2t.txt')
    d_4=np.loadtxt('Week7_hw/txt/g3t.txt')
    d_5=np.loadtxt('Week7_hw/txt/g4t.txt')
    d_6=np.loadtxt('Week7_hw/txt/g5t.txt')
    
    #將讀入的檔案寫成串列方便計算
    d = [d_1,d_2,d_3,d_4,d_5,d_6]
    
    # 初始化
    d_max = 0
    s_max = 0

    #計算差距總和
    for i in range(len(d)):
        # x= np.linspace(0,len(d),len(d))
        y = d[i]
        dx=len(d)/len(d)
        L = np.array([1,-1])
        dydx = np.abs(np.convolve(y,L,'same')/dx) #計算微分
        s = int(sum(dydx))
        
        #找出最清晰的像
        if s>s_max:
            s_max = s
            d_max = f"g{str(i)}t.txt"
    print(f"The clearest image is {d_max}")

if __name__ == '__main__':
    main()