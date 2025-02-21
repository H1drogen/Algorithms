# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
from typing import List


def majorityElement(nums: List[int]) -> int:
    nums.sort()
    return nums[int(len(nums) / 2)]



# ANSWER
# it can be optimized to O(n) using the Boyer-Moore Voting Algorithm

def majorityElement(nums: List[int]) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate