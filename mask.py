import cv2
import numpy as np

img = cv2.imread('foto2.jpg')
# cv2.imshow('Foto', img)

blank = np.zeros(img.shape[:2], dtype= 'uint8')
# cv2.imshow('Bos Goruntu', blank)

mask = cv2.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
# cv2.imshow('Maskeli Bos Goruntu', mask)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('Maskeli Dolu Goruntu', masked)

cv2.waitKey(0)