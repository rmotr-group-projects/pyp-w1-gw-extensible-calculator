from functools import reduce

def add(*args):
    return sum(args)

def subtract(*args):
    return reduce(lambda x,y: x-y, args[1:], args[0])

def multiply(*args):
    return reduce(lambda x,y: x*y, args, 1)

def divide(*args):
    return reduce(lambda x,y: float(x)/y, args[1:], args[0])

# add your custom operations here
