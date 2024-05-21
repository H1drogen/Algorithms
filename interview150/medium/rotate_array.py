# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative
from typing import List


def rotate(self, nums: List[int], k: int) -> None:
    for n in range(k):
        nums.insert(0, nums.pop(len(nums) - 1))

        