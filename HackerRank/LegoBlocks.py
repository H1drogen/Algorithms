#You have an infinite number of 4 types of lego blocks of sizes given as (depth x height x width):

#Using these blocks, you want to make a wall of height  and width . Features of the wall are: The wall should not have any holes in it, The wall you build should be one solid structure, so there should not be a straight vertical break across all rows of bricks, The bricks must be laid horizontally.

# How many ways can the wall be built?




def LegoBlocks(n, m):
    mod = 1000000007
    dp = [0] * (m + 1)
    ways = [0] * (m + 1)
    ways[0] = 1

    for i in range(1, m + 1):
        for length in range(1, min(i, 4) + 1):
            ways[i] = (ways[i] + ways[i - length]) % mod

    dp[0] = 1
    for i in range(1, m + 1):
        dp[i] = pow(ways[i], n, mod)
        for j in range(i):
            dp[i] = (dp[i] - dp[j] * ways[i - j]) % mod

    return dp[n]


#TRICK:

LegoBlocks(2, 2)