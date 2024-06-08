import cv2
import numpy as np

img = cv2.imread('foto2.jpg')
# cv2.imshow('Foto', img)

siyahBeyaz = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Siyah Beyaz Goruntu', siyahBeyaz)

lap = cv2.Laplacian(siyahBeyaz, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
# cv2.imshow('Laplacian', lap)

sobelx = cv2.Sobel(siyahBeyaz, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(siyahBeyaz, cv2.CV_64F, 0, 1)
com_sobel = cv2.bitwise_or(sobelx, sobely)

cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Combined Sobel', com_sobel)

cv2.waitKey(0)