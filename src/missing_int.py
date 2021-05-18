"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def missing_int(l: list) -> int:
    s = set(l)
    i = 1
    while True:
        if i in s:
            i += 1
        else:
            return i


assert missing_int([3, 4, -1, 1]) == 2
assert missing_int([1, 2, 0]) == 3
