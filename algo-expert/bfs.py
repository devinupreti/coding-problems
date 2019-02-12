class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self
        
    # Time : O(v + e) | Space : O(v)
    def breadthFirstSearch(self, array):
        queue = []
        queue.append(self)
        while len(queue) != 0:
            elem = queue.pop(0)
            for child in elem.children:
                queue.append(child)
            array.append(elem.name)
        return array

        

