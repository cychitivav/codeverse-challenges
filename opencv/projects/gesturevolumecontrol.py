#!/usr/bin/env python3
# Gesture Volume control

__author__ = "Cristian Chitiva"
__date__ = "September 19, 2021"
__email__ = "cychitivav@unal.edu.co"

import cv2
import numpy as np
import mediapipe as mp
import time


if __name__ == "__main__":
    cap = cv2.VideoCapture(1)

    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    hands = mp_hands.Hands()

    prev_time = 0
    while cv2.waitKey(1) < 0:
        success, frame = cap.read()
        frame = cv2.flip(frame, flipCode=1)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(frameRGB)
        # print(results.multi_handedness)

        h, w, c = frame.shape

        if results.multi_hand_landmarks:
            for handLandmark in results.multi_hand_landmarks:
                lm = handLandmark.landmark[4]
                thumb_tip = np.array([int(lm.x*w), int(lm.y*h)])
                cv2.circle(frame, tuple(thumb_tip), 7, (255, 0, 255), cv2.FILLED)

                lm = handLandmark.landmark[8]
                index_tip = np.array([int(lm.x*w), int(lm.y*h)])
                cv2.circle(frame, tuple(index_tip), 7, (255, 0, 255), cv2.FILLED)
                        
                cv2.line(frame, tuple(thumb_tip), tuple(index_tip), (255,0,255), 3)
                cv2.putText(frame, str(np.linalg.norm(thumb_tip-index_tip)), (w-50, 20),
                                    cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 0), 2)


                mp_draw.draw_landmarks(
                    frame, handLandmark, mp_hands.HAND_CONNECTIONS)

        curre_time = time.time()
        fps = int(1/(curre_time - prev_time))
        prev_time = curre_time

        frame = cv2.putText(frame, str(fps), (0, 20),
                            cv2.FONT_HERSHEY_PLAIN, 1.5, (255, 0, 255), 2)
        cv2.imshow('Original', frame)
