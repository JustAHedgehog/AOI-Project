import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(0)
    # cap = cv2.VideoCapture(r'week_10\motionPattern_0506.MOV')
    ret_1, img_1 = cap.read()  # 讀取影像
    cv2.waitKey(600)
    ret_2, img_2 = cap.read()
    while True:
        diff = cv2.absdiff(img_1, img_2)  # 計算差異
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # 灰階
        blur = cv2.GaussianBlur(gray, (5, 5), 0)  # 設定kernal大小為(5,5)，標準差為2
        # 調整二值化範圍大於20變成255，其餘變為0
        a, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
        b = np.where(thresh == 255)  # 找到二值化圖像中像素值為255的位置
        if b[0].size == 0:
            print('no motion')
        else:
            Y = int(np.average(b[0]))
            X = int(np.average(b[1]))
            cv2.circle(img_1, (X, Y), 10, (255, 0, 0), 5)  # 標記藍色圓圈
            cv2.imshow('diff', img_1)
        # 寫在迴圈外以保障永遠更新影像做計算
        img_1 = img_2.copy()
        cv2.waitKey(20)
        ret_2, img_2 = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
