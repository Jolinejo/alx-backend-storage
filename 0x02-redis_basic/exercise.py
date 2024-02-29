#!/usr/bin/env python3
"""
redis ex
"""

import redis
import uuid
from typing import Union, Callable


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

    def get(self, key: str, fn: Callable = None):
        """convert into original type"""
        val = self._redis.get(key)
        if fn:
            return fn(data)
        return val

    def get_str(self, key: str):
        """convert to str"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        """convert to int"""
        return self.get(key, int)
