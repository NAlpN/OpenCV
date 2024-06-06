import cv2
import matplotlib.pyplot as plt

img = cv2.imread('foto2.jpg')
# cv2.imshow('Foto', img)

# plt.imshow(img)
# plt.show()

siyahBeyaz = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Siyah Beyaz Gorsel', siyahBeyaz)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV', hsv)

lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# cv2.imshow('LAB', lab)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

plt.imshow(rgb)
plt.show()

cv2.waitKey(0)