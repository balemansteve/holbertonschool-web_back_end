#!/usr/bin/env python3
""" Module to safely get the first element of a sequence """

from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of the list if it
    exists, otherwise returns None.
    Returns:
        Optional[Any]: The first element of the
        sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
