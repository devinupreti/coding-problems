# PROBLEM : Check if a given string is a palindrome

# Time : O(n) | Space : O(1)
def isPalindrome(string):
    first = 0
    last = len(string) - 1
    while first < last:
        if string[first] != string[last]:
                return False
        first += 1
        last -= 1
    return True

assert isPalindrome("acbbca") == True
assert isPalindrome("devin") == False

