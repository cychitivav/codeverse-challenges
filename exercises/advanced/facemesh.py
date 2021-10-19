#!/usr/bin/env python3
# Face detection

__author__ = "Cristian Chitiva"
__date__ = "September 19, 2021"
__email__ = "cychitivav@unal.edu.co"

import cv2
import numpy as np
import mediapipe as mp
import time


if __name__ == "__main__":
    cap = cv2.VideoCapture(1)

    mp_face_mesh = mp.solutions.face_mesh
    mp_draw = mp.solutions.drawing_utils

    face_mesh = mp_face_mesh.FaceMesh(max_num_faces=3)

    prev_time = 0
    while cv2.waitKey(1) < 0:
        success, frame = cap.read()
        frame = cv2.flip(frame, flipCode=1)
        frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(frame_RGB)
        # print(results.multi_face_landmarks)
        # print(len(results.multi_face_landmarks[0].landmark))

        if results.multi_face_landmarks:
            for face_lms in results.multi_face_landmarks:
                draw_spec = mp_draw.DrawingSpec(color=(0,255,0),thickness=1, circle_radius=1)
                mp_draw.draw_landmarks(frame, face_lms, mp_face_mesh.FACE_CONNECTIONS,
                                       landmark_drawing_spec=draw_spec)

                for kp, lm in enumerate(face_lms.landmark):
                    h, w, c = frame.shape
                    x, y = int(lm.x*w), int(lm.y*h)

        curre_time = time.time()
        fps = int(1/(curre_time - prev_time))
        prev_time = curre_time

        frame = cv2.putText(frame, str(fps), (0, 20),
                            cv2.FONT_HERSHEY_PLAIN, 1.5,
                            (255, 0, 255), 3)
        cv2.imshow('Face detection', frame)
