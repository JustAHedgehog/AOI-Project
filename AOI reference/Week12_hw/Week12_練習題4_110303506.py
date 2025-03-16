import cv2
import numpy as np

def main():
    img = cv2.imread('Week12_hw/Coin and Paper.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 95)
    N = lines.shape[0]
    for n in range(0,N-1):
        r = lines[n,0,0]
        q = lines[n,0,1]
        L = 1000
        x_0 = int(r*np.cos(q)); y_0 = int(r*np.sin(q))
        x_1 = int(x_0+L*np.sin(q)); y_1 = int(y_0-L*np.cos(q))
        x_2 = int(x_0-L*np.sin(q)); y_2 = int(y_0+L*np.cos(q))
        cv2.line(img, (x_1,y_1),(x_2,y_2),(0,0,255),2)
    cv2.imshow('line',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__=='__main__':
    main()