import numpy as np
import cv2

haar_cascade = cv2.CascadeClassifier('hear_face.xml')

siniflar = ['Chris Evans', 'Chris Hemsworth', 'Mark Ruffalo', 'Robert Downey Jr', 'Scarlett Johansson']
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('yuzTanima_train.yml')

img = cv2.imread('C:/Users/alpnn/Masaüstü/Python-Dosyaları/OpenCV/data/Robert Downey Jr/robert_downey_jr1.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

yuz_tanima = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in yuz_tanima:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {siniflar[labels]} with a confidence of {confidence}')

    cv2.putText(img, str(siniflar[label]), (20, 20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv2.imshow('Taninan Yuz', img)
cv2.waitKey(0) 