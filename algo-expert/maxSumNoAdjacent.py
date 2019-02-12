# PROBLEM : Given an array, return the max sum that can be generated using elements
#           from that array such that no adjacent elements are chosen.


# Dynamic Programming
# Time : O(n) | Space : O(1)
def maxSumNoAdjacent(array):
    # Base cases
    if not len(array):
        return 0
    elif len(array) == 1:
        return array[0]
    second = array[0]
    first = max(array[0],array[1])
    for i in range(2, len(array)):
        current = max(first, second + array[i])
        second = first
        first = current
    return first

assert maxSumNoAdjacent([75,105,120,75,90,135]) == 330
