from test_framework import generic_test

"""
Time Complexity: O(1)
Space Complexity: O(1)
Hint: We check the last bit of x and then replace it with first bit of the result. We will do this for all 64 bits of x.
"""

def reverse_bits(x: int) -> int:
    res = 0
    for i in range(64):
        bit = (x >> i) & 1
        res |= bit << (63 - i)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
