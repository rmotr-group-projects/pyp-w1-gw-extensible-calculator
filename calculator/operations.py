from functools import reduce
from operator import mul,sub,truediv
def add(*args):
    return sum(args)

def subtract(*args):
    return reduce(sub,args)

def multiply(*args):
    return reduce(mul,args)

def divide(*args):
    return reduce(truediv,args)

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
