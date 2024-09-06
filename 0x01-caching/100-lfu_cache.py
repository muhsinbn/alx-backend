#!/usr/bin/env python3
""" Class LFUCache that inherits from BaseCaching in caching system."""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """Class that inherits from base_caching file."""

    def __init__(self):
        """Initialization"""
        super().__init__()

        # List to keep track of the order of insertion
        self.usage_order = {}
        self.frequency = {}
        self.time = 0

    def put(self, key, item):
        """Method that adds to the cache."""
        if key is None or item is None:
            return

        # If the cache is full, remove the least frequently used(LFU)
        if key not in self.cache_data and len(
                self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the least frequently used item (LFU)
            last_key = [k for k, v in self.frequency.items() if v == min(
                self.frequency.values())]
            if len(last_key) > 1:
                last_key = min(last_key, key=lambda k: self.usage_order[k])
            else:
                last_key = last_key[0]
            del self.cache_data[last_key]
            del self.frequency[last_key]
            del self.usage_order[last_key]
            print("DISCARD: {}".format(last_key))

        # If the key already exists, remove it from the order list
        if key in self.cache_data:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        self.cache_data[key] = item
        self.usage_order[key] = self._current_time()

    def get(self, key):
        """ get an item by key."""
        if key is None or key not in self.cache_data:
            return None
        self.frequency[key] += 1
        self.usage_order[key] = self._current_time()
        return self.cache_data[key]

    def _current_time(self):
        """Return the current time (used for tracking usage order)."""
        import time
        self.time += 1
        return time.time()
