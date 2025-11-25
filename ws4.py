import cv2 as cv
import numpy as np

img = cv.imread("omr.png")

image = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("image",image)

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

thres,white_mask = cv.threshold(gray,240,255,cv.THRESH_BINARY)

mask = cv.cvtColor(white_mask,cv.COLOR_GRAY2BGR)

whitespace = cv.bitwise_and(image,mask)
cv.imshow("whitespace",whitespace)

cv.waitKey(0)