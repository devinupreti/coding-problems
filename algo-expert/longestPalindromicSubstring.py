# PROBLEM : Given a string, return its longest palindromic substring.

# Time : O(n^2) | Space : O(1)
def longestPalindromicSubstring(string):
    currentLongest = [0,1]
    for index in range(1,len(string)):
        odd_centre = getPalindrome(string, index-1, index+1)
        even_centre = getPalindrome(string, index-1, index)
        longest = max(odd_centre, even_centre, key = lambda x : x[1] - x[0])
        currentLongest = max(longest,currentLongest, key = lambda x : x[1] - x[0])
    return string[currentLongest[0]:currentLongest[1]]
	
def getPalindrome(string, start, end):
    while start >= 0 and end < len(string):
        if string[start] != string[end]:
            break
        start -= 1
        end += 1
    return [start+1, end]
