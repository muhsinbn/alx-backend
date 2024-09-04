#!/usr/bin/env python3
""" A class BasicCache that inherits from BaseCaching."""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ class that inherits from the base_caching file"""

    def put(self, key, item):
        """ Method that adds to the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Method to get an item by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
