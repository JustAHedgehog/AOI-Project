import cv2

def main():
    i_max = 0; area_max = 0
    img = cv2.imread('Week13_hw/A4paper70cm.jpg')
    # cv2.imshow('test',img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    a, thr = cv2.threshold(blur, 150,255, cv2.THRESH_BINARY_INV)
    # edges = cv2.Canny(thr,35 ,125)
    contours,_ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(0,len(contours)):
        area = cv2.contourArea(contours[i])
        if area>area_max:
            area_max = area
            i_max = i
        print(i_max)
        print(contours[i_max])
        cv2.drawContours(img, contours, i_max, (0,0,255), 2)
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()