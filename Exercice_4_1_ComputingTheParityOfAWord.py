import unittest

from ProcessParity import process_parity


class Test_ComputingTheParityOfAWord(unittest.TestCase):

    def test_should_return__when(self):
        actual = process_parity(0)
        self.assertEqual(actual, 0, "Parity of 0 should be 0")