import numpy as np
import cv2
import glob
import os

def xy_axes(image, w, h):
    cv2.line(image, (0, int(h / 2)), (w, int(h / 2)), (0, 255, 0), 1)
    cv2.line(image, (int(w / 2), 0), (int(w / 2), h), (0, 255, 0), 1)
    cv2.circle(image, (int(w / 2), int(h / 2)), 8, (0, 255, 0), 1)

def drawImgAxes(img, corners, imgpts):
    corner = tuple(np.int32(corners[0, 0]))
    Xaxis = tuple(np.int32(imgpts[0, 0]))
    Yaxis = tuple(np.int32(imgpts[1, 0]))
    Zaxis = tuple(np.int32(imgpts[2, 0]))

    cv2.line(img, corner, Xaxis, (255, 0, 0), 4)
    cv2.line(img, corner, Yaxis, (0, 255, 0), 4)
    cv2.line(img, corner, Zaxis, (0, 0, 255), 4)

def camCaptureChessBoard(save_folder="Picture"):
    save_path = os.path.join("final/prob_3", save_folder)
    os.makedirs(save_path, exist_ok=True)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    i = 0

    print("拍攝模式：按 'o' 拍照並顯示，按 Esc 結束")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        h, w, _ = frame.shape
        xy_axes(frame, w, h)
        cv2.imshow("Live Capture", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("o"):
            filename = f"final/prob_3/{save_folder}/testBoard{i}.jpg"
            cv2.putText(frame, str(i), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imwrite(filename, frame)
            print(f"Saved and showing: {filename}")
            img = cv2.imread(filename)
            if img is not None:
                cv2.imshow(f"Captured {i}", img)
            i += 1
        elif key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

def CBxyzNuv(save_folder="Picture", pattern_size=(10, 7)):
    objp = np.zeros((pattern_size[0]*pattern_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

    objpoints, imgpoints = [], []
    images = glob.glob(f"final/prob_3/{save_folder}/testBoard*.jpg")
    print(f"共讀取到 {len(images)} 張圖片進行角點偵測")

    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, pattern_size, None)
        if ret:
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1),
                        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
            objpoints.append(objp)
            imgpoints.append(corners2)
            img = cv2.drawChessboardCorners(img, pattern_size, corners2, ret)
            cv2.imshow("Detected Corners", img)
            cv2.waitKey(300)
    cv2.destroyAllWindows()
    if len(objpoints) == 0:
        print("沒有成功偵測任何棋盤角點，請檢查圖片或 pattern_size")
        exit()
    return objpoints, imgpoints, gray.shape[::-1]

def camCalibration(objpoints, imgpoints, imgshape):
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, imgshape, None, None)
    np.save("final/prob_3/M.npy", mtx)
    np.save("final/prob_3/D.npy", dist)
    print("\nCamera Matrix:\n", mtx)
    print("\nDistortion Coefficients:\n", dist)

if __name__ == "__main__":
    pattern_size = (10, 7)
    axis = np.float32([[3, 0, 0], [0, 3, 0], [0, 0, -3]])

    YN = input("Would you like to capture the testBoard images for calibration? y/n: ").lower()
    if YN == "y":
        camCaptureChessBoard()
        objpoints, imgpoints, imgshape = CBxyzNuv(pattern_size=pattern_size)
        camCalibration(objpoints, imgpoints, imgshape)

    mtx = np.load("final/prob_3/M.npy")
    dist = np.load("final/prob_3/D.npy")
    objp = np.zeros((pattern_size[0]*pattern_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    save_id = 0

    print("即時姿態估測中：將棋盤格放到畫面中")
    print("按 'o' 截圖，'f' 或 'Esc' 結束")

    while True:
        ret, img = cap.read()
        if not ret:
            break
        img = cv2.resize(img, (1280, 720))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        found, corners = cv2.findChessboardCorners(gray, pattern_size, None)
        if found:
            img = cv2.drawChessboardCorners(img, pattern_size, corners, found)
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
            ret_pnp, rvecs, tvecs = cv2.solvePnP(objp, corners2, mtx, dist)
            imgpts, _ = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)
            drawImgAxes(img, corners2, imgpts)

            x, y, z = tvecs.flatten()
            l = np.linalg.norm([x, y, z])

            R, _ = cv2.Rodrigues(rvecs)
            sy = np.sqrt(R[0, 0]**2 + R[1, 0]**2)
            singular = sy < 1e-6
            if not singular:
                alpha = np.arctan2(R[2, 1], R[2, 2])
                beta  = np.arctan2(-R[2, 0], sy)
                gamma = np.arctan2(R[1, 0], R[0, 0])
            else:
                alpha = np.arctan2(-R[1, 2], R[1, 1])
                beta  = np.arctan2(-R[2, 0], sy)
                gamma = 0
            alpha_deg = np.degrees(alpha)
            beta_deg = np.degrees(beta)
            gamma_deg = np.degrees(gamma)

            overlay = [
                f"l= {l:.1f} mm",
                f"(x,y,z)= ({x:.1f}, {y:.1f}, {z:.1f})",
                f"(a,b,c)= ({alpha_deg:.1f}, {beta_deg:.1f}, {gamma_deg:.1f})",
            ]
            for i, text in enumerate(overlay):
                cv2.putText(img, text, (10, 30 + i * 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        else:
            cv2.putText(img, "No pattern detected", (30, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Pose Estimation Result", img)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("f") or key == 27:
            print("結束姿態估測")
            break
        elif key == ord("o"):
            filename = f"savedPose_{save_id}.jpg"
            cv2.imwrite(filename, img)
            print(f"已儲存影像：{filename}")
            cv2.imshow(f"Saved {save_id}", img)
            save_id += 1

    cap.release()
    cv2.destroyAllWindows()