
def add(*args):
    return sum(args)

def subtract(*args):
    # need to handle len 0 and len 1
    x = args[0]
    for i in args[1:]:
        x -= i
    return x

def multiply(*args):
    # need to handle len 0 and len 1
    # what about floating point?
    x = args[0]
    for i in args[1:]:
        x *= i
    return x

def divide(*args):
    # need to handle len 0 and len 1
    # what about floating point?
    x = float(args[0])
    for i in args[1:]:
        x /= i
    return x

'''
def square(*args):
    # square the first argument and return it.
    return args[0] * args[0]
'''