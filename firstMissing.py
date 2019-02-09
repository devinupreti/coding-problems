# PROBLEM : Given an array of integers, find the first missing positive integer
#           in linear time and constant space.
#           In other words, find the lowest positive integer that does not exist
#           in the array. The array can contain duplicates and negative numbers..

# Credit - asones
def firstMissing(nums):
    """
    Idea : 
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    nums.append(0)
    n = len(nums)

    print(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0

    print(nums)
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        nums[nums[i]%n]+=n

    print(nums)
    for i in range(1,len(nums)):
        if nums[i]/n==0:
            return i
    return n

nums = [3, 4, -1, 1]
print(firstMissing(nums))
assert (firstMissing(nums) == 2, "Test Failed")
