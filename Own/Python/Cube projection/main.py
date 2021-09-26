from tkinter import Tk, Canvas
from math import cos, sin
from MatrixMultiplication import *
import time


def createPoint(canvas, x, y, r=5):
    x = x+200
    y = y+150
    canvas.create_oval(x-r, y-r, x+r, y+r, fill='white', outline='white')


def close_window():
    global running
    running = False


def main():
    points = [[-50, -50, -50], [-50, -50, 50], [-50, 50, 50], [-50, 50, -50],
              [50, -50, 50], [50, -50, -50], [50, 50, 50], [50, 50, -50]]

    projection = [[1, 0, 0],
                  [0, 1, 0]]

    root = Tk()
    root.protocol("WM_DELETE_WINDOW", close_window)

    w = Canvas(root, height=400, width=600)
    w.config(bg='black')
    w.pack(fill="both", expand=True)

    angle = 0
    global running
    running = True

    while running:
        if root == None:
            break
        angle += 0.1
        rotationX = [[1, 0, 0],
                     [0, cos(angle), -sin(angle)],
                     [0, sin(angle), cos(angle)]]

        rotationY = [[cos(angle), 0, -sin(angle)],
                     [0, 1, 0],
                     [sin(angle), 0, cos(angle)]]

        rotationZ = [[cos(angle), -sin(angle), 0],
                     [sin(angle), cos(angle), 0],
                     [0, 0, 1]]

        w.delete("all")
        for point in points:
            rotated = matmul(rotationY, vecToMatriz(point))
            rotated = matmul(rotationX, rotated)
            rotated = matmul(rotationZ, rotated)
            projected2D = matrixToVec(matmul(projection, rotated))
            createPoint(w, projected2D[0], projected2D[1])
        root.update()
        time.sleep(.01)

    root.destroy()


if __name__ == "__main__":
    main()
