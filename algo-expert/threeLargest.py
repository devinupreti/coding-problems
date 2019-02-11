# PROBLEM : Given array, return a sorted array of the three largest values in the original array.

# Time : O(n) | Space : O(1)
def findThreeLargestNumbers(array):
    num1 = -float("inf") # largest
    num2 = -float("inf")
    num3 = -float("inf") # smallest
    for number in array:
        if number > num3:
            if number > num2:
                if number > num1:
                        num3 = num2
                        num2 = num1
                        num1 = number
                else:
                        num3 = num2
                        num2 = number
            else:
                num3 = number
    return [num3,num2,num1]

assert findThreeLargestNumbers([141,1,17,-7,-17,-27,18,541,8,7,7]) == [18,141,541]
			 
