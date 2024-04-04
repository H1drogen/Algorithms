
def solution(A):
    country_count = 0
    rows = len(A)
    columns = len(A[0])
    for n in range(rows):
        for m in range(columns):
            if A[n][m] == 0:
                continue
            else:
                country_count += 1
                eliminate_country(A, n, m)
    return country_count

def eliminate_country(A, n, m):
    value = A[n][m]
    A[n][m] = 0
    if n + 1 < len(A):
        if value == A[n+1][m]:
           eliminate_country(A, n + 1, m)
    if n - 1 >= 0:
        if value == A[n-1][m]:
            eliminate_country(A, n - 1, m)
    if m + 1 < len(A[0]):
        if value == A[n][m+1]:
            eliminate_country(A, n, m + 1)
    if m - 1 >= 0:
        if value == A[n][m-1]:
            eliminate_country(A, n, m - 1)
    return

solution([[5,4,4],[4,3,4],[3,2,4],[2,2,2],[3,3,4],[1,4,4],[4,1,1]])
