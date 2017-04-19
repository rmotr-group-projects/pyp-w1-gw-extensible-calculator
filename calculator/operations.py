import sys
from sympy import symbols
from sympy.plotting import plot as plt

if sys.version_info[0] > 2:
    from functools import reduce
    
def add(*args):
    return reduce(lambda x, y: x+y, args)

def subtract(*args):
    return reduce(lambda x, y: x-y, args)

def multiply(*args):
    return reduce(lambda x, y: x*y, args)

def divide(*args):
    return reduce(lambda x, y: float(x)/float(y), args)

def plot(*args):
    if len(args) != 3:
        return None
    x = symbols('x')
    expression = args[0]
    plot_range = range(args[1], args[2] + 1)
    plot_points = map(lambda x: eval(expression), plot_range) 
    return (plt(args[0], (x, args[1], args[2])), list(plot_points))[1]


# add your custom operations here
