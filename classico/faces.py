import numpy as np
import cv2
import os

class FaceDetector:

    eyes=None,
    face_cascade = None
    eye_cascade = None

    def __init__(self,face_cascade='haarcascade_frontalface_default.xml',eye_cascade = 'haarcascade_eye.xml', eyes=True):

        self.eyes = eyes
        self.face_cascade = cv2.CascadeClassifier(face_cascade)

        if(self.eyes):
            self.eye_cascade = cv2.CascadeClassifier(eye_cascade)


    def detect_face_from_img(self,image):
        #check if image is greyscale, if not convert to gs

        if(len(image.shape)==3):
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        else:
            gray = np.copy(image)

        faces = self.face_cascade.detectMultiScale(gray, 1.2, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = image[y:y + h, x:x + w]

            if(self.eyes):
                eyes = self.eye_cascade.detectMultiScale(roi_gray)
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


        return image