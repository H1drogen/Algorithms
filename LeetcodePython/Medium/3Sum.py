
def threesum(nums):
    if len(nums) > 3:
        output = []
        for x in range(len(nums)):
            for y in range(len(nums) - x):
                value = nums[x] + nums[y+x]
                antagonistic_pair = 0 - value
                if antagonistic_pair in nums:
                    if x!=(y+x) and x!=nums.index(antagonistic_pair) and y!=nums.index(antagonistic_pair):
                        output.append([nums[x], nums[y+x], antagonistic_pair])
                        break
        return output
    else:
        return []




print(threesum([-1,0,1,2,-1,-4]))
