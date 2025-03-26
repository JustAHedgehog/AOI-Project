import numpy as np


def xNalpha(x_0, a_0, d_1, f, d_2):  # 定義一個光追跡副函式

    X0 = np.array([[x_0], [a_0]])
    T01 = np.array([[1, d_1], [0, 1]])
    T12 = np.array([[1, d_2], [0, 1]])
    L1 = np.array([[1, 0], [(-1/f), 1]])
    xa = T12.dot(L1).dot(T01).dot(X0)
    return xa

input_array = np.array([[0, 0], [-5, 5]])

d_2 = 0
xa = xNalpha(input_array[0, 0], input_array[1, 1], 200, 100, d_2)
while xa[0] != 0:
    d_2 += 1
    xa = xNalpha(input_array[0, 0], input_array[1, 1], 200, 100, d_2)

print(d_2)