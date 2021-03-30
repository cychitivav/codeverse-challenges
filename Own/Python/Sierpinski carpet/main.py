from tkinter import Canvas
from time import sleep

canvas = Canvas(height=450, width=450)
canvas.master.resizable(0, 0)
canvas.config(bg="black")
canvas.pack()


def create_square(x, y, width=100):
    if width > 1:
        c1 = [x-width/2, y-width/2]
        c2 = [x+width/2, y+width/2]
        canvas.create_rectangle(c1, c2, fill="white")

        for i in range(-1, 2):
            for j in range(-1, 2):
                if  i != 0 or j != 0:
                    create_square(x+i*width, y+j*width, width/3)

        canvas.update()


def main():
    create_square(225, 225, 150)
    canvas.mainloop()


if __name__ == '__main__':
    main()
