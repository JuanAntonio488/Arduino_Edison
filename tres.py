import cv2
import urllib
import time
import numpy as np
import mraa
from Servo import *
myServo = Servo("Servo")
myServo.attach(9)

def getFrame(Camera_IP):

        imageFile = urllib.URLopener()
        imageFile.retrieve("http://"+ Camera_IP + ":8080/shot.jpg", 'shot.jpg')

def main():
        
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        camIP = raw_input("Insert your android camera's IP: ")

        while(1):
                getFrame(camIP)
                img = cv2.imread('shot.jpg',0)
                faces = face_cascade.detectMultiScale(img, 1.3, 5)
                if len (faces) > 0:
                        print ("Rostro Detectado!")
                        for angle in range(0,180):
                                myServo.write(angle)
                                time.sleep(0.005)
                        # From 180 to 0 degrees
                        for angle in range(180,-1,-1):
                                myServo.write(angle)
                                time.sleep(0.005)
                else:
                        print("Buscando rostro...")
                
                # time.sleep(1) # Delay 1 seg

                if cv2.waitKey(25) == 27:
                        break

main()
