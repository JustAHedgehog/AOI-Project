import cv2

img=cv2.imread(r'Week7_hw\Lenna.png') #將lena.png讀進來
cv2.imshow("orginal_image",img) #顯示原始影像
print(img.shape) #查看圖片大小
img_1 = img.copy() #複製一個新的影像
img_2 = img_1[0:50,0:50] #指定影像左上角50x50
img_3 = img_1[462:512,462:512] #指定影像右下角50x50
img[462:512,462:512]=img_2 #將圖片的兩個區塊對調
img[0:50,0:50]=img_3
cv2.imshow("modified_image",img) #顯示調整過後的影像
key=cv2.waitKey(0)
cv2.destroyAllWindows()
