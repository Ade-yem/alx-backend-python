#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """execute async_comprehension four times in parallel"""
    init = time.time()
    gather = [async_comprehension(), async_comprehension(),
              async_comprehension(), async_comprehension()]
    await asyncio.gather(*gather)
    return time.time() - init
