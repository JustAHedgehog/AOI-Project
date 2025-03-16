import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    img = cv2.imread('Week10_hw\coinOnDesk_lowC.jpg') #讀取圖像
    
    cv2.imshow('original image', img)
    equ_B = cv2.equalizeHist(img[:,:,0]) #分別針對三個通道增加對比度
    equ_G = cv2.equalizeHist(img[:,:,1]) 
    equ_R = cv2.equalizeHist(img[:,:,2]) 
    histgray_B = cv2.calcHist([img[:,:,0]], [0], None, [256], [0,256]) #計算直方圖每個bin值
    histgray_G = cv2.calcHist([img[:,:,1]], [0], None, [256], [0,256])
    histgray_R = cv2.calcHist([img[:,:,2]], [0], None, [256], [0,256]) 
    histequ_B = cv2.calcHist([equ_B], [0], None, [256], [0,256]) 
    histequ_G = cv2.calcHist([equ_G], [0], None, [256], [0,256]) 
    histequ_R = cv2.calcHist([equ_R], [0], None, [256], [0,256])
    img_ = cv2.merge((equ_B, equ_G, equ_R)) #將三通道疊加 
    cv2.imshow('equ image', img_) #顯示增加對比度後的圖片
    plt.subplot(2,1,1)
    plt.bar(range(0,256), histgray_B[:,0], color='blue') #直方圖
    plt.bar(range(0,256), histgray_G[:,0], color='blue')
    plt.bar(range(0,256), histgray_R[:,0], color='blue')
    plt.subplot(2,1,2)
    plt.bar(range(0,256), histequ_B[:,0], color='blue')
    plt.bar(range(0,256), histequ_G[:,0], color='blue')
    plt.bar(range(0,256), histequ_R[:,0], color='blue')
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()