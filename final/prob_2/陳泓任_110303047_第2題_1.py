import cv2
import numpy as np
from 陳泓任_110303047_第2題_2 import calibration
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def findMarker(image):
    blur = cv2.GaussianBlur(image, (5,5), 0)
    thr = cv2.adaptiveThreshold(blur, 250, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,2)
    contours,_ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key = cv2.contourArea)
    return cnt_max

def draw_contours(image, cnt_max):
    rect = cv2.minAreaRect(cnt_max)
    box = np.intp(cv2.boxPoints(rect))
    cv2.drawContours(image, [box], 0, (0,0,255), 2)
    return int(rect[0][0]), int(rect[0][1])

def puttxt(image, key, value, pos_x, pos_y):  # 在影像上放置文字
    text = f'{key} = {np.round(value, 1)}'
    cv2.putText(image, text, (pos_x, pos_y),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

def axis(w, h, image): #draw x and y axis
    cv2.line(image, (0, int(h/2)), (w, int(h/2)), (255, 0, 0), 2)
    cv2.line(image, (int(w/2), 0), (int(w/2), h), (255, 0, 0), 2)

def main():
    # 設定初始參數
    w = 14  # 矩形實際邊長(cm)
    p = -1.0  # 矩形螢幕寬度(pixel)
    d = 50  # 圖像與相機距離(cm)
    D = 0  # 即時量測距離(cm)
    cap_1 = cv2.VideoCapture(r'final\prob_2\right_f.mkv')
    f_0 = calibration(w, p, d, cap_1)  # 校正相機焦距
    print(f'f_0={np.round(f_0, 1)}')  # 印出焦距
    cap_2 = cv2.VideoCapture(r'final\prob_2\left_f.mkv')
    f_1 = calibration(w, p, d, cap_2)  # 校正相機焦距
    print(f'f_0={np.round(f_1, 1)}')  # 印出焦距
    print("Calibration complete.")

    # 初始化 3D 軌跡圖視窗
    plt.ion()  # 啟用互動模式
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim([-15, 15])
    ax.set_ylim([-15, 15])
    ax.set_zlim([-90, -40])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Ball Trajectory')

    trajectory = []  # 用來記錄所有點
    trajectory_plot, = ax.plot([], [], [], 'ro-')  # 初始化空圖線

    l = 12 # 兩相機之間的距離(cm)
    cap_1 = cv2.VideoCapture(r'final\prob_2\right_video.mp4')
    cap_2 = cv2.VideoCapture(r'final\prob_2\left_video.mp4')
    while True:
        ret_1, img_1 = cap_1.read()
        ret_2, img_2 = cap_2.read()
        if not ret_1 or not ret_2:
            break
        w_1 = img_1.shape[1]; h_1 = img_1.shape[0]
        w_2 = img_2.shape[1]; h_2 = img_2.shape[0]
        U_red = np.array([100,220,220])
        L_red = np.array([60,143,140])
        
        mask_1 = cv2.inRange(img_1, L_red, U_red)
        mask_2 = cv2.inRange(img_2, L_red, U_red)
        try:
            cnt_1 = findMarker(mask_1)
            cnt_2 = findMarker(mask_2)
            x_1, y_1 = draw_contours(img_1, cnt_1)
            x_2, y_2 = draw_contours(img_2, cnt_2)
            a_1 = np.arctan((x_1-w_1/2)/f_0)
            b_1 = np.arctan(-(y_1-h_1/2)/f_0)
            a_2 = np.arctan((x_2-w_2/2)/f_1)
            b_2 = np.arctan(-(y_2-h_2/2)/f_1)
            z = l/(np.tan(a_1)-np.tan(a_2))
            x = (l/2)*((np.tan(a_1)+np.tan(a_2))/(np.tan(a_1)-np.tan(a_2)))
            y_1 = z*np.tan(b_1) 
            y_2 = z*np.tan(b_2)
            puttxt(img_1, 'f0', f_0, 80, 80)
            puttxt(img_2, 'f1', f_1, 80, 80)
            puttxt(img_1, 'x', x, 80, 120)
            puttxt(img_1, 'y', y_1, 80, 160)
            puttxt(img_1, 'z', z, 80, 200)
            axis(w_1, h_1, img_1)
            axis(w_2, h_2, img_2)
            # 儲存新座標
            trajectory.append((x, y_1, z))

            # 拆開 x, y, z 資料
            xs, ys, zs = zip(*trajectory)
            trajectory_plot.set_data(xs, ys)
            trajectory_plot.set_3d_properties(zs)

            plt.draw()
            plt.pause(0.01)
        except:
            continue
        cv2.imshow('img', img_1)
        cv2.imshow('img2', img_2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap_1.release()
    cap_2.release()
    cv2.destroyAllWindows()

    fig.savefig('final/prob_2/3D_ball_trajectory.png', dpi=300)


if __name__=='__main__':
    main()

