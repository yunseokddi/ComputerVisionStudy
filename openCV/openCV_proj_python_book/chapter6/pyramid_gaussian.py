import cv2

img = cv2.imread('../img/girl.jpg')

smaller = cv2.pyrDown(img)
bigger = cv2.pyrUp(img)

cv2.imshow('img', img)
cv2.imshow('small', smaller)
cv2.imshow('bigger', bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()