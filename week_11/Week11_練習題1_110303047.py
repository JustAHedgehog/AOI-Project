import cv2
import numpy as np

def main():
    # 讀取circles.jpg的灰階圖片，以利後續雜訊處理
    img = cv2.imread(r'week_11\circles.jpg', 0)
    cv2.imshow('original', img)

    # 設定核函數進行雜訊處理
    kernel = np.ones((3,3))
    eroded = cv2.erode(img, kernel, iterations=6) # 先侵蝕將雜訊去除
    cv2.imshow('eroded', eroded)
    dilated = cv2.dilate(eroded, kernel, iterations=6) # 再透過擴張將侵蝕的部分補回來
    cv2.imshow('dilated', dilated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
