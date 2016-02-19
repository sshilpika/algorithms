import sys
import unittest
import random
sys.path.append('../src')
from quick_sort import QuickSort

class Test(unittest.TestCase):
    def testquicksort(self):
        items = [random.randint(-100,100) for c in range(10000)]
        print("before sort ",items)
        QuickSort.sort(items)
        print("after sort ", items)
        for i in range(len(items)-1):
            if(items[i] > items[i+1]):
                self.fail("Quick sort failed!")
print(__name__)
if __name__ == '__main__':
    unittest.main()
