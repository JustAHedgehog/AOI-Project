import cv2

def main():
    img_1 = cv2.imread('Week10_hw\messi5.jpg') #讀取影像
    img_2 = cv2.imread('Week10_hw\messi5p.jpg')
    diff = cv2.absdiff(img_1, img_2) #相減運算
    cv2.imshow('img_1', img_1) #顯示原圖以及相減結果
    cv2.imshow('img_2', img_2)
    cv2.imshow('diff', diff)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()