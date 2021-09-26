from tkinter import Tk, Canvas
import numpy as np
import cv2


if __name__ == "__main__":
    points = np.array([[-50, -50, -50], [-50, -50, 50], [-50, 50, 50], [-50, 50, -50],
                       [50, -50, 50], [50, -50, -50], [50, 50, 50], [50, 50, -50]])

    angle = 0
    while cv2.waitKey(50) < 0:
        angle += 0.1

        translation = np.array([[1, 0, 0, 150],
                                [0, 1, 0, 150],
                                [0, 0, 1,   0],
                                [0, 0, 0,   1]])

        rotation_x = np.array([[1,             0,              0, 0],
                               [0, np.cos(angle), -np.sin(angle), 0],
                               [0, np.sin(angle),  np.cos(angle), 0],
                               [0,              0,             0, 1]])

        rotation_y = np.array([[np.cos(angle), 0, -np.sin(angle), 0],
                               [0,             1,              0, 0],
                               [np.sin(angle), 0,  np.cos(angle), 0],
                               [0,             0,              0, 1]])

        rotation_z = np.array([[np.cos(angle), -np.sin(angle), 0, 0],
                               [np.sin(angle),  np.cos(angle), 0, 0],
                               [0,              0, 1, 0],
                               [0,              0, 0, 1]])

        img = np.zeros((300, 300))
        for point in points:
            point_mth = np.append(point, 1)
            rotated = np.matmul(rotation_x, point_mth)

            rotated = np.matmul(rotation_y, rotated)
            rotated = np.matmul(rotation_z, rotated)

            translated = np.matmul(translation, rotated)
            pixels = translated.astype(np.uint8)
            cv2.circle(img, tuple(pixels[:2]), 5, 255, cv2.FILLED)

        cv2.imshow('Cube', img)
