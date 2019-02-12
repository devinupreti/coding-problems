# PROBLEM : Given non-empty array of integers, return maximum sum that can be obtained
#           using only adjacent numbers.

# Time : O(n) | Space : O(1)
def kadanesAlgorithm(array):
    for index in range(1,len(array)):
        array[index] = max(array[index],array[index]+array[index-1])
    return max(array)

assert kadanesAlgorithm([3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]) == 19


