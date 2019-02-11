# PROBLEM : Given array and target, find index of target in array using Binary Search

# Iterative
# Time : O(log n) | Space : O(1)
def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2 # Floor division
        consider = array[middle]
        if target == consider:
            return middle
        elif target < consider:
            right = middle - 1
        else:
            left = middle + 1
    return -1
        

# Recursion
# Time : O(log n) | Space :  O(log n) - recursion stack
def binarySearchRec(array, target):
    if len(array) == 1 and array[0] != target:
        return -1
    middle = int(len(array) / 2)
    if array[middle] < target:
        index = binarySearchRec(array[middle:len(array)],target)
        if index == -1:
                return -1
        return middle + index
    elif array[middle] > target:
        return binarySearchRec(array[0:middle],target)
    else:
        return middle
		

assert binarySearch([0,1,21,33,45,45,61,71,72,73],33) == 3
assert binarySearchRec([0,1,21,33,45,45,61,71,72,73],33) == 3

