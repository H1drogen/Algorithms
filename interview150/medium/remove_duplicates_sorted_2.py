from typing import List

def removeDuplicates2(nums: List[int]) -> int:
    not_duplicate = True
    i = len(nums) - 1
    while i > 0:
        if nums[i] == nums[i - 1]:
            if not_duplicate:
                not_duplicate = False
            else:
                nums.pop(i)
        else:
            not_duplicate = True
        i -= 1

    return len(nums)