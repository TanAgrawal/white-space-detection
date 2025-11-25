import cv2 as cv

img = cv.imread("mount.jpg")

resize = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("Resize image",resize)

gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
cv.imshow("gray image", gray)

threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Threshold Image", threshold)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
morph = cv.morphologyEx(threshold, cv.MORPH_OPEN, kernel)

countour, heirarchy = cv.findContours(morph,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)


for cnt in countour:
    area = cv.contourArea(cnt)

    if area>100:
        x,y,w,h =cv.boundingRect(cnt)
        cv.rectangle(resize,(x,y),(x+w,y+h),(0,235,255),2)

cv.imshow("white space",resize)
cv.waitKey(0)