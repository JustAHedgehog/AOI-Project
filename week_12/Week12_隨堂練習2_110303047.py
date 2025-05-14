import cv2
import numpy as np


def main():
    cap = cv2.VideoCapture('coin.mp4')
    ret, img_1 = cap.read()  # 讀取影像
    # cv2.waitKey(40)
    ret_2, img_2 = cap.read()
    while True:
        gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(img_1, 5)
        edges = cv2.Canny(gray, 100, 250)
        circles = cv2.HoughCircles(
            edges, cv2.HOUGH_GRADIENT, 1, 100, param1=250, param2=25, minRadius=10, maxRadius=100)

        if circles is not None:  # 避免偵測不到圓而當機
            circles = np.int16(np.around(circles))
            c = circles[0]
            c = sorted(c, key=lambda c:c[2], reverse=True)
            c_top = c[:2]
            if len(c_top) == 2:
                x_0, y_0, r_0 = c_top[0]
                x_1, y_1, r_1 = c_top[1]
                cv2.circle(img_1, (x_0, y_0), r_0, (0, 0, 255), 2)
                cv2.circle(img_1, (x_1, y_1), r_1, (0, 0, 255), 2)
                cv2.line(img_1, (x_0, y_0), (x_1, y_1), (0, 0, 255), 2)
                dis = np.sqrt(float(x_1-x_0)**2+float(y_1-y_0)**2)
                print(np.around(dis,1))
                txt = f'distance={np.around(dis, 1):.1f} px' # 顯示至小數點後第一位
                cv2.putText(img_1, txt, (0, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            0.8, (255, 0, 0), 2, cv2.LINE_AA)  # 於左上角顯示距離
        cv2.imshow('result', img_1)
        img_1 = img_2.copy()
        # cv2.waitKey(0)
        ret_2, img_2 = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按下q鍵退出
            break
    cap.release()
    cv2.destroyAllWindows()
    print(c)


if __name__ == '__main__':
    main()
