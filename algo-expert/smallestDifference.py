# PROBLEM : Given two non empty arrays, return two numbers (one from each) whose difference is smallest

# Time : O(nlogn + mlogm) | Space : O(1)
def smallestDifference(arrayOne, arrayTwo):
    smallestDiff = float("inf")
    solution = [0,0]
    firstIndex = 0 
    secondIndex = 0
    arrayOne.sort()
    arrayTwo.sort()
    while firstIndex < len(arrayOne) and secondIndex < len(arrayTwo):
        if abs(arrayOne[firstIndex] - arrayTwo[secondIndex]) < smallestDiff:
            smallestDiff = abs(arrayOne[firstIndex] - arrayTwo[secondIndex])
            solution = [arrayOne[firstIndex],arrayTwo[secondIndex]]
        if arrayOne[firstIndex] < arrayTwo[secondIndex]:
            firstIndex += 1
        else:
            secondIndex += 1
    return solution

a1 = [-1,5,10,20,28,3]
a2 = [26,134,135,15,17]
assert smallestDifference(a1,a2) == [28,26]
