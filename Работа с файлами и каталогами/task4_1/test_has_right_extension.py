import unittest
import random
from task4_1 import has_right_extension

class TestsHasRightExtension(unittest.TestCase):

    def test_regression(self):
        self.assertTrue(has_right_extension("test.txt", "txt"))
        self.assertFalse(has_right_extension("test.txt", "exe"))

    def test_border(self):
        self.assertFalse(has_right_extension("test.t", "txt"))
        self.assertFalse(has_right_extension("txt.", "txt"))
        self.assertFalse(has_right_extension(".txt", "txt"))
        self.assertFalse(has_right_extension("test.txttxt", "txt"))

    def test_empty(self):
        self.assertFalse(has_right_extension("test.txt", ""))
        self.assertFalse(has_right_extension("", "txt"))
        self.assertFalse(has_right_extension("", ""))

    def test_random(self):
        for i in range(100000):
            name = []
            extension = []
            fake_extension = []
            for j in range(random.randint(0, 10)):
                name.append(str(random.randint(0, 9)))
            for j in range(random.randint(0, 10)):
                extension.append(str(random.randint(0, 9)))
            for j in range(random.randint(0, 10)):
                fake_extension.append(str(random.randint(0, 9)))

            name = "".join(name)
            extension = "".join(extension)
            file_name = name + "." + extension
            fake_extension = "".join(fake_extension)
            fake_file_name = name + "." + fake_extension

            if extension != fake_extension:
                self.assertFalse(has_right_extension(file_name, fake_extension))
                self.assertFalse(has_right_extension(fake_file_name, extension))

            if name == "" or extension == "":
                self.assertFalse(has_right_extension(file_name, extension))
                continue
            self.assertTrue(has_right_extension(file_name, extension))

if __name__ == "__main__":
    unittest.main()