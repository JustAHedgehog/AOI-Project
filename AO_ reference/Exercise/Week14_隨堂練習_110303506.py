# Pixel at (126, 250) - RGB: (145, 149, 153)
# Pixel at (123, 243) - RGB: (142, 146, 150)
# Pixel at (127, 235) - RGB: (141, 145, 149)
# Pixel at (136, 231) - RGB: (143, 144, 149)
# Pixel at (143, 236) - RGB: (143, 144, 149)
# Pixel at (152, 244) - RGB: (145, 146, 151)
# Pixel at (154, 245) - RGB: (145, 146, 151)
# Pixel at (158, 251) - RGB: (145, 146, 151)
# Pixel at (163, 256) - RGB: (108, 109, 112)
# Pixel at (166, 255) - RGB: (119, 120, 125)
# Pixel at (169, 262) - RGB: (84, 85, 88)
# Pixel at (174, 273) - RGB: (147, 146, 149)
# Pixel at (180, 279) - RGB: (94, 93, 96)
# Pixel at (182, 284) - RGB: (149, 148, 151)
# Pixel at (182, 289) - RGB: (150, 148, 149)
# Pixel at (177, 297) - RGB: (79, 74, 76)
# Pixel at (178, 303) - RGB: (79, 74, 76)
# Pixel at (178, 311) - RGB: (94, 86, 92)
# Pixel at (181, 320) - RGB: (103, 93, 97)
# Pixel at (184, 326) - RGB: (105, 93, 98)
# Pixel at (184, 329) - RGB: (94, 82, 84)
# Pixel at (183, 333) - RGB: (80, 68, 70)
# Pixel at (168, 332) - RGB: (84, 74, 75)
# Pixel at (159, 329) - RGB: (80, 78, 76)
# Pixel at (152, 329) - RGB: (81, 79, 77)
# Pixel at (151, 334) - RGB: (83, 78, 77)
# Pixel at (146, 315) - RGB: (81, 81, 78)
# Pixel at (135, 309) - RGB: (82, 82, 82)
# Pixel at (133, 297) - RGB: (119, 118, 121)
# Pixel at (128, 292) - RGB: (150, 151, 154)
# Pixel at (119, 292) - RGB: (150, 151, 154)
# Pixel at (114, 283) - RGB: (143, 142, 147)
# Pixel at (116, 269) - RGB: (141, 142, 147)
# Pixel at (154, 336) - RGB: (87, 77, 76)
# Pixel at (160, 339) - RGB: (90, 77, 74)
# Pixel at (166, 343) - RGB: (108, 85, 82)
# Pixel at (166, 349) - RGB: (143, 115, 102)
# Pixel at (166, 353) - RGB: (135, 102, 91)
import cv2
import numpy as np

def findMarker(image):
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(image, (5,5), 0)
    thr = cv2.adaptiveThreshold(blur, 250, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11,2)
    contours,_ = cv2.findContours(thr, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt_max = max(contours, key = cv2.contourArea)
    return cnt_max

def draw_contours(image, cnt_max):
    rect = cv2.minAreaRect(cnt_max)
    box = np.int0(cv2.boxPoints(rect))
    cv2.drawContours(image, [box], 0, (0,0,255), 2)
    return int(rect[0][0]), int(rect[0][1])

def main():
    cap = cv2.VideoCapture('Exercise/1.mp4')
    while True:
        ret, img = cap.read()
        U_red = np.array([80,48,190])
        L_red = np.array([50,30,120])
        mask = cv2.inRange(img, L_red, U_red)
        cnt = findMarker(mask)
        x, y = draw_contours(img, cnt)
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()

