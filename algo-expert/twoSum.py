"""
PROBLEM :
Given an array of integers and a target
return the two numbers such that they add up to a specific target.

If no solution exists then return empty array
"""

# Example :
# [3,5,-4,8,11,1,-1,6], 10
# returns - [-1,11]

# Using two pointers
# Time : O(nlogn) | Space : O(1)
def twoSum(array, targetSum):
    array.sort()
    first = 0
    last = len(array) - 1
    while first < last:
        num1 = array[first]
        oneNeeds = targetSum - num1
        num2 = array[last]

        if num2 > oneNeeds:
            last = last - 1
        elif num2 < oneNeeds:
            first = first + 1
        else:
            return [num1,num2]
    return []

# Using Hash Table
# Time : O(n) | Space : O(n)
def twoSumHT(array, targetSum):
    table = set([])
    for number in array:
        required = targetSum - number
        if required in table:
            return sorted([required,number]) # If you want the answer to be sorted
        else:
            table.add(number)
    return []


assert twoSum([3,5,-4,8,11,1,-1,6], 10) == [-1,11]
assert twoSumHT([3,5,-4,8,11,1,-1,6], 10) == [-1,11]


