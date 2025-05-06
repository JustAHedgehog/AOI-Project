import cv2
import numpy as np


def main():
    tmp = []
    cap = cv2.VideoCapture(r'Source\viewFromME_video1.mp4')
    ret_1, img_1 = cap.read()  # 讀取影像
    cv2.waitKey(600)
    ret_2, img_2 = cap.read()
    while True:
        diff = cv2.absdiff(img_1, img_2)  # 找出差異
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # 灰階
        blur = cv2.GaussianBlur(gray, (5, 5), 0)  # 設定kernal大小為(5,5)，標準差為2
        # 調整二值化範圍大於10變成250，其餘變為0
        a, thresh = cv2.threshold(blur, 10, 250, cv2.THRESH_BINARY)
        kernel = np.ones([3, 3])
        eroded = cv2.erode(thresh, kernel, iterations=1)  # 侵蝕以濾除小雜訊
        dilated = cv2.dilate(eroded, kernel, iterations=5)  # 擴張以將相近的區域連接
        contours, _ = cv2.findContours(
            dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 找輪廓
        for i in contours:
            x, y, w, h = cv2.boundingRect(i)
            if cv2.contourArea(i) < 1000:  # 過濾掉小的輪廓
                continue
            cv2.rectangle(img_1, (x, y), (x+w, y+h), (0, 0, 255), 2)
            cv2.imshow('bounding box', img_1)
        # 寫在迴圈外以保障永遠更新影像做計算
        img_1 = img_2.copy()
        cv2.waitKey(20)
        ret_2, img_2 = cap.read()
        # 按下q鍵提早結束
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
