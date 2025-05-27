import cv2
import numpy as np


def findMarker(image):  # 找出畫面中最大的輪廓
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thr = cv2.threshold(blur, 150, 250, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(
        thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key=cv2.contourArea)
    return cnt_max


def axis(w, h, image):  # 畫出x軸和y軸
    cv2.circle(image, (int(w / 2), int(h / 2)), 7, (0, 255, 0), -1)  # 畫出圓心
    cv2.line(image, (0, int(h / 2)), (w, int(h / 2)), (0, 255, 0), 2)
    cv2.line(image, (int(w / 2), 0), (int(w / 2), h), (0, 255, 0), 2)


def obj_center(x, y, w, h, image):
    cv2.circle(image, (x, y), 5, (0, 0, 255), -1)  # 畫出圓心
    cv2.line(image, (int(w / 2), int(h / 2)),
             (x, y), (0, 0, 255), 2)  # 圓心到原點的連線
    cv2.line(image, (x, y), (x, int(h / 2)), (0, 0, 255), 2)  # 圓心到x軸的連線
    cv2.line(image, (x, y), (int(w / 2), y), (0, 0, 255), 2)  # 圓心到y軸的連線


def puttxt(image, key, value, pos_x, pos_y):  # 在影像上放置文字
    text = f'{key} = {np.round(value, 1)}'
    cv2.putText(image, text, (pos_x, pos_y),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)


def main():
    # 設定初始參數
    w = 12  # 矩形實際邊長(cm)
    p = -1.0  # 矩形螢幕寬度(pixel)
    d = 50  # 圖像與相機距離(cm)
    f = p*d/w
    D = 0  # 即時量測距離(cm)

    cap = cv2.VideoCapture(r'week_14\motionPattens3.mov')
    ret, img = cap.read()
    while ret:
        half_h, half_w = img.shape[0]//2, img.shape[1]//2
        img = cv2.resize(img, (half_w, half_h))  # 調整影像大小以適應視窗
        cnt_max = findMarker(img)  # 找出畫面中最大輪廓
        rect = cv2.minAreaRect(cnt_max)  # 計算該輪廓的最小外接矩形
        box = np.intp(cv2.boxPoints(rect))
        cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
        obj_center(int(rect[0][0]), int(rect[0][1]), half_w, half_h, img)
        x_ = np.rad2deg(np.arctan((rect[0][0] - half_w / 2) / f))
        y_ = np.rad2deg(np.arctan(-(rect[0][1] - half_h / 2) / f))
        puttxt(img, 'f', f, 50, 350)
        puttxt(img, 'D', D, 50, 400)
        puttxt(img, 'Vx', x_, 50, 450)
        puttxt(img, 'Vy', y_, 50, 500)
        axis(half_w, half_h, img)  # 最後再畫出座標軸以避免輪廓誤判
        cv2.imshow('result', img)
        ret, img = cap.read()  # 因為這邊的img是從cap.read()讀取的，所以要在這邊更新img

        if cv2.waitKey(10) & 0xFF == ord('c'):  # 按下c鍵進行校正
            p = rect[1][0]  # 校正後的pixel
            f = p*d/w  # 更新成當下的焦距
        p = rect[1][0]  # 抓取當前pixel
        D = f*w/p  # 量測現在距離

        if cv2.waitKey(1) & 0xFF == ord('q'):  # 按下q鍵提早結束
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
