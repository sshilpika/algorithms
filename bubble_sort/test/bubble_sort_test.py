import random
import sys
sys.path.append('../src')
from bubble_sort import BubbleSort
import unittest

class Test(unittest.TestCase):
    def testbubblesort(self):
        a = [random.randint(-100,100) for c in range(1000)]

        print('before sort', a)
        BubbleSort.sort(a)
        print('after sort',a)
        for i in range(len(a)-1):
            if(a[i] > a[i+1]):
                self.fail('bubble sort failed')
if __name__ == '__main__':
    unittest.main()
