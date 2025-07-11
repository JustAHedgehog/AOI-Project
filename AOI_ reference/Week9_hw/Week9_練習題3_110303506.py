import numpy as np 
import cv2 

def main():

    img = cv2.imread('Week9_hw\coinOnDesk.jpg', 0) #讀影像
    rows, cols = img.shape #計算座標
    # cv2.circle(img, (cols, rows), 20, (0,0,255),-1) 
    cv2.circle(img, (105, 125), 5, (0,0,255),2) #畫圓點
    cv2.circle(img, (433, 125), 5, (0,0,255),2)
    cv2.circle(img, (35, 305), 5, (0,0,255),2)
    cv2.circle(img, (535, 305), 5, (0,0,255),2)

    s = np.array([[105,125],[433,125], [35,305], [535,305] ], np.float32) #原本的點
    d = np.array([[90,35],[435,35], [90,320], [435,320] ], np.float32) #轉換的點
    p = cv2.getPerspectiveTransform(s,d) #轉換
    r = cv2.warpPerspective(img, p, (cols,rows))
    cv2.imshow('test', img) #原本影像
    cv2.imshow('r', r) #轉換後影像
    key = cv2.waitKey(0)

if __name__ == '__main__':
    main()