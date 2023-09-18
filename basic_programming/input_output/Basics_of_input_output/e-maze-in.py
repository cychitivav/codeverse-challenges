#!/Usr/bin/env python
"""
Ankit is in maze. The command center sent him a string which decodes to come out from the maze. He is initially at (0, 0). String contains L, R, U, D denoting left, right, up and down. In each command he will traverse 1 unit distance in the respective direction.

For example if he is at (2, 0) and the command is L he will go to (1, 0).

INPUT:
Input contains a single string.

OUTPUT:
Print the final point where he came out.

CONSTRAINTS:
1 ≤ |S| ≤ 200
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"


S = input()
x = 0
y = 0

for c in S:
    if c == "L":
        x -= 1
    elif c == "R":
        x += 1
    elif c == "U":
        y += 1
    else:
        y -= 1

print(str(x) + " " + str(y))
