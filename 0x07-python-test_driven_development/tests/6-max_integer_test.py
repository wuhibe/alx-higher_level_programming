#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for integers"""

    def test_max_integer(self):
        """Cases"""
        self.assertEqual(max_integer([6, 7, 9]), 9)
        self.assertEqual(max_integer([13, -2, -1, -9]), 13)
        self.assertEqual(max_integer([11, 22, -9]), 22)
        self.assertEqual(max_integer([-11, -22, -9]), -9)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([13]), 13)
        self.assertEqual(max_integer([2, 26, 9]), 26)
        self.assertEqual(max_integer([756980, 21756, -96]), 756980)
        self.assertEqual(max_integer(), None)

if __name__ == '__main__':
    unittest.main()
