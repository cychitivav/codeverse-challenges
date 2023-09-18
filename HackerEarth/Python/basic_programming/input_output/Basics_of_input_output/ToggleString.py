#!/Usr/bin/env python
"""
You have been given a String S consisting of uppercase and lowercase English alphabets. You need to change the case of each alphabet in this String. That is, all the uppercase letters should be converted to lowercase and all the lowercase letters should be converted to uppercase. You need to then print the resultant String to output.

INPUT:
The first and only line of input contains the String S

OUTPUT:
Print the resultant String on a single line.

CONSTRAINTS:
1 ≤ |S| ≤ 100 where S denotes the length of string S.
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"


S = input()

print(S.swapcase())