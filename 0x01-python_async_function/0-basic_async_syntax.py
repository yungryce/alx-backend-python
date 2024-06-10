#!/usr/bin/env python3
'''Task 0's module.'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Generate and return a random float within the range 0 and max_int."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
