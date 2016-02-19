import sys
import random
import unittest
sys.path.append('../src')
from heap_sort import HeapSort

class Test(unittest.TestCase):
    def testHeapSort(self):
        items = [random.randint(-1000,1000) for i in range(100000)]
        print('before sort ', items)
        HeapSort.sort(items)
        print('after sort ',items)
        for i in range(len(items)-1):
            if items[i] > items[i+1]:
                self.fail("Heap sort failed")
if __name__ == '__main__':
    unittest.main()
