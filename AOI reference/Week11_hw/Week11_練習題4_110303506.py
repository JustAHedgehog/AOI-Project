import cv2
import numpy as np
import random as rd

def main():
    img = cv2.imread('Week11_hw\img_dilate_google0424.jpg') #讀檔
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#灰階
    # cv2.imshow('import', img)
    a, thr = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV) #二值化
    # cv2.imshow('import_2', thr)
    # kernel = np.ones([4,4])
    # dilated = cv2.dilate(thr, kernel, iterations=3)#擴張
    contours, a = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #找輪廓
    # print(contours)
    for i in contours:
        x,y,w,h = cv2.boundingRect(i)
        cv2.rectangle(img, (x,y), (x+w, y+h), (rd.randint(0,255), rd.randint(0,255), rd.randint(0,255)), 2)
        cv2.imshow('google', img)
        cv2.waitKey(500)
    # cv2.drawContours(img, contours, -1, (0,0,255),2)
    # cv2.imshow('test_', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()