import cv2
import numpy as np

def main():
    img=cv2.imread('Week7_hw/Lenna.png') #讀影像
    cv2.imshow("orginal_image",img) #顯示調整前影像
    cv2.circle(img, (50,50), 40, (255,0,0), 0) #畫圓中心在(50,50)
    cv2.rectangle(img, (22,22), (78,78), (255,0,0), 1) #畫正方形
    cv2.imshow("modified_image",img) #顯示調整後圖片
    cv2.imwrite("C:/Users/lisan/Desktop/SHIUAN/AOI/Week8_hw/lenna.jpg", img) #存檔
    key=cv2.waitKey(0)

if __name__=='__main__':
    main()

