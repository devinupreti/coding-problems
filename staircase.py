# PROBLEM : There exists a staircase with N steps, and you can climb up
#           either 1 or 2 steps at a time.
#           Given N, write a function that returns
#           the number of unique ways you can climb the staircase.
#           The order of the steps matters.

# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2

# Time : O(2^n) | Space : O(n) - recursion stack
def climbStairs(stairs):
    if stairs < 2:
        return 1
    elif stairs == 2:
        return 2
    else:
        return climbStairs(stairs-1) + climbStairs(stairs-2)

# Time : O(n) | Space : O(n)
def climbStairsDP(stairs):
    if stairs < 2:
        return 1
    ways = [0 for _ in range(stairs)]
    ways[0] = 1 # base case
    ways[1] = 2 # base case
    for index in range(2,stairs):
        ways[index] = ways[index-1] + ways[index-2]
    return ways[stairs-1]

assert climbStairs(4) == 5
assert climbStairsDP(4) == 5

# What if, instead of being able to climb 1 or 2 steps at a time,
# you could climb any number from a set of positive integers X?
# For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

# Note : This is similar to the coin change problem but order matters

# Recursion
# l - possible number of steps | n - stairs
# Time : O(l^n) | Space : O(n) - recursion stack
def climbStairsAny(stairs ,steps_list):
    n = stairs
    X = steps_list
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in X:
        return 1 + sum(staircase(n - x, X) for x in X if x < n)
    else:
        return sum(staircase(n - x, X) for x in X if x < n)


# Dynamic Programming
# Time : O(mn) | Space : O(n)
def staircase(stairs, step_list):
    cache = [0 for _ in range(stairs + 1)]
    cache[0] = 1
    for i in range(stairs + 1):
        for x in step_list:
            if i - x > 0:
                cache[i] += cache[i - x]
        cache[i] += 1 if i in step_list else 0
    return cache[stairs]

print(climbStairsAny(4,[1,2]))
assert climbStairsAny(4,[1,2]) == 5

print(climbStairsAny(4,[3,2]))
print(staircase(4,[3,2]))
