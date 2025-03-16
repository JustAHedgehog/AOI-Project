import math as m
def distance(x_1,y_1,x_2,y_2):
    a=m.sqrt(pow((x_2-x_1),2)+pow((y_2-y_1),2))
    return a


x_1=float(input("please input x_1:"))
y_1=float(input("please input y_1:"))
x_2=float(input("please input x_2:"))
y_2=float(input("please input y_2:"))

d=distance(x_1,y_1,x_2,y_2)
print('{:.2f}'.format(d))
