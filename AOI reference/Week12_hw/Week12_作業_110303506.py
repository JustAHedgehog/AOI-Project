import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture('Week12_hw/2coins_motion.wmv')
    ret, img_1 = cap.read() #讀取影像
    ret_2, img_2 = cap.read()
    while True:
        gray = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(img_1, 3)
        edges = cv2.Canny(gray, 100, 250)
        circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 100, param1=250, param2=25, minRadius=10, maxRadius=300)
        
        if circles is not None:
            circles = np.int16(np.around(circles))
            # print(circles)
            c = circles[0]
            x_0 = c[0,0]; y_0 = c[0,1]; r_0 = c[0,2]; x_1 = c[1,0]; y_1 = c[1,1]; r_1 = c[1,2]
            cv2.circle(img_1, (x_0, y_0), r_0, (0,0,255),2)
            cv2.circle(img_1, (x_1, y_1), r_1, (0,0,255),2)
            cv2.line(img_1, (x_0, y_0), (x_1, y_1), (0,0,255),2)
            dis = np.sqrt((x_1-x_0)**2+(y_1-y_0)**2)
            print(np.around(dis,1))
            txt = f'distance={np.around(dis,1)}'
            cv2.putText(img_1, txt, (80, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2, cv2.LINE_AA)
        cv2.imshow('test', img_1)
        img_1 = img_2.copy()
        cv2.waitKey(20)
        ret_2, img_2 = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()