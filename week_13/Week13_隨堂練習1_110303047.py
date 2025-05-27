import cv2

# 撰寫findMarker函數以獲取該影像中最大的輪廓
def findMarker(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    a, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_contour = min(contours, key=cv2.contourArea)
    min_arc_length_contour = min(contours, key=lambda c: cv2.arcLength(c,False))
    return min_contour, min_arc_length_contour
    
if __name__ == "__main__":
    cap = cv2.VideoCapture(r'week_13\motionPattens2.mov')
    
    while cap.isOpened():   
        ret, img = cap.read()
        img = img[ : -10, :] # 裁切底部以避免誤判
        h, w = img.shape[:2]
        img = cv2.resize(img, (int(h*0.5), int(w*0.5)))

        min_contour, min_arc_length_contour = findMarker(img)
        cv2.drawContours(img, [min_contour], 0, (0, 0, 255), 2)
        cv2.drawContours(img, [min_arc_length_contour], 0, (0, 255, 0), 2)
        cv2.imshow('result', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): # 按下q鍵提早結束
            break
    cap.release()
    cv2.destroyAllWindows()