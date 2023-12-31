#!/usr/bin/env python
"""
Rahul is a very busy persion he dont wan't to waste his time . He keeps account of duration of each and every work. Now he don't even get time to calculate duration of works, So your job is to count the durations for each work and give it to rahul.

INPUT:
First line will be given by N number of works.
Next N line will be given SH,SM,EH and EM  each separated by space(SH=starting hr, SM=starting min, EH=ending hr, EM=ending min)

OUTPUT:
N lines with duration HH MM(hours and minutes separated by space)
"""

__author__ = "Cristian Chitiva"
__date__ = "March 18, 2019"
__email__ = "cychitivav@unal.edu.co"


N = int(input())

while N > 0:
    SH, SM, EH, EM = map(int, input().split())

    minutes = 60 - SM + EM + 60*(EH - SH-1)
    hours = 0
    if minutes >= 60:
        hours += minutes//60
        minutes %= 60

    print(str(hours)+" "+str(minutes))
    N -= 1
