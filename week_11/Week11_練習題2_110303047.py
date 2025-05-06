import cv2
import numpy as np
def main():
    img = cv2.imread(r'Source\img_dilate_google0424.jpg', 0) # 讀取灰階圖片
    cv2.imshow('import', img) # 顯示原圖
    a, thr = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV) # 二值化
    kernel = np.ones((3, 3), np.uint8) # 定義結構元素
    dilated = cv2.dilate(thr, kernel, iterations=6) # 擴張使輪廓互相交集，減少輪廓數
    cv2.imshow('dilated', dilated) # 顯示擴張後的圖片
    contours,_ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 找輪廓
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2) # 在原本圖上畫出輪廓
    print(f'Number of contours = {len(contours)}') # 輸出輪廓數量以確認成功與否
    cv2.imshow('contours', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()