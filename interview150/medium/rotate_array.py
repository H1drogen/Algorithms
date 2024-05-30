# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative
from typing import List


def rotate(self, nums: List[int], k: int) -> None:
    for n in range(k):
        nums.insert(0, nums.pop(len(nums) - 1))

# pop and insert have time complexity O(n). This is complexity O(n*k)

# use slicing, which has a time complexity of O(k).

def rotate(nums: List[int], k: int) -> None:
    k %= len(nums)  # Ensure k is within the range of the list length
    nums[:] = nums[-k:] + nums[:-k]