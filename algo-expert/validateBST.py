# PROBLEM : Validate if a given binary tree is a BST (Binary Search Tree)
# - every node in left child tree is less node's value
# - vice versa for right tree

def validateBST(tree):
    def helper(tree, minValue, maxValue):
        if tree is None:
            return True
        if tree.value < minValue and tree.value >= maxValue:
            return False
        leftIsValid = helper(tree.left, minValue, tree.value)
        return leftIsValid and helper(tree.right, tree.value, maxValue)
    return helper(tree, float("-inf"),float("inf"))


        
