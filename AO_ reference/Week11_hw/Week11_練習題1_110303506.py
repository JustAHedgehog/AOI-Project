import cv2
import numpy as np

def main():
    img = cv2.imread('Week11_hw\circles.jpg', 0) #讀檔
    cv2.imshow('import', img)
    kernel = np.ones((3,3))
    dilated = cv2.dilate(img, kernel, iterations=10)#擴張
    eroded = cv2.erode(dilated, kernel, iterations=16)#侵蝕
    cv2.imshow('test_', eroded)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()