import cv2
import numpy as np

def main():
    # 設定初始參數
    w = 26  # 矩形實際邊長(mm)
    p = -1.0  # 目標於螢幕中寬度(pixel)
    d = 450  # 圖像與相機距離(mm)
    f = p*d/w
    cap = cv2.VideoCapture(r'week_13\movingCoin.wmv')
    ret, img = cap.read()
    dim = (img.shape[1]//2, img.shape[0]//2)  # 將影像大小縮小一半，(334,236)
    while ret:
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        eroded = cv2.erode(blur, np.ones((3, 3), np.uint8), iterations=10) # 腐蝕以去除文字雜訊
        dilaed = cv2.dilate(eroded, np.ones((3, 3), np.uint8), iterations=10) # 膨脹以復原
        circles = cv2.HoughCircles(dilaed, cv2.HOUGH_GRADIENT, 1, 100, param1=90, param2=10, minRadius=20, maxRadius=25)
        if circles is not None: 
            circles = np.uint16(np.around(circles))  # 將圆心及半徑轉換成整數
            c = circles[0][0]
            cv2.circle(img, (c[0], c[1]), c[2], (0, 0, 255), 2)  # 在圓形處畫圓
            if cv2.waitKey(10) & 0xFF == ord('c'): # 按下c鍵進行校正
                p = c[2] # 更新pixel
                f = p*d/w # 更新成當下的焦距
            # 按下c鍵進行校正
            txt_c = 'press c to calibrate focal length'
            cv2.putText(img, txt_c, (250,450), cv2.FONT_HERSHEY_SIMPLEX,
                        0.8, (255, 255, 255), 2, cv2.LINE_AA)
            # 顯示園心的螢幕座標(x,y,z)
            txt = f'c({c[0]}, {c[1]}, {np.round(f,1)})px'
            cv2.putText(img, txt, (300,50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 0, 255), 2, cv2.LINE_AA)
        # 按下q鍵退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        txt_p = 'press q to exit'
        cv2.putText(img, txt_p, (470,400), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('result', img)
        ret, img = cap.read()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()