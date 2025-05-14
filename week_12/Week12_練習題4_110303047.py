import cv2
import numpy as np

def main():
    img = cv2.imread(r'week_12\Coin and Paper.jpg') # 讀取原圖以利最終結果疊加
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 轉為灰階
    edges = cv2.Canny(gray, 107, 200) # 尋邊以獲取目標邊緣
    cv2.imshow('edges', edges) # 顯示邊緣檢測結果
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 110) # 霍夫變換，以1px為單位，角度以1度為單位，110為閾值以減少雜訊
    N = lines.shape[0]
    print(np.shape(lines))
    for n in range(N):
        r, theta = lines[n][0]
        L = 1000
        x0 = r * np.cos(theta)
        y0 = r * np.sin(theta)
        x1 = int(x0 + L * np.sin(theta))
        y1 = int(y0 - L * np.cos(theta))
        x2 = int(x0 - L * np.sin(theta))
        y2 = int(y0 + L * np.cos(theta))
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    cv2.imshow('line', img) # 顯示畫出來的線
    cv2.waitKey(0)
    cv2.destroyAllWindows() # 關閉所有視窗
if __name__ == '__main__':
    main()
