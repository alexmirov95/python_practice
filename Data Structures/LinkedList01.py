import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


    def insert (self, data):
        '''
        Inserts new node into linked list containing data.
        '''
        if (self.head == None):
            self.head = Node(data)
        else:
            pointer = self.head
            while (pointer.next is not None):
                pointer = pointer.next
            pointer.next = Node(data)


    def delete (self, index):
        '''
        Removes node from linked list that matches data.
        '''
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
        '''
        Returns the number of nodes in the linked list.
        '''
        count = 0
        pointer = self.head
        
        if self.head is None:
            return 0
        else:
            count += 1

        while pointer.next is not None:
            pointer = pointer.next
            count += 1
        return count


    def checkEmpty(self, exit=True):
        '''
        Exits the program if the linked list is empty.
        '''
        if (self.head is None):
            print("Empty list!")
            if exit: sys.exit(1)


    def access(self, index):
        '''
        Returns the data found at the index into the linked list.
        '''
        self.checkEmpty()
        if index < 0 or index >= self.length():
            print("Out of bounds")
            sys.exit(1)

        ct = 0
        pointer = self.head
        while pointer.next is not None:
            if ct == index:
                return pointer.data
            ct += 1
            pointer = pointer.next
        if ct == index:
            return pointer.data



    def find(self, data):
        '''
        Returns index of first instance of data match.
        '''
        self.checkEmpty()
        ct = 0
        pointer = self.head
        while pointer.next is not None:
            if pointer.data is data:
                return ct
            ct += 1
            pointer = pointer.next
        if pointer.data is data:
            return ct
        return None


    def printList (self):
        '''
        Prints all node's data in the linked list.
        '''
        self.checkEmpty(exit=False)
        pointer = self.head
        while (pointer.next is not None):
            print(pointer.data, " ", end="")
            pointer = pointer.next
        print(pointer.data, " ", end="")
        print("")


    def getList (self):
        '''
        Returns an array containing the data from all nodes in the linked list.
        '''
        self.checkEmpty()
        arr = []
        pointer = self.head
        while (pointer.next is not None):
            arr.append(pointer.data)
            pointer = pointer.next
        arr.append(pointer.data)
        return arr

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

    print(myList.access(2))
    print(myList.access(0))
    print(myList.access(myList.length() - 1))

    print(myList.find("b"))
    print(myList.find(5))
