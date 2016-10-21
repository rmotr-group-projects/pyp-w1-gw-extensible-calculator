from functools import reduce
import operator

def add(*args):
    return sum(args)

def subtract(*args):
    return args[0] - sum(args[1:])

def multiply(*args):
    # StackOverflow link: https://goo.gl/nH8d5c
    # the '1' since multiplying anything to '1' doesn't affect the result
    return reduce(operator.mul, args, 1)

def divide(*args):
    # since: (12 / 2)/3 == (12/(2*3))
    return args[0] / float(reduce(operator.mul, args[1:], 1))

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
