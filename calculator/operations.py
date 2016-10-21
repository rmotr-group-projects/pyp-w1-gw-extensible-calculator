from functools import reduce
import operator as op
from sympy import symbols
from sympy.plotting import plot
from sympy.parsing.sympy_parser import parse_expr

def add(*args):
    return sum(args)

def subtract(*args):
    return reduce(op.sub, args)

def multiply(*args):
    return reduce(op.mul, args)

def divide(*args):
    return reduce(op.truediv, args)

def plot_op(expr, a, b):
    x = symbols("x")
    p_expr = parse_expr(expr)
    return plot(p_expr, (x, a, b))
    
