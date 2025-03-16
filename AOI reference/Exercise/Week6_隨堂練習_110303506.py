import numpy as np
from matplotlib import pyplot as plt
# 轉移矩陣
def transfer(d:float):
    return np.array([[1, d],
                    [0, 1]])
# 折射矩陣
def thinlens(f:float):
    return np.array([[1, 0],
                    [-1/f, 1]])

def main():
    # 入射[x,alpha]
    input_array = np.array([[0,0],
                            [-5,5]])

    # instance
    t1 = transfer(200)
    r1 = thinlens(100)
    # 出射[x,alpha]
    m2 = r1.dot(t1).dot(input_array)

    # 從透鏡向後尋找成像點(向後迭代長度)
    x1 = m2[0,0]
    x2 = m2[0,1]
    distance = 0
    d_distance = 1
    while x1 < x2:
        distance += d_distance
        t2 = transfer(distance)
        m_temp = t2.dot(m2)
        x1 = m_temp[0,0]
        x2 = m_temp[0,1]
    print(distance)



if __name__ == '__main__':
    main()


