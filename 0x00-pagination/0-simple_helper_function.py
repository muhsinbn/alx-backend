#!/usr/bin/env python3
""" Helper function index_range that takes two int args."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Calculate the start and end indices for pagination.

    Given a page number and the size of the page (number of items per page),
    this function returns a tuple containing the start index and the end index
    for that page.

    Args:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    tuple: A tuple containing the start index and the end index.
    """
    # Calculate the start index for the given page
    start_index = (page - 1) * page_size

    # Calculate the end index for the given page
    end_index = start_index + page_size

    return start_index, end_index
