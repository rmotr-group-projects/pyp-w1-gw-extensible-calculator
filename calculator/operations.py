from calculator.exceptions import *

def add(*args):
    # your implementation here
    if len(args) < 1:
        raise InvalidParams()
    for i in args:
        if not isinstance(i, int) and not isinstance(i, float):
            raise InvalidParams()
    return sum(args)

def subtract(*args):
    # your implementation here
    if len(args) < 1:
        raise InvalidParams()
    for i in args:
        if not isinstance(i, int) and not isinstance(i, float):
            raise InvalidParams()
    return args[0] - sum(args[1:])

def multiply(*args):
    # your implementation here
    if len(args) < 1:
        raise InvalidParams()
    result = 1
    for i in args:
        result *= i
    return result

def divide(*args):
    # your implementation here
    if len(args) < 1:
        raise InvalidParams()
    if len(args) == 1:
        return args[0]
    if 0 in args[1:]:
        raise InvalidParams()
    return 1.0 * args[0] / multiply(*args[1:])

'''
def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    return args[0] / args[1]
'''

# add your custom operations here
def factorial(*args):
    if len(args) != 1:
        raise InvalidParams()
    if not isinstance(args[0], int):
        raise InvalidParams()
    result = 1
    for i in range(1, args[0] + 1):
        result *= i
    return result
