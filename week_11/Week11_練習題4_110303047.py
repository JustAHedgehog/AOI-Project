import cv2
import numpy as np


def main():
    img = cv2.imread(r'Source\img_dilate_google0424.jpg')  # 讀檔
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階以利二值化
    a, thr = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)  # 二值化以利找輪廓
    contours, a = cv2.findContours(
        thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 找所有輪廓
    # 針對每個輪廓畫出外圍矩形
    for i in contours:
        x, y, w, h = cv2.boundingRect(i)
        cv2.rectangle(img, (x, y), (x+w, y+h), (np.random.randint(0, 255),
                      np.random.randint(0, 255), np.random.randint(0, 255)), 2)
        cv2.imshow('google', img)
        cv2.waitKey(500)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
