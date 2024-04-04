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

print(gridChallenge(['abc', 'Imp', 'qrt']))