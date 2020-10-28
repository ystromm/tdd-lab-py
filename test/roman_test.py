import unittest
from src.roman import to_int

class RomanTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_i_should_return_1(self):
        self.assertEqual(1, to_int("i"))

if __name__ == '__main__':
    unittest.main()
