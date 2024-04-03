#!/usr/bin/python3
"""Create a class BasicCache that inherits from BaseCaching
and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class inheriting from BaseCache"""
    def __init__(self):
        """Initialization of class"""
        super().__init__()

    def put(self, key, item):
        """Puts a key"""
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """gets a key"""
        if key not in self.cache_data.keys() or key is None:
            return None
        return self.cache_data.get(key)
