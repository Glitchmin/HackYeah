from typing import Tuple


def v_add(a: Tuple, b: Tuple):
    return tuple(a + b for (a, b) in zip(a, b))


def v_subtract(a: Tuple, b: Tuple):
    return tuple(a - b for (a, b) in zip(a, b))


def v_mul(a: Tuple, b: Tuple):
    return tuple(a * b for (a, b) in zip(a, b))


def v_div(a: Tuple, b: Tuple):
    return tuple(a / b for (a, b) in zip(a, b))
