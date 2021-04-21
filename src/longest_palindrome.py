"""Longest palindrome substring
Python Algorithms String Manipulation

A palindrome is "a word, phrase, or sequence that reads the same backward as forward." Below are some example palindromes:

madam
racecar
tat
Can you write a python function that takes in a string and outputs the longest palindrome? If the string itself is a palindrome, the function would output the original string."""

def is_pal(s: str) -> bool:
    s_list = [c for c in s]
    r_list = s_list.copy()
    r_list.reverse()
    if s_list == r_list:
        return True
    return False

def lp(s: str) -> str:
    blank = ""
    for j in range(len(s), 1, -1): # length of word
        for i in range(len(s) - j + 1): # start of word
            w = s[i:i+j]
            if is_pal(w):
                return(w)
    return blank 


print(lp("racecar"))
print(lp("rdmadamiii"))
print(lp("rewq"))
