import numpy as np

def incident_light(height,angle, dimension:bool=True):
    if dimension:
        return np.array([height, np.deg2rad(angle)])
    else:
        return np.array([height, angle])
class M_Len():
    def __init__(self, n, n_L, f=None, r_i=None, r_o=None, D=0):
        self.n = n  # 外部折射率
        self.n_L = n_L  # 透鏡折射率
        self.D = D  # 光在同介質中的位移
        
        # 判斷使用焦距 f 還是曲率半徑 r_i, r_o 來計算
        if f is not None:
            self.MR_i = np.array([[1, 0], [-1 / f, 1]])  # 透鏡矩陣（焦距公式）
            self.MR_o = np.identity(2)  # 外側矩陣為單位矩陣，因為已由 f 計算
        else:
            self.Ri = r_i if r_i is not None else 1
            self.Ro = r_o if r_o is not None else -1
            self.p_i = (self.n_L - self.n) / self.Ri
            self.p_o = (self.n - self.n_L) / self.Ro
            self.MR_i = np.array([[1, 0], [-self.p_i / self.n_L, self.n / self.n_L]])
            self.MR_o = np.array([[1, 0], [-self.p_o / self.n, self.n_L / self.n]])
        # else:
        #     raise ValueError("請提供焦距 f 或 (r_i, r_o) 來建立透鏡")

        self.MT = np.array([[1, self.D], [0, 1]])
        self.M_Len = self.MT.dot(self.MR_i)



x_ = incident_light(height=1, angle=1)
M_Len_1 = M_Len(n=1, n_L=1.5, r_i=15)

print(f'練習題2答案：{np.rad2deg(M_Len_1.MR_i.dot(x_)[1]):.3f} deg.')
print('='*20)

# 練習題3
n_2 = 1
n_L2 = 1.5
R_1 = 10
R_2 = -10

print(f'練習題3答案：\n{M_Len(n_2, n_L2, R_1, R_2).M_Len}')
print('='*20)

# 練習題4
x_ = incident_light(height=0, angle=1, dimension=False)
air_1 = M_Len(n=1, n_L=1, D=120)
air_2 = M_Len(n=1, n_L=1, D=220)
air_3 = M_Len(n=1, n_L=1, D=150)
M_Len_1 = M_Len(n=1, n_L=1.5, f=100)
M_Len_2 = M_Len(n=1, n_L=1.5, f=80)

x_1 = air_3.MT.dot(M_Len_2.M_Len.dot(air_2.MT.dot(M_Len_1.M_Len.dot(air_1.MT.dot(x_)))))
# print(x_)
# print(f'M_Len_1.M_Len:\n{M_Len_1.M_Len}')
# print(f'M_Len_2.M_Len:\n{M_Len_2.M_Len}')
print(f"HW1答案：\nx = {x_1[0]:.2f}\nalpha = {x_1[1]:.2f}")