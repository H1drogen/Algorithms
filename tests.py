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

cookies(9, [2,7,3,6,4,6])

