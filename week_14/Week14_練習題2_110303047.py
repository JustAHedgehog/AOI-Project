import cv2
import numpy as np

def findMarker(image, w, f): 
    """Find the circular marker in the image and calculate the angle."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=150, param2=10, minRadius=10, maxRadius=50)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        c = circles[0][0]  # Return the first detected circle
        cv2.circle(image, (c[0], c[1]), c[2], (0, 255, 0), 2)
        x = c[0]
        a = np.arctan((x-w/2)/f)
        return a
    
def main():
    f = 1000
    l = 30
    img_1 = cv2.imread(r'week_14\0609_circleCam0.jpg')
    img_2 = cv2.imread(r'Week_14\0609_circleCam1.jpg')
    w_1 = img_1.shape[1]
    w_2 = img_2.shape[1]
    a_1 = findMarker(img_1, w_1, f)
    a_2 = findMarker(img_2, w_2, f)
    z = l/(np.tan(a_1)-np.tan(a_2))
    x = (l/2)*((np.tan(a_1)+np.tan(a_2))/(np.tan(a_1)-np.tan(a_2)))
    print(f'The point is at x={np.round(x,1)} px, z={np.round(z,1)} px')

if __name__ == '__main__':
    main()