import cv2;
import numpy as np;

img=cv2.imread(r"C:\Users\abc\OneDrive\Pictures\download.jpg")


pts1=np.array([[50,50],[450,450],[70,420],[420,70]],np.float32)
pts2=np.array([[0,0],[299,299],[0,299],[299,0]],np.float32)

matrix=cv2.getPerspectiveTransform(pts1,pts2)
img2=cv2.warpPerspective(img,matrix,(299,299))

cv2.imshow("image loaded",img2)
cv2.waitKey(0)