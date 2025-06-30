import unittest
from calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = StringCalculator()

    def test_empty_string_returns_zero(self):
        self.assertEqual(self.calc.add(""), 0)

    def test_single_number_returns_value(self):
        self.assertEqual(self.calc.add("1"), 1)

    def test_two_numbers_comma_separated(self):
        self.assertEqual(self.calc.add("1,2"), 3)

    def test_multiple_numbers(self):
        self.assertEqual(self.calc.add("1,2,3,4"), 10)

    def test_newline_as_delimiter(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)

    def test_custom_delimiter_semicolon(self):
        self.assertEqual(self.calc.add("//;\n1;2"), 3)

    def test_custom_delimiter_pipe(self):
        self.assertEqual(self.calc.add("//|\n1|2|3"), 6)

    def test_negative_number_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("1,-2,3")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2")

    def test_multiple_negatives_in_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("1,-2,-5,3")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2,-5")

if __name__ == '__main__':
    unittest.main()
