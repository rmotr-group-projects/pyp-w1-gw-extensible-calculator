from functools import reduce
from sympy import symbols
from sympy.plotting import textplot

def add(*args):
    # add variable arguments, return the sum
    return reduce((lambda x,y: x+y),args)

def subtract(*args):
    # your implementation here
    return reduce((lambda x,y: x-y), args)

def multiply(*args):
    # your implementation here
    return reduce((lambda x,y: x*y), args)

def divide(*args):
    # your implementation here
    try:
        result = reduce((lambda x,y: float(x)/y),args)
    except ZeroDivisionError:
        print "Division by zero!"
    
    return result

def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION! 
    # See README for info.
    x = symbols('x')
    return textplot(eval(args[0]),args[1],args[2])

# add your custom operations here
