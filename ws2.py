import cv2 as cv
import numpy as np

img = cv.imread("omr.png")

resize = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("Resize image",resize)

gray = cv.cvtColor(resize,cv.COLOR_BGR2GRAY)
cv.imshow("gray image", gray)

blank= np.ones_like(gray) * 255  # White background


threshold = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow("Threshold Image", threshold)

kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
morph = cv.morphologyEx(threshold, cv.MORPH_OPEN, kernel)
cv.imshow("Morph Image", morph)

countour,heirarchy = cv.findContours(morph,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
for cnt in countour:
    area = cv.contourArea(cnt)
    if area > 100:  # Adjust threshold as needed
        cv.drawContours(blank, [cnt], -1, 0, -1)  # Fill with black to mark white space

cv.imshow("final",blank)

cv.waitKey(0)