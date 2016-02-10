import unittest
import sys
sys.path.append('../src')
from insertion_sort import InsertionSort
import random
class Test(unittest.TestCase):
    def testInsertionSort(self):
        # randomly generate 1000 random numbers in the range -100 to 100
        A = [random.randint(-100,100) for c in range(1000)]

        print("before sort",A)
        InsertionSort.sort(A)
        print('After sort',A)
        for i in range(1, len(A)):
            if(A[i-1] > A[i]):
                self.fail('insertion sort method fails')
if __name__ == '__main__':
    unittest.main()
