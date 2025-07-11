import cv2
import numpy as np

# 撰寫findMarker函數以獲取該影像中最大的輪廓
def findMarker(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    thr = cv2.adaptiveThreshold(blur, 197, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,2)
    contours, _ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key=cv2.contourArea)
    return cnt_max
    
def calibration(w=14,p=-1,d=50,cap=cv2.VideoCapture(r'week_13\motionPattens3.mov')):
    f = p*d/w
    D = 0
    ret, img = cap.read()
    while ret:
        cnt_max = findMarker(img)
        rect = cv2.minAreaRect(cnt_max)
        box = np.intp(cv2.boxPoints(rect)) # 找出最小外接矩形，因為int0已停用，故更改為intp
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
        ret, img = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'): # 按下q鍵提早結束
            break
        if cv2.waitKey(10) & 0xFF == ord('c'):  # 按下c鍵進行校正
            p = rect[1][0]  # 校正後的pixel
            f = p*d/w # 更新成當下的焦距
        p = rect[1][0]  # 抓取當前pixel
        D = f*w/p  # 量測現在距離
    cap.release()
    cv2.destroyAllWindows()
    return f  # 回傳焦距

if __name__ == "__main__":
    calibration()
