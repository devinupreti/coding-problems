# PROBLEM : Given the mapping a = 1, b = 2, ... z = 26,
#           and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3,
# since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable.
# For example, '001' is not allowed.

# Creating Mapping
import string
char_string = string.ascii_lowercase[:26]

current = 1
mapping = {}
for char in char_string:
    mapping[current] = char
    current += 1

# Time : O(2^n) | Space : O(n) - recursion stack
# T(n) = T(n-1) + T(n-2)
def decode(string):
    def helper(string):
        if len(string) < 2:
            return 1

        number = int(string)
        length = len(string)
        lastTwo = number % (10**2)

        if lastTwo in mapping:
            return helper(string[:-2]) + helper(string[:-1])
        else:
            return helper(string[:-1])
        
    count = helper(string)
    return count

# Dynamic Programming
# Time : O(n) | Space : O(n) - Hash Table
def decodeDP(string):
    if len(string) < 2:
        return 1
    count = [0 for _ in range(len(string)+1)]
    count[0] = 1
    count[1] = 1
    for index in range(2,len(string)+1):
        last = int(string[index-1])
        lastTwo = int(string[index-2:index])
        
        count[index] = count[index - 1] # for tree made by last index
        if lastTwo in mapping:
            count[index] += count[index - 2] # for tree made by last two index
    return count[len(string)]        
    
        
   
print(decode('111'))
print(decode('1234'))
print(decode('11111'))
print(decode('333'))
print("------------")
print(decodeDP('111'))
print(decodeDP('1234'))
print(decodeDP('11111'))
print(decodeDP('333'))
