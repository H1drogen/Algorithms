from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    dic = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in dic:
            return [i, dic[complement]]
        else:
            dic[num] = i


# Example usage:
# nums = [2, 7, 11, 15]
# target = 9
print(twoSum([2, 7, 11, 15], 9))  # Outputs: [2, 7] since nums[0] + nums[1] = 9