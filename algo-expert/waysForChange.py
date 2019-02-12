# PROBLEM : Given array representing coins and a target value.
#           Return the number of ways to make change for that amount.
#           You can use unlimited number of coins for each.

# Time : O(nd) | Space: O(n)
def waysForChange(n, denoms):
    ways = [0 for _ in range(n+1)] # each index represents target value
    ways[0] = 1 # base case
    for currency in denoms:
        for target in range(len(ways)):
            if currency <= target:
                ways[target] += ways[target - currency]
    return ways[n]

assert waysForChange(6,[1,5]) == 2

        
