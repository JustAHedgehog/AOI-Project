import numpy as np
import cv2





def main():
    img = np.full((300,300,3),(255,255,255), np.uint8) #創建畫布

    #創建正方形
    cv2.rectangle(img, (0,0), (150,150), (0,0,0), -1)
    cv2.rectangle(img, (150,0), (300,150), (255,0,0), -1)
    cv2.rectangle(img, (0,150), (150,300), (0,255,0), -1)
    cv2.rectangle(img, (150,150), (300,300), (0,255,255), -1)
    cv2.rectangle(img, (75,75), (225,225), (255,255,255),3) #線寬=3
    
    #創建圓形
    cv2.circle(img, (150,150), 75, (50,150,200), -1)

    #創建菱形
    cv2.line(img, (150,75), (75,150), (255,255,255), 3)
    cv2.line(img, (150,75), (225,150), (255,255,255), 3)
    cv2.line(img, (225,150), (150,225), (255,255,255), 3)
    cv2.line(img, (150,225), (75,150), (255,255,255), 3)

    #橢圓
    cv2.ellipse(img, (150,150), (65,35), 0,0,360,3)
    cv2.imshow("img", img)
    key=cv2.waitKey(0)



if __name__=='__main__':
    main()