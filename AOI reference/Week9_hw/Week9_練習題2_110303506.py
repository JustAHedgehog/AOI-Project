import cv2
import numpy as np

def main():

    img = cv2.imread('Week7_hw\Lenna.png') #讀取影像
    rows, cols = img.shape[:2] #計算座標
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1) #中心旋轉45度的旋轉矩陣
    dst = cv2.warpAffine(img, M, (cols, rows)) #旋轉
    cv2.imshow('test', dst) #顯示結果
    key = cv2.waitKey()

if __name__=='__main__':
    main()

