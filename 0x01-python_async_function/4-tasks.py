#!/usr/bin/env python3
"""Contains a method that spawns Tasks n times with a
specified delay between each call."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Asynchronous routine that spawns task_wait_random
    n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds
        for each task_wait_random call. Default is 10.

    Returns:
        List[float]: The list of delays in ascending order.
    """
    delays = []

    # Create a list to hold tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Await all tasks concurrently
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
