#!/usr/bin/env python3
'''Module for a list of tuples
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Returns a list of tuples containing element and its length.
    '''
    return [(i, len(i)) for i in lst]
