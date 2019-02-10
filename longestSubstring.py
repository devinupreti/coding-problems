# PROBLEM : Given an integer k and a string s,
#           find the length of the longest substring
#           that contains at most k distinct characters.

# For example, given s = "abcba" and k = 2, the longest substring
# with k distinct characters is "bcb".

# Leetcode - Question 340

# Brute Force Solution - O(N^3)

# Time : O(n) | Space : O(m) - hash table for char counts
from collections import defaultdict
def longestSub(k, s):
    st = 0  # start
    counter = defaultdict(int)
    maxa = 0
    for index, val in enumerate(s):
        if counter[val] == 0:
            k -= 1
        counter[val] += 1
        while k < 0:
            counter[s[st]] -= 1
            if counter[s[st]] == 0:
                k += 1
            st += 1

        maxa = max(maxa, index - st + 1)
    return maxa

print(longestSub(2,"abcba")) # 3
print(longestSub(3,"aabacbebebe")) # cbebebe - 7

            
            
        
        
    
