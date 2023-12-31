#!/usr/bin/env python
"""
Arpasland has surrounded by attackers. A truck enters the city. The driver claims the load is food and medicine from Iranians. Ali is one of the soldiers in Arpasland. He doubts about the truck, maybe it's from the siege. He knows that a tag is valid if the sum of every two consecutive digits of it is even and its letter is not a vowel. Determine if the tag of the truck is valid or not.

We consider the letters "A","E","I","O","U","Y" to be vowels for this problem.

INPUT:
The first line contains a string of length 9. The format is "DDXDDD-DD", where D stands for a digit (non zero) and X is an uppercase english letter.

OUTPUT:
Print "valid" (without quotes) if the tag is valid, print "invalid" otherwise (without quotes)
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"


S = input()

vowels = ["A", "E", "I", "O", "U", "Y"]

if S[2] in vowels:
    print("invalid")
elif (int(S[0]) + int(S[1])) % 2 != 0:
    print("invalid")
elif (int(S[3]) + int(S[4])) % 2 != 0:
    print("invalid")
elif (int(S[4]) + int(S[5])) % 2 != 0:
    print("invalid")
elif (int(S[7]) + int(S[8])) % 2 != 0:
    print("invalid")
else:
    print("valid")
