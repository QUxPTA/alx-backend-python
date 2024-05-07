#!/usr/bin/env python3
"""Contains a method that returns a task"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.
    Task for wait_random function with the specified max_delay.

    Args:
        max_delay (int): The maximum delay in seconds for wait_random.

    Returns:
        asyncio.Task: The asyncio Task object.
    """
    # Create and return the asyncio.Task object
    return asyncio.create_task(wait_random(max_delay))
