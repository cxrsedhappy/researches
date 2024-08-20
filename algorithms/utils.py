from typing import Callable, Union, List

import numpy as np
from time import time


class Core:
    _registry = {}

    @classmethod
    def register(cls, func_names: Union[List[str], str, None] = None):
        """
        Decorator that registering functions.
        Passing no parameters means that function will be registered with func.__name__
        """
        if callable(func_names):
            func = func_names
            func_names = func.__name__
            cls._registry[func_names] = [func]
            return func

        def decorator(func: Callable) -> Callable:
            if func_names is None:
                cls._registry[func.__name__] = [func]
            elif isinstance(func_names, str):
                cls._registry.setdefault(func_names, []).append(func)
            elif isinstance(func_names, list):
                for name in func_names:
                    cls._registry.setdefault(name, []).append(func)
            return func
        return decorator

    @classmethod
    def show(cls):
        """Shows registered functions"""
        return cls._registry

    @classmethod
    def get_funcs(cls, names: list[str] | str) -> list[Callable]:
        result = []

        if isinstance(names, str):
            names = [names]

        for name in names:
            if name in cls._registry:
                for func in cls._registry[name]:
                    result.append(func)

        return list(set(result))


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


