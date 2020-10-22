import cv2
import numpy as np
import os

def func():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('trainer/trainer.yml')
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX

    id = 0

    names = ['NoFace', 'Raghav', 'Ishita', 'Vasu', 'Disha', 'Aarushi']

    cam = cv2.VideoCapture(0)
    cam.set(3, 640)
    cam.set(4, 480)

    minW = 0.1*cam.get(3)
    minH = 0.1*cam.get(4)

    while True:
        ret, img =cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5, minSize = (int(minW), int(minH)),)

        for(x,y,w,h) in faces:
            cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
            id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

            if (confidence < 100):
                id = names[id]
                confidence = "{0}%".format(round(100 - confidence))

                if id == 'Raghav':
                    return id
                elif id == 'Ishita':
                    return id
                elif id == 'Vasu':
                    return id)
                else:
                    print("\n****************************************Try Again****************************************\n")

        cv2.waitKey(5)
        break

    cam.release()
    cv2.destroyAllWindows()

i=func()
print(i)
