# PROBLEM : Given a list of integers, write a function that returns the
#           largest sum of non-adjacent numbers. Numbers can be 0 or negative.

# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5.
# [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Can you do this in O(N) time and constant space?

# Time : O(n) | Space : O(1)
def nonAdjacentSum(array):
    if len(array) < 3:
        return max(array)
    maxSecondLast = array[0]
    maxLast = array[1]
    for index in range(2,len(array)):
        maxYet = max(maxLast,maxSecondLast + array[index])
        maxSecondLast = max(maxLast,maxSecondLast)
        maxLast = maxYet
    return maxYet

arr = [2, 4, 6, 2, 5] 
assert nonAdjacentSum(arr) == 13, "Test 1 Failed"
arr2 = [5, 1, 1, 5]
assert nonAdjacentSum(arr2) == 10, "Test 2 Failed"
