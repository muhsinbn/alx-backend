#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
            self, index: int = None, page_size: int = 10) -> Dict[str, Any]:
        """
        Get a page from the indexed dataset with additional
        pagination metadata.

        Args:
        index (int): The start index of the return page.
        page_size (int): The number of items per page.

        Returns:
        Dict[str, Any]: A dictionary containing the dataset page and metadata
        """
        assert isinstance(
                index, int) and index >= 0, \
            "index must be a non-negative integer"
        assert isinstance(
                page_size, int) and page_size > 0, \
            "page_size must be an integer greater than 0"

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index
        dataset_len = len(indexed_data)

        while len(data) < page_size and current_index < dataset_len:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        next_index = current_index if current_index < dataset_len else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }
