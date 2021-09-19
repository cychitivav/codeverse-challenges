#!/usr/bin/env python3
# Joining images

__author__ = "Cristian Chitiva"
__date__ = "September 12, 2021"
__email__ = "cychitivav@unal.edu.co"



import cv2 
import numpy as np


img = cv2.imread('resources/images/lena.png')

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))


cv2.imshow('Image', img)
cv2.imshow('Horizontal', imgHor)
cv2.imshow('Vertical', imgVer)
cv2.waitKey(0)