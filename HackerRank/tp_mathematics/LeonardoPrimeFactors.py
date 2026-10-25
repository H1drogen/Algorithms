#!/bin/python3

import math
import os
import random
import re
import sys

# Leonardo loves primes and created q queries where each query takes the form of an integer, n. For each n, count the maximum number of distinct prime factors of any number in the inclusive range [1,n].


# Complete the 'primeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def primeCount(n):
    # Write your code here


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
