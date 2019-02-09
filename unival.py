# PROBLEM : A unival tree (which stands for "universal value") is a tree
#           where all nodes under it have the same value. (even None)
#           Given the root to a binary tree, count the number of unival subtrees.

class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

# Time : O(n) | Space : O(n) - recursion stack
def countUnival(node):
    if node is None:
        return 0
    
    if node.left is None and node.right is None:
        return 1
    elif node.left is None:
        return countUnival(node.right)
    elif node.right is None:
        return countUnival(node.left)
    elif node.left.value == node.right.value:
        return 1 + countUnival(node.left) + countUnival(node.right)
    else:
        return countUnival(node.left) + countUnival(node.right)

node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0) ) )
print(countUnival(node))
assert(countUnival(node) == 5, "Test Failed")
