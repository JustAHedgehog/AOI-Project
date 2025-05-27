import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture('Week10_hw/motionPattern_0506.MOV')
    ret, img_1 = cap.read() #讀取影像
    cv2.waitKey(1000)
    ret, img_2 = cap.read()
    diff = cv2.absdiff(img_1, img_2) #計算差異
    cv2.imshow('test', diff) #顯示圖像
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) #灰階
    blur = cv2.GaussianBlur(gray, (3,3), 2) #設定kernal大小為(3,3)，標準差為2
    a, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) #調整二值化範圍大於20變成255，其餘變為0
    # b = np.where(thresh==255)
    # Y = int(np.average(b[0]))
    # X = int(np.average(b[1]))
    # cv2.circle(img_1, (X,Y), 10,(255,0,0), 5)
    cv2.imwrite('C:/Users/user/Desktop/Week10_練習題6_110303506.jpg', thresh) #存檔
    cv2.imshow('diff', thresh)
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()