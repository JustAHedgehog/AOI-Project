import cv2

def main():
    img = cv2.imread(r'week_13\A4paper70cm.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    a, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    areas = []
    for contour in contours:
        areas.append(cv2.contourArea(contour))
    target_index = areas.index(max(areas))
    cv2.drawContours(img, contours, target_index, (0, 0, 255), 2)
    cv2.imshow('results', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()