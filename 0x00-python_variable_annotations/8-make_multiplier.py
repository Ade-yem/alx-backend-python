#!/usr/bin/env python3
"""Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier"""
    def multiply(value: float) -> float:
        """multiplies"""
        return value * multiplier
    return multiply
