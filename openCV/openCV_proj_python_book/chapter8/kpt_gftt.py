import cv2
import numpy as np

img = cv2.imread('../img/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

gftt = cv2.GFTTDetector_create()
keypoints = gftt.detect(gray, None)
img_draw = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow('GFTTDetector', img_draw)
cv2.waitKey()
cv2.destroyAllWindows()