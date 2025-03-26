import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 50*2)  # 設定x座標數
T = np.linspace(-10, 10, 50*2)  # 設定時間T數目

# 初始化y座標
Y_1 = np.zeros(len(T))
Y_2 = np.zeros(len(T))
dx = (10-(-10))/100  # 設定間距dx

choice = bool(int(input("Please choose one, one wave function[0] or two wave function[1]: ")))
print(choice)
plt.ion() # 允許動態圖
plt.figure(1)
if choice: # y_1 = e^-(x+2)^^2; y_2 = e^-(x-2)^^2
    for i in range(0, len(T)):
        t = T[i]

        # 生成方波
        y_0 = np.exp(-(t-x)**2)
        y_0[np.where(y_0 > 0.1)] = 1
        y_0[np.where(y_0 <= 0.1)] = 0

        y_1 = np.exp(-(x+2)**2)
        y_2 = np.exp(-(x-2)**2)
        Y_1[i] = np.sum(y_1*y_0)*dx  # 捲積
        Y_2[i] = np.sum(y_2*y_0)*dx
        plt.subplot(2, 1, 1)
        plt.cla()
        plt.plot(x, y_0, color="b")  # 畫出函數
        plt.plot(x, y_1, color="orange")
        plt.plot(x, y_2, color="orange")
        plt.axis([-10, 10, 0, 3])
        plt.draw()
        plt.subplot(2, 1, 2)
        plt.plot(x[i], max(Y_1[i], Y_2[i]), "o")  # 畫出函數與方波捲積的結果
        plt.axis([-10, 10, 0, 3])
        plt.draw()
        plt.pause(0.1)
    plt.ioff() # 關閉動態圖

    plt.figure(2)
    plt.plot(x, y_1/max(y_1), x, y_2/max(y_2), x, Y_1/max(Y_1), x, Y_2/max(Y_2))
    plt.plot(x, y_1/max(y_1), x, Y_1/max(Y_1))
    plt.show()
else: # y_1 = e^-(x+2)^^2 + e^-(x-2)^^2
    for i in range(0, len(T)):
        t = T[i]
        y_0 = np.exp(-(t-x)**2)
        y_0[np.where(y_0 > 0.1)] = 1
        y_0[np.where(y_0 <= 0.1)] = 0
        y_1 = np.exp(-(x+2)**2) + np.exp(-(x-2)**2)
        Y_1[i] = np.sum(y_1*y_0)*dx
        plt.subplot(2, 1, 1)
        plt.cla()
        plt.plot(x, y_0, color="b")
        plt.plot(x, y_1, color="orange")
        plt.axis([-10, 10, 0, 3])
        plt.draw()
        plt.subplot(2, 1, 2)
        plt.plot(x[i], Y_1[i], "o")
        plt.axis([-10, 10, 0, 3])
        plt.draw()
        plt.pause(0.1)
    plt.ioff()

    plt.figure(2)
    plt.plot(x, y_1/max(y_1), x, Y_1/max(Y_1))
    plt.show()