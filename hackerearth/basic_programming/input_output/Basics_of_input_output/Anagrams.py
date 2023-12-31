#!/usr/bin/env python
"""
Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

INPUT:
Test cases,t.
Two strings a and b, for each test case.

OUTPUT:
Desired O/p

CONSTRAINTS:
string lengths ≤ 10000

Note:
Anagram of a word is formed by rearranging the letters of the word.
For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.
"""

__author__ = "Cristian Chitiva"
__date__ = "March 17, 2019"
__email__ = "cychitivav@unal.edu.co"


T = int(input())

while T > 0:
    A = list(input().lower())
    B = list(input().lower())
    total = len(A) + len(B)
    common = 0

    for c in A:
        if c in B:
            B.remove(c)
            common += 2

    print(total - common)
    T -= 1
