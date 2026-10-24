
# Given an integer array of size n, find the maximum of the minimum(s) of every window size in the array. The window size varies from 1 to n.


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

#TRICK: The efficient trick is to turn the question around: for each array value, find the largest window in which that value can be the minimum. Use a monotonic stack to find the nearest smaller value on each side; those smaller values mark where its window must stop. Then record the value as a candidate answer for that window length. Finally, fill any missing lengths by carrying the best answer down from larger windows. This reduces the runtime to O(n).