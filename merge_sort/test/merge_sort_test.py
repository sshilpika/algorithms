import unittest
import sys
sys.path.append('../src')
from merge_sort import MergeSort
import random
class Test(unittest.TestCase):
    def testmergesort(self):
        print('main')
        A = [random.randint(-100,100) for c in range(100000)]
        print('before sort',A)
        MergeSort.sort(A)
        print('after sort', A)
        for i in range(len(A)-1):
            if A[i] > A[i+1]:
                self.fail('Error in Merge Sort')

if __name__ == '__main__':
    unittest.main()
