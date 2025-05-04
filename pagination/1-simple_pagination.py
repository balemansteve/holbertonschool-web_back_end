#!/usr/bin/env python3
"""
Module for pagination using a CSV file with baby names.
"""

from typing import List, Tuple
import math
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for pagination.
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.
    Returns:
        tuple: A tuple (start_index, end_index) for slicing the dataset.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache the dataset from the CSV file.
        Returns:
            List[List]: The dataset as a list of rows (excluding header).
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of the dataset.
        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.
        Returns:
            List[List]: A list of dataset rows for the requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(self.__dataset):
            return []
        return self.__dataset[start_index:end_index]
    