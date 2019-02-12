# PROBLEM : Given array, return its powerset

# Time : O(n.2^n) | Space : O(n.2^n) - n is avg length of currentSubset
def powerset(array):
    subsets = [[]] 
    for elem in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [elem])
                
    return subsets

print(powerset([1,2,3]))
