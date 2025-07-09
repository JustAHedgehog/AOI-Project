import cv2
import numpy as np

def findMarker(image):
    blur = cv2.GaussianBlur(image, (5,5), 0)
    thr = cv2.adaptiveThreshold(blur, 250, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,2)
    contours,_ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key = cv2.contourArea)
    return cnt_max

def draw_contours(image, cnt_max):
    rect = cv2.minAreaRect(cnt_max)
    box = np.intp(cv2.boxPoints(rect))
    cv2.drawContours(image, [box], 0, (0,0,255), 2)
    return int(rect[0][0]), int(rect[0][1])

def puttxt(image, key, value, pos_x, pos_y):  # 在影像上放置文字
    text = f'{key} = {np.round(value, 1)}'
    cv2.putText(image, text, (pos_x, pos_y),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

def main():
    
    f_0 = 593
    f_1 = 675
    l = 18
    img_1 = cv2.imread('week_14/Position1(z69cm)_Cam0.jpg')
    img_2 = cv2.imread('week_14/Position1(z69cm)_Cam1.jpg')
    w_1 = img_1.shape[1]; h_1 = img_1.shape[0]
    w_2 = img_2.shape[1]; h_2 = img_2.shape[0]
    U_red = np.array([118,195,255])
    L_red = np.array([34,117,202])
    mask_1 = cv2.inRange(img_1, L_red, U_red)
    mask_2 = cv2.inRange(img_2, L_red, U_red)
    cnt_1 = findMarker(mask_1)
    cnt_2 = findMarker(mask_2)
    x_1, y_1 = draw_contours(img_1, cnt_1)
    x_2, y_2 = draw_contours(img_2, cnt_2)
    a_1 = np.arctan((x_1-w_1/2)/f_0)
    b_1 = np.arctan(-(y_1-h_1/2)/f_0)
    a_2 = np.arctan((x_2-w_2/2)/f_1)
    b_2 = np.arctan(-(y_2-h_2/2)/f_1)
    z = l/(np.tan(a_1)-np.tan(a_2))
    x = (l/2)*((np.tan(a_1)+np.tan(a_2))/(np.tan(a_1)-np.tan(a_2)))
    y_1 = z*np.tan(b_1) 
    y_2 = z*np.tan(b_2)
    y = (y_1 + y_2)/2
    puttxt(img_1, 'f0', f_0, 80, 80)
    puttxt(img_2, 'f1', f_1, 80, 80)
    puttxt(img_1, 'x', x, 80, 120)
    puttxt(img_1, 'y', y, 80, 160)
    puttxt(img_1, 'z', z, 80, 200)
    cv2.imshow('img', img_1)
    cv2.imshow('img2', img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()