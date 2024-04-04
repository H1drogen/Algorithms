import heapq


def cookies(k, A):
    iterations = 0
    heapq.heapify(A)
    while A[0] < k:
        iterations += 1
        temp = heapq.heappop(A)
        combined_cookie = temp + 2 * heapq.heappop(A)
        heapq.heappush(A, combined_cookie)
    if iterations == 0:
        return -1
    return iterations

cookies(9, [2, 7, 3, 6, 4, 6])
