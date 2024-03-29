"""
Test for CustomList
"""

import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    """
    Testing class for CustomList
    """

    def test_str(self):
        """
        test __str__ method of CustomList
        """
        self.assertEqual(CustomList([]).__str__(), "[] sum 0")
        self.assertEqual(CustomList([-1, 0, 3]).__str__(), "[-1, 0, 3] sum 2")
        self.assertEqual(CustomList([2.5, 4, 3.5]).__str__(),
                         "[2.5, 4, 3.5] sum 10.0")
        self.assertEqual(CustomList([1, 2, 3]).__str__(), "[1, 2, 3] sum 6")

    def test_neg(self):
        """
        test __neg__ method of CustomList
        """
        self.assertEqual(list(-CustomList([1, 2, 3])),
                         list(CustomList([-1, -2, -3])))

    def test_add_custom_lists(self):
        """
        test + operator for two CustomLists
        """
        first = CustomList([1, 2])
        second = CustomList([1, 3, 4])
        self.assertEqual(list(first + second), [2, 5, 4])
        self.assertEqual(list(first), [1, 2])
        self.assertEqual(list(second), [1, 3, 4])
        self.assertEqual(list(second + first), [2, 5, 4])
        self.assertEqual(list(first), [1, 2])
        self.assertEqual(list(second), [1, 3, 4])
        first = CustomList([1, 2, 5])
        second = CustomList([1, 3, 4])
        self.assertEqual(list(second + first), [2, 5, 9])
        self.assertEqual(list(first), [1, 2, 5])
        self.assertEqual(list(second), [1, 3, 4])

    def test_add_list_and_custom_list(self):
        """
        test + operator for list and CustomList
        """
        first = [1, 2, 3]
        second = CustomList([1, 3, 4])
        self.assertEqual(list(first + second), [2, 5, 7])
        self.assertEqual(list(first), [1, 2, 3])
        self.assertEqual(list(second), [1, 3, 4])
        self.assertEqual(list(second + first), [2, 5, 7])
        self.assertEqual(list(first), [1, 2, 3])
        self.assertEqual(list(second), [1, 3, 4])
        first = CustomList([1, 2, 4])
        second = [1, 3]
        self.assertEqual(list(first + second), [2, 5, 4])
        self.assertEqual(list(first), [1, 2, 4])
        self.assertEqual(list(second), [1, 3])
        self.assertEqual(list(second + first), [2, 5, 4])
        self.assertEqual(list(first), [1, 2, 4])
        self.assertEqual(list(second), [1, 3])

    def test_subtract_custom_lists(self):
        """
        test - operator for two CustomLists
        """
        first = CustomList([1, 2, 4])
        second = CustomList([1, 3])
        self.assertEqual(first - second, [0, -1, 4])
        self.assertEqual(first, [1, 2, 4])
        self.assertEqual(second, [1, 3])
        self.assertEqual(second - first, [0, 1, -4])
        self.assertEqual(first, [1, 2, 4])
        self.assertEqual(second, [1, 3])
        first = CustomList([1, 2, 4])
        second = CustomList([1, 3, 5])
        self.assertEqual(first - second, [0, -1, -1])
        self.assertEqual(first, [1, 2, 4])
        self.assertEqual(second, [1, 3, 5])
        self.assertEqual(second - first, [0, 1, 1])
        self.assertEqual(first, [1, 2, 4])
        self.assertEqual(second, [1, 3, 5])

    def test_subtract_custom_list_and_list(self):
        """
        test - operator for CustomList and list
        """
        first = CustomList([1, 2])
        second = [1, 3, 4]
        self.assertEqual(list(first - second), [0, -1, -4])
        self.assertEqual(list(first), [1, 2])
        self.assertEqual(list(second), [1, 3, 4])
        self.assertEqual(list(second - first), [0, 1, 4])
        self.assertEqual(list(first), [1, 2])
        self.assertEqual(list(second), [1, 3, 4])
        first = CustomList([1, 2, 4])
        second = [1, 3, 4]
        self.assertEqual(list(first - second), [0, -1, 0])
        self.assertEqual(list(first), [1, 2, 4])
        self.assertEqual(list(second), [1, 3, 4])
        self.assertEqual(list(second - first), [0, 1, 0])
        self.assertEqual(list(first), [1, 2, 4])
        self.assertEqual(list(second), [1, 3, 4])

    def test_compare(self):
        """
        Test comparisons of CustomList
        """
        first = CustomList([1, 2, 3])
        second = CustomList([-1, 2])
        self.assertTrue(first > second)
        self.assertTrue(second < first)
        self.assertTrue(first >= second)
        self.assertTrue(second <= first)
        self.assertTrue(first != second)
        second = CustomList([1, 2, 3])
        self.assertTrue(first >= second)
        self.assertTrue(second <= first)
        self.assertTrue(first == second)
        first = CustomList([1, 2])
        second = CustomList([3])
        self.assertTrue(first == second)


if __name__ == '__main__':
    unittest.main()
