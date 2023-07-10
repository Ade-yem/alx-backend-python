#!/usr/bin/env python3
"""Tasks"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """will spawn wait_random n times with the specified max_delay
    Keyword arguments:
    n -- number of times to be spawned
    max_delay -- maximum time of delay
    Return:  return the list of all the delays (float values).
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))
