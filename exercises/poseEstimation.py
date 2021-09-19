#!/usr/bin/env python3
# Pose estimation

__author__ = "Cristian Chitiva"
__date__ = "September 18, 2021"
__email__ = "cychitivav@unal.edu.co"

import cv2
import numpy as np
import mediapipe as mp
import time


if __name__ == "__main__":
    cap = cv2.VideoCapture(1)

    mpPose = mp.solutions.pose
    mpDraw = mp.solutions.drawing_utils

    pose = mpPose.Pose(upper_body_only=True)

    prevTime = 0
    while cv2.waitKey(1) < 0:
        success, frame = cap.read()
        frame = cv2.flip(frame, flipCode=1)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        currentTime = time.time()
        fps = int(1/(currentTime - prevTime))
        prevTime = currentTime

        frame = cv2.putText(frame, str(fps), (0, 20),
                            cv2.FONT_HERSHEY_PLAIN, 1.5,
                            (255, 0, 255), 3)
        cv2.imshow('Original', frame)
