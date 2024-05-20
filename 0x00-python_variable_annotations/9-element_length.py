#!/usr/bin/env python3
"""
Module that returns a list of tuples containing
elements from lst and their respective lengths.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing
    elements from lst and their respective lengths."""
    return [(i, len(i)) for i in lst]
