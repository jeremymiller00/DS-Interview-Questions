"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""

def non_adj_ints(l: list) -> int:
    incl = 0
    excl = 0
    for i in l:
        new_excl = excl if excl > incl else incl
        incl = excl + i
        excl = new_excl
    return max(incl, excl)

######

if __name__ == '__main__':
    assert non_adj_ints([5, 5, 10, 40, 50, 35]) == 80
    assert non_adj_ints([2, 4, 6, 2, 5]) == 13
    assert non_adj_ints([5, 1, 1, 5] ) == 10
    # print(non_adj_ints([2, 4, 6, 2, 5]))
    # # assert non_adj_ints([5, 1, 1, 5] ) == 10