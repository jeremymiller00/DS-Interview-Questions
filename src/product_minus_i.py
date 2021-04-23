"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

def product_without(arr: list) -> list:
    grand_product = 1
    for x in arr:
        grand_product *= x
    result = [grand_product / y for y in arr]
    return result

def product_without_div(arr: list) -> list:
    result = []
    for i in range(len(arr)):
        temp = arr[:i] + arr[i+1:]
        p = 1
        for x in temp:
            p *= x
        result.append(p)
    return result


assert product_without([1,2,3,4,5]) == [120,60,40,30,24]
assert product_without([3,2,1]) == [2,3,6]
res3 = product_without_div([1,2,3,4,5])
res4 = product_without_div([3,2,1])
assert res3 == [120,60,40,30,24]
assert res4 == [2,3,6]