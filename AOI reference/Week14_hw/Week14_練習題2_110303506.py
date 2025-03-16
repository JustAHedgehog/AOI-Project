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
    cv2.line(image, (0, int(h/2)), (w, int(h/2)), (255, 0, 0), 2)
    cv2.line(image, (int(w/2), 0), (int(w/2), h), (255, 0, 0), 2)

def point(x, y, w, h, image): #center of circle
    cv2.circle(image,(x,y),7,(0,0,255),-1)
    cv2.line(image,(int(w/2),int(h/2)),(x,y),(0,0,255),2)

def puttxt(image, text, pos_x, pos_y): #put text on image
    cv2.putText(image, text, (pos_x, pos_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

def draw_contours(image, cnt_max):
    rect = cv2.minAreaRect(cnt_max)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(image, [box], 0, (0,0,255), 2)
    return int(rect[0][0]), int(rect[0][1])

def main():
    f_0 = 1000
    f_1 = 1000
    l = 30
    img_1 = cv2.imread('Week14_hw/0609_circleCam0.jpg')
    img_2 = cv2.imread('Week14_hw/0609_circleCam1.jpg')
    w_1 = img_1.shape[1]; h_1 = img_1.shape[0]
    w_2 = img_2.shape[1]; h_2 = img_2.shape[0]
    cntMax_1 = findMarker(img_1)
    cntMax_2 = findMarker(img_2)
    axis(w_1, h_1, img_1)
    axis(w_2, h_2, img_2)
    x_1, y_1 = draw_contours(img_1, cntMax_1)
    x_2, y_2 = draw_contours(img_2, cntMax_2)
    v_x1 = np.arctan((x_1-w_1/2)/f_0)
    v_y1 = np.arctan((y_1-h_1/2)/f_0)
    v_x2 = np.arctan((x_2-w_2/2)/f_1)
    v_y2 = np.arctan((y_2-h_2/2)/f_1)
    z = l/(np.tan(v_x1)-np.tan(v_x2))
    x = (l/2)*((np.tan(v_x1)+np.tan(v_x2))/(np.tan(v_x1)-np.tan(v_x2)))
    text_z = f'z = {np.round(z,1)}'
    text_x = f'x = {np.round(x,1)}'
    text_f0 = f'f0 = {np.round(f_0,1)}'
    text_f1 = f'f1 = {np.round(f_1,1)}'
    puttxt(img_1, text_f0, 80, 80)
    puttxt(img_2, text_f1, 80, 80)
    puttxt(img_1, text_x, 80, 120)
    puttxt(img_1, text_z, 80, 160)
    cv2.imshow('r1', img_1)
    cv2.imshow('r2', img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()