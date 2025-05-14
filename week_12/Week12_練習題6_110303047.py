import cv2
import numpy as np

def main():
    img = cv2.imread(r'week_12\severalPatten.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(img, 3) # 中值滤波已模糊空心圓內外圈
    edges = cv2.Canny(gray, 150, 250)
    cv2.imshow('edges', edges)
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=100,
                            param1=250, param2=25, minRadius=10, maxRadius=100) # param1: Canny高斯滤波器的高阈值，param2: 圆心检测的阈值，minRadius: 最小半径，maxRadius: 最大半径
    print(circles.shape)
    circles = np.uint16(np.around(circles)) # 將圆心及半徑轉換成整數
    for i in circles[0, :]:
        cv2.circle(img, (i[0], i[1]), i[2], (0, 0, 255), 2) # 在圓形處畫圓
        # 於圓心處撰寫圓面積
        txt = f'{np.uint16(i[2]**2*np.pi)}' 
        cv2.putText(img, txt, (i[0], i[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
    cv2.imshow('detected circles', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()