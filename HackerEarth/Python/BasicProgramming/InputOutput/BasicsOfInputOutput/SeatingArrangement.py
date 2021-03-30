#!/Usr/bin/env python
"""
Akash and Vishal are quite fond of travelling. They mostly travel by railways. They were travelling in a train one day and they got interested in the seating arrangement of their compartment. The compartment looked something like

So they got interested to know the seat number facing them and the seat type facing them. The seats are denoted as follows : 
Window Seat : WS
Middle Seat : MS
Aisle Seat : AS

You will be given a seat number, find out the seat number facing you and the seat type, i.e. WS, MS or AS.

INPUT:
First line of input will consist of a single integer T denoting number of test-cases. Each test-case consists of a single integer N denoting the seat-number.

OUTPUT:
For each test case, print the facing seat-number and the seat-type, separated by a single space in a new line.

CONSTRAINTS:
1 ≤ T ≤ 10^5
1 ≤ N ≤ 10^8
"""

__author__ = "Cristian Chitiva"
__date__ = "March 17, 2019"
__email__ = "cychitivav@unal.edu.co"


T = int(input())

while T > 0:
    N = int(input())
    position = N % 12
    section = N//12

    if position == 1:
        word = str((position + 11) + 12*section)
        print(word + ' WS')
    elif position == 2:
        word = str((position + 9) + 12*section)
        print(word + ' MS')
    elif position == 3:
        word = str((position + 7) + 12*section)
        print(word + ' AS')
    elif position == 4:
        word = str((position + 5) + 12*section)
        print(word + ' AS')
    elif position == 5:
        word = str((position + 3) + 12*section)
        print(word + ' MS')
    elif position == 6:
        word = str((position + 1) + 12*section)
        print(word + ' WS')
    elif position == 7:
        word = str((position - 1) + 12*section)
        print(word + ' WS')
    elif position == 8:
        word = str((position - 3) + 12*section)
        print(word + ' MS')
    elif position == 9:
        word = str((position - 5) + 12*section)
        print(word + ' AS')
    elif position == 10:
        word = str((position - 7) + 12*section)
        print(word + ' AS')
    elif position == 11:
        word = str((position - 9) + 12*section)
        print(word + ' MS')
    else:
        word = str((position - 11) + 12*section)
        print(word + ' WS')

    T -= 1
