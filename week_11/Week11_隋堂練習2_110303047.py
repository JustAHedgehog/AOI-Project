import cv2
import numpy as np
def main():
    img = cv2.imread(r'week_11\ebay.png') # 讀取灰階圖片
    cv2.imshow('import', img) # 顯示原圖
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    a, thr = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY) # 二值化
    contours,_ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 找輪廓
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2) # 在原本圖上畫出輪廓
    print(f'Number of contours = {len(contours)}') # 輸出輪廓數量以確認成功與否
    cv2.imshow('contours', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()