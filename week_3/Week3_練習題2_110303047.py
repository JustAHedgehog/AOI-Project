"""
Subject: 計算兩點距離
"""
import math

print("請輸入兩點座標")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("兩點距離: {:.2f}".format(distance))