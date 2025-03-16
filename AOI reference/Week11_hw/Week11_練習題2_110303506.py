import cv2
import numpy as np

def main():
    img = cv2.imread('Week11_hw\img_dilate_google0424.jpg') #讀檔
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#灰階
    cv2.imshow('import', img)
    a, thr = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV) #二值化
    cv2.imshow('import_2', thr)
    kernel = np.ones([4,4])
    dilated = cv2.dilate(thr, kernel, iterations=3)#擴張
    contours, a = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0,0,255),2)
    print(len(contours))
    cv2.imshow('test_', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()