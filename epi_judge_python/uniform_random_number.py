import functools
import random

from test_framework import generic_test
from test_framework.random_sequence_checker import (
    check_sequence_is_uniformly_random, run_func_with_retries)
from test_framework.test_utils import enable_executor_hook


def zero_one_random():
    return random.randrange(2)

"""
Time complexity: O(log(b - a + 1))
Space complexity: O(1)
Hint: Use the fact that the uniform random number is in the range [a, b]. It is easy to produce a random integerbetween 0 and 2^i-1, 
inclusive: concatenate I bits produced by the random number generator. For example, two calls to the random number generator will produce 
one of (00)2, (01)2, (10)2, (11)2. These four possible outcomes encode the four integers 0,1,2,3, and all of them are equally likely.
"""

def uniform_random(lower_bound: int, upper_bound: int) -> int:
    num_of_outcomes = upper_bound - lower_bound + 1
    while True:
        res, i = 0, 0
        while (1 << i) < num_of_outcomes:
            res = (res << 1) | zero_one_random()
            i += 1
        if res < num_of_outcomes:
            break
    return res + lower_bound


@enable_executor_hook
def uniform_random_wrapper(executor, lower_bound, upper_bound):
    def uniform_random_runner(executor, lower_bound, upper_bound):
        result = executor.run(
            lambda:
            [uniform_random(lower_bound, upper_bound) for _ in range(100000)])

        return check_sequence_is_uniformly_random(
            [a - lower_bound for a in result], upper_bound - lower_bound + 1,
            0.01)

    run_func_with_retries(
        functools.partial(uniform_random_runner, executor, lower_bound,
                          upper_bound))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('uniform_random_number.py',
                                       'uniform_random_number.tsv',
                                       uniform_random_wrapper))
