import cv2

def get_pixel_rgb(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        b, g, r = img[y, x]
        print(f"Pixel at ({x}, {y}) - RGB: ({r}, {g}, {b})")
cap = cv2.VideoCapture('Exercise/1.mp4')
ret,img = cap.read()
while ret:
    ret,img = cap.read()
# dim = (720,360)
# resized = cv2.resize(img, dim)
    cv2.imshow('image',img)
    # ret,img = cap.read()
cv2.setMouseCallback('image', get_pixel_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()