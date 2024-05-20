#!/usr/bin/env python3
"""
Module that returns the value associated with the given key in the dictionary,
or the default value if the key is not found.
"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Returns the value associated with the given key in the dictionary,
    or the default value if the key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
