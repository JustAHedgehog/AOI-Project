import numpy as np

datas = []
L = np.array([1,-1])

for i in range(0, 5):
    path = r'week_7\txt\g' + str(i) + 't.txt'
    d = np.loadtxt(path)
    x = np.linspace(0, 10, len(d))  # 設定x座標數
    y_L = np.abs(np.convolve(d, L, mode='same'))  # 使用卷積運算
    S = np.sum(y_L)  # 計算總和
    datas.append(S)

max_index = datas.index(max(datas))  # 找出最大值的索引

print(f"The clearest image is g{max_index}t.txt")  # 印出結果