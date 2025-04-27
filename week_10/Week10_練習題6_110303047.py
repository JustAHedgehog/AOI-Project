import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture(r'Source\motionPattern_0506.MOV')
    ret, frame1 = cap.read()  # 讀取影像
    cv2.waitKey(1000)
    ret, frame2 = cap.read()
    diff = cv2.absdiff(frame1, frame2)  # 計算前後圖像差異
    cv2.imshow('before', diff)  # 顯示有變化的部分圖像
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)  # 灰階
    blur = cv2.GaussianBlur(gray, (3, 3), 2)  # 設定kernal大小為(3,3)，標準差為2
    # 調整二值化範圍大於20變成255，其餘變為0
    a, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    cv2.imshow('after', thresh)
    cv2.imwrite(r'week_10\threshed.jpg', thresh)  # 存檔，其中檔名不可含有中文（會無法儲存）
    b = np.where(thresh == 255)
    Y = int(np.average(b[0])) # 因無設定權重，也可以使用np.mean(b[0])
    X = int(np.average(b[1]))
    cv2.circle(frame1, (X, Y), 10, (255, 0, 0), 5)
    cv2.imshow('move_center', frame1)  # 顯示圓圈的影像
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
