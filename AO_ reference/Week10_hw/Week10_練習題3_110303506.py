import cv2

def main():
    cap = cv2.VideoCapture('Week10_hw\motionPattern_0506.MOV')
    for i in range(0,10):
        ret, frame = cap.read() # 讀取影像
        cv2.imshow('WebCam', frame) # 顯示影像
        cv2.waitKey(1000)
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()