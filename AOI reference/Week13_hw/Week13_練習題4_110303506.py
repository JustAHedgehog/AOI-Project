from Week13_練習題2_110303506 import findMarker
import numpy as np
import cv2

def main():
    w = 12; p = -1.0; d = 50; D = 0
    f = p*d/w
    cap = cv2.VideoCapture('Week13_hw/cam_f_Calibration_d_Meas.mp4')
    ret, img = cap.read()
    while ret:
        cnt_max = findMarker(img)
        rect = cv2.minAreaRect(cnt_max)
        box = np.int0(cv2.boxPoints(rect))
        cv2.drawContours(img, [box], 0, (0,0,255), 2)
        txt_f = f'focal length={np.round(f,1)}'
        cv2.putText(img, txt_f, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)
        txt_d = f'D={np.round(D,1)}'
        cv2.putText(img, txt_d, (1000,650), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1, cv2.LINE_AA)
        cv2.imshow('result', img)
        ret, img = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(10) & 0xFF == ord('c'):
            p = rect[1][0]
            f = p*d/w
        p = rect[1][0]
        D = f*w/p
    cap.release()
    cv2.destroyAllWindows()
if __name__=='__main__':
    main()