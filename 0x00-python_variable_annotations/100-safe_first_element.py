#!/usr/bin/env python3
"""
Module that returns the first element of a list if it exists,
otherwise returns None
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a list if it exists,
    otherwise returns None."""
    if lst:
        return lst[0]
    else:
        return None
