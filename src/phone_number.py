import sys
'''
Suppose you're given a portion of a phone number. Each digit corresponds to letters (as shown below). Using python, write code to return all possible combinations the given number could represent.
Telephone digits, for reference:

For example:

Input: "24"

Output: 
['a', 'g']
['a', 'h']
['a', 'i']
['b', 'g']
['b', 'h']
['b', 'i']
['c', 'g']
['c', 'h']
['c', 'i']
'''

import sys

def phone_letters(num):
    keypad = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
    
    ret = ['']
    for char in num:
        letters = keypad.get(char, '')
        # ret = [prefix+letter for prefix in ret for letter in letters]
        # implement without list comprehension
        ret2 = []
        for prefix in ret:
            for letter in letters:
                ret2.append(prefix+letter)
        ret = ret2

    return ret


#############

if __name__ == '__main__':
    num = sys.argv[1]
    # assert phone_letters(24) == [['a', 'g'],['a', 'h'],['a', 'i'],['b', 'g'],['b', 'h'],['b', 'i'],['c', 'g'],['c', 'h'],['c', 'i']]
    result = phone_letters(num)
    print(result)










