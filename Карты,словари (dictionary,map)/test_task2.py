import unittest
import random
from task2 import get_met_n

class TestsGetMetN(unittest.TestCase):

    def test_regression(self):
        self.assertCountEqual(get_met_n([1, 2, 3, 4, 3, 4], 2), [3, 4])

    def test_empty(self):
        self.assertCountEqual(get_met_n([], 1), [])
        self.assertCountEqual(get_met_n([1], 1), [1])

    def test_random(self):
        for i in range(5000):
            array = []
            count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            random_n = random.randint(0, 1000)

            # Запоняем массив случайными числами и считаем
            # количество каждого элемента.
            for i in range(0, 1000):
                random_number = random.randint(0, 9)
                array.append(random_number)
                count[random_number] += 1

            filtered = get_met_n(array, random_n)
            if random_n == 0:
                self.assertEqual(filtered, [])
                continue
            
            for i in range(len(count)):
                if count[i] >= random_n:
                    self.assertIn(i, filtered)
                    continue
                self.assertNotIn(i, filtered)

    def test_border(self):
        self.assertEqual(get_met_n([], 0), [])
        self.assertEqual(get_met_n([1, 2, 3, 3], 0), [])
        self.assertEqual(get_met_n([3, 3, 3, 3], 4), [3])

if __name__ == "__main__":
    unittest.main()
