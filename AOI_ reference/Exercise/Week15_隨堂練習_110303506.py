import numpy as np; import cv2; import glob
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

def camCaptureChessBoard():
    cap=cv2.VideoCapture(0)
    a, b=cap.read()
    i=0
    while a:
        a, b=cap.read()
        h,w,_=b.shape
        xy_axes(b,w,h)
        cv2.imshow("img0",b)
        if cv2.waitKey(1) & 0xff==ord("o"):
            ret, frame=cap.read()
            if ret==True:
                cv2.imwrite("Exercise/Picture/testBoard%d.jpg"%i,frame)
                print (i)
                i=i+1
        if cv2.waitKey(1) & 0xff==ord("q"):
            break
    cv2.waitKey()
    cv2.destroyAllWindows()
    cap.release()

def CBxyzNuv():
    objp = np.zeros((11*8,3), np.float32)# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
    objp[:,:2] = np.mgrid[0:8,0:11].T.reshape(-1,2) #世界座標
    
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    images = glob.glob('Exercise/Picture/testBoard*.jpg')
    
    for fname in images:
        img = cv2.imread(fname)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (8,11))    # Find the chess board corners
        # 輸入輸入棋盤格灰階圖片，和棋盤內角點數
        # 輸出布林值ret & 檢測到角點數組corners
        
        if ret == True:       # If found, add object points, image points (after refining them)
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            # 找更精準的角點座標
            # 輸入輸入棋盤格灰階圖片，檢測到角點數組，
            # winSize: kernel size，設定一範圍進行搜尋
            # zeroZone: 影像基點位置不進行搜尋，-1,-1表示不使用此功能
            # criteria: 迭代的方法
            # cv2.TERM_CRITERIA_EPS: 找到最小精確點停止 0.001
            # cv2.TERM_CRITERIA_MAX_ITER: 最大迭代次數 30            
            imgpoints.append(corners2)            
    return objpoints, imgpoints,gray.shape[::-1]

def putext(image, text, x,y):
    cv2.putText ( image, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, .8, (0, 0, 255), 2, cv2.LINE_AA)

def xy_axes(image, w,h):
    cv2.line(image,(0,int(h/2)),(w,int(h/2)),(0,255,0),1)
    cv2.line(image,(int(w/2),0),(int(w/2),h),(0,255,0),1)
    cv2.circle(image,(int(w/2),int(h/2)),8,(0,255,0),1)

def camClibration (objpoints, imgpoints, imgshape):
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, imgshape ,None,None)
    # 世界座標objpoints，影像座標角點imgpoints，影像大小imgshape
    # mtx: 相機内參矩陣，dist: 畸變參數矩陣
    # rvecs: 旋轉矩陣，tvecs: 平移距離
    np.save("Exercise/M.npy",mtx)
    np.save("Exercise/D.npy",dist)
    # np.save("D:/w15/R.npy",rvecs)
    # np.save("D:/w15/T.npy",tvecs)
    cv2.destroyAllWindows()
    # print(mtx)
    # print(dist)
    
def drawImgAxes(img, corners, imgpts):
    corner=(int(corners[0,0,0]), int(corners[0,0,1])) # 棋盤格的原點(第一個點
    Xaxis=(int(imgpts[0,0,0]), int(imgpts[0,0,1])) # 影像上的X向量(從棋盤格原點~這個座標點
    Yaxis=(int(imgpts[1,0,0]), int(imgpts[1,0,1])) # 影像上的Y向量
    Zaxis=(int(imgpts[2,0,0]), int(imgpts[2,0,1])) # 影像上的Z向量
    img = cv2.line(img, corner, Xaxis, (255,0,0), 5) # 畫線 從棋盤格原點畫到Xaxis這個座標點
    img = cv2.line(img, corner, Yaxis, (0,255,0), 5)
    img = cv2.line(img, corner, Zaxis, (0,0,255), 5)


if __name__=="__main__":
    YN=input("Would you like to capture the testBoard images for calibration? y/n? " )
    if YN =="y": # 進行相機校正
        # camCaptureChessBoard() # 先拍棋盤格
        objp, imgp, imgshape=CBxyzNuv() 
        camClibration (objp, imgp, imgshape)

    mtx=np.load("Exercise/M.npy")
    dist=np.load("Exercise/D.npy")
    cx=int(mtx[0,2]); cy=int(mtx[1,2]) # 相機校正後的畫面中心
    objp = np.zeros((8*11,3), np.float32)
    objp[:,:2] = np.mgrid[0:11,0:8].T.reshape(-1,2) #世界座標
    axis = np.float32([[3,0,0], [0,3,0], [0,0,-3]]) # 棋盤格世界座標的XYZ軸向量(投影用
    
    cap=cv2.VideoCapture('Exercise/1111.mp4')
    a, img=cap.read()
    while a:
        a, img=cap.read()
        h,w,_=img.shape
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret, corners = cv2.findChessboardCorners(gray, (11,8),None)
        #
        
        if ret == True:
            corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
            #
            
            ret,rvecs, tvecs, inliers= cv2.solvePnPRansac(objp, corners2, mtx, dist)# Find the rotation and translation vectors.#(don't forget "ret" in front of rvecs)
            # solvePnPRansac 找相機與棋盤格之間的相對距離跟相對姿態
            # 輸入世界座標objp，棋盤格角點座標corner2，mtx: 相機内參矩陣，dist: 畸變參數
            # rvecs: 旋轉矩陣，tvecs: 平移距離，inliers: 內部參數
        
            imgpts, jac = cv2.projectPoints(axis, rvecs, tvecs, mtx, dist)# project 3D points to image plane
            # axis: 用來投影XYZ軸向量
            #imgpts: axis世界座標的XYZ軸經轉換後顯示再影像上的XYZ軸
            
            drawImgAxes(img, corners2, imgpts)
            
            x,y,z=np.round(tvecs[0],1), np.round(tvecs[1],1), np.round(tvecs[2],1)
            l=np.sqrt(x**2+y**2+z**2) #相機相對於世界座標原點的距離
            textXYZ="(x,y,z)=("+ str(x[0])+", "+str(y[0])+", "+str(z[0])+")"
            k=180/np.pi
            alpha, beta, gamma=np.round(rvecs[0]*k,1), np.round(rvecs[1]*k,1), np.round(rvecs[2]*k,1)
            textABC="(a,b,c)=("+ str(alpha[0])+", "+str(beta[0])+", "+str(gamma[0])+")"
            putext(img,textXYZ,30,60)
            putext(img,textABC,30,90)
            putext(img,"l="+str(int(l)), 30,30)
            
            xy_axes(img,w,h)
            
            cv2.circle(img,(cx,cy),8,(255,0,0),2)
            cv2.imshow('img',img)
        else:
            cv2.imshow('img',img)
        if cv2.waitKey(1) & 0xff==ord("f"):
            break


cap.release()
cv2.waitKey()
cv2.destroyAllWindows()
