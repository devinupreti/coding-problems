# PROBLEM : Given two strings, return the minimum number of edit operations that
#           need to be performed on the first string to obtain the second string.
#           Operations - insert char, delete char, substitute char
#           Each Operation counts as 1.

# Time : O(nm) | Space : O(nm)
# Can be Optimized -> Time : O(nm) | Space : O(min(n,m)) 
def levenshteinDistance(str1, str2):
    edits = [[0 for col in range(len(str2)+1)] for row in range(len(str1)+1)]
    edits[0][0] = 0
    for col in range(1,len(str2)+1):
        edits[0][col] = 1 + edits[0][col-1]
    for row in range(1,len(str1)+1):
        edits[row][0] = 1 + edits[row-1][0]
    for row in range(1,len(str1)+1):
        for col in range(1,len(str2)+1):
            if str1[row-1] == str2[col-1]:
                    edits[row][col] = edits[row-1][col-1]
            else:
                    edits[row][col] = 1 + min(edits[row][col-1], edits[row-1][col-1], edits[row-1][col])
    return edits[len(str1)][len(str2)]
	
	
assert levenshteinDistance("abc","yabd") == 2
