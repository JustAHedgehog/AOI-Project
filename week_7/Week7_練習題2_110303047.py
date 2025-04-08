import cv2

#若今天圖片是在其他工作目錄，則可以絕對路徑/相對路徑指定該圖片

img_1=cv2.imread(r'Source\Lenna.png') #相對路徑
img_2=cv2.imread(r'D:\AOI-Project\Source\Lenna.png') #絕對路徑
cv2.imshow("relative_path",img_1)
cv2.imshow("absolute_path",img_2)
key=cv2.waitKey(0)