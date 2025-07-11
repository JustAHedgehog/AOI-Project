import cv2
import numpy as np
import os

def load_templates(template_dir):
    '''載入樣板拼圖碎片並建立 ORB 特徵點和描述子'''
    templates = {}
    orb = cv2.ORB_create()
    for fname in os.listdir(template_dir):
        if fname.endswith('.png'):
            label = fname[:-4]  # e.g., '1-1'
            img = cv2.imread(os.path.join(template_dir, fname), cv2.IMREAD_GRAYSCALE)
            kp, des = orb.detectAndCompute(img, None)
            templates[label] = (img, kp, des)
    return templates

def extract_aligned_piece(img, contour):
    rect = cv2.minAreaRect(contour)
    box = cv2.boxPoints(rect)
    box = np.intp(box)

    width = int(rect[1][0])
    height = int(rect[1][1])

    src_pts = box.astype("float32")
    # 計算對齊矩形的目標點位置
    dst_pts = np.array([[0, height-1],
                        [0, 0],
                        [width-1, 0],
                        [width-1, height-1]], dtype="float32")

    # 取得仿射變換矩陣並校正圖像方向
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warped = cv2.warpPerspective(img, M, (width, height))

    return warped

def rotate_image(image, angle):
    h, w = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_LINEAR)
    return rotated

def match_piece_to_templates(piece_img,  templates: dict, matcher: cv2.BFMatcher, orb):
    piece_gray = cv2.cvtColor(piece_img, cv2.COLOR_BGR2GRAY)
    kp2, des2 = orb.detectAndCompute(piece_gray, None)

    best_label = None
    max_good_matches = 0

    for label, (tpl_img, kp1, des1) in templates.items():
        if des1 is None or des2 is None:
            continue

        # 建立四種旋轉角度的樣板圖像與特徵
        for angle in [0, 90, 180, 270]:
            rotated = rotate_image(tpl_img, angle)
            kp_rot, des_rot = orb.detectAndCompute(rotated, None)
            if des_rot is None:
                continue

            matches = matcher.knnMatch(des_rot, des2, k=2)
            good = [m for match in matches if len(match) == 2 for m, n in [match] if m.distance < 0.75 * n.distance]

            if len(good) > max_good_matches:
                max_good_matches = len(good)
                best_label = label

    return best_label, max_good_matches


def detect_puzzle_pieces(img, template_dir):
    orb = cv2.ORB_create()
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

    templates = load_templates(template_dir)
    original = img.copy()

    # 把圖轉為灰階並模糊去噪
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 用Canny偵測邊緣
    edges = cv2.Canny(blurred, 40, 80)

    # 膨脹邊緣讓輪廓封閉
    kernel = np.ones((5,5), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)
    eroded = cv2.erode(dilated, kernel, iterations=1)

    # 找輪廓
    contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area < 1000 or area > 10000:  # 設定合理的大小範圍
            continue
        x, y, w, h = cv2.boundingRect(cnt)
        piece = extract_aligned_piece(img, cnt)

        label, match_count = match_piece_to_templates(piece, templates, matcher, orb)
        if label:
            rect = cv2.minAreaRect(cnt)
            box = np.intp(cv2.boxPoints(rect))
            cv2.drawContours(original, [box], 0, (0,255,0), 2)
            cv2.putText(original, label, (x+w//2, y+h//2), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    return original


def main():
    cap = cv2.VideoCapture(r'final\prob_1\puzzle.mp4')
    ret, frame = cap.read()
    while ret:
        result = detect_puzzle_pieces(frame, "final/prob_1/train_set/manual")
        cv2.imshow("Result", result)
        ret, frame = cap.read()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()