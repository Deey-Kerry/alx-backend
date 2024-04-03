#!/usr/bin/python3
"""a class MRUCache that inherits from BaseCaching and is
a caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """Initialization of a class"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """puts a key in a method"""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Gets key in a method"""
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
