# Implement DFS on class Node

# DFS can be implemented using Recursion or Stack
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # Recursion 
    # Time : O(v + e) | Space : O(v) - for array and recursion stack
    def depthFirstSearch(self, array):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)
        return array

    # Stack 
    # Time : O(v + e) | Space : O(v) - for array and recursion stack
    def dfs(self,array):
        stack = [self]
        while len(stack) > 0:
            current = stack.pop()
            array.append(current.name)
            for child in current.children:
                stack.append(child)
        return array

test = Node("A")
test.addChild("B").addChild("C")
test.children[0].addChild("D")

assert test.depthFirstSearch([]) == ["A","B","D","C"]
assert test.dfs([]) == ["A","C","B","D"]


        
