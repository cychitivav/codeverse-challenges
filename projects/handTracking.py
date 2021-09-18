#!/usr/bin/env python3
# Virtual paint

__author__ = "Cristian Chitiva"
__date__ = "September 13, 2021"
__email__ = "cychitivav@unal.edu.co"

import cv2
import numpy as np
import mediapipe as mp


if __name__ == "__main__":
    cap = cv2.VideoCapture(1)

    mpHands = mp.solutions.hands
    mpDraw = mp.solutions.drawing_utils

    hands = mpHands.Hands()

    while cv2.waitKey(1) < 0:
        success, frame = cap.read()
        frame = cv2.flip(frame, flipCode=1)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frameRGB)
        # print(results.multi_handedness)

        if results.multi_hand_landmarks:
            for handLandmark in results.multi_hand_landmarks:
                mpDraw.draw_landmarks(frame, handLandmark, mpHands.HAND_CONNECTIONS)
                
        

        cv2.imshow('Original', frame)
