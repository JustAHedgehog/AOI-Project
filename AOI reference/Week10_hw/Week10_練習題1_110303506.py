import cv2
import numpy as np
import random

def main():
    img = cv2.imread('Week7_hw\Lenna.png',0) #讀取圖片
    shape = img.shape
    print(shape)
    noise = 2000 #加入雜訊
    for i in range(noise):
        i = random.randint(0,shape[0]-1)
        j = random.randint(0,shape[1]-1)
        if (len(shape)==2):
            img.itemset((i,j), 0)
        else:
            img.itemset((i,j,0), 0)
            img.itemset((i,j,1), 0)
            img.itemset((i,j,2), 0)
    cv2.imshow('OriginalImage',img)
    cv2.imwrite('Week10_hw/lenna.jpg',img)
    img_1 = cv2.imread('Week10_hw/lenna.jpg',0) #讀雜訊圖片

    dst_1 = cv2.medianBlur(img_1,5) #medium filter
    dst_2 = cv2.GaussianBlur(img_1,(5,5),1,1) #gaussian filter
    cv2.imshow('MediumFilter',dst_1)
    cv2.imshow('GaussianFilter',dst_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()