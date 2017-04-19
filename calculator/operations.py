import functools

def add(*args):
    return sum(args)
    pass

def subtract(*args):
    return args[0] - sum(args[1:])
    pass

def multiply(*args):
    # your implementation here
    pValue = 1
    for arg in args:
        pValue *= arg
    return pValue
    pass

def divide(*args):
    # your implementation here
    return functools.reduce(lambda x,y:float(x)/y,args)
    pass

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
