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

    mp_face_detection = mp.solutions.face_detection
    mp_draw = mp.solutions.drawing_utils

    face_detection = mp_face_detection.FaceDetection()

    prev_time = 0
    while cv2.waitKey(1) < 0:
        success, frame = cap.read()
        frame = cv2.flip(frame, flipCode=1)
        frame_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_detection.process(frame_RGB)
        # print(results.detections)

        if results.detections:
            for kp, detection in enumerate(results.detections):
                # mp_draw.draw_detection(frame, det)
                bbox_r = detection.location_data.relative_bounding_box
                h, w, c = frame.shape
                bbox = int(bbox_r.xmin*w), int(bbox_r.ymin*h), int(bbox_r.width*w), int(bbox_r.height*h)

                score = round(detection.score[0]*100)

                cv2.rectangle(frame, bbox, (255,0,255),2)
                cv2.putText(frame, str(score)+'%', (bbox[0], bbox[1]-20),
                            cv2.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2)

        curre_time = time.time()
        fps = int(1/(curre_time - prev_time))
        prev_time = curre_time

        frame = cv2.putText(frame, str(fps), (0, 20),
                            cv2.FONT_HERSHEY_PLAIN, 1.5,
                            (255, 0, 255), 3)
        cv2.imshow('Face detection', frame)
