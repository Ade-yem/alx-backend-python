#!/usr/bin/env python3
"""Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """type-annotated function sum_mixed_list which takes a list mxd_lst of
    integers and floats and returns their sum as a float"""
    sum: float = 0
    for i in mxd_lst:
        sum += float(i)
    return sum
