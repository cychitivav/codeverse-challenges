#!/Usr/bin/env python
"""
Indian army is going to do a surprise attack on one of its enemies country. The President of India, the Supreme Commander of the Indian Army will be sending an alert message to all its commanding centers. As enemy would be monitoring the message, Indian army is going to encrypt(cipher) the message using basic encryption technique. A decoding key 'K' (number) would be sent secretly.

You are assigned to develop a cipher program to encrypt the message. Your cipher must rotate every character in the message by a fixed number making it unreadable by enemies.

Given a single line of string 'S' containing alpha, numeric and symbols, followed by a number '0 ≤ N ≤ 1000'. Encrypt and print the resulting string.

Note: The cipher only encrypts Alpha and Numeric. (A-Z, a-z, and 0-9) . All Symbols, such as - , ; %, remain unencrypted.
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"

S = input()
N = int(input())
C = ""

for i in S:
    if (ord(i) > 47 and ord(i) < 58):
        C += chr((ord(i) - 48 + N) % 10 + 48)
    elif (ord(i) > 64 and ord(i) < 91):
        C += chr((ord(i) - 65 + N) % 26 + 65)
    elif (ord(i) > 96 and ord(i) < 123):
        C += chr((ord(i) - 97 + N) % 26 + 97)
    else:
        C += i

print(C)
