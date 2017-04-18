from __future__ import division
try:
    from functools import reduce
except ImportError:
    pass
from calculator.exceptions import *

def add(*args):
    return sum(args)

def subtract(*args):
   return reduce(lambda x, y: x-y, args)
   
def multiply(*args):
    return reduce(lambda x, y: x*y, args)

def divide(*args):
    return reduce(lambda x, y: x/y, args)

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here

def mod(*args):
    """
    Returns the result of first arg mod second arg
    """
    if len(args) != 2:
        raise InvalidNumParams
    else:
        return args[0] % args[1]

def factorial(*args):
    """
    Returns the factorial of a given number.
    """
    if len(args) != 1:
        raise InvalidNumParams
    else:
        nums = [x for x in range(args[0])]
        return multiply([nums])
