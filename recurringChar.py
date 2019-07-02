"""
Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, 
"acbbac" -> "b"
"abcdef" -> null

1. Search - O(n^2) | O(1)
2. Sort - O(nlogn) | O(1)
3. Hash Set - O(n) | O(n)
"""

# Using set 
# Time : O(n) | Space : O(n)
def repeatChar(string):
    seen = set()
    for char in string:
        if char in seen:
            return char
        else:
            seen.add(char)
    
    return None

answer = repeatChar("abcdef")
print(answer)
