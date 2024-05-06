#!/usr/bin/env python3
"""Contains a method that spawns wait_random n times with a
specified delay between each call."""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times
    with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds for
        each wait_random call. Default is 10.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    delays = []

    # Create a list to hold tasks
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Await all tasks concurrently
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
