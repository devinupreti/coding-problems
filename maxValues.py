"""
Leetcode 239
PROBLEM :
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example,
given array = [10, 5, 2, 7, 8, 7] and k = 3,
we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2) | O(k)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space.
"""

# Hints :
# - Maintain Queue
# - Use Indexes
# - Largest element always on left
# - Keep only useful elements | Not less than incoming element
from collections import deque # Queue
def maxValues(nums, k):
    q = deque()
    result = []
    for i in range(len(nums)):
        # the first/left (max) element is out of the current window
        if q and i - q[0] == k:
            q.popleft()
        
        while q:
            # pop lesser elements from last
            #print(i,nums[i],q[-1],q)
            if nums[q[-1]] < nums[i]:
                q.pop()
            else:
                break
        
        q.append(i)
        
        if i >= k-1: # i == k-1 is the beginning of a full window
            result.append(nums[q[0]])
        
    return result

#print([10, 5, 2, 7, 8, 7])
print(maxValues([10, 5, 2, 7, 8, 7],3))
