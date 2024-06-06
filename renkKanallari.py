import cv2
import numpy as np

img = cv2.imread('foto2.jpg')
# cv2.imshow('Foto', img)

b, g, r = cv2.split(img)

# cv2.imshow('Mavi', b)
# cv2.imshow('Yesil', g)
# cv2.imshow('Kırmızı', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

birlesim = cv2.merge([b, g, r])
# cv2.imshow('Birlestirilmis Goruntu', birlesim)

print(birlesim.shape)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

mavi = cv2.merge([b, blank, blank])
yesil = cv2.merge([blank, g, blank])
kirmizi = cv2.merge([blank, blank, r])

cv2.imshow('Mavi', mavi)
cv2.imshow('Yesil', yesil)
cv2.imshow('Kırmızı', kirmizi)

cv2.waitKey(0)