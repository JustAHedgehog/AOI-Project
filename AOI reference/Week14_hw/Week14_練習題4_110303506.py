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



def main():
    
    img = cv2.imread('Week14_hw/traffic0609_2.jpg')
    w = img.shape[1]; h = img.shape[0]
    L_red = np.array([52,23,14])
    U_red = np.array([165,81,29])
    mask = cv2.inRange(img, L_red, U_red)
    cnt = findMarker(mask)
    x, y = draw_contours(img, cnt)
    text_u = f'u = {x}'
    text_v = f'v = {y}'
    puttxt(img, text_u, 850, 50)
    puttxt(img, text_v, 850, 90)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()

