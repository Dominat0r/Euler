#! /usr/bin/env python

"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2 digit numbers is 9009
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys


def _isPalindrome(prd):
    """
    Check number is palindrome or not
    """
    if str(prd) == str(prd)[::-1]:
        return True
    return False


def getLargestPalindrome(num1, num2):
    """
    Return largest palindrome number
    """
    palindrome = 0
    for each1 in xrange(num1, 100, -1):
        for each2 in xrange(num2, 100, -1):
            prd = each1 * each2
            if prd > palindrome and _isPalindrome(prd):
                palindrome = prd
    return palindrome

if __name__ == '__main__':
    num1, num2 = int(sys.argv[1]), int(sys.argv[2])
    palindrome_num = getLargestPalindrome(num1, num2)
    print palindrome_num
