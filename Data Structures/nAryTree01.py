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
            Every node must be full (number of children == n) before creating another level.
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


    def preOrderPrint(self):
        self._preOrderPrint(self.root)
        print("")


    def _preOrderPrint(self, node):
        '''
        Visit the root node first and then traverse the subtree rooted at its children one by one
        '''
        if node is not None:
            # Print node
            print(node.data, " ", end="")
            
            # Traverse on children
            for i in range(0, self.n):
                self._preOrderPrint(node.children[i])


    def postOrderPrint(self):
        self._postOrderPrint(self.root)
        print("")


    def _postOrderPrint(self, node):
        '''
        Traverse the subtree rooted at its children first and then visit the root node itself. 
        '''
        if node is not None:
            # Traverse on children
            for i in range(0, self.n):
                self._postOrderPrint(node.children[i])
            
            # Print node
            print(node.data, " ", end="")


    def levelOrderPrint(self):
        # Print Root
        if self.root is not None:
            print(self.root.data, " ", end="")

        self._levelOrderPrint(self.root)
        print("")


    def _levelOrderPrint(self, node):
        '''
        Same with a binary tree. BFS will traverse the tree in level order. 
        '''
        if node is not None:
            # Print the children's data first
            for i in range(0, self.n):
                if node.children[i] is not None:
                    print(node.children[i].data, " ", end="")

            # Traverse on children
            for i in range(0, self.n):
                self._levelOrderPrint(node.children[i])


    def inOrderPrint(self):
        self._inOrderPrint(self.root, float("-inf"))
        print("")


    def _inOrderPrint(self, node, curMax):
        if node is not None:

            # Traverse on nodes less than current node's value
            for i in range(0, self.n):
                if node.children[i] is not None and \
                        node.children[i].data < node.data:
                    if node.children[i].data < curMax:
                        self._inOrderPrint(node.children[i], node.data)
                    # else:


            # Print Current Node
            print(node.data, " ", end="")

            # Traverse on nodes greater than current node's value
            for i in range(0, self.n):
                if node.children[i] is not None and node.children[i].data >= node.data:

                    self._inOrderPrint(node.children[i], curMax)


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

    myTree.preOrderPrint()
    myTree.postOrderPrint()
    myTree.levelOrderPrint()
    myTree.inOrderPrint()


