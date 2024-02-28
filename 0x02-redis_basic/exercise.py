#!/usr/bin/env python3
"""
redis ex
"""

import redis
import uuid
from typing import Union


class Cache:
    """cache class using redis"""
    def __init__(self):
        """init for the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store key and val"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
