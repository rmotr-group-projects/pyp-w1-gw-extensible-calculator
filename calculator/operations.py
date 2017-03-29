from functools import reduce

def add(*args):
    return sum(args)

def subtract(*args):
    return args[0] - sum(args[1:])
    
def multiply(*args):
    return reduce(lambda x, y: x * y, args, 1)

def divide(*args):
    return reduce(lambda x, y: float(x) / y, args[1:], args[0])

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
