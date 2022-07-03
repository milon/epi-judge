import math
from test_framework import generic_test

"""
Time Complexity: O(n)
Space Complexity: O(1)
Hint: Count the number of digits in the number. Then check the most significant digit of x and the least significant digit of x. 
If they are the same, then check the next most significant digit and the next least significant digit. And so on.
"""

def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        return x == 0
    num_digit = math.floor(math.log10(x)) + 1
    mask = 10 ** (num_digit - 1)
    for i in range(num_digit // 2):
        if x // mask != x % 10:
            return False
        x %= mask   # Renove the nost significant digit of x
        x //= 10    # Remove the least significant digit of x
        mask //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
