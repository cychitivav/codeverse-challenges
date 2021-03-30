from tkinter import Canvas
from time import sleep

canvas = Canvas(height=250, width=150)
canvas.config(bg='black')
canvas.master.resizable(False, False)
canvas.pack(fill="both", expand=True)

def create_seven_segment(canvas, number):
    canvas.delete('all')
    # A
    if (number >> 6) & 1:
        canvas.create_polygon(30, 30, 40, 20, 100, 20, 110, 30,
                              100, 40, 40, 40, fill="red", outline="black", width=3)
    # B
    if (number >> 5) & 1:
        canvas.create_polygon(110, 30, 100, 40, 100, 100, 110, 110,
                              120, 100, 120, 40, fill="red", outline="black", width=3)
    # C
    if (number >> 4) & 1:
        canvas.create_polygon(110, 110, 100, 120, 100, 180, 110, 190,
                              120, 180, 120, 120, fill="red", outline="black", width=3)
    # D
    if (number >> 3) & 1:
        canvas.create_polygon(30, 190, 40, 180, 100, 180, 110, 190,
                              100, 200, 40, 200, fill="red", outline="black", width=3)
    # E
    if (number >> 2) & 1:
        canvas.create_polygon(30, 110, 20, 120, 20, 180, 30, 190,
                              40, 180, 40, 120, fill="red", outline="black", width=3)
    # F
    if (number >> 1) & 1:
        canvas.create_polygon(30, 30, 20, 40, 20, 100, 30, 110,
                              40, 100, 40, 40, fill="red", outline="black", width=3)
    # G
    if (number >> 0) & 1:
        canvas.create_polygon(30, 110, 40, 100, 100, 100, 110, 110,
                              100, 120, 40, 120, fill="red", outline="black", width=3)


def main():    

    leds = [0b1111110,  # 0
            0b0110000,  # 1
            0b1101101,  # 2
            0b1111001,  # 3
            0b0110011,  # 4
            0b1011011,  # 5
            0b1011111,  # 6
            0b1110000,  # 7
            0b1111111,  # 8
            0b1111011]  # 9
    
    try:
        i = 0
        while True:
            create_seven_segment(canvas, leds[i])
            canvas.update()
            sleep(0.2)
            if i < 9:
                i += 1
            else:
                i = 0
    except: 
        pass
                
if __name__ == '__main__':
    main()
