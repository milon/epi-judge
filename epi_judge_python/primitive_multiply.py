from test_framework import generic_test

"""
Time Complexity: O(n)
Space Complexity: O(1)
Hint: We add x, y times to get the result.
"""

def multiply(x: int, y: int) -> int:
    def add(a: int, b: int) -> int:
        running_sum, carry, k, temp_a, temp_b = 0, 0, 1, a, b
        while temp_a or temp_b:
            ak, bk = a & k, b & k
            carry_out = (ak & bk) | (ak & carry) | (bk & carry)
            running_sum |= ak ^ bk ^ carry
            carry, k, temp_a, temp_b = carry_out << 1, k << 1, temp_a >> 1, temp_b >> 1
        return running_sum | carry

    running_sum= 0
    while x:
        if x & 1:
            running_sum = add(running_sum, y)
        x, y = x >> 1, y << 1
    return running_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
