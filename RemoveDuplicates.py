

def removeDuplicates(nums):
    myset = set(nums)
    newarray = []
    for x in myset:
        newarray.append(x)
    nums = newarray
    return len(myset)

def removeDuplicatesanswer(nums):
    nums[:] = set(nums)
    return len(nums)

print(removeDuplicates([1,1,2]))
print(removeDuplicatesanswer([1,1,2]))