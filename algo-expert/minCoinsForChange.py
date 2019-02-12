# PROBLEM : Given array of coin denominations and target value.
#           Return smallest number of coins required to make target.
#           If impossible return -1.

# Time : O(nd) | Space : O(n)
def minCoins(n, denoms):
    numOfCoins = [float("inf") for amount in range(n + 1)]
    numOfCoins[0] = 0 # Base Case
    for denom in denoms:
        for amount in range(len(numOfCoins)):
            if denom <= amount:
                numOfCoins[amount] = min(numOfCoins[amount], numOfCoins[amount - denom] + 1)
    if numOfCoins[n] == float("inf"):
        return -1
    else:
        return numOfCoins[n]

assert minCoins(7,[1,5,10]) == 3

        
