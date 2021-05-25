"""cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
""" 

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def get_first(*args):
        for a in args:
            return a
    return pair(get_first)

def cdr(pair):
    def get_last(*args):
        arg_list = []
        for a in args:
            arg_list.append(a)
        return arg_list[-1]
    return pair(get_last)

if __name__ == '__main__':
    assert car(cons(3, 4)) == 3
    assert cdr(cons(3, 4)) == 4