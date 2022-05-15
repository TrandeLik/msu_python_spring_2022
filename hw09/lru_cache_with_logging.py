"""
Least recently used cache implementation with heapq python module
"""

import heapq
import sys
import logging.config
from logger_config import log_config


class LRUCache:
    """
    Least recently used cache class
    """
    def __init__(self, limit=42, cache_logger=None):
        """
        Initialization of cache with given limit of size
        """
        self.cache_logger = cache_logger
        if self.cache_logger:
            self.cache_logger.info(f"LRUCache with capacity {limit} initialization")
        self.usage = []
        self.limit = limit
        if limit < 0:
            if self.cache_logger:
                self.cache_logger.error("Using cache with negative capacity")
        self.data = {}
        self.current_priority = 0

    def __update_priority(self, key):
        """
        Update priority of element with given key
        """
        if self.cache_logger:
            self.cache_logger.info(f"Update priority for element with key {key}."
                                   f" It's new priority: {self.current_priority}")
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
            if self.cache_logger:
                self.cache_logger.warning(f"This cache hasn't element with key {key}")
            return None
        self.__update_priority(key)
        if self.cache_logger:
            self.cache_logger.info(f"Successfully got element with key {key}")
        return self.data[key]

    def set(self, key, value):
        """
        Put element with given key and value
        """
        if self.limit <= 0:
            if self.cache_logger:
                self.cache_logger.error("Using cache with negative capacity")
            return
        if key in self.data:
            if self.cache_logger:
                self.cache_logger.info(f"Set new value {value} to element with key {key}")
            self.data[key] = value
        else:
            if len(self.usage) >= self.limit:
                least_used = heapq.heappop(self.usage)
                if self.cache_logger:
                    self.cache_logger.info(f"Deleting least recently used element (key = {least_used[1]})")
                self.data.pop(least_used[1])
            self.data[key] = value
            if self.cache_logger:
                self.cache_logger.info(f"Adding a new element with key {key} and value {value}")
            heapq.heappush(self.usage, [0, key])
        self.__update_priority(key)


if __name__ == "__main__":
    logging.config.dictConfig(log_config)
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        logger = logging.getLogger("stream_logger")
    else:
        logger = logging.getLogger("file_logger")
    cache = LRUCache(2, logger)
    cache.set("k1", 0)
    cache.set("k1", 1)
    cache.get("k1")
    cache.set("k2", 2)
    cache.set("k3", 3)
    cache.get("k1")
    cache.get("k2")
    cache.get("k3")
    cache.set("k1", 4)
    cache.get("k1")
    cache.get("k2")
    cache.get("k3")
    cache = LRUCache(-1, logger)
    cache.set("k1", 0)
    cache.set("k1", 1)
    cache.get("k1")
