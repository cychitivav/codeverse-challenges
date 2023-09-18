#!/Usr/bin/env python
"""
Dhananjay has recently learned about ASCII values.He is very fond of experimenting. With his knowledge of ASCII values and character he has developed a special word and named it Dhananjay's Magical word.

A word which consist of alphabets whose ASCII values is a prime number is an Dhananjay's Magical word. An alphabet is Dhananjay's Magical alphabet if its ASCII value is prime.

Dhananjay's nature is to boast about the things he know or have learnt about. So just to defame his friends he gives few string to his friends and ask them to convert it to Dhananjay's Magical word. None of his friends would like to get insulted. Help them to convert the given strings to Dhananjay's Magical Word.

Rules for converting:
1.Each character should be replaced by the nearest Dhananjay's Magical alphabet.
2.If the character is equidistant with 2 Magical alphabets. The one with lower ASCII value will be considered as its replacement.

INPUT:
First line of input contains an integer T number of test cases. Each test case contains an integer N (denoting the length of the string) and a string S.

OUTPUT:
For each test case, print Dhananjay's Magical Word in a new line.

CONSTRAINTS:
1 ≤ T ≤ 100
1 ≤ |S| ≤ 500
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"

T = int(input())
primes = [67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

while T > 0:
    N = int(input())
    S = input()

    for c in S:
        if ord(c) in primes:
            print(c, end="")
        else:
            for i in range(100):
                if ord(c)-i in primes:
                    print(chr(ord(c)-i), end="")
                    break
                elif ord(c)+i in primes:
                    print(chr(ord(c)+i), end="")
                    break
    print("")
    T -= 1
