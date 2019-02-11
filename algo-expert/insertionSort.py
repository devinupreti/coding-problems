# Time : O(n) | Space : (1) - Best
# Time : O(n^2) | Space : O(1) - Avg / Worst
def insertionSort(array):
    for i in range(1,len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1],array[j] = array[j],array[j+1]
            j = j - 1
    return array

assert insertionSort([8,5,2,9,5,6,3]) == [2,3,5,5,6,8,9]
