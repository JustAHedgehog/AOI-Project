import cv2

def main():
    img = cv2.imread('Week12_hw/0518_5p.png')
    cv2.imshow('test', img)
    edges = cv2.Canny(img, 10,50)
    cv2.imshow('edge',edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()