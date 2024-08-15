import numpy as np

from utils import generate_array, speed

array = generate_array(n=10)


@speed
def find_max(a: list[array] | np.ndarray) -> int:
    """
    Time: O(n)
    Space : O(1)
    """
    _max = -999999999
    for i in range(len(a)):
        if a[i] > _max:
            _max = a[i]
    return _max


print(array)
print(find_max(array))
