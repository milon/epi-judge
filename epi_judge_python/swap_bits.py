from test_framework import generic_test

"""
Time Complexity: O(1)
Space Complexity: O(1)
Hint: First we extract the bits at i and j, then we XOR them if they are different.
"""

def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        x ^= (1 << i) | (1 << j)
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
