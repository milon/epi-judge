from test_framework import generic_test

"""
Time Complexity: O(n)
Space Complexity: O(1)
Hint: get the last digit of x, then add it to the result. And then divide x by 10. Then do the same thing again until x is 0.
"""

def reverse(x: int) -> int:
    res, x_remaining = 0, abs(x)
    while x_remaining:
        res = res * 10 + x_remaining % 10
        x_remaining //= 10
    return -res if x < 0 else res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
