# Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

def gridChallenge(grid):
    n = len(grid)
    for index, entry in enumerate(grid):
        grid[index] = sorted(entry)
    for i in range(n):
        for j in range(1, n):
            if grid[j][i] < grid[j-1][i]:
                return 'NO'
    return 'YES'



def gridChallengeAns(grid):
    for i in range(len(grid)):
        grid[i] = sorted(grid[i])
    for i in range(len(grid[0])):
        for j in range(1, len(grid)):
            if grid[j][i] < grid[j - 1][i]:
                return 'NO'
    return 'YES'

#TRICK: The first function is more efficient because it uses enumerate to iterate through the grid, which is faster than using a range and indexing. The second function uses a range and indexing, which is slower. Additionally, the first function uses a single loop to sort the rows, while the second function uses two loops to sort the rows and check the columns. This makes the first function more efficient overall.

print(gridChallenge(['abc', 'Imp', 'qrt']))