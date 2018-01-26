import cv2
import numpy as np
from classico.faces import FaceDetector as FD
import matplotlib.pyplot as plt
import os

fd = FD()

dir = os.path.join('data','frames','webcam2')
dir_results = os.path.join('data','frames','webcam2_results')

for i in sorted(os.listdir(dir)):
    img = cv2.imread(os.path.join(dir,i))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = fd.detect_face_from_img(img)
    plt.axis('off')
    plt.imshow(img)
    plt.savefig(os.path.join(dir_results,i),bbox_inches='tight')
    plt.close()

