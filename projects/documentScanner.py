#!/usr/bin/env python3
# Document Scanner

__author__ = "Cristian Chitiva"
__date__ = "September 16, 2021"
__email__ = "cychitivav@unal.edu.co"

import cv2
import numpy as np


def preProcessing(image):
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, ksize=(5, 5), sigmaX=1)
    imgCanny = cv2.Canny(imgBlur, threshold1=75, threshold2=75)

    k = np.ones((3, 3))
    imgDilate = cv2.dilate(imgCanny, kernel=k, iterations=2)
    imgThresh = cv2.erode(imgDilate, kernel=k, iterations=1)

    cv2.imshow('Threshold', imgThresh)
    return imgThresh


def getCorners(image):
    w = image.shape[0]
    h = image.shape[1]
    biggest = np.array([[[0, 0],
                         [w, 0],
                         [w, h],
                         [0, h]]])
    maxArea = 0

    imgContour = image.copy()
    image = preProcessing(image)
    contours, _ = cv2.findContours(
        image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            # cv2.drawContours(imgContour, contours=cnt, contourIdx=-1, color=(255,0,0), thickness=3)
            peri = cv2.arcLength(cnt, closed=True)
            approx = cv2.approxPolyDP(cnt, epsilon=0.02*peri, closed=True)

            if area > maxArea and len(approx) == 4:
                biggest = approx
                maxArea = area

    cv2.drawContours(imgContour, contours=biggest, contourIdx=-1, color=(255, 0, 0), thickness=20)
    cv2.imshow('Contours', imgContour)
    return biggest

def reorder(corners):
    corners = corners.reshape((4,2))
    newCorners = np.zeros((4,1,2))
    
    add = np.sum(corners, axis=1)
    newCorners[0] = corners[np.argmin(add)]
    newCorners[3] = corners[np.argmax(add)]
    
    diff = np.diff(corners, axis=1)
    newCorners[1] = corners[np.argmin(diff)]
    newCorners[2] = corners[np.argmax(diff)]
    
    return newCorners

def getWarp(image, corners):
    width, height = [480, 640]

    pts1 = np.float32(reorder(corners))
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    return cv2.warpPerspective(img, M=matrix, dsize=(width, height))


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    retval = -1
    while retval < 0:
        success, img = cap.read()
        # img = cv2.flip(img, flipCode=1)

        imgThresh = preProcessing(img)
        corners = getCorners(img)

        plainSheet = getWarp(img, corners)

        cv2.imshow('Original', img)        
        cv2.imshow('Warp', plainSheet)
        retval = cv2.waitKey(1)
