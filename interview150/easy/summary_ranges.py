from typing import List

# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

def summaryRanges(nums: List[int]) -> List[str]:
    if not nums:
        return []
    ranges = []
    start = nums[0]
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{nums[i - 1]}")
            start = nums[i]
    if start == nums[-1]:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}->{nums[-1]}")
    return ranges
