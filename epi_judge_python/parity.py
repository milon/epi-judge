from test_framework import generic_test

"""
Time Complexity: O(n)
Space Complexity: O(1)
Hint: Count the last bit of x by logical AND it with 1 and XOR it with the result to find parity.
"""

def parity(x: int) -> int:
    res = 0
    while x:
        res ^= x & 1
        x >>= 1
    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
