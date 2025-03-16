import numpy as np
import cv2



def main():

    #創建三個黑色影像
    b = np.zeros([300,300,3],dtype='uint8')
    g = np.zeros([300,300,3],dtype='uint8')
    r = np.zeros([300,300,3],dtype='uint8')

    #畫三個原色的圓形
    cv2.circle(b, (150,167), 67, (255,0,0), -1)
    cv2.circle(g, (200,100), 67, (0,255,0), -1)
    cv2.circle(r, (100,100), 67, (0,0,255), -1)

    #用cv2.add()
    output_1 = cv2.add(b,g)
    output_1 = cv2.add(output_1,r)

    #用cv2.addWeighr()
    output_2 = cv2.addWeighted(b,0.7,g,0.7,0)
    output_2 = cv2.addWeighted(output_2,0.7,r,0.7,0)

    cv2.imshow('use add image',output_1)
    cv2.imshow('use addWeight image',output_2)
    key=cv2.waitKey(0)

if __name__=='__main__':
    main()