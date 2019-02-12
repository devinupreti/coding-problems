# PROBLEM :Given array of unique integers, return all possible permutations of it.

# Time : O(n*n!) | Space : O(n*n!)
def getPermutations(array):
    def helper(i, array, permutations):
        if i == len(array) - 1:
            permutations.append(array[:])
        else:
            for j in range(i, len(array)):
                array[i], array[j] = array[j], array[i]
                helper(i+1,array,permutations)
                array[j], array[i] = array[i], array[j]

    permutations = []
    helper(0,array, permutations)
    return permutations

print(getPermutations([1,2,3]))
