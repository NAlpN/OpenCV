import cv2
import numpy as np

blank = np.zeros((400,400), dtype=('uint8'))

dikdortgen = cv2.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cember = cv2.circle(blank.copy(), (200,200), 200, 255, -1)

# cv2.imshow('Dikdortgen', dikdortgen)
# cv2.imshow('Cember', cember)

dikdortgen_and = cv2.bitwise_and(dikdortgen, cember)
# cv2.imshow('Dikdortgen ve Cember', dikdortgen_and)

dikdortgen_or = cv2.bitwise_or(dikdortgen, cember)
# cv2.imshow('Dikdortgen veya Cember', dikdortgen_or)

dikdortgen_xor = cv2.bitwise_xor(dikdortgen, cember)
# cv2.imshow('Dikdortgen XOR', dikdortgen_xor)

dikdortgen_not = cv2.bitwise_not(dikdortgen)
cv2.imshow('Dikdortgen NOT', dikdortgen_not)

cv2.waitKey(0)