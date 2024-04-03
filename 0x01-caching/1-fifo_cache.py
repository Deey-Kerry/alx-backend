#!/usr/bin/python3
"""a class FIFOCache that inherits from BaseCaching and is
a caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """inherits from BaseCaching and isa caching system"""
    def __init__(self):
        """Initialization the function"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """puts key in a function"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """gets a key"""
        return self.cache_data.get(key, None)
