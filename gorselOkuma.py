import cv2

img = cv2.imread('foto.png')

cv2.imshow('Görüntü', img)

cv2.waitKey(0)