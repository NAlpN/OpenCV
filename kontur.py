import cv2
import numpy as np

img = cv2.imread('foto2.jpg')
cv2.imshow('Foto', img)

blank = np.zeros(img.shape, dtype='uint8')
cv2.imshow('Blank', blank)

siyahBeyaz = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Siyah Beyaz Goruntu', siyahBeyaz)

# blur = cv2.GaussianBlur(siyahBeyaz, (5, 5), cv2.BORDER_DEFAULT)
# cv2.imshow('Blur Goruntu', blur)

keskinKenarlar = cv2.Canny(img, 150, 200)
cv2.imshow('Keskin Kenarlı Goruntu', keskinKenarlar)

# ret, thresh = cv2.threshold(siyahBeyaz, 125, 255, cv2.THRESH_BINARY)
# cv2.imshow('Thresh', thresh)

kontur, asama = cv2.findContours(keskinKenarlar, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(kontur)} kontör bulundu.')

cv2.drawContours(blank, kontur, -1, (0,0,255), 1)
cv2.imshow('Cizdirilmis Kontur', blank)

cv2.waitKey(0)