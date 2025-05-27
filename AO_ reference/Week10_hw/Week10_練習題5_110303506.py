import cv2

def main():
    cap = cv2.VideoCapture('Week10_hw\motionPattern_0506.MOV') 
    ret, img_1 = cap.read() #擷取圖片
    cv2.waitKey(1000)
    ret,img_2 = cap.read()
    diff = cv2.absdiff(img_1, img_2) #計算差異
    cv2.imshow('img_1', img_1)
    cv2.imshow('img_2', img_2)
    cv2.imshow('diff', diff)
    cv2.imwrite('test.jpg', diff)
    cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()