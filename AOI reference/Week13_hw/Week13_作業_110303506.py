import cv2
import numpy as np

def findMarker (image): #find circle
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3,3), 0)
    edges=cv2.Canny(blur,50,90)
    circles=cv2.HoughCircles(edges,cv2.HOUGH_GRADIENT,1,100,param1=250,param2=30,minRadius=30,maxRadius=55)
    return circles

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
    cap = cv2.VideoCapture('Week13_hw/movingCoin.wmv') #source
    ret, img = cap.read()
    while ret:
        dim = (1280, 720)
        resized_img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) #resize image shape to 1280x720
        axis(1280, 720, resized_img)
        circles = findMarker( resized_img)
        if circles is not None:
            circles = np.int16(np.around(circles))
            c = circles[0]
            x = c[0,0]; y = c[0,1]; r = c[0,2]
            x_ = np.rad2deg(np.arctan((x-1280/2)/f))
            y_ = np.rad2deg(np.arctan((y-720/2)/f))
            text_f = f'f_L = {np.round(f,1)}'
            text_D = f'D = {np.round(D,1)}'
            text_x = f'x = {np.round(x_,1)}'
            text_y = f'y = {np.round(y_,1)}'
            puttxt(resized_img, text_f, 850, 80)
            puttxt(resized_img, text_D, 850, 120)
            puttxt(resized_img, text_x, 850, 160)
            puttxt(resized_img, text_y, 850, 200)
            cv2.circle( resized_img, (x,y), r, (0,0,255), 2)
            point(x, y, 1280, 720, resized_img)
            cv2.imshow('result',  resized_img)
            if cv2.waitKey(10) & 0xFF == ord('c'):
                p = c[0,0]
                f = p*d/w
            p = c[0,0]
            D = f*w/p
            print(f"c={c}")
            print(f"p={p}")
        ret, img = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
if __name__=='__main__':
    main()