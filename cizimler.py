import cv2
import numpy as np

cizim = np.zeros((500, 500, 3), dtype= 'uint8')
cv2.imshow('Cizim', cizim)

cizim[:] = 0, 255, 0
cv2.imshow('Yesil', cizim)

cizim[200:300, 300:400] = 0, 0, 255
cv2.imshow('Kirmizi Kutu', cizim)

cv2.rectangle(cizim, (0, 0), (250, 250), (0, 255, 0), thickness= 2)
cv2.imshow('ici bos dikdörtgen', cizim)

cv2.rectangle(cizim, (0, 0), (cizim.shape[1]//2, cizim.shape[0]//2), (0, 255, 0), thickness= -1)
cv2.imshow('ici dolu dikdörtgen', cizim)

cv2.circle(cizim, (cizim.shape[1]//2, cizim.shape[0]//2), 40, (0, 0, 255), thickness=3)
cv2.imshow('ici bos daire', cizim)

cv2.circle(cizim, (cizim.shape[1]//2, cizim.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv2.imshow('ici dolu daire', cizim)

cv2.line(cizim, (0, 0), (cizim.shape[1]//2, cizim.shape[0]//2), (255, 255, 255), thickness= 3)
cv2.imshow('Cizgi', cizim)

cv2.putText(cizim, 'Alp', (225, 225), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv2.imshow('Yazi', cizim)

cv2.waitKey(0)