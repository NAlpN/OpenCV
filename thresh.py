import cv2

img = cv2.imread('foto2.jpg')
# cv2.imshow('Foto', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)

esik, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
# cv2.imshow('Basit Esikli Gorsel', thresh) 

esik, thresh_inv = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('Ters Basit Esik Gorseli', thresh_inv) 

uyarlanabilir_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)
cv2.imshow('Uyarlanabilir Harman Goruntu', uyarlanabilir_thresh)

cv2.waitKey(0)