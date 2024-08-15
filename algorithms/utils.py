from typing import Callable

import numpy as np
from time import time


def speed(func: Callable):
    def wrapper(*args, **kwargs):
        _st = time()
        result = func(*args, **kwargs)
        _fn = time()
        print(f'{func.__name__}: Finished in {_fn - _st:.3f} seconds')
        return result
    return wrapper


def generate_array(low: int = -10, high: int = 10, n: int = 10) -> np.ndarray:
    """Generates random array from *low* (inclusive) to *high* (exclusive) with shape of *n*"""
    return np.random.randint(low, high, n)


def generate_matrix(low: int = -10, high: int = 10, n: int = (10, 10)) -> np.ndarray:
    """Generates matrix from *low* (inclusive) to *high* (exclusive) with shape of *n*"""
    return np.random.randint(low, high, n)


