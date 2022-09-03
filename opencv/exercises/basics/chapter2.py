#!/usr/bin/env python3
# Basic functions 

__author__ = "Cristian Chitiva"
__date__ = "September 12, 2021"
__email__ = "cychitivav@unal.edu.co"


import cv2 
import numpy as np


img = cv2.imread('resources/images/lena.png')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, ksize=(5,5), sigmaX=0)

imgCanny = cv2.Canny(img, threshold1=150, threshold2=200)

k = np.ones((5,5), dtype=np.uint8)
imgDilate = cv2.dilate(imgCanny, kernel=k, iterations=1)
imgErode = cv2.erode(imgDilate, kernel=k, iterations=1)

cv2.imshow('Original image', img)
cv2.imshow('Gray image', imgGray)
cv2.imshow('Blur image', imgBlur)
cv2.imshow('Canny image', imgCanny)
cv2.imshow('Dilate image', imgDilate)
cv2.imshow('Erode image', imgErode)
cv2.waitKey(0)