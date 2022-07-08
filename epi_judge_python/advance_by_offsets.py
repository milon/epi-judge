from typing import List

from test_framework import generic_test

"""
Time complexity: O(n)
Space complexity: O(1)
"""

def can_reach_end(A: List[int]) -> bool:
    furtherest_step, last_index = 0, len(A) - 1
    i = 0
    while i <= furtherest_step and i < last_index:
        furtherest_step = max(furtherest_step, A[i] + i)
        i += 1
    return furtherest_step >= last_index


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
