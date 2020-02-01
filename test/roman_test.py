import unittest

import roman


class RomanTestCase(unittest.TestCase):
    def test_I_should_be_1(self):
        self.assertEqual(roman.to_int("I"), 1)

    def test_II_should_be_2(self):
        self.assertEqual(roman.to_int("II"), 2)

    def test_III_should_be_3(self):
        self.assertEqual(roman.to_int("III"), 3)

    def test_iii_should_be_3(self):
        self.assertEqual(roman.to_int("iii"), 3)

    def test_Q_should_raise(self):
        with self.assertRaises(roman.RomanNumberFormatException):
            roman.to_int("Q")

    def test_i_should_be_1(self):
        self.assertEqual(roman.to_int("i"), 1)


if __name__ == '__main__':
    unittest.main()
