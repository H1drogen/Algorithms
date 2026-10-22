#Jesse loves cookies and wants the sweetness of some cookies to be greater than value l. To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

# sweetness = ( 1 * Least sweet cookie + 2 * 2nd least sweet cookie).

# This occurs until all the cookies have a sweetness >= k.

# Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return -1 .



import heapq

def cookies(k, A):
    iterations = 0
    heapq.heapify(A)
    while A[0] < k and len(A) > 1:
        iterations += 1
        temp = heapq.heappop(A)
        combined_cookie = temp + 2 * heapq.heappop(A)
        heapq.heappush(A, combined_cookie)
    if A[-1] < k:
        iterations = -1
    return iterations

#TRICK: The key insight is to use a min-heap to efficiently get the two lightest cookies in each iteration. This ensures that we always combine the two smallest cookies, which minimizes the number of iterations needed to reach the target weight.

cookies(9, [2, 7, 3, 6, 4, 6])
