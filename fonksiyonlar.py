import cv2

img = cv2.imread('foto2.jpg')

cv2.imshow('Foto', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)

blur = cv2.GaussianBlur(img, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)

canny = cv2.Canny(img, 125, 175)
cv2.imshow('Keskin Kenar', canny)

dilated = cv2.dilate(img, (7, 7), iterations=3)
cv2.imshow('Genisletilmis Gorsel', dilated)

eroded = cv2.erode(img, (7, 7), iterations=3)
cv2.imshow('Asinma', eroded)

resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Yeniden Boyutlandirilmis', resized)

cropped = img[50:200, 200:400]
cv2.imshow('Kirpilmis', cropped)

cv2.waitKey(0)