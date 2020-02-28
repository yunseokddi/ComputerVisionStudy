import cv2
import numpy as np
import matplotlib.pyplot as plt

blk_size = 9
c = 5
img = cv2.imread("../img/sudoku.png", cv2.IMREAD_GRAYSCALE)

ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blk_size, c)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, blk_size, c)

imgs = {'orignal': img, 'global otsu' : th1, 'Adapt': th2, 'gaussian': th3}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 2, i + 1)
    plt.title(k)
    plt.imshow(v, 'gray')
    plt.xticks([]), plt.yticks([])

plt.show()
