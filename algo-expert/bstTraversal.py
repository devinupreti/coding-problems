# For all three
# Time : O(n) | Space : O(n) 

def inOrderTraverse(tree, array):
    if tree is None:
        return array
    else:
        array = inOrderTraverse(tree.left,array)
        array.append(tree.value)
        array = inOrderTraverse(tree.right,array)
        return array

def preOrderTraverse(tree, array):
    if tree is None:
        return array
    else:
        array.append(tree.value)
        array = preOrderTraverse(tree.left,array)
        array = preOrderTraverse(tree.right,array)
        return array

def postOrderTraverse(tree, array):
    if tree is None:
        return array
    else:
        array = postOrderTraverse(tree.left,array)
        array = postOrderTraverse(tree.right,array)
        array.append(tree.value)
        return array


