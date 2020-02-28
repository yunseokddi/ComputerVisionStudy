import cv2
import numpy as np
import matplotlib.pyplot as plt

alpha = 0.5

img1 = cv2.imread("../img/wing_wall.jpg")
img2 = cv2.imread("../img/yate.jpg")

dst = cv2.addWeighted(img1, alpha, img2, (1-alpha), 0)
cv2.imshow("cv2", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()