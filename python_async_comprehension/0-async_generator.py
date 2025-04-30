#!/usr/bin/env python3
"""
This module contains function to work
with asyncio
"""

import asyncio
import random

async def async_generator():
    """
    This function implement async generator yielding
    random numbers with delay
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
