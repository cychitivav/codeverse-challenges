#!/usr/bin/env python3
# Number plate detection


__author__ = "Cristian Chitiva"
__date__ = "September 17, 2021"
__email__ = "cychitivav@unal.edu.co"

import cv2
import numpy as np


if __name__ == '__main__':
    cap = cv2.VideoCapture(0)

    plateCascade = cv2.CascadeClassifier()
    plateCascade.load(
        'exercises/resources/haarcascade_russian_plate_number.xml')
    minArea = 200

    retval = -1
    while retval < 0:
        success, img = cap.read()
        # img = cv2.flip(img, flipCode=1)

        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        plates = plateCascade.detectMultiScale(
            imgGray, scaleFactor=1.1, minNeighbors=4)

        for (x, y, w, h) in plates:
            area = w*h
            if area > minArea:
                cv2.rectangle(img, pt1=(x, y), pt2=(x+w, y+h),
                              color=(255, 0, 0), thickness=2)
                cv2.putText(img, text='Number plate', org=(x, y-5),
                            fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                            fontScale=1, color=(255, 0, 0), thickness=2)

                imgROI = img[y:y+h, x:x+w]
                cv2.imshow('Plate', imgROI)

        cv2.imshow('Original', img)
        retval = cv2.waitKey(1)
        
    cv2.imwrite('projects/outputs/numberPlate.jpg', imgROI)
