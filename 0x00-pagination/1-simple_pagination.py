#!/usr/bin/env python3

""" Python script that contains function named index_range
that takes two integer arguments page and page_size.
Function returns a tuple of size two containing a start index
and an end index corresponding to the range of indexes to return
in a list for those particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
"""

import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple containing the start index and end index for pagination.
    Args:
        page (int): The current page number.
        page_size (int): The number of items per page.
    Returns:
        tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a page of data from the dataset
            based on pagination parameters.
        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of items per page (default is 10).
        Returns:
            List[List]: A list of rows corresponding to the requested page.
        """
        dataset = self.dataset()  # Get the dataset

        # Validate page
        assert isinstance(page, int) and page > 0
        # Validate page_size
        assert isinstance(page_size, int) and page_size > 0

        try:
            # Get the start and end indexes
            start_index, end_index = index_range(page, page_size)
            return dataset[start_index:end_index]
        except IndexError as e:
            return []
