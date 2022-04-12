"""
Tests for written descriptors
"""

import unittest
from descriptor import Integer, PositiveInteger, String


class TestInteger(unittest.TestCase):
    """
    Tests for Integer descriptor
    """
    def setUp(self):
        """
        Creates a testing object
        """
        class Data:
            """
            Container for Integer
            """
            int_val = Integer()

            def __init__(self):
                self.int_val = 0

        self.instance = Data()

    def test_set_int(self):
        """
        Correct assignment
        """
        self.instance.int_val = 100
        self.assertEqual(100, self.instance.int_val)
        self.instance.int_val = 0
        self.assertEqual(0, self.instance.int_val)
        self.instance.int_val = -34
        self.assertEqual(-34, self.instance.int_val)

    def test_set_not_int(self):
        """
        Non-correct assignment
        """
        self.instance.int_val = "not int"
        self.assertEqual(0, self.instance.int_val)
        self.instance.int_val = 10
        self.assertEqual(10, self.instance.int_val)
        self.instance.int_val = {}
        self.assertEqual(10, self.instance.int_val)
        self.instance.int_val = 1.2
        self.assertEqual(10, self.instance.int_val)


class TestPositiveInteger(unittest.TestCase):
    """
    Tests for PositiveInteger descriptor
    """
    def setUp(self):
        """
        Creates a testing object
        """
        class Data:
            """
            Container for PositiveInteger
            """
            uint_val = PositiveInteger()

            def __init__(self):
                self.uint_val = 0

        self.instance = Data()

    def test_set_uint(self):
        """
        Correct assignment
        """
        self.instance.uint_val = 100
        self.assertEqual(100, self.instance.uint_val)
        self.instance.uint_val = 0
        self.assertEqual(0, self.instance.uint_val)

    def test_set_not_uint(self):
        """
        Non-correct assignment
        """
        self.instance.uint_val = "also not int"
        self.assertEqual(0, self.instance.uint_val)
        self.instance.uint_val = 10
        self.assertEqual(10, self.instance.uint_val)
        self.instance.uint_val = {}
        self.assertEqual(10, self.instance.uint_val)
        self.instance.uint_val = -1
        self.assertEqual(10, self.instance.uint_val)
        self.instance.uint_val = 1.2
        self.assertEqual(10, self.instance.uint_val)


class TestString(unittest.TestCase):
    """
    Tests for String descriptor
    """
    def setUp(self):
        """
        Creates a testing object
        """
        class Data:
            """
            Container for String
            """
            str_val = String()

            def __init__(self):
                self.str_val = 0

        self.instance = Data()

    def test_set_string(self):
        """
        Correct assignment
        """
        self.instance.str_val = "it is string"
        self.assertEqual("it is string", self.instance.str_val)
        self.instance.str_val = ""
        self.assertEqual("", self.instance.str_val)

    def test_set_not_uint(self):
        """
        Non-correct assignment
        """
        self.instance.str_val = 100
        self.assertEqual("", self.instance.str_val)
        self.instance.str_val = "it is string"
        self.assertEqual("it is string", self.instance.str_val)
        self.instance.str_val = {}
        self.assertEqual("it is string", self.instance.str_val)
        self.instance.str_val = 1.2
        self.assertEqual("it is string", self.instance.str_val)


if __name__ == "__main__":
    unittest.main()
