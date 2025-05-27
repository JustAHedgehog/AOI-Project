import cv2
import numpy as np
from Week13_練習題2_110303047 import findMarker


def main():
    # 設定初始參數
    w = 12  # 矩形實際邊長(cm)
    p = -1.0  # 矩形螢幕寬度(pixel)
    d = 50  # 圖像與相機距離(cm)
    f = p*d/w
    D = 0  # 即時量測距離(cm)
    cap = cv2.VideoCapture(r'Week_13/cam_f_Calibration_d_Meas.mp4')
    ret, img = cap.read()  # img.shape: (720, 1280, 3)
    height, width = img.shape[0], img.shape[1]
    Cen_X, Cen_Y = width//2, height//2
    while ret:
        cv2.line(img, (0, Cen_Y), (width, Cen_Y), (0, 255, 0), 2)  # 畫出x軸
        cv2.line(img, (Cen_X, 0), (Cen_X, height), (0, 255, 0), 2)  # 畫出y軸
        cv2.circle(img, (Cen_X, Cen_Y), 10, (0, 255, 0), -1)  # 畫出原點
        cnt_max = findMarker(img)  # 找出畫面中最大輪廓
        rect = cv2.minAreaRect(cnt_max)  # 計算該輪廓的最小外接矩形
        box = np.intp(cv2.boxPoints(rect))
        cv2.drawContours(img, [box], 0, (0, 255, 0), 2)  # 畫出最小外接矩形
        cv2.circle(img, (int(rect[0][0]), int(
            rect[0][1])), 5, (255, 0, 0), -1)  # 畫出輪廓的圓心
        cv2.line(img, (Cen_X, Cen_Y),
                 (int(rect[0][0]), int(rect[0][1])), (0, 0, 255), 2) # 畫出圓心到原點的連線
        cv2.line(img, (int(rect[0][0]), int(
            rect[0][1])), (int(rect[0][0]), Cen_Y), (0, 0, 255), 2) # 畫出圓心到x軸的連線
        cv2.line(img, (int(rect[0][0]), int(
            rect[0][1])), (Cen_X, int(rect[0][1])), (0, 0, 255), 2) # 畫出圓心到y軸的連線
        txt_f = f'focal length={np.round(f, 1)}'
        cv2.putText(img, txt_f, (50, 100), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 1, cv2.LINE_AA)
        txt_d = f'D={np.round(D, 1)}'
        cv2.putText(img, txt_d, (1000, 650), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imshow('result', img)
        ret, img = cap.read()  # 因為這邊的img是從cap.read()讀取的，所以要在這邊更新img
        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按下q鍵提早結束
            break
        if cv2.waitKey(10) & 0xFF == ord('c'): # 按下c鍵進行校正
            p = rect[1][0] # 校正後的pixel
            f = p*d/w # 更新成當下的焦距
        p = rect[1][0] # 抓取當前pixel
        D = f*w/p # 量測現在距離

        # 在畫面上顯示物體的圓心座標
        txt_c = f'obj center=({np.round(rect[0][0], 1)}, {np.round(rect[0][1], 1)}, {np.round(D, 1)})'
        cv2.putText(img, txt_c, (50, 650), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 1, cv2.LINE_AA)
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
