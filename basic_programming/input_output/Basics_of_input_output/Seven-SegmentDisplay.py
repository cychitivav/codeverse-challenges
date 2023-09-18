#!/Usr/bin/env python
"""
You all must have seen a seven segment display.If not here it is:

Alice got a number written in seven segment format where each segment was creatted used a matchstick.

Example: If Alice gets a number 123 so basically Alice used 12 matchsticks for this number. 

Alice is wondering what is the numerically largest value that she can generate by using at most the matchsticks that she currently possess.Help Alice out by telling her that number.

INPUT:
First line contains T (test cases).
Next T lines contain a Number N.

OUTPUT:
Print the largest possible number numerically that can be generated using at max that many number of matchsticks which was used to generate N.

CONSTRAINTS:
1 ≤ T ≤ 100
1 ≤ length(N) ≤ 100
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"

T = int(input())
numbers = {'0': 6, '1': 2, '2': 5, '3': 5, '4': 4,
           '5': 5, '6': 6, '7': 3, '8': 7, '9': 6}

while T > 0:
    N = [i for i in input()]
    sticks = 0
    for i in N:
        sticks += numbers[i]

    if sticks % 2 == 0:
        for i in range(sticks//2):
            print(1, end="")
    else:
        print(7, end="")
        for i in range(sticks//2-1):
            print(1, end="")

    print("")
    T -= 1
