#!/Usr/bin/env python
"""
You have been given an array A of size N consisting of positive integers. You need to find and print the product of all the number in this array Modulo 10^9 + 7.

INPUT:
The first line contains a single integer N denoting the size of the array. The next line contains N space separated integers denoting the elements of the array

OUTPUT:
Print a single integer denoting the product of all the elements of the array Modulo 10^9 + 7.

CONSTRAINTS:
1 ≤ N ≤ 10^3
1 ≤ A[i] ≤ 10^3
"""

__author__ = "Cristian Chitiva"
__date__ = "March 17, 2019"
__email__ = "cychitivav@unal.edu.co"

N = int(input())
answer = 1
A = list(map(int,input().split()))

for i in A:
    answer *= i
    answer %= 1000000007

print(answer)