
def numPaths(warehouse):
    count = [0]
    recursivesearch(0, 0, warehouse, count)
    return count[0] % (10**9 + 7)

def recursivesearch(n, m, warehouse, count):
    if n >= len(warehouse) or m >= len(warehouse[0]) or warehouse[n][m] == 0:
        return
    if n == len(warehouse) - 1 and m == len(warehouse[0]) - 1:
        count[0] += 1
        return
    if warehouse[n][m] == 1:
        recursivesearch(n + 1, m, warehouse, count)
        recursivesearch(n, m + 1, warehouse, count)


print(numPaths([[1, 1, 1, 1], [1, 1, 0, 1]]))



    # Write your code here
    # def dfs(x, y):
    #     if x < 0 or x >= len(warehouse) or y < 0 or y >= len(warehouse[0]) or warehouse[x][y] == 1:
    #         return 0
    #     if x == len(warehouse) - 1 and y == len(warehouse[0]) - 1:
    #         return 1
    #     warehouse[x][y] = 1
    #     paths = dfs(x + 1, y) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x, y - 1)
    #     warehouse[x][y] = 0
    #     return paths
    #
    # return dfs(0, 0)