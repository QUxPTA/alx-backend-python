#!/usr/bin/env python3
"""Module that returns the sum of integers and floats in a mixed list."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of integers and floats in a mixed list."""
    return sum(mxd_lst)
