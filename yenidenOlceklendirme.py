import cv2

def olceklendirme(frame, olcek = 0.5):
    width = int(frame.shape[1] * olcek)
    height = int(frame.shape[0] * olcek)
    boyutlar = (width, height)

    return cv2.resize(frame, boyutlar, interpolation= cv2.INTER_AREA)

cap = cv2.VideoCapture('video.mp4')

while True:
    isTrue, frame = cap.read()
    olceklendirilmis_frame = olceklendirme(frame)

    cv2.imshow('Video', frame)
    cv2.imshow('Ölçeklendirilmiş Video', olceklendirilmis_frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break