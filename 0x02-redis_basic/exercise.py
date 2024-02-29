#!/usr/bin/env python3
"""
redis ex
"""

import redis
import uuid
import functools
from typing import Union, Callable


def call_history(method: Callable) -> Callable:
    """create input output list"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper decorator"""
        ip = method.__qualname__ + ":inputs"
        op = method.__qualname__ + ":outputs"
        self._redis.rpush(ip, str(args))
        out = method(self, *args, **kwargs)
        self._redis.rpush(op, out)
        return out
    return wrapper


def count_calls(method: Callable) -> Callable:
    """creates wrapper"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper function for the method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method):
    """get everything back"""
    calls = method.__self__.get_str(method.__qualname__)
    name = method.__qualname__
    print("{} was called {} times:".format(name, calls))
    key = method.__qualname__ + ":inputs"
    ip = method.__self__._redis.lrange(key, 0, -1)
    key = method.__qualname__ + ":outputs"
    op = method.__self__._redis.lrange(key, 0, -1)
    for i, o in zip(ip, op):
        i = i.decode("utf-8")
        o = o.decode("utf-8")
        print("{}(*{}) -> {}".format(name, i, o))


class Cache:
    """cache class using redis"""
    def __init__(self):
        """init for the class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store key and val"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None):
        """convert into original type"""
        val = self._redis.get(key)
        if fn:
            return fn(val)
        return val

    def get_str(self, key: str):
        """convert to str"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str):
        """convert to int"""
        return self.get(key, int)
