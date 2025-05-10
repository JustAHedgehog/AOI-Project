import numpy as np
import matplotlib.pyplot as plt

def main(): # Hough轉換演示
    # 紀錄A-G點的座標
    x = [1, 2, 3, 4, 5, 5]
    y = [1, 2, 3, 4, 5, 20]

    q = np.linspace(-np.pi, np.pi, 100) # 角度範圍

    plt.figure('result', figsize=(10, 5))
    plt.subplot(121)
    plt.title('Real Space') # 繪製原始空間
    plt.plot(x, y, 'o-')
    plt.grid()
    plt.subplot(122)
    plt.title('Hough Space') # 繪製Hough空間
    plt.grid()
    for i in range(len(x)):
        r = x[i]*np.cos(q) + y[i]*np.sin(q) # 計算r = x*cos(q) + y*sin(q)
        plt.plot(q, r)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()