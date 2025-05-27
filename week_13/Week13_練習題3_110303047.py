import cv2
import numpy as np
from Week13_練習題2_110303047 import findMarker

def main():
    cap = cv2.VideoCapture(r'week_13\motionPattens3.mov')
    ret, img = cap.read()
    while ret:
        max_contour = findMarker(img)
        rect = cv2.minAreaRect(max_contour)
        box = np.intp(cv2.boxPoints(rect)) # 找出最小外接矩形，因為int0已停用，故更改為intp
        cv2.drawContours(img, [box], 0, (0, 255, 0), 2)
        txt = f'width={int(rect[1][1])}'
        cv2.putText(img, txt, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)
        cv2.imshow('result', img)
        ret, img = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'): # 按下q鍵提早結束
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    