import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if (self.root is None):
            self.root = Node(value)
        else:
            pointer = self.root
            while (pointer is not None):
                if value < pointer.value: # left
                    left = pointer.left
                    if left is not None:
                        pointer = left
                    else:
                        pointer.left = Node(value)
                        break
                elif value > pointer.value: # right
                    right = pointer.right
                    if right is not None:
                        pointer = right
                    else:
                        pointer.right = Node(value)
                        break
                else:
                    print("No redundant values allowed!")
                    sys.exit(1)

    def preOrderPrint (self):
        self.checkEmpty()
        self._preOrderHelper(self.root)
        print("")

    def _preOrderHelper(self, node):
        if node is not None:
            print(node.value, " ", end="")
            self._preOrderHelper(node.left)
            self._preOrderHelper(node.right)

    def inOrderPrint (self):
        self.checkEmpty()
        self._inOrderHelper(self.root)
        print("")

    def _inOrderHelper (self, node):
        if node is not None:
            self._inOrderHelper(node.left)
            print(node.value, " ", end="")
            self._inOrderHelper(node.right)

    def postOrderPrint (self):
        self.checkEmpty()
        self._postOrderHelper(self.root)
        print("")

    def _postOrderHelper (self, node):
        if node is not None:
            self._postOrderHelper(node.left)
            self._postOrderHelper(node.right)
            print(node.value, " ", end="")

    def levelOrderPrint (self):
        self.checkEmpty()
        print(self.root.value, " ", end="")
        self._levelOrderHelper(self.root)
        print("")

    def _levelOrderHelper (self, node):
        if node is not None:
            if node.left is not None:
                print (node.left.value, " ", end="")
            if node.right is not None:
                print (node.right.value, " ", end="")

            self._levelOrderHelper(node.left)
            self._levelOrderHelper(node.right)

    def checkEmpty(self):
        if self.root is None:
            print("Empty Tree!")
            sys.exit(1)


#########################################

myTree = BST()

#              5
#           /     \
#          3       8
#        /  \     /  \
#       1    2   7    10
#               /       \
#              6         12
#                       /  \
#                     11    14

myTree.insert(5)
myTree.insert(3)
myTree.insert(8)
myTree.insert(10)
myTree.insert(7)
myTree.insert(1)
myTree.insert(2)
myTree.insert(6)
myTree.insert(12)
myTree.insert(11)
myTree.insert(14)

print("Preorder:")
myTree.preOrderPrint()

print("Inorder:")
myTree.inOrderPrint()

print("Postorder:")
myTree.postOrderPrint()

print("Levelorder:")
myTree.levelOrderPrint()






