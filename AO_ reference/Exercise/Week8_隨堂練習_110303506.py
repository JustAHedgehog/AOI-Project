import cv2

img = cv2.imread(r"circle_BGR.jpg")
print(img.shape)
tmp = 0
tmp_2 = 0
tmp_3 = 0
for i in range(0,400):
    for j in range(0,500):
        if img[i,j,0] > 100:
            tmp +=1
        elif img[i,j,1] > 100:
            tmp_2 +=1
        elif img[i,j,2] > 100:
            tmp_3 +=1

print(f"B = {tmp}, G = {tmp_2}, R = {tmp_3}")
