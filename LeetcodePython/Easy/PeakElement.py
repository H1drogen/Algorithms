
class Solution(object):
    def findPeakElement(self, nums):
        x = 1
        if len(nums) <= 1:
            return 0
        if nums[x] < nums[x-1]:
            return 0
        while x < len(nums) - 1:
            if nums[x] > nums[x+1]:
                if nums[x] > nums[x-1]:
                    return x
            x += 1
        return x

Solution().findPeakElement([1,2,3,1])