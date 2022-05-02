"""
Tests for LRUCache
"""

import unittest
from LRUCache import LRUCache


class TestCache(unittest.TestCase):
    """
    Test cases for LRUCache
    """
    def test_size_one(self):
        """
        Cache size of one element
        """
        cache = LRUCache(1)
        cache.set("k1", 1)
        self.assertEqual(1, cache.get("k1"))
        cache.set(frozenset([1, 2]), LRUCache)
        self.assertEqual(LRUCache, cache.get(frozenset([1, 2])))
        self.assertEqual(None, cache.get("k1"))

    def test_simple_input(self):
        """
        Simple sequence of requests
        """
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")
        self.assertEqual(None, cache.get("k3"))
        self.assertEqual("val2", cache.get("k2"))
        self.assertEqual("val1", cache.get("k1"))
        cache.set("k3", [1, 2, 3])
        self.assertEqual([1, 2, 3], cache.get("k3"))
        self.assertEqual(None, cache.get("k2"))
        self.assertEqual("val1", cache.get("k1"))

    def test_empty_cache(self):
        """
        Cache size of zero
        """
        cache = LRUCache(0)
        cache.set("k1", 1)
        self.assertEqual(None, cache.get("k1"))

    def test_check_before_input(self):
        """
        Check if cache is empty before usage
        """
        cache = LRUCache(1)
        self.assertEqual(None, cache.get("k1"))
        cache.set("k1", -1)
        self.assertEqual(-1, cache.get("k1"))

    def test_multiple_set_and_get(self):
        """
        Multiple set and get operations for one key
        """
        cache = LRUCache(2)
        cache.set("k1", 0)
        cache.set("k1", 1)
        self.assertEqual(1, cache.get("k1"))
        self.assertEqual(1, cache.get("k1"))
        cache.set("k2", 2)
        cache.set("k3", 3)
        self.assertEqual(None, cache.get("k1"))
        self.assertEqual(2, cache.get("k2"))
        self.assertEqual(3, cache.get("k3"))
        cache.set("k1", 4)
        self.assertEqual(4, cache.get("k1"))
        self.assertEqual(None, cache.get("k2"))
        self.assertEqual(3, cache.get("k3"))
