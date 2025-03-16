import cv2
import numpy as np

def findMarker(image):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(image, (5,5), 0)
    thr = cv2.adaptiveThreshold(blur, 250, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,2)
    contours,_ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key = cv2.contourArea)
    return cnt_max

def draw_contours(image, cnt_max):
    rect = cv2.minAreaRect(cnt_max)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(image, [box], 0, (0,0,255), 2)
    return int(rect[0][0]), int(rect[0][1])

def puttxt(image, text, pos_x, pos_y): #put text on image
    cv2.putText(image, text, (pos_x, pos_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)

def axis(w, h, image): #draw x and y axis
    cv2.line(image, (0, int(h/2)), (w, int(h/2)), (255, 0, 0), 2)
    cv2.line(image, (int(w/2), 0), (int(w/2), h), (255, 0, 0), 2)

def main():
    
    f_0 = 593
    f_1 = 675
    l = 18
    cap_1 = cv2.VideoCapture('Week14_hw/videoCam0_calbrateNballPos.mp4')
    cap_2 = cv2.VideoCapture('Week14_hw/videoCam1_calbrateNballPos.mp4')
    while True:
        ret_1, img_1 = cap_1.read()
        ret_2, img_2 = cap_2.read()
        w_1 = img_1.shape[1]; h_1 = img_1.shape[0]
        w_2 = img_2.shape[1]; h_2 = img_2.shape[0]
        U_red = np.array([118,195,255])
        L_red = np.array([34,117,220])
        
        mask_1 = cv2.inRange(img_1, L_red, U_red)
        mask_2 = cv2.inRange(img_2, L_red, U_red)
        try:
            cnt_1 = findMarker(mask_1)
            cnt_2 = findMarker(mask_2)
            x_1, y_1 = draw_contours(img_1, cnt_1)
            x_2, y_2 = draw_contours(img_2, cnt_2)
            v_x1 = np.arctan((x_1-w_1/2)/f_0)
            v_y1 = np.arctan((y_1-h_1/2)/f_0)
            v_x2 = np.arctan((x_2-w_2/2)/f_1)
            v_y2 = np.arctan((y_2-h_2/2)/f_1)
            z = l/(np.tan(v_x1)-np.tan(v_x2))
            x = (l/2)*((np.tan(v_x1)+np.tan(v_x2))/(np.tan(v_x1)-np.tan(v_x2)))
            y_1 = z*np.tan(v_y1) 
            y_2 = z*np.tan(v_y2)
            text_z = f'z = {np.round(z,1)}'
            text_x = f'x = {np.round(x,1)}'
            text_y = f'y = {np.round(y_1,1)}'
            text_f0 = f'f0 = {np.round(f_0,1)}'
            text_f1 = f'f1 = {np.round(f_1,1)}'
            puttxt(img_1, text_f0, 80, 80)
            puttxt(img_2, text_f1, 80, 80)
            puttxt(img_1, text_x, 80, 120)
            puttxt(img_1, text_y, 80, 160)
            puttxt(img_1, text_z, 80, 200)
            axis(w_1, h_1, img_1)
            axis(w_2, h_2, img_2)
        except:
            continue
        cv2.imshow('img', img_1)
        cv2.imshow('img2', img_2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()

