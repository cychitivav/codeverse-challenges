#!/usr/bin/env python
"""
Project Euler, Problem 2: Even Fibonacci Numbers

Each new term in the Fibonacci sequence is generated by adding the previous two
terms. By starting with 1 and 2, the first 10 terms will be:
    
    1, 2, 3, 5, 8, 13, 21, 34, 55, and 89.

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.


Author: Cristian Chitiva <cychitivav@unal.edu.co>
Date: 30 December 2023

Solution: 4613732
"""


def fibonacci():
    """
    This function is a infinite generator of the Fibonacci sequence
    """
    first = 1
    second = 2

    while True:
        yield first
        first, second = second, first + second


if __name__ == "__main__":
    total = 0

    fib_gen = fibonacci()
    n_fib = next(fib_gen)

    while n_fib < 4000000:
        if n_fib % 2 == 0:
            total += n_fib

        n_fib = next(fib_gen)

    print(total)