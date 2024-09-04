#!/usr/bin/env python3
""" Class LIFOCache that inherits from BaseCaching in caching system."""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Class that inherits from base_caching file."""

    def __init__(self):
        """Initialization"""
        super().__init__()

        # List to keep track of the order of insertion
        self.order = []

    def put(self, key, item):
        """Method that adds to the cache."""
        if key is None or item is None:
            return

        # If the cache is full, remove the first item (FIFO)
        if key not in self.cache_data and len(
                self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the last item (LIFO)
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

        # If the key already exists, remove it from the order list
        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ get an item by key."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
