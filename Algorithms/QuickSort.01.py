'''
Ascending Quick Sort
By: Alex Mirov
March 2019
'''

import random

class QuickSort:
    '''
    Quick sort using random pivot selection.
    '''

    def sort(self, arr):
        sortedArr = []
        self._partition(arr, sortedArr)
        return sortedArr


    def _partition(self, arr, sortedArr):
        if len(arr) == 0: return

        # Append equal elements to sortedArr
        elif len(set(arr)) == 1:
            for el in arr: sortedArr.append(el)
            return

        # Randomly select pivot
        pivotIndex = random.randint(0, len(arr) - 1)
        pivot = arr[pivotIndex]
        
        # Split array into less than pivot and greater than or equal to pivot
        lessThan, greaterThan = self._split(arr, pivot)

        # Recurse on sub arrays
        self._partition(lessThan, sortedArr)
        self._partition(greaterThan, sortedArr)


    def _split(self, arr, pivot):
        '''
        Split arr[] into 2 sub arrays, one that is < than the pivot, and another that 
        is >= the pivot.
        '''
        lessThan = []
        greaterThan = []
        for el in arr:
            if el < pivot:
                lessThan.append(el)
            else:
                greaterThan.append(el)

        return lessThan, greaterThan



if __name__ == "__main__":

    def simpleSortTest():
        myArr = [6, 2, 7, 13, 1, 10, 3, 8, 4, 5, 9, 11, 14, 12, 11]
        
        correct = myArr.copy()
        correct.sort()

        myArrSorted = QuickSort().sort(myArr)
        assert myArrSorted == correct, "Incorrect Sort!"


    def fuzzyTest1(n):
        myArr = []
        for i in range(0, n): myArr.append(random.randint(-500, 500))
        
        correct = myArr.copy()
        correct.sort()

        myArrSorted = QuickSort().sort(myArr)
        assert myArrSorted == correct, "Incorrect Sort!"
    

    simpleSortTest()
    fuzzyTest1(5000)
