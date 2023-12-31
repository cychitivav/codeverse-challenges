#!/usr/bin/env python
"""
Project Euler, Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Solution: 233168
"""

__author__ = "Cristian Chitiva"
__date__ = "2019/12/30"
__email__ = "cychitivav@unal.edu.co"


def sum_multiples(n):
    """
    This function returns the sum of all the multiples of 3 or 5 below n
    """
    total = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total


if __name__ == "__main__":
    print(sum_multiples(1000))
