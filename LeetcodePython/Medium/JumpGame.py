# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
from typing import List


def canJump(nums: List[int]) -> bool:
    def check_jumps(arr, i):
        if len(arr) == 1:
            return True
        while i >= 0:
            if arr[i] == (len(arr) - i - 1):
                check_jumps(arr[0:i+1], i-1)
                continue
            else:
                i-=1
        return False
    return check_jumps(nums, len(nums) - 2)

print(canJump([2,3,1,1,4]))

# we can use a greedy algorithm.
# The idea is to keep track of the farthest position we can reach as we iterate through the array.
# If at any point the current index is greater than the farthest position we can reach, we return False.
# If we can reach or exceed the last index, we return True.

def canJump(nums: List[int]) -> bool:
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])
    return True

# Example usage:
print(canJump([2, 3, 1, 1, 4]))  # Outputs: True
print(canJump([3, 2, 1, 0, 4]))  # Outputs: False
