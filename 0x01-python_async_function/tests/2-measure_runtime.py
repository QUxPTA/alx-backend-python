#!/usr/bin/env python3
"""Contains a method that measure the total execution time of
a function"""
from time import perf_counter
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay)
    and returns average time per call.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay in seconds for each wait_n call.

    Returns:
        float: Average execution time per call.
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
