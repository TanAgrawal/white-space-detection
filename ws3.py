import cv2
import numpy as np

img = cv2.imread('omr.png')

image = cv2.resize(img,(500,500))
cv2.imshow('original',image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, white_mask = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

white_mask_bgr = cv2.cvtColor(white_mask, cv2.COLOR_GRAY2BGR)

result = cv2.bitwise_and(image, white_mask_bgr)

cv2.imshow('White on Black Canvas', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
