#!/usr/bin/env python3
# Test file

import cv2
import time


if __name__ == "__main__":
    cap = cv2.VideoCapture(1)

    prevTime = 0
    currentTime = 0
    while cv2.waitKey(1) < 0:
        success, frame = cap.read()
        

        currentTime = time.time()
        fps = 1//(currentTime - prevTime)
        prevTime = currentTime

        frame = cv2.putText(frame, str(fps), (0, 20),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
        cv2.imshow('Original', frame)
