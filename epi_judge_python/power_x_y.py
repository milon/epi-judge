from test_framework import generic_test

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

def power(x: float, y: int) -> float:
    res, power = 1.0, y
    if y < 0:
        power, x = -power, 1.0 / x
    while power:
        if power & 1:
            res *= x
        x, power = x * x, power >> 1
    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
