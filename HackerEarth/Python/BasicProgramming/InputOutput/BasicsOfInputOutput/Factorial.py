#!/Usr/bin/env python
"""
You have been given a positive integer N. You need to find and print the Factorial of this number. The Factorial of a positive integer N refers to the product of all number in the range from 1 to N. You can read more about the factorial of a number here.

INPUT:
The first and only line of the input contains a single integer N denoting the number whose factorial you need to find.

OUTPUT:
Output a single line denoting the factorial of the number N.

CONSTRAINTS:
1 ≤ N ≤ 10
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"


N = int(input())

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
    
print(factorial(N))