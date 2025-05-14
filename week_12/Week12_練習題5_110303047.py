import cv2
import numpy as np


def main():
    img = cv2.imread(r'week_12\IMG_3973.JPG')  # 讀取原圖以利最終結果疊加
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 20, 60)
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100,
                            minLineLength=700, maxLineGap=70)
    print(lines.shape)
    for i in range(len(lines)):
        x1, y1, x2, y2 = lines[i, 0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 8)
    cv2.namedWindow('test', 0)
    cv2.resizeWindow('test', 500, 500)
    cv2.imshow('test', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 計算兩縣段夾角
    x1_1, y1_1, x1_2, y1_2 = lines[0, 0]
    x2_1, y2_1, x2_2, y2_2 = lines[3, 0]
    # 計算兩條線的法向量
    n_1 = np.array([y1_2 - y1_1, -(x1_2 - x1_1)])
    n_2 = np.array([y2_2 - y2_1, -(x2_2 - x2_1)])
    # 兩條線的內積
    inner_product = np.dot(n_1, n_2)
    theta = np.arccos(inner_product / (np.linalg.norm(n_1) * np.linalg.norm(n_2)))
    print(f'angle={180-np.degrees(theta)}')

if __name__ == '__main__':
    main()
