import cv2
import numpy as np

def main():
    img = cv2.imread(r'Source\Lenna.png')
    shape = img.shape
    noiseNum = 512  # number of noise pixels
    for i in range(noiseNum):
        i_noise = np.random.randint(0, shape[0])
        j_noise = np.random.randint(0, shape[1])
        if (len(shape) == 2): # 灰階
            img[i_noise, j_noise] = 0
        else: # 彩色
            img[i_noise, j_noise] = [0, 0, 0]
    cv2.imwrite(r'week_10\noise_img.png', img)
    dst_1 = cv2.medianBlur(img, 5)  # medium filter
    cv2.imshow('MediumFilter', dst_1)
    dst_2 = cv2.GaussianBlur(img, (3, 3), 1, 1)  # gaussian filter
    cv2.imshow('GaussianFilter', dst_2)
    cv2.imwrite(r'week_10\MediumFilter.png', dst_1)
    cv2.imwrite(r'week_10\GaussianFilter.png', dst_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()