# PROBLEM : Implement an autocomplete system.
#           That is, given a query string s and a set of all possible query strings,
#           return all strings in the set that have s as a prefix

# For example, given the query string de and the set of strings [dog, deer, deal],
# return [deer, deal].

# n - number of strings
# m - length of longest string
# Time : O(n*m) | Space : O(n) - to store the solutions
def autoComplete(string_list, query):
    havePrefix = []
    for string in string_list:
        if string.startswith(query):
            havePrefix.append(string)
    return havePrefix

# !!!! Use Trie - [this is not complete solution to #11 ]

print(autoComplete(['dog','deer','deal'], 'de'))
            
