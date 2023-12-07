#!/usr/bin/env python3
'''Module for sequece
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns the first element of a sequence or None if empty.
    '''
    if lst:
        return lst[0]
    else:
        return None
