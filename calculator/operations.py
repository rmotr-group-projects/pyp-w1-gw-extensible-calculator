from __future__ import division
from functools import reduce
from sympy import symbols
from sympy.plotting import textplot


def add(*args):
    return reduce(lambda x,y: x+y, args)
    
def subtract(*args):
    return reduce(lambda x,y: x-y, args)

def multiply(*args):
    return reduce(lambda x,y: x*y, args)

def divide(*args):
    return reduce(lambda x,y: x/y, args)

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    if len(args) != 3:
        return None
    x = symbols('x')
    #expression
    exp = eval(args[0])
    range_ = args[1:]
    return textplot(exp, *range_)
    