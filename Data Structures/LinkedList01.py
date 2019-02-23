import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert (self, data):
        if (self.head == None):
            self.head = Node(data)
        else:
            pointer = self.head
            while (pointer.next is not None):
                pointer = pointer.next
            pointer.next = Node(data)

    def delete (self, index):
        self.checkEmpty()
        if (index > self.length() or index < 0):
            print("Index out of bounds!")
            sys.exit(1)
        if index == 0:
            self.head = self.head.next
        else:
            count = 0
            pointer = self.head
            while (pointer.next is not None):
                if (count == index - 1):
                    break
                pointer = pointer.next
                count += 1
            pointer.next = pointer.next.next

    def length (self):
        count = 0
        pointer = self.head
        if (self.head is not None):
            count += 1
        while(pointer.next is not None):
            pointer = pointer.next
            count += 1
        return count

    def checkEmpty(self):
        if (self.head is None):
            print("Empty list!")
            sys.exit(1)

    def printList (self):
        self.checkEmpty()
        pointer = self.head
        while (pointer.next is not None):
            print(pointer.data, " ", end="")
            pointer = pointer.next
        print(pointer.data, " ", end="")
        print("")




##########################

if __name__ == "__main__":

    myList = LinkedList()

    myList.insert('a')
    myList.insert('b')
    myList.insert(3)
    myList.insert(4)
    myList.insert(5)

    myList.printList()

    myList.delete(0)

    myList.printList()
