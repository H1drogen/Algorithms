#!/bin/python3

import math
import os
import random
import re
import sys

# Easy

# Leonardo loves primes and created q queries where each query takes the form of an integer, n. For each n, count the maximum number of distinct prime factors of any number in the inclusive range [1,n].

# Example: for n = 10, the maximum number of distinct prime factors of any number in the range [1,10] is 2. The number 6 has two distinct prime factors: 2 and 3.



def primeCount(n):
    # Write your code here
    prime_current = 2
    prime_count = 2
    result = 0

    def find_next_prime(number):
        while True:
            number += 1
            flag = True
            for divisor in range(2,number):
                if number % divisor == 0:
                    flag = False
                    break
            if flag:
                return number

    if n < 2:
        return 0

    while n >= prime_count:
        result += 1
        prime_current = find_next_prime(prime_current)
        prime_count = prime_count * prime_current

    return result



# TRICK: the smallest number with k distinct prime factors is the product of the k smallest primes: 2 × 3 × 5 × .... Using larger primes—or powers of primes—only makes the number bigger, so it can’t increase how many distinct prime factors fit within n.

if __name__ == '__main__':
    print(primeCount(30))  # Output: 3
    print(primeCount(100))  # Output: 4
