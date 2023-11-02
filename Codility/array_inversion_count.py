
def solution(A):
    total_count = len(A)
    count = 0
    for p in range(0, total_count - 1):
        for q in range(1 + p, total_count):
            if A[q] < A[p]:
                count += 1
        if count > 1000000000:
            count = -1
            break
    return count

solution([-1, 6, 3, 4, 7, 4])


