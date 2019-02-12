"""
PROBLEM:
Given 2d matrix of distinct integers and target number.
Each row is sorted and each column is sorted.
Return [row, col] of target, if not in matrix return [-1,-1]
"""

# Time : O(n + m) | Space : O(n + m)
def searchSortedMatrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row,col]
    return [-1,-1]

