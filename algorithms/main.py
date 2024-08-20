import numpy as np

from utils import Core, generate_array, speed

array = generate_array(n=10000000)


@speed
@Core.register(['leetcode', 'array'])
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


@speed
@Core.register('leetcode')
def canBeIncreasing(nums: list[int]) -> bool:
    """
    **https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/\n**
    Time: O(n)
    Space : O(1)
    """
    already_removed = False
    for i in range(1, len(nums)):
        if nums[i - 1] >= nums[i]:
            if already_removed:
                return False
            if i > 1 and nums[i] <= nums[i - 2]:
                nums[i] = nums[i - 1]
            already_removed = True
    return True


@Core.register
def ping() -> bool:
    return True


if __name__ == '__main__':
    print(Core.show())
    print(Core.get_funcs(['leetcode', 'test']))
    assert Core.get_funcs('test') == []
    assert Core.get_funcs('ping') == [ping]
