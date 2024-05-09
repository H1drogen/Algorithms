from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
                count += 1
            else:
                index += 1
        return count



