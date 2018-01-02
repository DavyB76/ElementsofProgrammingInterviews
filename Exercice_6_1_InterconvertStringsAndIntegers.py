import unittest

from convertNumeralToString import convertNumeralToString


class Test_6_1_InterconvertStringsAndIntegers(unittest.TestCase):

    def test_should_return_the_zero_string_when_converting_the_zero_number(self):
        actual = convertNumeralToString(0)
        self.assertEqual(actual, "0", "the zero number should be converted to the zero string")