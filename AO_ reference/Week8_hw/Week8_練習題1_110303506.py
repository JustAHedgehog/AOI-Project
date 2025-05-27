import cv2
import numpy as np

def main():
    img = np.full((300, 300, 3), (255, 255, 255), np.uint8) #創建300x300的白色畫布
    t = np.linspace(0, 2*np.pi, 300)
    x = 150+100*np.cos(t) #圓參數式
    y = 150+100*np.sin(t)
    img[np.uint16(x), np.uint16(y), :] =(255,0,0) #畫圓
    cv2.imshow("img", img)
    key=cv2.waitKey(0)

if __name__=='__main__':
    main()

