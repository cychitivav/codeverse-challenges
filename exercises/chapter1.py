#!/usr/bin/env python3
# Read images-videos-webcam

__author__ = "Cristian Chitiva"
__date__ = "September 12, 2021"
__email__ = "cychitivav@unal.edu.co"


import cv2
print('Package imported')

# IMAGES
img = cv2.imread('exercises/images/street.jpg')

cv2.imshow('Street',img)
cv2.waitKey(0)

# VIDEOS
cap = cv2.VideoCapture('videos/galope.mp4')

while True:
    success, frame = cap.read()
    cv2.imshow('video',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# WEBCAM
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    success, frame = cap.read()
    cv2.imshow('video',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break