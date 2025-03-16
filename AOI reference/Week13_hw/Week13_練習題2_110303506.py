import cv2

def findMarker(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    a, thr = cv2.threshold(blur, 150,250, cv2.THRESH_BINARY_INV)
    contours,_ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key = cv2.contourArea)
    return cnt_max

def main():
    cap = cv2.VideoCapture('Week13_hw/motionPattens2.mov')
    ret, img = cap.read()
    while ret:
        cnt_max = findMarker(img)
        cv2.drawContours(img, [cnt_max], 0, (0,0,255), 5)
        cv2.imshow('result', img)
        ret, img = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()