import cv2

# 撰寫findMarker函數以獲取該影像中最大的輪廓
def findMarker(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    a, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    max_contour = max(contours, key=cv2.contourArea)
    return max_contour
    
if __name__ == "__main__":
    cap = cv2.VideoCapture(r'week_13\motionPattens2.mov')
    ret, img = cap.read()
    while ret:
        max_contour = findMarker(img)
        cv2.drawContours(img, [max_contour], 0, (0, 0, 255), 2)
        cv2.imshow('result', img)
        ret, img = cap.read() # 因為這邊的img是從cap.read()讀取的，所以要在這邊更新img
        
        if cv2.waitKey(1) & 0xFF == ord('q'): # 按下q鍵提早結束
            break
    cap.release()
    cv2.destroyAllWindows()