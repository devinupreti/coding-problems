# PROBLEM : Find closest value to given value in BST
# Assume there will be only 1 closest value

# Time : O(n) [avg - O(logn)] | Space : O(1)
def findClosest(tree, target):
    closest = float("inf")
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
    

# Time : O(n) [avg - O(logn)] | Space : O(n) - recursion stack
def findClosestRecursion(tree, target):
    def helper(tree, target, closest):
        if tree is None:
            return closest
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target < tree.value:
            return helper(tree.left, target, closest)
        elif target > tree.value:
            return helper(tree.right, target, closest)
        else:
            return closest
    # Original Function 
    return helper(tree, target, float("inf"))


