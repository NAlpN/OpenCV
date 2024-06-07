import cv2
import matplotlib.pyplot as plt

img = cv2.imread('foto2.jpg')
# cv2.imshow('Foto', img)

siyahBeyaz = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Siyah Beyaz Goruntu', siyahBeyaz)

siyahBeyaz_hist = cv2.calcHist([siyahBeyaz], [0], None, [256], [0, 256])

plt.figure()
plt.title('Siyah Beyaz Görüntü Historgramı')
plt.xlabel('Bins')
plt.ylabel('Pixels')
plt.plot(siyahBeyaz_hist)
plt.xlim([0, 256])
plt.show()

cv2.waitKey(0)