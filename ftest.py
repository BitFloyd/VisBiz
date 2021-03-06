import cv2
import numpy as np
from classico.faces import FaceDetector as FD
import matplotlib.pyplot as plt
import os
import sys

fd = FD(face_cascade=os.path.join('..','data_folder','haarcascades','haarcascade_frontalface_default.xml'),
        face_profile_cascade=os.path.join('..','data_folder','haarcascades','haarcascade_frontalface_default.xml'),
        eye_cascade=None,
        eyes=False)

dir = os.path.join('..','data_folder','frames','webcam1_frames')
assert os.path.exists(dir),'Directory '+dir+' does not exist'


dir_results = os.path.join('..','data_folder','frames','webcam1_results')

if(not os.path.exists(dir_results)):
    os.makedirs(dir_results)

for i in sorted(os.listdir(dir)):
    img = cv2.imread(os.path.join(dir,i))
    img = fd.detect_face_from_img(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite(os.path.join(dir_results,i),img)


dir = os.path.join('..','data_folder','frames','webcam2_frames')
assert os.path.exists(dir),'Directory '+dir+' does not exist'


dir_results = os.path.join('..','data_folder','frames','webcam2_results')

if(not os.path.exists(dir_results)):
    os.makedirs(dir_results)

for i in sorted(os.listdir(dir)):
    img = cv2.imread(os.path.join(dir,i))
    img = fd.detect_face_from_img(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite(os.path.join(dir_results, i),img)
