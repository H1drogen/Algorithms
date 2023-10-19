#Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):
    temp = nums[-k]
    for _ in range(k):
        for x in range(len(nums)):
            temp2 = nums[x]
            nums[x] = temp
            temp = temp2

print(rotate([1,2,3,4,5,6,7], 2))