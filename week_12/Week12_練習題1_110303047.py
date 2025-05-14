import cv2

def main():
    img = cv2.imread(r'week_12\0518_5p.png') # 讀取圖片
    cv2.imshow('origin', img)
    edges = cv2.Canny(img, 20,20) # 尋邊
    cv2.imshow('edge',edges) # 顯示邊緣
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()