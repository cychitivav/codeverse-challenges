#!/Usr/bin/env python
"""
You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k. You do not need to print these numbers, you just have to find their count.

INPUT:
The first and only line of input contains 3 space separated integers l, r and k.

OUTPUT:
Print the required answer on a single line.

CONSTRAINTS:
1 ≤ l ≤ r ≤ 1000
1 ≤ k ≤ 1000
"""

__author__ = "Cristian Chitiva"
__date__ = "March 17, 2019"
__email__ = "cychitivav@unal.edu.co"


l,r,k = list(map(int, input().split()))
c = 0

for i in range(l, r+1):
    if i % k == 0:
        c += 1
    
print(c)