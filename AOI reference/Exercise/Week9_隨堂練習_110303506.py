import cv2
import numpy as np


img=cv2.imread('E:/NCU/book.jpg')
cv2.imshow('test',img)
print(img.shape)
rows, cols = img.shape[:2] #計算座標
s = np.array([[14,128],[182,120], [126,356], [320,296] ], np.float32) #原本的點
d = np.array([[0,0],[343,0], [0,610], [343,610] ], np.float32) #轉換的點
p = cv2.getPerspectiveTransform(s,d) #轉換
r = cv2.warpPerspective(img, p, (cols,rows))
cv2.imshow('r',r)
key = cv2.waitKey(0)
