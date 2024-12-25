
# Given an integer array of size , find the maximum of the minimum(s) of every window size in the array. The window size varies from to
# For example, given
# , consider window sizes of through . Windows of size are . The maximum value of the minimum values of these windows is . Windows of size are and their minima are . The maximum of these values is . Continue this process through window size to finally consider the entire array. All of the answers are .


def riddle(arr):
    ans = []
    for i in range(1, len(arr) + 1):
        array = []
        left_pointer = 0
        rightpointer = i
        while rightpointer < len(arr) + 1:
            subarray = arr[left_pointer:rightpointer]
            array.append(min(subarray))
            left_pointer += 1
            rightpointer += 1
        ans.append(max(array))
    return ans

print(riddle([6, 3, 5, 1, 12]))
# [12, 3, 3, 1]