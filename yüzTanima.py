import cv2

# img = cv2.imread('face.jpeg')
img = cv2.imread('topluluk.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier('hear_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

for (x, y, w, h) in faces_rect:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv2.imshow('Yuz Tespiti', img)

cv2.waitKey(0)