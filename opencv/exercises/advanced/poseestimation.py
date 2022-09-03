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

    mp_pose = mp.solutions.pose
    mp_draw = mp.solutions.drawing_utils

    pose = mp_pose.Pose()

    prev_time = 0
    while cv2.waitKey(1) < 0:
        success, frame = cap.read()
        frame = cv2.flip(frame, flipCode=1)
        frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = pose.process(frame_RGB)
        # print(results.pose_landmarks)

        if results.pose_landmarks:
            mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        for kp, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(lm.x*w), int(lm.y*h)

            if kp == 12 or kp == 11:
                cv2.circle(frame, (cx, cy), 7, (255,255,0), cv2.FILLED)

        curre_time = time.time()
        fps = int(1/(curre_time - prev_time))
        prev_time = curre_time

        frame = cv2.putText(frame, str(fps), (0, 20),
                            cv2.FONT_HERSHEY_PLAIN, 1.5,
                            (255, 0, 255), 3)
        cv2.imshow('Original', frame)
