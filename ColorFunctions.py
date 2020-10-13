import cv2;
img=cv2.imread(r"C:\Users\abc\OneDrive\Pictures\wallpapers\wp3131108.jpg")
# gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("image loaded",gray_img)

# blur_img=cv2.GaussianBlur(img,(7,7),0)
# cv2.imshow("image loaded",blur_img)

canny_img=cv2.Canny(img,200,100,edges=3)
# cv2.imshow("image loaded",canny_img)

# dilated_img=cv2.dilate(canny_img,(5,5),iterations=1)
# cv2.imshow("image loaded",dilated_img)

eroded_img=cv2.erode(canny_img,(5,5),iterations=1)
cv2.imshow("image loaded",eroded_img)

cv2.waitKey(0)