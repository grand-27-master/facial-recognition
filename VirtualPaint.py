# import cv2;
# import numpy as np;

# cap=cv2.VideoCapture(0)

# #create a list of color values
# myColors=[[5,107,0,19,255,255],[133,56,0,159,156,255],[57,76,0,100,255,255],[90,48,0,118,255,255]]

# #color values to show
# myValues=[[204,0,204]]

# #create list for displaying lines
# myLines=[] #[x,y,colorID]

# #function for finding different colors
# def findColors(img,myColors,myValues):
#     hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#     #setting up limits

#     #to output all colors
#     count=0
#     newLines=[]
#     for colors in myColors:
#         lower=np.array([colors[0:3]])
#         upper=np.array(colors[3:6])
#         mask=cv2.inRange(hsv_img,lower,upper)
#         x,y=getContours(mask)
#         cv2.circle(imgResult,(x,y),3,myValues[count],2)
#         if x!=0 and y!=0:
#             newLines.append([x,y,count])
#         #cv2.imshow(str(colors[0]),mask)
#     return newLines    

# #to seperate out an object we need to use contour function
# def getContours(img):
#     contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     x,y,w,h = 0,0,0,0
#     for cnt in contours:
#         area = cv2.contourArea(cnt)
#         if area>500:
#             cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
#             peri = cv2.arcLength(cnt,True)
#             approx = cv2.approxPolyDP(cnt,0.02*peri,True)
#             x, y, w, h = cv2.boundingRect(approx)

#     #for tip recognition only
#     return (x+y)//2,y           

# def drawLines(myLines,myValues):
#     for lines in myLines:
#         cv2.circle(imgResult,(lines[0],lines[1]),3,(255,0,0),2)

# while True:
#     frame,img=cap.read()

#     #creating a copy of image
#     imgResult=img.copy()
#     newLines=findColors(img,myColors,myValues)
#     if len(newLines)!=0:
#         for newLine in newLines:
#             myLines.append(newLine)

#     if len(myLines)!=0:
#            drawLines(myLines,myValues)     
#     cv2.imshow("camera started",imgResult)
#     if cv2.waitKey(1)==13:
#         break

# cap.release()
# cv2.destroyAllWindows()    


import cv2
import numpy as np
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
 
myColors = [[5,107,0,19,255,255],
            [133,56,0,159,156,255],
            [57,76,0,100,255,255],
            [90,48,0,118,255,255]]
myColorValues = [[204,0,204],          ## BGR
                 [255,0,255],
                 [0,255,0],
                 [255,0,0]]
 
myPoints =  []  ## [x , y , colorId ]
 
def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y=getContours(mask)
        cv2.circle(imgResult,(x,y),15,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
        #cv2.imshow(str(color[0]),mask)
    return newPoints
 
def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y
 
def drawOnCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)
 
 
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors,myColorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)
 
 
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()    