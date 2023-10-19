

def removeDuplicates(nums):
    myset = set(nums)
    newarray = []
    for x in myset:
        newarray.append(x)
    nums = newarray
    return len(myset)

print(removeDuplicates([1,1,2]))

def removeDuplicatesanswer(nums):
    