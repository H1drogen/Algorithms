#It is New Year's Day and people are in line for the Wonderland rollercoaster ride. Each person wears a sticker indicating their initial position in the queue from  to . Any person can bribe the person directly in front of them to swap positions, but they still wear their original sticker. One person can bribe at most two others.
#Determine the minimum number of bribes that took place to get to a given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.



import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    last_num = 0
    bribe_count = 0
    anchor = 0
    bribe = 0

    for num in q:
        if anchor > num:
            bribe += 1
            bribe_count += 1
            if bribe_count >= 2:
                print('Too chaotic')
                return
            continue
        if last_num > num:
            bribe += 1
            anchor = last_num
            continue
        last_num = num

    print(bribe)

if __name__ == '__main__':
    test_cases = [
        # [2, 1, 5, 3, 4], # three bribes, valid
        # [2, 5, 1, 3, 4], # too chaotic
        [1, 2, 5, 3, 4, 7, 8, 6], # four bribes
    ]

    for q in test_cases:
        minimumBribes(q)
