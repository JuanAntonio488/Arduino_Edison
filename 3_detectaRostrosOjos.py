import cv2
import sys
import os

faceCascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\opencv\sources\data\haarcascades\haarcascade_eye.xml')

video_capture = cv2.VideoCapture(0)
while (1):
    # Captura frame por frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5) 
    
    # Dibujar un rectangulo en los rostros
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

        gray_face = gray[y:y+h, x:x+w] # cut the gray face frame out
        face = frame[y:y+h, x:x+w] # cut the face frame out
        eyes = eye_cascade.detectMultiScale(gray_face)

        # Dibujar un rectangulo en los ojos
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(0,225,255),2)


    # Muestra los rostros y los ojos con el rectangulito
    cv2.imshow('Video', frame)

    if cv2.waitKey(25) == 27:
        video_capture.release()
        break

# Termino del programa
video_capture.release()
cv2.destroyAllWindows()
