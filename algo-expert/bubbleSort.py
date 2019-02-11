
# Better Implementation
# -----------------------
# Space - O(1) - always
# Best - Time : O(n)
# Avg/Worst -  Time : O(n^2)
# ------------------------
def bubbleS(array):
    isSorted = False
    index = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - index):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
        index += 1
    return array


# Time : O(n^2) | Space : O(1)
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1): # Iterate over all but the last element
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


assert bubbleS([8,5,2,9,5,6,3]) == [2,3,5,5,6,8,9]
assert bubbleSort([8,5,2,9,5,6,3]) == [2,3,5,5,6,8,9]

