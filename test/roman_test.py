import unittest

import roman


class RomanTestCase(unittest.TestCase):
    def test_I_should_be_1(self):
        self.assertEqual(roman.to_int("I"), 1)

    def test_II_should_be_2(self):
        self.assertEqual(roman.to_int("II"), 2)

    def test_Q_should_raise(self):
        with self.assertRaises(roman.RomanNumberFormatException):
            roman.to_int("Q")


if __name__ == '__main__':
    unittest.main()
