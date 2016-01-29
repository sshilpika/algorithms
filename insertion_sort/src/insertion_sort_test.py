import unittest
from insertion_sort import InsertionSort
class Test(unittest.TestCase):
    def testInsertionSort(self):
        A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
        InsertionSort.sort(A)
        for i in range(1, len(A)):
            if(A[i-1] > A[i]):
                self.fail('insertion sort method fails')
if __name__ == '__main__':
    unittest.main()
