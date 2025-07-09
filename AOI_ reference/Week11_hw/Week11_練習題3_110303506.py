import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture('Week11_hw\IMG_3006.MOV')
    while True:
        ret, frame = cap.read()
        if ret == True:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            a, thr = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV) #二值化
            kernel = np.ones([3,3])
            eroded = cv2.erode(thr, kernel, iterations=5) #侵蝕
            dilated = cv2.dilate(eroded, kernel, iterations=10) #擴張
            contours, a = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #找輪廓
            for i in contours: #找輪廓中心
                x = int((max(i[:,0,0])+min(i[:,0,0]))/2)
                y = int((max(i[:,0,1])+min(i[:,0,1]))/2)
                cv2.circle(frame, (x,y), 10, (255,0,0),-1)
            cv2.drawContours(frame, contours, -1, (0,0,255),2)
            cv2.imshow('test', frame)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()