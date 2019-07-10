
# Time : O(N) | Space : O(log N)
def maxPathSum(tree):
	return max(getmaxPath(tree))
			
def getmaxPath(tree):
	if tree == None:
		return (0,0)
	leftBranchSum, leftSum = getmaxPath(tree.left)
	rightBranchSum, rightSum = getmaxPath(tree.right)
	maxBranchSum = max(leftBranchSum, rightBranchSum)
	maxSumAsBranch = max(tree.value, tree.value + maxBranchSum)
	
	maxSumAsRoot = max(maxSumAsBranch, leftBranchSum + tree.value + rightBranchSum)
	maxRunningSum = max(leftSum, rightSum, maxSumAsRoot)
	return (maxSumAsBranch,maxRunningSum)
  
