#!/usr/bin/env python3
"""
Module that returns a tuple with the string k
and the square of int/float v.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with the string k and the square of int/float v."""
    return k, v ** 2
