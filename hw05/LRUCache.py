"""
Least recently used cache implementation with heapq python module
"""

import heapq


class LRUCache:
    """
    Least recently used cache class
    """
    def __init__(self, limit=42):
        """
        Initialization of cache with given limit of size
        """
        self.usage = []
        self.limit = limit
        self.data = {}
        self.current_priority = 0

    def __update_priority(self, key):
        """
        Update priority of element with given key
        """
        for element in self.usage:
            if element[1] == key:
                element[0] = self.current_priority
        self.current_priority += 1
        heapq.heapify(self.usage)

    def get(self, key):
        """
        Get value of element with given key
        """
        if key not in self.data:
            return None
        self.__update_priority(key)
        return self.data[key]

    def set(self, key, value):
        """
        Put element with given key and value
        """
        if self.limit <= 0:
            return
        if key in self.data:
            self.data[key] = value
        else:
            if len(self.usage) >= self.limit:
                least_used = heapq.heappop(self.usage)
                self.data.pop(least_used[1])
            self.data[key] = value
            heapq.heappush(self.usage, [0, key])
        self.__update_priority(key)
