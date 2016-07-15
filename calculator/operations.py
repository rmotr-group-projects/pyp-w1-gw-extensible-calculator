from functools import reduce
from sympy import symbols, plotting
from sympy.parsing.sympy_parser import parse_expr


def add(*args):
    return sum(args)

def subtract(*args):
    return reduce(lambda x,y: x-y, args)

def multiply(*args):
    return reduce(lambda x,y: x*y, args)

def divide(*args):
    return reduce(lambda x,y: float(x)/y, args)

def plot(*args):
    # plot requires 3 arguments: the expression and the min/max range
    # plot parses the expression and plots it within the specified range
    expr, min_range, max_range = args
    x = symbols('x')
    return plotting.plot(parse_expr(expr),(x,min_range,max_range))