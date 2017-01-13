from __future__ import division

def add(*args):
    return sum(args)

def subtract(*args):
    if len(args) is 1:
        return args[0]
    else:
        res = args[0]
        for n in args[1:]:
            res -= n
        return res

def multiply(*args):
    if len(args) is 1:
        return args[0]
    else:
        res = args[0]
        for n in args[1:]:
            res *= n
        return res

def divide(*args):
    if len(args) is 1:
        return args[0]
    else:
        res = args[0]
        for n in args[1:]:
            res /= n
        return res

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
