# Problem : Invert given Binary Tree

# Time : O(n) | Space : O(d) - recursion stack
def invertBinaryTree(tree):
    if tree is not None:
        tree.left, tree.right = tree.right, tree.left
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
