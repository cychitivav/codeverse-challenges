#!/usr/bin/env python3
# Contours, shape detection

__author__ = "Cristian Chitiva"
__date__ = "September 12, 2021"
__email__ = "cychitivav@unal.edu.co"


import cv2
import numpy as np

def getContours(image):
    contours, Hierarchy = cv2.findContours(image, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
                
        if area > 500:
            cv2.drawContours(imgContour, contours=cnt, contourIdx=-1, color=(255,0,0), thickness=3)
            perimeter = cv2.arcLength(curve=cnt, closed=True)
            print(perimeter)
            approx = cv2.approxPolyDP(curve=cnt, epsilon=0.02*perimeter, closed=True)
            objCor = len(approx)
            
            x, y, width, height = cv2.boundingRect(approx)
            
            if objCor == 3:
                objType = 'Tri'
            elif objCor == 4:
                aspRatio = width/float(height)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objType = 'Square'
                else:
                    objType = 'Rect'
            elif objCor > 4:
                objType = 'Circle'
            else:
                objType = 'None'                
                        
            cv2.rectangle(imgContour, pt1=(x,y), pt2=(x+width,y+height), color=(0,255,0), thickness=2)
            cv2.putText(imgContour, text=objType, org=(x+width//2, y+height//2), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5, color=(0,0,0), thickness=2)
    

# IMAGES
img = cv2.imread('exercises/images/shapes.png')
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, ksize=(7,7), sigmaX=1)
imgCanny = cv2.Canny(imgBlur, threshold1=50, threshold2=50)

getContours(imgCanny)



cv2.imshow('Original',img)
cv2.imshow('Gray',imgGray)
cv2.imshow('Blur',imgBlur)
cv2.imshow('Canny',imgCanny)
cv2.imshow('Contours',imgContour)
cv2.waitKey(0)