import cv2
import numpy as np 

'''
Author Name: Manas Gupta
Date : 1:14 AM 2/9/2020
Description : This code will just identify all the objects nearby seen through camera and display their edges 

'''


cap=cv2.VideoCapture(1)

while(1) :
    ret,frame=cap.read()
    
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)

    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=3)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=3)
    edges=cv2.Canny(frame,150,150)

    #cv2.imshow("laplacian",laplacian)
    cv2.imshow("frame",edges)
    #cv2.imshow("res",sobely+sobelx)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()
