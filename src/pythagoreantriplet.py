'''
Given an array of integers, can you write a function that returns "True" if there is a triplet (a, b, c) within the array that satisfies a^2 + b^2 = c^2?

For example:

Input: arr[] = [3, 1, 4, 6, 5]
Output: True
#There is a Pythagorean triplet (3, 4, 5) that exists in the input array.

Input: arr[] = {10, 4, 6, 12, 5}
Output: False
#There is no Pythagorean triplet that exists in the input array.
Solution will be written in Python for premium users.
'''

def pytrip(arr):
    arr = list(arr)
    squares = [x**2 for x in arr]
    # for each pair, get SS, check if in list
    for i in arr:
        templist = arr.copy()
        templist.remove(i)
        for t in templist:
            if (i**2 + t**2) in squares:
                return True
    return False