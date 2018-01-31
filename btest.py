import cv2
import numpy as np
from classico.people import BodyDetector as BD
import matplotlib.pyplot as plt
import os
import sys

bd = BD(bcascade=os.path.join('..','data_folder','haarcascades','haarcascade_upperbody.xml'))

dir = os.path.join('..','data_folder','frames','webcam1_frames')
assert os.path.exists(dir),'Directory '+dir+' does not exist'


dir_results = os.path.join('..','data_folder','frames','webcam1_upperbody_results')

if(not os.path.exists(dir_results)):
    os.makedirs(dir_results)

for i in sorted(os.listdir(dir)):
    img = cv2.imread(os.path.join(dir,i))
    img = bd.detect_body_from_img(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.axis('off')
    plt.imshow(img)
    plt.savefig(os.path.join(dir_results,i),bbox_inches='tight')
    plt.close()

dir = os.path.join('..','data_folder','frames','webcam2_frames')
assert os.path.exists(dir),'Directory '+dir+' does not exist'


dir_results = os.path.join('..','data_folder','frames','webcam2_upperbody_results')

if(not os.path.exists(dir_results)):
    os.makedirs(dir_results)

for i in sorted(os.listdir(dir)):
    img = cv2.imread(os.path.join(dir,i))
    img = bd.detect_body_from_img(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.axis('off')
    plt.imshow(img)
    plt.savefig(os.path.join(dir_results,i),bbox_inches='tight')
    plt.close()
