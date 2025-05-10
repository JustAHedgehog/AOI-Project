import cv2
import numpy as np


def main():
    img = cv2.imread(r'week_11\rice-shaded.tif')  # 讀檔
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階以利二值化
    a, thr = cv2.threshold(gray, 123, 255, cv2.THRESH_BINARY)  # 二值化以利找輪廓
    cv2.imshow('threshold', thr)

    kernel = np.ones((3,3))
    eroded = cv2.erode(thr, kernel, iterations=5) # 先侵蝕將雜訊去除
    cv2.imshow('eroded', eroded)
    dilated = cv2.dilate(eroded, kernel, iterations=5) # 再透過擴張將侵蝕的部分補回來
    cv2.imshow('eroded', dilated)
    contours, _ = cv2.findContours(
        thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 找所有輪廓
    cv2.drawContours(img, contours, -1, (0, 0, 255), 2) # 畫出所有硬幣的輪廓
    print(f'Number of contours = {len(contours)}')
    cv2.imshow('google', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()