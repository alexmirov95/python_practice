'''
N-Ary Tree
By: Alex Mirov
Feb 2019
'''

class NAryTree:
    '''
    Complete N-Ary Tree.
    '''

    class Node():

        def __init__(self, n, data=None):
            self.data = data
            self.n = n
            self.children = [None] * n


        def emptyChildren(self):
            '''
            Returns the number of children that are None.
            '''
            ct = 0
            for child in self.children: 
                if child is None: ct += 1
            return ct


        def insertChild(self, data):
            '''
            Inserts child node at appropriate place in children array.
            Every node must be full before creating another level.
            '''
            # Iterate through children to find propper place to insert new node
            for i in range(0, self.n):
                # Check if new data is < child
                if self.children[i] is None or data < self.children[i].data:
                    # Check if children[] is not full
                    if self.emptyChildren() > 0 and self.emptyChildren() <= self.n:
                        # Shift all children right to make room for new node
                        for j in range(self.n - 1, i, -1): self.children[j] = self.children[j - 1]
                        # Create new node at i
                        self.children[i] = NAryTree.Node(self.n, data)
                    # Else children[] is completely full
                    else:
                        # Recursively insert at correct place
                        self.children[i].insertChild(data)
                    return
            # Case: Children[] is full and data is larger than all children --> Recurse at right most node
            self.children[self.n - 1].insertChild(data)


        def printNode(self):
            print(self.data, "( ", end="")
            for child in self.children:
                if child is None:
                    print(child, end="")
                    print(" ", end="")
                else:
                    print(child.data, end="")
                    print(" ", end="")

            print(")")


    def __init__(self, n=2):
        self.root = None
        self.n = n

    
    def insert (self, data):
        '''
        Inserts new node containing data into tree.
        '''
        if self.root is None:
            # Init root
            self.root = self.Node(self.n, data)
        else:
            # Insert new node
            self.root.insertChild(data)


    def _printTree(self, node):
        if node is None:
            return
        else:
            node.printNode()

            for child in node.children:
                if child is not None:
                    self._printTree(child)


    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)
        else:
            print("Empty tree!")


    def inOrderPrint(self):
        self._inOrderPrint(self.root)
        print("")


    def _inOrderPrint(self, node):
        if node is not None:
            for i in range(0, self.n - 1):
                self._inOrderPrint(node.children[i])
                print(node.data, " ", end="")

            self._inOrderPrint(node.children[self.n - 1])


if __name__ == "__main__":
    
    myTree = NAryTree(2)

    myTree.insert(5)
    myTree.insert(3)
    myTree.insert(10)
    myTree.insert(8)
    myTree.insert(7)
    myTree.insert(1)
    myTree.insert(2)
    myTree.insert(12)
    myTree.insert(11)
    myTree.insert(18)
    myTree.insert(6)

    myTree.printTree()

    myTree.inOrderPrint()


