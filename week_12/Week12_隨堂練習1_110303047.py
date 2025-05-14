import cv2
import numpy as np

def main():
    img = cv2.imread(r'Source\rice-shaded.tif')
    edges = cv2.Canny(img,100,200)

    # 將邊緣資訊重疊到原始圖片上
    # 建立一個與原始圖片大小相同的全黑圖片
    contour_img = np.zeros_like(img)

    # 將 Canny 偵測到的邊緣 (白色像素) 複製到 contour_img 上
    contour_img[edges != 0] = (0, 0, 255)  # 使用紅色 (0, 0, 255) 標記邊緣

    # 將 contour_img 與原始圖片 img 重疊
    # result = cv2.addWeighted(img, 1, contour_img, 0.5, 0)
    result = cv2.add(img, contour_img)

    # 顯示結果
    cv2.imshow('result',result)
    cv2.waitKey(0) 
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()