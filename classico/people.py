import numpy as np
import cv2
import os

class BodyDetector:

    bcascade = None
    def __init__(self,bcascade='haarcascade_fullbody.xml'):

        self.bcascade = cv2.CascadeClassifier(bcascade)



    def detect_body_from_img(self,image):
        #check if image is greyscale, if not convert to gs

        if(len(image.shape)==3):
            gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        else:
            gray = np.copy(image)

        bodies = self.bcascade.detectMultiScale(gray, 1.2, 4)
        for (x, y, w, h) in bodies:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        return image