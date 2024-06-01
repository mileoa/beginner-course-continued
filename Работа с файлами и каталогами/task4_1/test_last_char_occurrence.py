import unittest
import random
from task4_1 import last_char_occurrence

class TestsLastCharOccurence(unittest.TestCase):

    def test_regressiion(self):
        self.assertEqual(last_char_occurrence("abcde", "d"), 3)

    def test_border(self):
        self.assertEqual(last_char_occurrence("abcde", "z"), -1)
        self.assertEqual(last_char_occurrence("zbcde", "z"), 0)
        self.assertEqual(last_char_occurrence("zbcdz", "z"), 4)
        self.assertEqual(last_char_occurrence("zbcdz", "zz"), -1)

    def test_empty(self):
        self.assertEqual(last_char_occurrence("", "z"), -1)
        self.assertEqual(last_char_occurrence("abcd", ""), -1)
        self.assertEqual(last_char_occurrence("", ""), -1)

    def test_random(self):
        for i in range(100000):
            string = []
            char = str(random.randint(0, 9))
            k = -1
            for j in range(random.randint(0, 10)):
                string.append(str(random.randint(0, 9)))
                if string[j] == char:
                    k = j

            self.assertEqual(last_char_occurrence("".join(string), char), k)

if __name__ == "__main__":
    unittest.main()
