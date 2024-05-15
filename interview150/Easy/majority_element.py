# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
from typing import List


def majorityElement(nums: List[int]) -> int:
    nums.sort()
    return nums[int(len(nums) / 2)]