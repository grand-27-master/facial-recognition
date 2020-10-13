import cv2;
import numpy as np;

img=cv2.imread(r"C:\Users\abc\OneDrive\Pictures\rainbow-sq.jpg")

#stacking image with itself
hor_img=np.hstack((img,img))
ver_img=np.vstack((img,img))

cv2.imshow("image loaded",ver_img)
cv2.waitKey(0)