import cv2
import numpy as np

def main():
    tmp=[]
    cap = cv2.VideoCapture('Week11_hw/viewFromME_video1.mp4')
    ret, img_1 = cap.read() #讀取影像
    ret_2, img_2 = cap.read()
    while True:
        diff = cv2.absdiff(img_1, img_2) #計算差異
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) #灰階
        blur = cv2.GaussianBlur(gray, (3,3), 0) #設定kernal大小為(3,3)，標準差為2
        a, thresh = cv2.threshold(blur, 10, 250, cv2.THRESH_BINARY) #調整二值化範圍大於10變成250，其餘變為0
        kernel = np.ones([3,3])
        eroded = cv2.erode(thresh, kernel, iterations=7) #侵蝕
        dilated = cv2.dilate(eroded, kernel, iterations=16) #擴張
        contours, a = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #找輪廓
        for i in contours:
             for i in contours:
                x,y,w,h = cv2.boundingRect(i)
                cv2.rectangle(img_1, (x,y), (x+w, y+h), (0,0,255), 2)
                cv2.imshow('test', img_1)
        img_1 = img_2.copy()
        cv2.waitKey(20)
        ret_2, img_2 = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()