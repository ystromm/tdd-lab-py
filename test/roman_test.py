import unittest
from src.roman import to_int, NotARomanNumber


class RomanTestCase(unittest.TestCase):


    def test_roman_i_convert_to_int_one(self):
      # given
      expected = 1
      # when
      actual = to_int("i")
      # then
      self.assertEqual(expected, actual)

    def test_roman_I_convert_to_int_one(self):
      # given
      expected = 1
      # when
      actual = to_int("I")
      # then
      self.assertEqual(expected, actual)

# with self.assertRaises(TypeError):
#    self.testListNone[:1]

    def test_roman_ii_convert_to_two(self):
      expected = 2
      actual = to_int("ii")
      self.assertEqual(expected, actual)

    def test_roman_II_convert_to_two(self):
      expected = 2
      actual = to_int("II")
      self.assertEqual(expected, actual)

    def test_blablabla_convert_to_incorrect_input(self):
      expected = NotARomanNumber 
      with self.assertRaises(expected):
        to_int("blablabla")


if __name__ == '__main__':
    unittest.main()
