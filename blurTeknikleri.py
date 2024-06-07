import cv2

img = cv2.imread('foto2.jpg')
# cv2.imshow('Foto', img)

ortalama = cv2.blur(img, (3,3))
# cv2.imshow('Ortalama Blur', ortalama)

gauss = cv2.GaussianBlur(img, (7,7), 0)
# cv2.imshow('Gaussian Blur', gauss)

medyan = cv2.medianBlur(img,3)
# cv2.imshow('Medyan Blur', medyan)

ciftTarafli = cv2.bilateralFilter(img, 20, 35, 25)
cv2.imshow('iki Tarafli Blur', ciftTarafli)

cv2.waitKey(0)