from test_framework import generic_test

"""
Time Complexity: O(n)
Space Complexity: O(1)
Hint: Count the last bit of x by logical AND it with 1 and add it to the result.
"""

def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
