#!/bin/python3

import math
import os
import random
import re
import sys

# Medium
# Watson gives an integer (N) to Sherlock and asks him: What is the number of divisors of N that are divisible by 2?.

def divisors(n):
    # Write your code here
    count = 0
    for num in range(2, n + 1):
        if n % num == 0:
            if num % 2 == 0:
                count += 1
    return count

# This answer is not efficient enough

if __name__ == '__main__':
    print(divisors(9)) # Output: 0
    print(divisors(8)) # Output: 3
    print(divisors(24)) # Output: 6




