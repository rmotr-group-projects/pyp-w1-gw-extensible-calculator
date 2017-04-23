from functools import reduce
#from sympy import *

def add(*args):
    return reduce(lambda x,y:x+y, args)
    
def subtract(*args):
    return reduce(lambda x,y:x-y, args)

def multiply(*args):
    return reduce(lambda x,y:x*y, args)

def divide(*args):
    return reduce(lambda x,y:float(x)/y, args)

def plot(*args):
#    x = symbols('x')
#    return plot(args)
    pass