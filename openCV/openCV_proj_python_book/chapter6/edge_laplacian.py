import cv2
import numpy as np

img = cv2.imread('../img/sudoku.jpg')

edge = cv2.Laplacian(img, -1)

merged = np.hstack((img,edge))

cv2.imshow('laplacian', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()