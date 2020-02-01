import unittest

import roman


class RomanTestCase(unittest.TestCase):
    def test_I_should_be_1(self):
        self.assertEqual(roman.to_int("I"), 1)

    def test_II_should_be_2(self):
        self.assertEqual(roman.to_int("II"), 2)

if __name__ == '__main__':
    unittest.main()
