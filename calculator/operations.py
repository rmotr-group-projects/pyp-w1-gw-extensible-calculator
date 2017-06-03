from functools import reduce
from sympy import symbols
from sympy.plotting import textplot

def add(*args):
    return sum(args)

def subtract(*args):
    return reduce((lambda x, y: x - y), args)

def multiply(*args):
    return reduce((lambda x, y: x * y), args)

def divide(*args):
    return reduce((lambda x, y: x / float(y)), args)

def plot(*args):
    if len(args) != 3:
        return None
    x = symbols('x')
    expr = args[0]
    values = args[1:]
    return textplot(expr, *values)
        
