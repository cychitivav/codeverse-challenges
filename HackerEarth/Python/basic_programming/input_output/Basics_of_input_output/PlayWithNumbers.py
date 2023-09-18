#!/Usr/bin/env python
"""
You are given an array of n numbers and q queries. For each query you have to print the floor of the expected value(mean) of the subarray rom L to R.

INPUT:
First line contains two integers N and Q denoting number of array elements and number of queries.
Next line contains N space seperated integers denoting array elements.
Next Q lines contain two integers L and R(indices of the array).

OUTPUT:
Print a single integer denoting the answer.

CONSTRAINTS:
1 ≤ N,Q,L,R ≤ 10^6
1 ≤ Array elements ≤ 10^9

NOTE:
Use Fast I/O
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"

from os import read, write

N, Q = map(int, str(read(0, 100)).split())
A = [int(i) for i in read(0, 100).split()]

for i in range(Q):
    L, R = map(int, read(0, 100).split(' '))
    print(sum(A[L-1:R])//(R-L+1))

