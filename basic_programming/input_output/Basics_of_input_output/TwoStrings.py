#!/Usr/bin/env python
"""
Given two strings of equal length, you have to tell whether they both strings are identical.

Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2. See Sample explanation for more details.

INPUT:
First line, contains an intger 'T' denoting no. of test cases.
Each test consists of a single line, containing two space separated strings S1 and S2 of equal length.

OUTPUT:
For each test case, if any of the permutation of string S1 is equal to the string S2 print YES else print NO.

CONSTRAINTS:
1 ≤ T ≤ 100
1 ≤ |S1| = |S2| ≤ 10^5
String is made up of lower case letters only.

Note : Use Hashing Concept Only . Try to do it in O(string length).
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"


T = int(input())

while T > 0:
    S1, S2 = map(list, input().split())

    for c in S1:
        if c not in S2:
            print("NO")
            break
        else:
            S2.remove(c)
    else:
        print("YES")

    T -= 1
