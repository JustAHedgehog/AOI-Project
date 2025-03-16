import cv2
import numpy as np

def main():
    img = cv2.imread('Week12_hw/IMG_3973.JPG')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50,150)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=20, maxLineGap=70)
    print(lines.shape)
    print(f'L0={lines[0]}')
    print(f'L1={lines[1]}')
    for i in range(len(lines)):
        x_1 = lines[i,0,0];y_1 = lines[i,0,1]
        x_2 = lines[i,0,2];y_2 = lines[i,0,3]
        cv2.line(img, (x_1,y_1), (x_2,y_2),(0,0,255),8)
    cv2.namedWindow('test',0)
    cv2.resizeWindow('test',500,500)
    cv2.imshow('test',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()