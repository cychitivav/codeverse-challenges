#!/usr/bin/env python3
# Hand Tracking

__author__ = "Cristian Chitiva"
__date__ = "September 13, 2021"
__email__ = "cychitivav@unal.edu.co"

import cv2
import numpy as np
import mediapipe as mp
import time


if __name__ == "__main__":
    cap = cv2.VideoCapture(1)

    mpHands = mp.solutions.hands
    mpDraw = mp.solutions.drawing_utils

    hands = mpHands.Hands()

    prevTime = 0
    currentTime = 0
    while cv2.waitKey(1) < 0:
        success, frame = cap.read()
        frame = cv2.flip(frame, flipCode=1)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frameRGB)
        # print(results.multi_handedness)

        if results.multi_hand_landmarks:
            for idx, handLandmark in enumerate(results.multi_hand_landmarks):
                for kp, lm in enumerate(handLandmark.landmark):
                    # print(kp, lm)
                    h, w, c = frame.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    print(kp, cx, cy)

                    if kp%4 == 0:
                        cv2.circle(frame, (cx, cy), 10,
                                   (255, 0, 255), cv2.FILLED)
                    
                    if kp == 0:
                        cv2.putText(frame, results.multi_handedness[idx].classification[0].label, (cx, cy),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), 2)

                mpDraw.draw_landmarks(
                    frame, handLandmark, mpHands.HAND_CONNECTIONS)

        currentTime = time.time()
        fps = int(1/(currentTime - prevTime))
        prevTime = currentTime

        frame = cv2.putText(frame, str(fps), (0, 20),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), 2)
        cv2.imshow('Original', frame)
