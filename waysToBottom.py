"""
You are given an N by M matrix of 0s and 1s. 
Starting from the top left corner, how many ways are there to reach the bottom right corner?

You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

For example, given the following matrix:
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:

Right, down, down, right
Down, right, down, right
"""

def traverse(matrix, row, col):
    # at end
    if row == len(matrix) - 1  and col == len(matrix[0]) - 1:
        return 1
    
    # invalid indexes
    if row > len(matrix) - 1  or col > len(matrix[0]) - 1 or matrix[row][col] == 1:
        return 0 
    
    down = traverse(matrix, row + 1, col) # down
    right = traverse(matrix, row, col + 1) # right
    return down + right

def totalWays(matrix):
    if len(matrix) > 0 and len(matrix[0]) > 0:
        return traverse(matrix, 0, 0)
    return 0


matrix = [[0, 0, 1], [0, 0, 1], [1, 0, 0]]
print(totalWays(matrix))
