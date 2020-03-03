import cv2
import numpy as np

img = cv2.imread('../img/fish.jpg')

rows = img.shape[0]
cols = img.shape[1]

dx, dy = 100, 50

mtrx = np.float32([[1, 0, dx], [0, 1, dy]])

dst = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy))

dst2 = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy), None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT, (255, 0, 0))

dst3 = cv2.warpAffine(img, mtrx, (cols + dx, rows + dy), None, cv2.INTER_LINEAR, cv2.BORDER_REFLECT)

cv2.imshow('orginal', img)
cv2.imshow('transformation', dst)
cv2.imshow('border_constant', dst2)
cv2.imshow('border_feflect', dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()