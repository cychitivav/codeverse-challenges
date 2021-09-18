#!/usr/bin/env python3
# Warp perspective

__author__ = "Cristian Chitiva"
__date__ = "September 12, 2021"
__email__ = "cychitivav@unal.edu.co"


import cv2
import numpy as np


img = cv2.imread('exercises/images/cards.jpg')

width, height = [250, 350]
pts1 = np.float32([[802, 94], [1175, 264], [892, 972], [465, 761]])
pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

imgOutput = cv2.warpPerspective(img, M=matrix, dsize=(width, height))


cv2.imshow('Image', img)
cv2.imshow('Output', imgOutput)
cv2.waitKey(0)
