import os
import cv2
import numpy as np

siniflar = ['Chris Evans', 'Chris Hemsworth', 'Mark Ruffalo', 'Robert Downey Jr', 'Scarlett Johansson']
PATH = r'C:/Users/alpnn/Masaüstü/Python-Dosyaları/OpenCV/data/train'
haar_cascade = cv2.CascadeClassifier('hear_face.xml')

features = []
labels = []

def create_train():
    for person in siniflar:
        path = os.path.join(PATH, person)
        label = siniflar.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv2.imread(img_path)
            gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

features = np.array(features, dtype= 'object')
labels = np.array(labels)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

face_recognizer.save('yuzTanima_train.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)