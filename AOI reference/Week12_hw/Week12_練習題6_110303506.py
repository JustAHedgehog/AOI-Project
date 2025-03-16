import cv2
import numpy as np

def main():
    img = cv2.imread('Week12_hw/severalPatten.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(img, 3)
    edges = cv2.Canny(gray, 100, 250)
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 100, param1=250, param2=25, minRadius=10, maxRadius=100)
    circles = np.int16(np.around(circles))
    for i in circles[0,:]:
        cv2.circle(img, (i[0], i[1]), i[2], (0,0,255),2)
        cv2.circle(img, (i[0], i[1]), 2, (0,0,255),3)
        txt = f'area={np.uint16(i[2]**2*np.pi)}'
        cv2.putText(img, txt, (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,0,0), 2, cv2.LINE_AA)
    cv2.imshow('test', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()