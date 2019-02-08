# PROBLEM : Given array and target number, tell if two numbers whose sum is equal
#           to target exist in the array.

# Time : O(nlogn) | Space : O(1) - Sort and two pointers
def twoSum(array, target):
    array.sort()
    if len(array) < 2:
        return False

    first_index = 0
    last_index = len(array) - 1

    while first_index < last_index:
        twoSum = array[first_index] + array[last_index]
        if twoSum == target:
            return True
        elif twoSum > target:
            last_index -= 1
        else:
            first_index += 1
            
    return False

# Time : O(n) | Space : O(n) - Hash Table or Set
def twoSumHT(array, target):
    diffTable = set([])
    for num in array:
        need = target - num
        if need in diffTable:
            return True
        else:
            diffTable.add(num)
    return False

# Brute Force
# Time : O(n^2) | Space : O(1)

test_array = [10,15,3,7]
test_target = 17

print(twoSum(test_array,test_target))
print(twoSumHT(test_array,test_target))
        

