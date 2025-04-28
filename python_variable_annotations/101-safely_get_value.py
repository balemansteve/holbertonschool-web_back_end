#!/usr/bin/env python3
"""Module to Given the parameters and the return values,
add type annotations to the function"""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping, key: Any, default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Retrieve a value from a dictionary using a given key, returning a
    default value if the key is not found.

    Returns:
        Union[Any, T]: The value associated with the key if found,
        otherwise the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
