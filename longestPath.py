"""
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2.
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format,
return the length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.
"""

# NOTE :
# The name of a file contains at least a period and an extension.
# The name of a directory or sub-directory will not contain a period.


# Time : O(n) | Space : O(m) - hash table for length at each depth
def lengthLongestPath(pathString):
    maxlen = 0
    pathlen = {0: 0} # Depth : Length
    l = pathString.splitlines()
    for line in l:
        depth = line.count('\t')
        name = line.lstrip('\t')
        #print(name, depth)
        if '.' in name: # If is a file
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1 # 1 for / between 
    #print(pathlen)
    return maxlen
    

p = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
test = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
assert lengthLongestPath(test) == 32 
assert lengthLongestPath(p) == 20

