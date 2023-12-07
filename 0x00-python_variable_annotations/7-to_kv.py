#!/usr/bin/env python3
'''Module for tuple of (k, v^2)
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Returns a tuple of (k, v^2).
    '''
    return (k, float(v**2))
