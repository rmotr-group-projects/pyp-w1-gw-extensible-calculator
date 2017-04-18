from functools import reduce

def add(*args):
    return sum(args)

def subtract(*args):
    return args[0] - sum(args[1:])

def multiply(*args):
    return reduce(lambda x, y: x*y, args)

def divide(*args):
    return reduce(lambda x, y: x / float(y), args)

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
