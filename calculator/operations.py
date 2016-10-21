from functools import reduce
import operator as op

def add(*args):
    return sum(args)

def subtract(*args):
    return reduce(op.sub, args)

def multiply(*args):
    return reduce(op.mul, args)

def divide(*args):
    return reduce(op.truediv, args)

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
