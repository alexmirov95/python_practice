'''
Merge Sort
By: Alex Mirov
'''
class MergeSort:
    '''
    Ascending merge sort
    '''

    def sort (self, arr):
        arrLeft = []
        arrRight = []

        self._splitLists(arr, arrLeft, arrRight)

        if len(arrLeft) > 1:
            arrLeft = self.sort(arrLeft)
        if len(arrRight) > 1:
           arrRight = self.sort(arrRight)

        return self._mergeLists(arrLeft, arrRight) 


    def _splitLists (self, arr, arrLeft, arrRight):
        n = len(arr)
        for i in range (0, n):
            if i <= (n/2) - 1:
                arrLeft.append(arr[i])
            else:
                arrRight.append(arr[i])


    def _mergeLists (self, listA, listB):
        a = 0
        b = 0
        merged = []
        for k in range (0, (len(listA) + len(listB))):
            if listA[a] < listB[b]:
                merged.append( listA[a] )
                a += 1
            else:
                merged.append( listB[b] )
                b += 1
                
            if a >= len(listA):
                while b < len(listB) :
                    merged.append( listB[b] )
                    b += 1
                break
            if b >= len(listB):
                while a < len(listA):
                    merged.append( listA[a] )
                    a += 1
                break
        return merged




##############################################################

if __name__ == "__main__":

    myArr = [6, 2, 7, 13, 1, 10, 3, 8, 4, 5, 9, 11, 14, 12]

    mergeStort = MergeSort()
    myArrSorted = mergeStort.sort(myArr)

    print("Original:")
    print(myArr)

    print("Merge Sorted:")
    print(myArrSorted)

