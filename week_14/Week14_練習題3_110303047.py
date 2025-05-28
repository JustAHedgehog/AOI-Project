import cv2
import numpy as np

def findMarker(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    a, thr = cv2.threshold(blur, 50,250, cv2.THRESH_BINARY_INV)
    contours,_ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key = cv2.contourArea)
    return cnt_max

def axes(w, h, image): #draw x and y axis
    cv2.line(image, (0, int(h/2)), (w, int(h/2)), (255, 0, 0), 2)
    cv2.line(image, (int(w/2), 0), (int(w/2), h), (255, 0, 0), 2)
    cv2.circle(image, (int(w/2), int(h/2)), 7, (255, 0, 0), 2)  # center point

def puttxt(image, key, value, pos_x, pos_y):  # 在影像上放置文字
    text = f'{key} = {np.round(value, 1)}'
    cv2.putText(image, text, (pos_x, pos_y),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

def draw_contours(image, cnt_max):
    rect = cv2.minAreaRect(cnt_max)
    box = np.intp(cv2.boxPoints(rect))
    cv2.drawContours(image, [box], 0, (0,0,255), 2)
    return int(rect[0][0]), int(rect[0][1])

def main():
    f_0 = 867 # focal length for camera 0(px)
    f_1 = 544 # focal length for camera 1(px)
    l = 10 # distance between the two cameras(cm)
    img_1 = cv2.imread('week_14/0609cam0.jpg')
    img_2 = cv2.imread('week_14/0609cam1.jpg')
    w_1 = img_1.shape[1]; h_1 = img_1.shape[0]
    w_2 = img_2.shape[1]; h_2 = img_2.shape[0]
    # Find and draw block in both images
    cntMax_1 = findMarker(img_1)
    cntMax_2 = findMarker(img_2)
    x_1, y_1 = draw_contours(img_1, cntMax_1)
    x_2, y_2 = draw_contours(img_2, cntMax_2)

    # Draw axes and center points
    axes(w_1, h_1, img_1)
    axes(w_2, h_2, img_2)

    a_1 = np.arctan((x_1-w_1/2)/f_0)
    b_1 = np.arctan(-(y_1-h_1/2)/f_0)
    a_2 = np.arctan((x_2-w_2/2)/f_1)
    b_2 = np.arctan(-(y_2-h_2/2)/f_1)
    z = l/(np.tan(a_1)-np.tan(a_2))
    x = (l/2)*((np.tan(a_1)+np.tan(a_2))/(np.tan(a_1)-np.tan(a_2)))
    y_1 = z*np.tan(b_1) 
    y_2 = z*np.tan(b_2)
    y = (y_1+y_2)/2 # average value y
    puttxt(img_1, 'f0', f_0, 80, 80)
    puttxt(img_2, 'f1', f_1, 80, 80)
    puttxt(img_1, 'x', x, 80, 120)
    puttxt(img_1, 'y', y_1, 80, 160)
    puttxt(img_2, 'y', y_2, 80, 160)
    puttxt(img_1, 'z', z, 80, 200)
    print(f'The point is at ({np.round(x,1)}, {np.round(y,1)}, {np.round(z,1)})')
    cv2.imshow('r1', img_1)
    cv2.imshow('r2', img_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()