"""
Tests for CustomMeta
"""

import unittest
from custom_meta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    """
    Class for testing of CustomMeta
    """
    x = 50
    _x = 0
    _x_ = -1
    _x__ = -2
    __x = -3

    def __init__(self, val=99):
        self.val = val

    def line(self):
        """
        method for test
        """
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class TestCustomMeta(unittest.TestCase):
    """
    Tests for CustomMeta class
    """
    def test_has_custom_attrs(self):
        """
        Checks that there are custom attributes
        """
        print(CustomClass.__dict__)
        instance = CustomClass()
        self.assertTrue(hasattr(instance, 'custom_x'))
        self.assertTrue(hasattr(instance, 'custom_val'))
        self.assertTrue(hasattr(instance, 'custom_line'))
        self.assertTrue(hasattr(CustomClass, 'custom_x'))
        self.assertTrue(hasattr(CustomClass, 'custom__x'))
        self.assertTrue(hasattr(CustomClass, 'custom__x_'))
        self.assertTrue(hasattr(CustomClass, 'custom__x__'))
        self.assertTrue(hasattr(CustomClass, 'custom__CustomClass__x'))

    # def test_new_attribute(self):
    #     instance = CustomClass()
    #     instance.new_attr = 0
    #     self.assertTrue(hasattr(instance, 'custom_new_attr'))
    #     self.assertFalse(hasattr(instance, 'new_attr'))

    def test_has_not_non_custom_attrs(self):
        """
        Checks that there not any non-custom attributes
        """
        instance = CustomClass()
        self.assertFalse(hasattr(instance, 'x'))
        self.assertFalse(hasattr(instance, 'val'))
        self.assertFalse(hasattr(instance, 'line'))
        self.assertFalse(hasattr(CustomClass, 'x'))
        self.assertFalse(hasattr(CustomClass, '_x'))
        self.assertFalse(hasattr(CustomClass, '_x_'))
        self.assertFalse(hasattr(CustomClass, '_x__'))
        self.assertFalse(hasattr(CustomClass, '_CustomClass__x'))

    def test_correct_working(self):
        """
        Checks that everything works correct after customization
        """
        instance = CustomClass(42)
        self.assertEqual(42, instance.custom_val)
        self.assertEqual(50, instance.custom_x)
        self.assertEqual(100, instance.custom_line())
        self.assertEqual(50, CustomClass.custom_x)
        self.assertEqual(0, CustomClass.custom__x)
        self.assertEqual(-1, CustomClass.custom__x_)
        self.assertEqual(-2, CustomClass.custom__x__)
        self.assertEqual(-3, CustomClass.custom__CustomClass__x)

    def test_magic_methods(self):
        """
        Checks that magic methods are not custom
        """
        instance = CustomClass()
        self.assertEqual("Custom_by_metaclass", instance.__str__())
        self.assertEqual("Custom_by_metaclass", str(instance))

    def test_new_attr(self):
        """
        Test for dynamically added attributes
        """
        instance = CustomClass()
        instance.very_interesting_new_attribute = -1
        self.assertTrue(hasattr(instance, 'custom_very_interesting_new_attribute'))
        self.assertFalse(hasattr(instance, 'very_interesting_new_attribute'))
        self.assertEqual(-1, instance.custom_very_interesting_new_attribute)


if __name__ == "__main__":
    unittest.main()
