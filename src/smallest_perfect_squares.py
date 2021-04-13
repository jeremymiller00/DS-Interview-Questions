"""Given a positive integer n, find the smallest number of perfect squares that sum up to n. For example, for n = 7, you should return 4since 7 = 4 + 1 + 1 +1, and for n = 13, you should return 2 since 13 = 4 + 9.
"""
import math

def find_smallest_n_perfect_squares(n: int) -> int:
    result_list = []
    for i in range(n, 0, -1):
        if is_perfect_square(i):
            result_list.append(i)
        if sum(result_list) == n:
            return len(result_list)
    while sum(result_list) != n:
        result_list.append(1)
    return len(result_list)

def is_perfect_square(i: int) -> bool:
    root = math.sqrt(i)
    int_root = int(root)
    return (root / int_root) == 1.0

############################
if __name__ == '__main__':
    assert is_perfect_square(9) == True
    assert is_perfect_square(25) == True
    assert is_perfect_square(13) == False
    
    assert find_smallest_n_perfect_squares(7) == 4
    assert find_smallest_n_perfect_squares(13) == 2

