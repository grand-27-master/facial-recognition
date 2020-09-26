import cv2
import numpy as np
import matplotlib as plt

#we will use convex hull technique 
hand=cv2.imread('0-1007_handprint-outline-finger-clipart-hand-palm-pencil-and.png',0)

ret,thresh=cv2.threshold(hand,70,255,cv2.THRESH_BINARY)

#find connected pixels
contours, hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#find convex hull
hull=[cv2.convexHull(c) for c in contours]
final=cv2.drawContours(hand,hull,-1,(255,0,0))

cv2.imshow('Original image',hand)
cv2.imshow('Thresholded image',thresh)
cv2.imshow('Convex hull',final)
cv2.waitKey(0)
cv2.destroyAllWindows()