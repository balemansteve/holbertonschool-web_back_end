#!/usr/bin/env python3
"""
Module for pagination of a dataset stored in a CSV file.
"""

from typing import List, Tuple
import math
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for a given page and page size.
    Args:
        page (int): The current page number (1-indexed).
        page_size (int): Number of items per page.
    Returns:
        Tuple[int, int]: A tuple containing the start and end
        indexes for slicing.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a CSV database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache dataset from the CSV file.
        Returns:
            List[List]: The dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a specific page of the dataset.
        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.
        Returns:
            List[List]: The corresponding slice of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()
        start_index, end_index = index_range(page, page_size)

        if start_index >= len(self.__dataset):
            return []
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieve a page of the dataset along with pagination metadata.
        Args:
            page (int): The current page number.
            page_size (int): Number of items per page.
        Returns:
            dict: Dictionary with pagination info:
                - page_size: actual number of items on this page
                - page: current page number
                - data: list of dataset rows for this page
                - next_page: next page number if available, else None
                - prev_page: previous page number if available, else None
                - total_pages: total number of pages
        """
        data = self.get_page(page, page_size)
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
