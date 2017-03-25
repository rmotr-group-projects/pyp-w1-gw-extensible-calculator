from functools import reduce 
from sympy import symbols
from sympy.plotting import textplot

def add(*args):
    # your implementation here
    add =lambda *args: sum(args)
    return add(*args)

def subtract(*args):
    # your implementation here
    subtract = lambda *args: args[0] - add(*args) + args[0]
    return subtract(*args)

def multiply(*args):
    # your implementation here
    multiply = reduce(lambda x,y: x*y, args)
    return multiply
    
def divide(*args):
    # your implementation here
    divide = reduce(lambda x,y: float(x)/y, args)
    return float(divide)

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    x = symbols('x')
    return textplot(eval(args[0]), args[1], args[2])


