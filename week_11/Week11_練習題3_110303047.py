import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(r'week_11\IMG_3006.MOV') # 
    while True:
        ret, frame = cap.read() # 讀取影像
        if ret: # 如果讀取失敗則結束
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 轉為灰階以利二值化
            a, thr = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV) # 二值化以利侵蝕，設定120以保障硬幣的高光面不會被侵蝕掉
            kernel = np.ones((3,3))
            eroded = cv2.erode(thr, kernel, iterations=5) # 腐蝕將底部雜訊濾掉
            dilated = cv2.dilate(eroded, kernel, iterations=10) # 將侵蝕的部分擴張回來以確保在同一輪廓上
            contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # 找輪廓
            # 繪製輪廓中心
            for c in contours:
                x = int((max(c[:,0,0]) + min(c[:,0,0])) / 2) # 找到輪廓的x座標
                y = int((max(c[:,0,1]) + min(c[:,0,1])) / 2) # 找到輪廓的x座標
                cv2.circle(frame, (x, y), 10, (255, 0, 0), -1)
            cv2.drawContours(frame, contours, -1, (0, 0, 255), 2) # 畫出所有硬幣的輪廓
            cv2.imshow('contours', frame)
        else:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release() # 釋放資源
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()