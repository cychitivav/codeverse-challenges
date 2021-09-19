#!/usr/bin/env python3
# Shapes and texts

__author__ = "Cristian Chitiva"
__date__ = "September 12, 2021"
__email__ = "cychitivav@unal.edu.co"


import cv2 
import numpy as np


img = np.zeros((512,512,3), dtype=np.uint8)
print(img.shape)

# img[200:300,100:300]= [255,0,0]
cv2.line(img, pt1=(10,10), pt2=(300,150), color=(0,255,0), thickness=3)
cv2.rectangle(img, pt1=(80,80), pt2=(120,120), color=(0,0,255), thickness=2)
cv2.circle(img, center=(400,400), radius=80, color=(255,0,0), thickness=cv2.FILLED)
cv2.putText(img, text='hi world', org=(300,100), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1, color=(255,255,0), thickness=1)

cv2.imshow('Image', img)
cv2.waitKey(0)