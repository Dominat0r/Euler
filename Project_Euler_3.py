#! /usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import sys


def getPrimeFactor(num):
    """
    Returns prime factor list fir given number
    """
    prime_fac_list = []
    defnum = 2
    while defnum <= num:
        if num % defnum:
            defnum += 1
        else:
            num = num // defnum
            prime_fac_list.append(defnum)
    return prime_fac_list

if __name__ == '__main__':
    num = int(sys.argv[1])
    prime_factors = getPrimeFactor(num)
    print max(prime_factors)
