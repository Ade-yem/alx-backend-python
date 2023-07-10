#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """will spawn wait_random n times with the specified max_delay
    Keyword arguments:
    n -- number of times to be spawned
    max_delay -- maximum time of delay
    Return:  return the list of all the delays (float values).
    """
    return sorted([await wait_random(max_delay) for _ in range(n)])
