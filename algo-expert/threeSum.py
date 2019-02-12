# PROBLEM : Given an array and a target, return all triplets that sum upto the target

# Time : O(n) 
def twoNumberSum(array, target):
    if len(array) < 2:
        return []
    first = 0
    last = len(array) - 1
    solution = []
    while first < last:
        if array[first] + array[last] < target:
            first += 1
        elif array[first] + array[last] > target:
            last -= 1
        else:
            solution.append([array[first],array[last]])
            first += 1
            last -= 1
    return solution

# Time : O(n^2) | Space : O(n)
def threeNumberSum(array, targetSum):
    array.sort() # O(nlogn) 
    solution = []
    for index in range(len(array)):
        target = targetSum - array[index]
        twoSums = twoNumberSum(array[index+1:], target)
        for sums in twoSums:
            x,y = sums
            solution.append([array[index],x,y])
    return solution
	



assert threeNumberSum([12,3,1,2,-6,5,-8,6],0) == [[-8,2,6],[-8,3,5],[-6,1,5]]

