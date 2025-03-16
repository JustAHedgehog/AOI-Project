import cv2
import numpy as np

def findMarker(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    a, thr = cv2.threshold(blur, 150,250, cv2.THRESH_BINARY_INV)
    contours,_ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key = cv2.contourArea)
    return cnt_max

def axis(w, h, image): #draw x and y axis
    cv2.line(image, (0, int(h/2)), (w, int(h/2)), (100, 255, 255), 2)
    cv2.line(image, (int(w/2), 0), (int(w/2), h), (100, 255, 255), 2)

def point(x, y, w, h, image): #center of circle
    cv2.circle(image,(x,y),7,(0,0,255),-1)
    cv2.line(image,(int(w/2),int(h/2)),(x,y),(0,0,255),2)

def puttxt(image, text, pos_x, pos_y): #put text on image
    cv2.putText(image, text, (pos_x, pos_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

def main():
    w = 12; p = -1.0; d = 50; D = 0 #initial value
    f = p*d/w
    cap = cv2.VideoCapture('Week14_hw/motionPattens3.mov')
    ret, img = cap.read()
    w = img.shape[1]; h = img.shape[0]
    print(w,h)
    while ret:
        axis(w,h,img)
        cnt_max = findMarker(img)
        rect = cv2.minAreaRect(cnt_max)
        box = np.int0(cv2.boxPoints(rect))
        cv2.drawContours(img, [box], 0, (0,0,255), 2)
        point(int(rect[0][0]), int(rect[0][1]), w, h, img)
        x_ = np.rad2deg(np.arctan((rect[0][0]-w/2)/f))
        y_ = np.rad2deg(np.arctan((rect[0][1]-h/2)/f))
        text_f = f'f_L = {np.round(f,1)}'
        text_D = f'D = {np.round(D,1)}'
        text_x = f'Vx = {np.round(x_,1)}'
        text_y = f'Vy = {np.round(y_,1)}'
        puttxt(img, text_f, 80, 80)
        puttxt(img, text_D, 80, 120)
        puttxt(img, text_x, 80, 160)
        puttxt(img, text_y, 80, 200)
        cv2.imshow('result', img)
        if cv2.waitKey(10) & 0xFF == ord('c'):
            p = rect[1][0]
            f = p*d/w
        p = rect[1][0]
        D = f*w/p
        ret, img = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()