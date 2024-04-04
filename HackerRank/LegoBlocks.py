
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


LegoBlocks(2, 2)