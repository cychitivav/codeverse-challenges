#!/usr/bin/env python3
# Color detection

__author__ = "Cristian Chitiva"
__date__ = "September 12, 2021"
__email__ = "cychitivav@unal.edu.co"



import cv2 
import numpy as np


def empty(arg):
    pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars',640,240)
cv2.createTrackbar('Hue min', 'TrackBars', 49, 255, empty)
cv2.createTrackbar('Hue max', 'TrackBars', 116, 255, empty)

cv2.createTrackbar('Sat min', 'TrackBars', 133, 255, empty)
cv2.createTrackbar('Sat max', 'TrackBars', 255, 255, empty)

cv2.createTrackbar('Val min', 'TrackBars', 0, 255, empty)
cv2.createTrackbar('Val max', 'TrackBars', 255, 255, empty)

retval = -1
while retval < 0:
    img = cv2.imread('resources/images/lambo.jpg')

    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue max', 'TrackBars')
    
    s_min = cv2.getTrackbarPos('Sat min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat max', 'TrackBars')
    
    v_min = cv2.getTrackbarPos('Val min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Val max', 'TrackBars')
    
    lowerArray = np.array([h_min, s_min, v_min])
    upperArray = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lowerArray, upperArray)
    
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow('Original', img)
    cv2.imshow('HSV', imgHSV)
    cv2.imshow('TrackBars', mask)
    cv2.imshow('Result', imgResult)
    
    retval = cv2.waitKey(1)