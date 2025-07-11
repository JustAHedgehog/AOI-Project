import cv2
import numpy as np

def main():
    img = cv2.imread('E:/NCU/rice-shaded.tif') #讀檔
    cv2.imshow('import', img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#灰階
    # blur = cv2.GaussianBlur(gray, (3,3), 0) #設定kernal大小為(3,3)，標準差為2
    a, thr = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY) #二值化
    cv2.imshow('thr', thr)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    dilated = cv2.dilate(thr, kernel, iterations=3)#擴張
    eroded = cv2.erode(dilated, kernel, iterations=8)#侵蝕
    cv2.imshow('ed', eroded)
    # cv2.imshow('test_', eroded)
    contours, a = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0,0,255),2)

    cv2.putText(img, 'count:'+str(len(contours)), (300,300), cv2.FONT_HERSHEY_COMPLEX, 2,(255,0,0))
    cv2.imshow('test_', img)
    print(len(contours))
    print(img.shape)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()