from random import randint as rand
from tkinter import Canvas


def create_matrix(cols, rows):
    return [[rand(0,1) for j in range(cols)] for i in range(rows)]


def draw(matrix):
    global canvas
    canvas.delete("all")
    height = 700/len(matrix)
    width = 700/len(matrix[0])

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]:
                canvas.create_rectangle(
                    col*width, row*height, (col+1)*width, (row+1)*height, fill="black")
            else:
                canvas.create_rectangle(
                    col*width, row*height, (col+1)*width, (row+1)*height)


def next_matrix(matrix):
    aux = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            neighbors = 0
            if matrix[i-1][j-1]:
                neighbors += 1
            if matrix[i-1][j]:
                neighbors += 1
            if matrix[i-1][j+1]:
                neighbors += 1
            if matrix[i][j-1]:
                neighbors += 1
            if matrix[i][j+1]:
                neighbors += 1
            if matrix[i+1][j-1]:
                neighbors += 1
            if matrix[i+1][j]:
                neighbors += 1
            if matrix[i+1][j+1]:
                neighbors += 1

            if matrix[i][j] and (neighbors < 2 or neighbors > 3):
                aux[i][j] = 0
            if matrix[i][j] and (neighbors == 2 or neighbors == 3):
                aux[i][j] = 1
            if not matrix[i][j] and neighbors == 3:
                aux[i][j] = 1

    return aux


def main():
    mat = create_matrix(50, 50)

    global canvas
    canvas = Canvas(height=700, width=700)
    canvas.master.resizable(False, False)
    canvas.pack()

    while True:
        draw(mat)
        mat = next_matrix(mat)
        canvas.update()


if __name__ == '__main__':
    main()
