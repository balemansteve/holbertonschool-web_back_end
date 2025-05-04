#!/usr/bin/env python3
"""
Module to deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Any


class Server:
    """
    Server class to paginate a database of popular baby names,
    supporting deletion-resilient pagination.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """
        Load and cache dataset from CSV file.
        Returns:
            List[List]: The dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Create and cache an indexed version of the dataset.
        Useful for deletion-resilient pagination.
        Returns:
            Dict[int, List]: A dict where each key is the index
            and value is the corresponding row from the dataset.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get a page of the dataset using hypermedia pagination that is
        resilient to deletions in the dataset.
        Args:
            index (int): The starting index for pagination.
            page_size (int): The number of items per page.
        Returns:
            Dict: A dictionary with the following keys:
                - index (int): the current start index,
                - data (List): the list of rows for this page,
                - page_size (int): the number of items returned,
                - next_index (int): the next index to continue pagination from.
        """

        assert index is not None and 0 <= index < len(self.indexed_dataset())

        indexed_dataset = self.indexed_dataset()

        data = []
        current_index = index
        while len(data) < page_size:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        next_index = current_index
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
