from functools import reduce
from sympy.plotting import plot as plt

def add(*args):
    return sum(args)

def subtract(*args):
    return args[0] - sum(args[1:])

def multiply(*args):
    return reduce(lambda x,y : x*y, args, 1)

def divide(*args):
    result = [float(arg) for arg in args]
    return reduce(lambda x,y: x/y, result)

# add your custom operations here
def plot(op, xMin, xMax):
    return plt(op, xLim = (float(xMin),float(xMax)))