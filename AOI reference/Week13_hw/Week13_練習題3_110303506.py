from Week13_練習題2_110303506 import findMarker
import numpy as np
import cv2
def main():
    cap = cv2.VideoCapture('Week13_hw/motionPattens3.mov')
    ret, img = cap.read()
    while ret:
        cnt_max = findMarker(img)
        # cv2.drawContours(img, [cnt_max], 0, (0,0,255), 5)
        rect = cv2.minAreaRect(cnt_max)
        box = np.int0(cv2.boxPoints(rect))
        cv2.drawContours(img, [box], 0, (0,0,255), 2)
        txt = f'width={int(rect[1][1])}'
        cv2.putText(img, txt, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)
        cv2.imshow('result', img)
        ret, img = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__=='__main__':
    main()