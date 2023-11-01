import heapq


def test(arr):
    positive = 0
    negative = 0
    zero = 0
    for x in arr:
        if x > 0:
            positive += 1
        elif x < 0:
            negative += 1
        else:
            zero += 1

def cookies(k, A):
    iterations = 0
    x = 0
    heapq.heapify(A)
    while A[0] < k and len(A) > 1:
        temp = heapq.heappop(A)
        new_cookie = temp + 2*A[0]
        heapq.heapreplace(A, new_cookie)
        iterations += 1
    if A[-1] < k:
        iterations = -1
    return iterations


def texteditor(Q: int, Operations):
    S = ''
    for Ops in Operations:
        command_array = Ops.split()
        if command_array[0] == '1':
            S = S + command_array[1]
        elif command_array[0] == '2':
            prefix_count = len(S) - int(command_array[1])
            prefix = ''
            for count, x in enumerate(S):
                if count < prefix_count:
                    prefix += x
                else:
                    break
            S = prefix
        elif command_array[0] == '3':
            print(list(S)[int(command_array[1])])
        elif command_array[0] == '4':
            continue



