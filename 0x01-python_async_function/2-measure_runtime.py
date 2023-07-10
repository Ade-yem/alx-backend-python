#!/usr/bin/env python3
"""Measure the runtime"""

import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)
    Keyword arguments:
    n -- number of times to run
    max_delay -- maximum time of delay
    Return: total_time / n
    """
    init = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - init
    return total_time / n
