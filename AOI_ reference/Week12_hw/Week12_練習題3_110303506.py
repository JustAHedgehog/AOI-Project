#A(0,0), B(1,1), C(2,2), D(3,3), E(2,3), F(4,4), G(6,5)
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = [0,1,2,3,2,4,6]
    y = [0,1,2,3,3,4,5]
    q = np.linspace(-np.pi/2,np.pi/2,300)
    R = np.linspace(-10,10,500)
    dR = (max(R)-min(R))/len(R)

    for Q in q:
        r_0= x[0]*np.cos(Q)+y[0]*np.sin(Q)
        r_1= x[1]*np.cos(Q)+y[1]*np.sin(Q)
        r_2= x[2]*np.cos(Q)+y[2]*np.sin(Q)
        r_3= x[3]*np.cos(Q)+y[3]*np.sin(Q)
        r_4= x[4]*np.cos(Q)+y[4]*np.sin(Q)
        r_5= x[5]*np.cos(Q)+y[5]*np.sin(Q)
        r_6= x[6]*np.cos(Q)+y[6]*np.sin(Q)
        box = []
        for i in R:
            if r_0>i and r_0<i+dR:
                box.append('A')
            if r_1>i and r_1<i+dR:
                box.append('B')
            if r_2>i and r_2<i+dR:
                box.append('C')
            if r_3>i and r_3<i+dR:
                box.append('D')
            if r_4>i and r_4<i+dR:
                box.append('E')
            if r_5>i and r_5<i+dR:
                box.append('F')
            if r_6>i and r_6<i+dR:
                box.append('G')
            if len(box)==3 or len(box)==5 : #找出共線的點
                print(box)
            else:
                box = []
if __name__=='__main__':
    main()