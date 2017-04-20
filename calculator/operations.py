from __future__ import division
from functools import reduce

def add(*args):
    return sum(args)

def subtract(*args):
    if len(args) < 2:
        return args[0]
    return args[0] - sum(args[1:])
    
def multiply(*args):
    return reduce(lambda x, y: x*y, args)

def divide(*args):
    return reduce(lambda x, y: x/y, args)

def our_plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here