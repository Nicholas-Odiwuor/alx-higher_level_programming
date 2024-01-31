#!/usr/bin/python3
"""
Unittests for max_integer function
"""

import unittest
max_integer = __import__('max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test cases for max_integer function
    """

    def test_regular_list(self):
        """
        Test max_integer with a regular list.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([10, -3, 5, 8]), 10)
        self.assertEqual(max_integer([-5, -2, -10, -1]), -1)

    def test_empty_list(self):
        """
        Test max_integer with an empty list.
        """
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        """
        Test max_integer with a list containing only one element.
        """
        self.assertEqual(max_integer([7]), 7)

    def test_duplicate_values(self):
        """
        Test max_integer with a list containing duplicate values.
        """
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
        self.assertEqual(max_integer([1, 1, 1, 4, 1, 1]), 4)

    def test_floats(self):
        """
        Test max_integer with a list containing floats.
        """
        self.assertEqual(max_integer([1.5, 2.3, 0.9, 1.7]), 2.3)
        self.assertEqual(max_integer([-5.2, 7.8, -2.3, 0.1]), 7.8)

    def test_mixed_types(self):
        """
        Test max_integer with a list containing mixed types.
        """
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3, 4])

if __name__ == '__main__':
    unittest.main()

