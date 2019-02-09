# PROBLEM : Given the root to a binary tree,
#           implement serialize(root), which serializes the tree into a string,
#           and deserialize(s), which deserializes the string back into the tree.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Time : O(n) - constant time for each node | Space : O(n + n) - worst case recursion stack and O(n) for string of nodes
def serialize(node):
    # Serialize tree
    def helper(node, traversed):
        if node is None:
            traversed.append("None")
            return traversed
        else:
            # Preorder Traversal
            traversed.append(node.val)
            helper(node.left, traversed)
            helper(node.right, traversed)
            return traversed
    s = helper(node, [])
    return ",".join(s)

# Time : O(n) | Space : O(n) - for the bst    
def deserialize(string):
    # Deserialize tree
    def helper(nodes):
        current = nodes[0]
        nodes.pop(0)
        if current == "None":
            return None
        root = Node(current)
        root.left = helper(nodes)
        root.right = helper(nodes)
        return root
    nodes = string.split(",")
    root = helper(nodes)
    return root

def test():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    

test()
