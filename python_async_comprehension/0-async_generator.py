#!/usr/bin/env python3
"""
This module contains function to work
with asyncio
"""

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    This function implement async generator yielding
    random numbers with delay
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
