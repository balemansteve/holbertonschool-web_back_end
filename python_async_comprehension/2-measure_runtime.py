#!/usr/bin/env python3
"""
Module that measures the runtime of executing async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of executing async_comprehension
    four times concurrently
    Returns:
        float: The total runtime in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - start
