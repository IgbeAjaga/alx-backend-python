#!/usr/bin/env python3
"""
Using a random module.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay of seconds.
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
