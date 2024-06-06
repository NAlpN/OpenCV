import cv2
import numpy as np

img = cv2.imread('foto2.jpg')
cv2.imshow('Foto', img)

def ceviri(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    boyutlar = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, boyutlar)

ceviriler = ceviri(img, 100, 100)
cv2.imshow('Cevilirmis Goruntu (Right&Down)', ceviriler)

ceviriler = ceviri(img, -100, 100)
cv2.imshow('Cevilirmis Goruntu (Left&Down)', ceviriler)

ceviriler = ceviri(img, 100, -100)
cv2.imshow('Cevilirmis Goruntu (Right&Up)', ceviriler)

ceviriler = ceviri(img, -100, -100)
cv2.imshow('Cevilirmis Goruntu (Left&Up)', ceviriler)

def dondur(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    boyutlar = (width, height)

    return cv2.warpAffine(img, rotMat, boyutlar)

dondurulmusGoruntu = dondur(img, 45)
cv2.imshow('Dondurulmus Goruntu', dondurulmusGoruntu)

yenidenBoyutlandirma = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Boyutlandirilmis Goruntu', yenidenBoyutlandirma)

flip = cv2.flip(img, -1)
cv2.imshow('Flip', flip)

kesilmisGoruntu = img[100:200, 150:300]
cv2.imshow('Kesilmis Goruntu', kesilmisGoruntu)

cv2.waitKey(0)