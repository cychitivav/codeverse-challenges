#!/usr/bin/env python3
# Face detection (Viola and Jones method)

__author__ = "Cristian Chitiva"
__date__ = "September 12, 2021"
__email__ = "cychitivav@unal.edu.co"

import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier()
faceCascade.load('exercises/resources/haarcascade_frontalface_default.xml')


cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

retval = -1
while retval < 0:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.1, minNeighbors=4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, pt1=(x,y), pt2=(x+w,y+h), color=(255,0,0), thickness=2)


    cv2.imshow('Original',img)
    retval = cv2.waitKey(1)