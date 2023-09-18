#!/Usr/bin/env python
"""
On a distant planet far away from Earth lives a boy named Aman.He loves to run everyday.But his running distance is directly affected by how much horlicks his mother mixed in his milk today.If his mother has mixed x grams of horlicks,then Aman will be capable of running 100*x meters at most on that day.

Aman's instructor, Mr.Sharma ,is a very strict yet very caring.Everyday he asks Aman to run around a circle of radius r once.If Aman is able to complete the circle,he would get a toffee.

INPUT:
First line contains d,no. of days Aman goes to his instructor.Next d lines each contain r,radius of circle and x,amount of horlicks.

OUTPUT:
Print total number of toffees Aman would finally have at the end of d days.

CONSTRAINTS:
1 ≤ d ≤ 10^5
1 ≤ r ≤ 10^6
1 ≤ x ≤ 10^4

Note:Take value of pi=22/7.
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"


d = int(input())
toffee = 0

for i in range(d):
    r, x = map(int, input().split())
    if (2*22/7*r) <= (100*x):
        toffee += 1

print(toffee)