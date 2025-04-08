import cv2
import numpy as np

def main():
    img=cv2.imread(r'Source\Lenna.png') #讀影像
    cv2.imshow("orginal_image",img) #顯示調整前影像
    center=(100,100) #圓心座標
    radius=60 #圓半徑
    cv2.circle(img, center, radius, (255,0,0), 0) #畫圓中心在(50,50)
    corner1 = (int(np.round(center[0] - radius * (1 / np.sqrt(2)))), int(np.round(center[1] - radius * (1 / np.sqrt(2)))))
    corner2 = (int(np.round(center[0] + radius * (1 / np.sqrt(2)))), int(np.round(center[1] + radius * (1 / np.sqrt(2)))))
    cv2.rectangle(img, corner1, corner2, (255,0,0), 1) #畫正方形
    cv2.imshow("modified_image",img) #顯示調整後圖片
    cv2.imwrite(r"D:\AOI-Project\week_8\lena_1.jpg", img) #存檔
    key=cv2.waitKey(0)

if __name__=='__main__':
    main()
