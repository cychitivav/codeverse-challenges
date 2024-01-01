#!/usr/bin/env python
"""
You are required to enter a word that consists of x and y that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if $2\times x = y$. 

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

INPUT:
    - First line: A word that starts with several Zs and continues by several Os.
      Note: The maximum length of this word must be 20.

OUTPUT:
Print Yes if the input word can be considered as the string zoo otherwise, print No.
"""

__author__ = "Cristian Chitiva"
__date__ = "January 1, 2023"
__email__ = "cychitivav@unal.edu.co"


if __name__ == "__main__":
    w = input()

    if w.count("z") * 2 == w.count("o"):
        print("Yes")
    else:
        print("No")
