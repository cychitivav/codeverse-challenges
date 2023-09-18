#!/Usr/bin/env python
"""
You are given an integer N. You need to print the series of all prime numbers till N.

INPUT:
The first and only line of the input contains a single integer N denoting the number till where you need to find the series of prime number.

OUTPUT:
Print the desired output in single line separated by spaces.

CONSTRAINTS:    
1 ≤ N ≤ 1000
"""

__author__ = "Cristian Chitiva"
__date__ = "March 17, 2019"
__email__ = "cychitivav@unal.edu.co"


N = int(input())

for n in range(2, N):
    isPrime = True
    for d in range(2, n):
        if n % d == 0:
            isPrime = False
    if isPrime:
        print(n, end=" ")
