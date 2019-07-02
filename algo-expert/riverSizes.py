"""
PROBLEM:
Given 2d array (matrix) of 1s and 0s.
0 - land
1 - part of river
A river consists of any number of 1s that are either horizontally or vertically adjacent.
The number of adjacent 1s forming a river determin its size.

Return an array of sizes of all rivers in the input matix. In any order.
"""

"""
Cleaner
Space : O(nm) | Time : O(nm)
def traverse(mat, i, j):
    if i < 0 or i > len(mat)-1 or j < 0 or j > len(mat[0])-1 or mat[i][j] == 0:
        return
    
    mat[i][j] = 0
    traverse(mat, i, j + 1)
    traverse(mat, i, j - 1)
    traverse(mat, i + 1, j)
    traverse(mat, i - 1, j)
    
    return 1
    
def riverSizes(mat):
    #visited = [ [False for col in range(len(mat[0])) ] for row in range(len(mat))]
    totalIslands = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                totalIslands += traverse(mat, i, j)
    return totalIslands
  
"""



# Time : O(wh) | Space: O(wh) - width and height of input matrix
def riverSizes(matrix):
    array = []
    visited = matrix[:]
    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if visited[i][j] == 1:
                    visited[i][j] = False
            else:
                    visited[i][j] = True
                
    solution = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if visited[row][col]:
                    continue
            else:  # 1 and not visited
                    traverseNode(row,col,matrix,visited,solution)
    return solution
	
def traverseNode(i,j,matrix,visited,solution):
    currentRiverSize = 0
    nodesToVisit = [[i,j]]
    while len(nodesToVisit) != 0:
        currentNode = nodesToVisit.pop()
        i,j = currentNode[0],currentNode[1]
        if visited[i][j]:
                visited[i][j] = True
                continue
        visited[i][j] = True
        currentRiverSize += 1
        connectedNodes = getNeighbours(i,j,matrix,visited)
        for node in connectedNodes:
                nodesToVisit.append(node)
    if currentRiverSize > 0:
            solution.append(currentRiverSize)

def getNeighbours(i,j,matrix,visited):
    neighbours = []
    if i-1 >= 0 and not visited[i-1][j]:
        neighbours.append([i-1,j])
    if i < len(matrix) - 1  and not visited[i+1][j]:
        neighbours.append([i+1,j])
    if j-1 >= 0 and not visited[i][j-1]:
        neighbours.append([i,j-1])
    if j < len(matrix[0]) - 1 and not visited[i][j+1]:
        neighbours.append([i,j+1])
    return neighbours
	
	
		
