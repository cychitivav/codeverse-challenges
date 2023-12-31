#!/usr/bin/env python
"""
Patlu and Motu works in a building construction, they have to put some number of bricks N from one place to another, and started doing their work. They decided , they end up with a fun challenge who will put the last brick.

They to follow a simple rule, In the i'th round, Patlu puts i bricks whereas Motu puts ix2 bricks.

There are only N bricks, you need to help find the challenge result to find who put the last brick.

INPUT:
First line contains an integer N.

OUTPUT:
Output "Patlu" (without the quotes) if Patlu puts the last bricks, Motu"(without the quotes) otherwise.

CONSTRAINTS:
1 ≤ N ≤ 10000
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"


N = int(input())

for i in range(N):
    N -= i
    if N < 0:
        print("Patlu")
        break
    N -= 2*i
    if N < 0:
        print("Motu")
        break
