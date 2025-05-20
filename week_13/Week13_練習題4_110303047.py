from Week13_練習題2_110303047 import findMarker
import numpy as np
import cv2


def main():
    # 設定初始參數
    w = 12  # 矩形實際邊長(cm)
    p = -1.0  # 矩形螢幕寬度(pixel)
    d = 50  # 圖像與相機距離(cm)
    f = p*d/w
    D = 0  # 即時量測距離(cm)
    cap = cv2.VideoCapture(r'Week_13/cam_f_Calibration_d_Meas.mp4')
    ret, img = cap.read()
    while ret:
        cnt_max = findMarker(img)  # 找出畫面中最大輪廓
        rect = cv2.minAreaRect(cnt_max)  # 計算該輪廓的最小外接矩形
        box = np.intp(cv2.boxPoints(rect))
        cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
        # 在畫面上顯示焦距
        txt_f = f'focal length={np.round(f, 1)}'
        cv2.putText(img, txt_f, (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 1, cv2.LINE_AA)
        # 在畫面上及時顯示測量距離
        txt_d = f'D={np.round(D, 1)}'
        cv2.putText(img, txt_d, (1000, 650), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('result', img)
        if cv2.waitKey(1) & 0xFF == ord('q'): # 按下q鍵結束
            break
        if cv2.waitKey(10) & 0xFF == ord('c'):  # 按下c鍵進行校正
            p = rect[1][0]  # 校正後的pixel
            f = p*d/w # 更新成當下的焦距
        p = rect[1][0]  # 抓取當前pixel
        D = f*w/p  # 量測現在距離
        ret, img = cap.read()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
