#!/usr/bin/env python3
# Resizing and cropping

__author__ = "Cristian Chitiva"
__date__ = "September 12, 2021"
__email__ = "cychitivav@unal.edu.co"


import cv2

img = cv2.imread('exercises/images/lambo.jpg')
print(img.shape)

imgResized = cv2.resize(img, dsize=(600,300))
print(imgResized.shape)

imgCropped = img[50:200,100:800]

cv2.imshow('Image', img)
cv2.imshow('Resized', imgResized)
cv2.imshow('Cropped', imgCropped)
cv2.waitKey(0)