#!/usr/bin/env python
"""
You have been given a String S. You need to find and print whether this string is a palindrome or not. If yes, print "YES" (without quotes), else print "NO" (without quotes).

INPUT:
The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.

OUTPUT:
Print the required answer on a single line.

CONSTRAINTS:
1 ≤ S ≤ 100

Note
String S consists of lowercase English Alphabets only.
"""

__author__ = "Cristian Chitiva"
__date__ = "March 17, 2019"
__email__ = "cychitivav@unal.edu.co"

S = input()


for i in range(len(S)//2):
    if S[i] != S[-i-1]:
        print("NO")
        break
else:
    print("YES")
