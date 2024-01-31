import sys


def coinchange(coins, amount):
    lowest_count = sys.maxsize

    sorted(coins, reverse = True)
    for coin in coins:
        #this is to check for any multiples that exist which will be more efficient (e.g. [5,3] with target of 6)
        if amount % coin == 0:
            precount = 1
            temp = amount - coin
            while temp % coin == 0 and temp != 0:
                precount += 1
                temp -= coin
            if precount < lowest_count:
                lowest_count = precount

    count = 0
    remainder = amount
    x = 0
    biggest_denomination = coins[x]
    while biggest_denomination <= remainder:
        remainder -= biggest_denomination
        count += 1
        while biggest_denomination > remainder and x < (len(coins) - 1):
            x += 1
            biggest_denomination = coins[x]
    if count < lowest_count and remainder == 0:
        lowest_count = count
        
    if lowest_count != sys.maxsize:
        return lowest_count
    else:
        return -1



coinchange([5,3], 6)
coinchange([5,3], 8)

