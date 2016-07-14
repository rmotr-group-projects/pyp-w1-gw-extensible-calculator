from functools import reduce
#using floats here to pass unit tests

def add(*args):
    return sum((args))
    
def subtract(*args):
    return reduce(lambda x, y: float(x) - float(y), args) 

def multiply(*args):
    return reduce(lambda x, y: float(x) * float(y), args)

def divide(*args):
    return reduce(lambda x, y: float(x) /float(y), args)
