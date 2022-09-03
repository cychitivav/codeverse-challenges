#!/usr/bin/env python3
# Virtual paint

__author__ = "Cristian Chitiva"
__date__ = "September 12, 2021"
__email__ = "cychitivav@unal.edu.co"

import cv2
import numpy as np


def findColor(img, lowerArray=[5, 0, 0], upperArray=[107, 19, 255]):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)    
    mask = cv2.inRange(imgHSV, np.array(lowerArray), np.array(upperArray))

    cv2.imshow('Mask', mask)
    return mask

def getTip(image, colorImg):
    contours, _ = cv2.findContours(image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    
    x, y, w, h = [0, 0, 0, 0]
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        # print(area)
                
        if area > 200:
            # cv2.drawContours(colorImg, contours=cnt, contourIdx=-1, color=(255,0,0), thickness=3)
            
            x, y, w, h = cv2.boundingRect(cnt)            
            # cv2.rectangle(colorImg, pt1=(x,y), pt2=(x+w,y+h), color=(0,255,0), thickness=2)
     
    return x+w//2, y, tuple(colorImg[y+h//2, x+w//2].tolist())
            
def empty(arg):
    pass

def getLimits():
    cv2.namedWindow('Mask')
    cv2.resizeWindow('Mask',640,240)
    cv2.createTrackbar('Hue min', 'Mask', 106, 255, empty)
    cv2.createTrackbar('Hue max', 'Mask', 152, 255, empty)

    cv2.createTrackbar('Sat min', 'Mask', 0, 255, empty)
    cv2.createTrackbar('Sat max', 'Mask', 255, 255, empty)

    cv2.createTrackbar('Val min', 'Mask', 157, 255, empty)
    cv2.createTrackbar('Val max', 'Mask', 255, 255, empty)


if __name__ == '__main__':
    # getLimits()
    cap = cv2.VideoCapture(1)
    canvas = []
    
    retval = -1
    while retval < 0:
        success, img = cap.read()
        img = cv2.flip(img, flipCode=1) 
        
        # h_min = cv2.getTrackbarPos('Hue min', 'Mask')
        # h_max = cv2.getTrackbarPos('Hue max', 'Mask')
        
        # s_min = cv2.getTrackbarPos('Sat min', 'Mask')
        # s_max = cv2.getTrackbarPos('Sat max', 'Mask')
        
        # v_min = cv2.getTrackbarPos('Val min', 'Mask')
        # v_max = cv2.getTrackbarPos('Val max', 'Mask')
        
        # lowerArray = np.array([h_min, s_min, v_min])
        # upperArray = np.array([h_max, s_max, v_max])
        
        lowerArray = np.array([115, 29, 100])
        upperArray = np.array([152, 204, 255])
        
        mask = findColor(img, lowerArray, upperArray)
        canvas.append(getTip(mask, img))
        
        for x, y, colorTip in canvas:
            cv2.circle(img, center=(x,y), radius=10, color=tuple(colorTip), thickness=cv2.FILLED)

        cv2.imshow('Original', img)
        retval = cv2.waitKey(1)