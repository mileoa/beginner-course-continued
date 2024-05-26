import unittest
import random

from simplesort import sort

class SimpleSortTests(unittest.TestCase):

    def test_regression(self):
        self.assertListEqual(sort([-4, -5, -3, 0, 4, 3, 2, 1, -1, -2]), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4])
        self.assertListEqual(sort([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]), [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4])
        self.assertListEqual(sort([7, 7, -5, -5, 6, 6, -1, -1, 2, 2]), [-5, -5, -1, -1, 2, 2, 6, 6, 7, 7])
        self.assertListEqual(sort([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]), [5, 5, 5, 5, 5, 5, 5, 5, 5, 5])
        self.assertListEqual(sort([-5, -5, -5, -5, -5, -5, -5, -5, -5, -5]), [-5, -5, -5, -5, -5, -5, -5, -5, -5, -5])

    def test_empty_list(self):
        self.assertListEqual(sort([]), [])

    def test_random(self):
        for i in range(100000):
            array = []
            for j in range(10):
                array.append(random.randint(-100, 100))
            sort(array)

            for k in range(len(array) - 1):
                self.assertLessEqual(array[k], array[k+1])
    
    def test_max(self):
        self.assertListEqual(sort([9223372036854775808, -4611686018427387904]), [-4611686018427387904, 9223372036854775808])

if __name__ == '__main__':
    unittest.main()