#Read an RGB image and convert it to Gray image

import cv2

image=cv2.imread('abc1.jpeg')
cv2.imshow('orginal',image)
cv2.waitKey()

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()