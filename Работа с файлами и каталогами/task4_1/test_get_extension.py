import unittest
import random
from task4_1 import get_extension

class TestsGetExtension(unittest.TestCase):
    
    def test_regressiion(self):
        self.assertEqual(get_extension("test.txt"), "txt")

    def test_border(self):
        self.assertIsNone(get_extension("test.txt."))
        self.assertIsNone(get_extension("testtxt"))
        self.assertIsNone(get_extension(".testtxt"))

    def test_empty(self):
        self.assertIsNone(get_extension(""))
    
    def test_random(self):
        for i in range(100000):
            name = []
            extension = []
            fake_extension = []
            for j in range(random.randint(0, 10)):
                name.append(str(random.randint(0, 9)))
            for j in range(random.randint(0, 10)):
                extension.append(str(random.randint(0, 9)))
            
            name = "".join(name)
            extension = "".join(extension)
            file_name = name + "." + extension

            if name == "" or extension == "":
                self.assertIsNone(get_extension(file_name))
                continue
            self.assertEqual(get_extension(file_name), extension)

if __name__ == "__main__":
    unittest.main()