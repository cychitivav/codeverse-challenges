from tkinter import Canvas
from math import cos, sin, pi

class Branch(Canvas):
    def __init__(self, x, y):
        Canvas.__init__(self, height=400, width=400)
        self.master.resizable(0, 0)
        self.config(bg="black")
        self.pack()

        self.x = x
        self.y = y
        self.pivot = x
        self.step = pi/2
        self.create_branch(x, y)

    def create_branch(self, x, y, angle=0, lenght=100, step=pi/2):
        if lenght > 1:
            x1 = x-lenght*sin(angle)
            y1 = y-lenght*cos(angle)
            self.create_line(x, y, x1, y1, fill="white")

            self.create_branch(x1, y1, angle-step, 2*lenght/3, step)
            self.create_branch(x1, y1, angle+step, 2*lenght/3, step)

    def move(self):
        self.delete("all")

        self.step += 0.1        
        self.create_branch(self.x, self.y, step=self.step)


def main():
    tree = Branch(200, 380)
    while True:
        tree.update()
        tree.move()
    #tree.mainloop()


if __name__ == '__main__':
    main()
