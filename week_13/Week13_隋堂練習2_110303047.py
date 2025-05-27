import cv2

# 撰寫findMarker函數以獲取該影像中最大的輪廓
def findMarker(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    a, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_contour = min(contours, key=cv2.contourArea)
    return min_contour
    
if __name__ == "__main__":
    cap = cv2.VideoCapture(r'week_13\motionPattens3.mov')
    
    while cap.isOpened():   
        ret, img = cap.read()
        img = img[ : -10, :] # 裁切底部以避免誤判
        h, w = img.shape[:2]
        img = cv2.resize(img, (int(w*0.5), int(h*0.5)))

        min_contour = findMarker(img)
        x,y,h,w = cv2.boundingRect(min_contour)
        img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,0,255),2)
        cv2.imshow('result', img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'): # 按下q鍵提早結束
            break
    cap.release()
    cv2.destroyAllWindows()