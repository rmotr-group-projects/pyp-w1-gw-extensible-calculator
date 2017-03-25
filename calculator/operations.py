from functools import reduce

def add(*args):
    # your implementation here
    if len(args) > 1:
        return reduce((lambda x, y: x + y), args)
    return args[0]

def subtract(*args):
    # your implementation here
    if len(args) > 1:
        return reduce((lambda x, y: x - y), args)
    return args[0]

def multiply(*args):
    # your implementation here
    if len(args) > 1:
        return reduce((lambda x, y: x * y), args)
    return args[0]

def divide(*args):
    # your implementation here
    if len(args) > 1:
        return reduce((lambda x, y: float(x) / y), args)
    return args[0]
def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
