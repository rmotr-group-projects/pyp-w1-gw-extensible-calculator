from __future__ import division

def add(*args):
    if len(args) == 1:
        return args[0]
    else:
        return sum(args)


def subtract(*args):
    return args[0] - sum(args[1:])

def multiply(*args):
    ans = 1
    for num in args:
        ans *= num
    return ans

def divide(*args):
    ans = args[0]
    for num in args[1:]:
        ans /= num
    return ans

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    pass

# add your custom operations here
